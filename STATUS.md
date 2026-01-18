# Project Status - Daily Life Visual Vocabulary Generator

**Last Updated:** 2026-01-17
**Phase:** POC Setup
**Started:** 2026-01-17

---

## Current Status

### Phase: POC Setup & Configuration

**What's Completed:**
- ✅ Project directory structure created
- ✅ Git repository initialized and first commit made
- ✅ Core documentation created (CLAUDE.md, STATUS.md, README.md)
- ✅ Requirements.txt created
- ✅ .gitignore configured
- ✅ **15 POC scenes selected** from bedroom, bathroom, kitchen
- ✅ **config/scenes_poc.json created** with 15 detailed scenes
- ✅ **config/character_profile.json created** with Matt's appearance and prompts
- ✅ **config/locations.json created** for 3 POC locations (bedroom, bathroom, kitchen)
- ✅ **scripts/runpod_manager.py created** - RunPod API wrapper for pod management

**What's In Progress:**
- ⏳ Additional automation scripts needed (remote_generate.py, etc.)

**What's Next:**
1. Get RunPod API key and test connection
2. Write scripts/remote_generate.py for automated image generation
3. Write scripts/generate_location_refs.py for location reference generation
4. Generate 9 location reference images (3 per location)
5. Find and download character LoRA from CivitAI
6. Set up ComfyUI workflow on RunPod
7. Generate 15 POC images

**Blockers:**
- Need RunPod API key to proceed with automation
- Need to decide on character LoRA from CivitAI

---

## POC Tracking (10-15 Images)

### Scene Selection
- **Status:** ✅ **Completed**
- **Target:** 10-15 scenes from 3 locations
- **Selected scenes:** 15 scenes total
  - **Bedroom (5 scenes):** The Alarm, Sitting Up in Bed, Opening Blinds, Picking Out Clothes, Clothes Laid on Bed
  - **Bathroom (5 scenes):** Looking in Mirror, Brushing Teeth, Under Showerhead, Wiping Mirror, Applying Deodorant
  - **Kitchen (5 scenes):** Entering Kitchen, Scooping Coffee Grounds, Placing Bread in Toaster, Spreading Butter on Toast, Pouring Coffee into Mug
- **File:** config/scenes_poc.json ✅ Created

### Location References
**Bedroom:**
- Reference images generated: ❌ No
- Count: 0/3
- Path: assets/location_refs/bedroom_*.png

**Bathroom:**
- Reference images generated: ❌ No
- Count: 0/3
- Path: assets/location_refs/bathroom_*.png

**Kitchen:**
- Reference images generated: ❌ No
- Count: 0/3
- Path: assets/location_refs/kitchen_*.png

### Character LoRA
- **Strategy:** Use existing LoRA from CivitAI
- **Downloaded:** ❌ No
- **Tested:** ❌ No
- **Selected LoRA:** TBD
- **Path:** assets/lora_weights/

### ComfyUI Workflow
- **Configured:** ❌ No
- **Tested:** ❌ No
- **Exported to JSON:** ❌ No
- **Path:** config/comfyui_workflow.json

### Image Generation Progress
- **Generated:** 0/15 images
- **Success rate:** N/A
- **Failed:** 0
- **Path:** output/poc/

### Quality Evaluation
- **Character consistency score:** N/A (scale 1-10)
- **Location consistency score:** N/A (scale 1-10)
- **Educational value:** N/A (are objects clearly identifiable?)
- **Issues log:** None yet

---

## File Inventory

### Configuration Files

| File | Created | Last Updated | Status |
|------|---------|--------------|--------|
| config/scenes_poc.json | ✅ Yes | 2026-01-17 | **Created - 15 scenes** |
| config/character_profile.json | ✅ Yes | 2026-01-17 | **Created - Matt's profile** |
| config/locations.json | ✅ Yes | 2026-01-17 | **Created - 3 POC locations** |
| config/scenes_full.json | ❌ No | N/A | Future work (308 scenes) |
| config/lighting_presets.json | ❌ No | N/A | Optional, may not need |
| config/comfyui_workflow.json | ❌ No | N/A | To be created after workflow testing |

### Scripts

| File | Created | Tested | Status |
|------|---------|--------|--------|
| scripts/runpod_manager.py | ✅ Yes | ❌ No | **Created - needs API key to test** |
| scripts/remote_generate.py | ❌ No | ❌ No | Not created - next priority |
| scripts/generate_location_refs.py | ❌ No | ❌ No | Not created - next priority |
| scripts/check_consistency.py | ❌ No | ❌ No | Not created |
| scripts/remote_train_lora.py | ❌ No | ❌ No | Optional (if custom LoRA needed) |
| scripts/prepare_lora_dataset.py | ❌ No | ❌ No | Optional (if custom LoRA needed) |

### Assets

| Asset Type | Count | Path | Status |
|------------|-------|------|--------|
| Location references | 0/9 | assets/location_refs/ | Not generated |
| Character references | 0 | assets/character_refs/ | Not needed (using existing LoRA) |
| LoRA weights | 0 | assets/lora_weights/ | Not downloaded |

### Generated Images

| Type | Count | Path | Status |
|------|-------|------|--------|
| POC images | 0/15 | output/poc/ | Not generated |
| Full project images | 0/308 | output/full/ | Future work |

---

## Technical Setup

### RunPod GPU
- **API key configured:** ❌ No
- **Account created:** ❓ Unknown
- **Preferred GPU:** RTX 4090 (or RTX 3090)
- **Test connection:** ❌ Not tested

### ComfyUI
- **Installed on RunPod:** ❌ No
- **Version:** TBD
- **Models downloaded:**
  - RealVisXL V5.0: ❌ No
  - IP-Adapter Plus: ❌ No
  - ControlNet Depth: ❌ No (optional)

### Dependencies
- **Python version:** 3.10+ required
- **requirements.txt created:** ✅ Yes
- **Dependencies installed:** ❌ No
- **runpod library installed:** ❌ No

---

## Quality Metrics

### POC Success Criteria

- [ ] Matt is recognizable in 70%+ of images
- [ ] Objects are clearly identifiable for vocabulary learning
- [ ] Images look natural (minimal AI artifacts)
- [ ] Workflow is repeatable
- [ ] Cost < $5

### Measurements (To be filled after POC)

**Character Consistency:** N/A
- Scale: 1-10 (subjective assessment)
- Target: 7+
- Actual: TBD

**Location Consistency:** N/A
- Scale: 1-10 (subjective assessment)
- Target: 7+
- Actual: TBD

**Educational Value:** N/A
- Can a child identify the objects? Yes/No per image
- Target: 80%+ yes
- Actual: TBD

**Technical Quality:** N/A
- AI artifacts: Count of images with hands, faces, or other artifacts
- Target: < 20%
- Actual: TBD

### Issues Log

| Date | Issue | Impact | Resolution | Status |
|------|-------|--------|------------|--------|
| N/A | No issues yet | N/A | N/A | N/A |

---

## Next Steps

### Immediate Actions (Prioritized)

1. **Read matt_daily_life_scenes.md** - Understand the 308 scenes
2. **Select 10-15 POC scenes** - Choose bedroom, bathroom, kitchen scenes
3. **Create config/scenes_poc.json** - Structure selected scenes as JSON
4. **Create config/character_profile.json** - Extract Matt's description
5. **Create config/locations.json** - Define 3 POC locations
6. **Write scripts/runpod_manager.py** - RunPod API wrapper
7. **Write scripts/remote_generate.py** - Automated generation script

### Decisions Needed

- [ ] Which specific 10-15 scenes to include in POC?
- [ ] Which character LoRA to use from CivitAI?
- [ ] Should we include ControlNet Depth or skip for POC?
- [ ] What image resolution? (1024x1024 or 1024x768?)

### Questions for User

- Do you have a RunPod account and API key?
- Any preference for which scenes to include in POC?
- Any specific requirements for image format/resolution?

---

## Timeline

### Milestones

| Milestone | Target Date | Actual Date | Status |
|-----------|-------------|-------------|--------|
| Project setup complete | 2026-01-17 | 2026-01-17 | ✅ Done |
| Config files created | 2026-01-17 | 2026-01-17 | ✅ Done |
| RunPod scripts written | 2026-01-17 | 2026-01-17 | 🔶 Partial (runpod_manager.py done) |
| Location refs generated | 2026-01-18 | TBD | ⏳ Pending |
| ComfyUI workflow setup | 2026-01-18 | TBD | ⏳ Pending |
| POC images generated | 2026-01-18 | TBD | ⏳ Pending |
| Quality evaluation | 2026-01-19 | TBD | ⏳ Pending |
| POC decision | 2026-01-19 | TBD | ⏳ Pending |

### Time Tracking

**Estimated POC Time:** 7-11 hours total
- Your time: 3.5-5.5 hours
- Claude Code time: 4-6 hours
- GPU time: 2-3 hours (automated)

**Actual Time:** TBD

---

## Cost Tracking

### Estimated Costs

**POC:**
- GPU time: 3-7 hours × $0.50/hour = **$1.50-$3.50**
- Total: **$1.50-$3.50**

**Full Project (if POC succeeds):**
- GPU time: 15-20 hours × $0.50/hour = **$7.50-$10.00**
- Total: **$7.50-$10.00**

### Actual Costs

| Date | Task | GPU Hours | Cost | Notes |
|------|------|-----------|------|-------|
| N/A | No costs yet | 0 | $0.00 | N/A |

**Total Spent:** $0.00

---

## Notes & Observations

### Session Notes

**2026-01-17 - Initial Setup & Configuration Complete**
- ✅ Created full project directory structure
- ✅ Initialized git repository with first commit
- ✅ Created comprehensive documentation (CLAUDE.md, STATUS.md, README.md)
- ✅ Created requirements.txt and .gitignore
- ✅ **Selected 15 POC scenes** from matt_daily_life_scenes.md (bedroom, bathroom, kitchen)
- ✅ **Created config/scenes_poc.json** with detailed prompts and metadata for all 15 scenes
- ✅ **Created config/character_profile.json** with Matt's appearance, prompt templates, LoRA settings
- ✅ **Created config/locations.json** with 3 POC locations and generation parameters
- ✅ **Created scripts/runpod_manager.py** - RunPod API wrapper for pod management

**Progress:** All configuration complete. Ready for RunPod API testing and image generation once API key is provided.

**Next Session:**
- Get RunPod API key and test connection
- Create remaining automation scripts (remote_generate.py, generate_location_refs.py)
- Generate location references
- Download character LoRA from CivitAI
- Begin ComfyUI workflow testing

### Learnings

- TBD (will be filled as we progress)

### Improvements for Next Time

- TBD (will be filled based on POC results)

---

**End of STATUS.md** - Updated 2026-01-17
