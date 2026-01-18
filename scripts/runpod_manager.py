#!/usr/bin/env python3
"""
RunPod API Manager - Handles all RunPod pod operations

This script provides a Python wrapper around the RunPod GraphQL API for:
- Starting/stopping GPU pods
- Uploading/downloading files
- Executing commands remotely
- Monitoring pod status

Usage:
    from runpod_manager import RunPodManager

    manager = RunPodManager(api_key="your-api-key")
    pod_id = manager.start_pod(gpu_type="RTX 4090")
    manager.execute_command(pod_id, "python generate.py")
    manager.download_file(pod_id, "/workspace/output.png", "local/output.png")
    manager.stop_pod(pod_id)

Author: Claude Code
Created: 2026-01-17
"""

import os
import time
import json
import requests
from typing import Optional, Dict, List, Any
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RunPodManager:
    """Manages RunPod GPU pods via GraphQL API"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize RunPod Manager

        Args:
            api_key: RunPod API key. If not provided, reads from RUNPOD_API_KEY env var
        """
        self.api_key = api_key or os.getenv('RUNPOD_API_KEY')
        if not self.api_key:
            raise ValueError(
                "RunPod API key not found. Set RUNPOD_API_KEY environment variable "
                "or pass api_key parameter"
            )

        self.api_url = "https://api.runpod.io/graphql"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def _graphql_request(self, query: str, variables: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Execute a GraphQL request to RunPod API

        Args:
            query: GraphQL query string
            variables: Optional variables for the query

        Returns:
            Response data dict

        Raises:
            Exception: If API request fails
        """
        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()

            data = response.json()

            if "errors" in data:
                error_msg = data["errors"][0].get("message", "Unknown error")
                raise Exception(f"GraphQL error: {error_msg}")

            return data.get("data", {})

        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise

    def start_pod(
        self,
        gpu_type: str = "RTX 4090",
        image: str = "runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04",
        disk_size: int = 50,
        cloud_type: str = "SECURE",
        name: Optional[str] = None
    ) -> str:
        """
        Start a new RunPod GPU pod

        Args:
            gpu_type: GPU type (e.g., "RTX 4090", "RTX 3090", "A100")
            image: Docker image to use
            disk_size: Disk size in GB
            cloud_type: "SECURE" or "COMMUNITY"
            name: Optional pod name

        Returns:
            Pod ID string
        """
        logger.info(f"Starting pod with GPU: {gpu_type}")

        query = """
        mutation {
          podFindAndDeployOnDemand(
            input: {
              cloudType: %s
              gpuTypeId: "%s"
              name: "%s"
              imageName: "%s"
              dockerArgs: ""
              volumeInGb: %d
              containerDiskInGb: %d
              minVcpuCount: 2
              minMemoryInGb: 15
              startSsh: true
            }
          ) {
            id
            imageName
            machineId
            machine {
              gpuDisplayName
            }
          }
        }
        """ % (
            cloud_type,
            self._get_gpu_id(gpu_type),
            name or f"daily_life_gen_{int(time.time())}",
            image,
            disk_size,
            disk_size
        )

        try:
            data = self._graphql_request(query)
            pod_data = data.get("podFindAndDeployOnDemand")

            if not pod_data:
                raise Exception("Failed to start pod - no pod data returned")

            pod_id = pod_data["id"]
            logger.info(f"Pod started successfully: {pod_id}")
            logger.info(f"GPU: {pod_data['machine']['gpuDisplayName']}")

            # Wait for pod to be ready
            self._wait_for_pod_ready(pod_id)

            return pod_id

        except Exception as e:
            logger.error(f"Failed to start pod: {e}")
            raise

    def stop_pod(self, pod_id: str) -> bool:
        """
        Stop a running pod

        Args:
            pod_id: Pod ID to stop

        Returns:
            True if successful
        """
        logger.info(f"Stopping pod: {pod_id}")

        query = """
        mutation {
          podStop(input: {podId: "%s"}) {
            id
            desiredStatus
          }
        }
        """ % pod_id

        try:
            data = self._graphql_request(query)
            if data.get("podStop"):
                logger.info(f"Pod stopped successfully: {pod_id}")
                return True
            return False

        except Exception as e:
            logger.error(f"Failed to stop pod: {e}")
            raise

    def get_pod_status(self, pod_id: str) -> Dict[str, Any]:
        """
        Get current status of a pod

        Args:
            pod_id: Pod ID to check

        Returns:
            Dict with pod status information
        """
        query = """
        query {
          pod(input: {podId: "%s"}) {
            id
            name
            runtime {
              uptimeInSeconds
              ports {
                ip
                isIpPublic
                privatePort
                publicPort
                type
              }
              gpus {
                id
                gpuUtilPercent
                memoryUtilPercent
              }
            }
            machine {
              gpuDisplayName
            }
            desiredStatus
            imageName
            lastStatusChange
          }
        }
        """ % pod_id

        try:
            data = self._graphql_request(query)
            return data.get("pod", {})

        except Exception as e:
            logger.error(f"Failed to get pod status: {e}")
            raise

    def execute_command(
        self,
        pod_id: str,
        command: str,
        timeout: int = 300
    ) -> Dict[str, Any]:
        """
        Execute a command on a running pod

        Note: This is a simplified version. For production, you'd use SSH or
        RunPod's exec API endpoint.

        Args:
            pod_id: Pod ID
            command: Command to execute
            timeout: Timeout in seconds

        Returns:
            Dict with command output
        """
        logger.info(f"Executing command on pod {pod_id}: {command}")

        # For now, this is a placeholder
        # In production, you'd implement SSH-based command execution
        # or use RunPod's specific exec endpoints

        logger.warning(
            "Command execution requires SSH access. "
            "Please implement SSH-based execution or use RunPod's exec API."
        )

        return {
            "status": "not_implemented",
            "message": "SSH-based execution needs to be implemented",
            "command": command
        }

    def upload_file(
        self,
        pod_id: str,
        local_path: str,
        remote_path: str
    ) -> bool:
        """
        Upload a file to the pod

        Args:
            pod_id: Pod ID
            local_path: Local file path
            remote_path: Remote destination path

        Returns:
            True if successful
        """
        logger.info(f"Uploading {local_path} to pod {pod_id}:{remote_path}")

        # Placeholder - requires SSH/SCP implementation
        logger.warning("File upload requires SSH access - not yet implemented")
        return False

    def download_file(
        self,
        pod_id: str,
        remote_path: str,
        local_path: str
    ) -> bool:
        """
        Download a file from the pod

        Args:
            pod_id: Pod ID
            remote_path: Remote file path
            local_path: Local destination path

        Returns:
            True if successful
        """
        logger.info(f"Downloading pod {pod_id}:{remote_path} to {local_path}")

        # Placeholder - requires SSH/SCP implementation
        logger.warning("File download requires SSH access - not yet implemented")
        return False

    def _wait_for_pod_ready(
        self,
        pod_id: str,
        max_wait: int = 300,
        check_interval: int = 10
    ) -> bool:
        """
        Wait for pod to be ready

        Args:
            pod_id: Pod ID
            max_wait: Maximum wait time in seconds
            check_interval: Check interval in seconds

        Returns:
            True if pod becomes ready

        Raises:
            TimeoutError: If pod doesn't become ready in time
        """
        logger.info(f"Waiting for pod {pod_id} to be ready...")

        start_time = time.time()
        while (time.time() - start_time) < max_wait:
            status = self.get_pod_status(pod_id)

            desired_status = status.get("desiredStatus")
            logger.debug(f"Pod status: {desired_status}")

            if desired_status == "RUNNING":
                logger.info(f"Pod {pod_id} is ready!")
                return True

            time.sleep(check_interval)

        raise TimeoutError(f"Pod {pod_id} did not become ready within {max_wait}s")

    def _get_gpu_id(self, gpu_type: str) -> str:
        """
        Get GPU type ID from friendly name

        Args:
            gpu_type: Friendly GPU name

        Returns:
            GPU type ID
        """
        # Common GPU type mappings
        # Note: These IDs may change - verify with RunPod API docs
        gpu_mapping = {
            "RTX 4090": "NVIDIA GeForce RTX 4090",
            "RTX 3090": "NVIDIA GeForce RTX 3090",
            "RTX 3080": "NVIDIA GeForce RTX 3080",
            "A100": "NVIDIA A100 80GB PCIe",
            "A40": "NVIDIA A40",
            "A6000": "NVIDIA RTX A6000"
        }

        return gpu_mapping.get(gpu_type, gpu_type)

    def list_my_pods(self) -> List[Dict[str, Any]]:
        """
        List all pods in your account

        Returns:
            List of pod info dicts
        """
        query = """
        query {
          myself {
            pods {
              id
              name
              runtime {
                uptimeInSeconds
              }
              machine {
                gpuDisplayName
              }
              desiredStatus
              costPerHr
            }
          }
        }
        """

        try:
            data = self._graphql_request(query)
            pods = data.get("myself", {}).get("pods", [])
            return pods

        except Exception as e:
            logger.error(f"Failed to list pods: {e}")
            raise

    def get_gpu_types(self) -> List[Dict[str, Any]]:
        """
        Get available GPU types

        Returns:
            List of available GPU types
        """
        query = """
        query {
          gpuTypes {
            id
            displayName
            memoryInGb
            securePrice
            communityPrice
            lowestPrice {
              minimumBidPrice
              uninterruptablePrice
            }
          }
        }
        """

        try:
            data = self._graphql_request(query)
            return data.get("gpuTypes", [])

        except Exception as e:
            logger.error(f"Failed to get GPU types: {e}")
            raise


def main():
    """Test/demo the RunPod manager"""
    import argparse

    parser = argparse.ArgumentParser(description="RunPod Manager CLI")
    parser.add_argument("--test", action="store_true", help="Test API connection")
    parser.add_argument("--list-pods", action="store_true", help="List all pods")
    parser.add_argument("--list-gpus", action="store_true", help="List available GPU types")
    parser.add_argument("--start-pod", type=str, help="Start pod with GPU type")
    parser.add_argument("--stop-pod", type=str, help="Stop pod by ID")
    parser.add_argument("--status", type=str, help="Get pod status by ID")

    args = parser.parse_args()

    try:
        manager = RunPodManager()

        if args.test:
            print("Testing RunPod API connection...")
            pods = manager.list_my_pods()
            print(f"✓ API connection successful! Found {len(pods)} pods")

        elif args.list_pods:
            pods = manager.list_my_pods()
            print(f"\nFound {len(pods)} pod(s):")
            for pod in pods:
                print(f"  - {pod['id']}: {pod['name']} ({pod['desiredStatus']})")
                print(f"    GPU: {pod['machine']['gpuDisplayName']}")
                print(f"    Cost: ${pod['costPerHr']}/hr")

        elif args.list_gpus:
            gpus = manager.get_gpu_types()
            print(f"\nAvailable GPU types ({len(gpus)}):")
            for gpu in gpus:
                print(f"  - {gpu['displayName']} ({gpu['memoryInGb']}GB)")
                print(f"    Secure: ${gpu['securePrice']}/hr")
                print(f"    Community: ${gpu['communityPrice']}/hr")

        elif args.start_pod:
            pod_id = manager.start_pod(gpu_type=args.start_pod)
            print(f"✓ Pod started: {pod_id}")

        elif args.stop_pod:
            manager.stop_pod(args.stop_pod)
            print(f"✓ Pod stopped: {args.stop_pod}")

        elif args.status:
            status = manager.get_pod_status(args.status)
            print(f"\nPod Status: {args.status}")
            print(json.dumps(status, indent=2))

        else:
            parser.print_help()

    except Exception as e:
        print(f"✗ Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
