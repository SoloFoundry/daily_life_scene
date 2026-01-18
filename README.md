# Daily Life Visual Vocabulary Generator

Automated pipeline to generate photorealistic images for visual vocabulary learning using Stable Diffusion on RunPod GPU.

## Quick Start

### 1. Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set RunPod API key
export RUNPOD_API_KEY="your-api-key-here"
```

### 2. Test RunPod Connection

```bash
python scripts/runpod_manager.py --test
```

### 3. Next Steps

See [CLAUDE.md](CLAUDE.md) for complete project documentation and [STATUS.md](STATUS.md) for current progress.

## Project Structure

```
daily_life/
├── CLAUDE.md                    # Comprehensive project context
├── STATUS.md                    # Real-time progress tracking
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── config/                      # Configuration files
│   ├── scenes_poc.json          # 15 POC scenes
│   ├── character_profile.json   # Matt's appearance
│   └── locations.json           # 3 POC locations
├── scripts/                     # Automation scripts
│   └── runpod_manager.py        # RunPod API wrapper
├── assets/                      # Generated assets
│   ├── location_refs/           # Location references
│   ├── character_refs/          # Character references
│   └── lora_weights/            # LoRA model weights
└── output/                      # Generated images
    ├── poc/                     # POC images (15)
    └── full/                    # Full project (308)
```

## POC Goals

Generate 15 high-quality photorealistic images to validate:
- Character consistency (Matt recognizable across images)
- Location consistency (bedroom, bathroom, kitchen)
- Educational value (objects clearly identifiable)
- Cost effectiveness (~$1.50-$3.50 for POC)

## Technologies

- **GPU**: RunPod (RTX 4090 or RTX 3090)
- **Model**: Stable Diffusion (RealVisXL V5.0)
- **Character**: Existing LoRA from CivitAI
- **Locations**: AI-generated references + IP-Adapter
- **Automation**: Python + RunPod API

## Documentation

- **[CLAUDE.md](CLAUDE.md)** - Complete project context for Claude Code sessions
- **[STATUS.md](STATUS.md)** - Current progress and tracking
- **[matt_daily_life_scenes.md](matt_daily_life_scenes.md)** - All 308 scene descriptions
- **[image_generation_pipeline.md](image_generation_pipeline.md)** - Technical pipeline details

## Current Status

**Phase**: POC Setup ✅
**Next**: Generate location references and POC images

See [STATUS.md](STATUS.md) for detailed progress.

## Contributing

This is an educational content generation project. Feel free to adapt for your own characters and scenarios!

## License

Educational use only.

---

**Created with** [Claude Code](https://claude.com/claude-code)
