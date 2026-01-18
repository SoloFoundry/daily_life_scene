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
├── scripts/                     # Automation scripts
│   └── runpod_manager.py        # RunPod API wrapper
│
├── matt_wm_25_yo/               # Matt's character directory
│   ├── matt_daily_life_scenes.md   # Matt's ~308 scene descriptions
│   ├── config/                  # Matt's config files
│   │   ├── scenes_poc.json      # 15 POC scenes
│   │   ├── character_profile.json # Matt's appearance
│   │   └── locations.json       # 3 POC locations
│   ├── assets/                  # Matt's generated assets
│   │   ├── location_refs/       # Location references
│   │   ├── character_refs/      # Character references
│   │   └── lora_weights/        # LoRA model weights
│   └── images/                  # Matt's generated images
│       ├── poc/                 # POC images (15)
│       └── full/                # Full project (308)
│
└── catalina_lf_21_yo/           # Catalina's character directory
    ├── catalina_daily_life_scenes.md # Catalina's ~280 scene descriptions
    ├── config/                  # Catalina's config files (to be created)
    ├── assets/                  # Catalina's generated assets
    │   ├── location_refs/       # Location references
    │   ├── character_refs/      # Character references
    │   └── lora_weights/        # LoRA model weights
    └── images/                  # Catalina's generated images
        ├── poc/                 # POC images (15)
        └── full/                # Full project (~280)
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
- **[matt_wm_25_yo/matt_daily_life_scenes.md](matt_wm_25_yo/matt_daily_life_scenes.md)** - Matt's 308 scene descriptions (American professional)
- **[catalina_lf_21_yo/catalina_daily_life_scenes.md](catalina_lf_21_yo/catalina_daily_life_scenes.md)** - Catalina's ~280 scene descriptions (Colombian student)
- **[image_generation_pipeline.md](image_generation_pipeline.md)** - Technical pipeline details

## Current Status

**Phase**: POC Configuration Complete + Multi-Character Template ✅
**Progress**:
- ✅ 15 scenes selected and configured (Matt)
- ✅ Character profile created (Matt)
- ✅ 3 locations configured (Matt)
- ✅ RunPod API wrapper created
- ✅ Multi-character template created (Catalina - Colombian student)
- ⏳ Next: API testing and image generation

**What's Done:**
- All project configuration files created for Matt
- RunPod automation framework ready
- Git repository initialized with first commit
- Multi-character expansion demonstrated with Catalina template
- Project now supports diverse characters, cultures, and demographics

**What's Next:**
- Get RunPod API key and test connection
- Generate 9 location reference images for Matt
- Download character LoRA from CivitAI
- Set up ComfyUI workflow and generate 15 POC images for Matt
- If successful, create POC configs for Catalina

See [STATUS.md](STATUS.md) for detailed progress.

## Contributing

This is an educational content generation project. Feel free to adapt for your own characters and scenarios!

## License

Educational use only.

---

**Created with** [Claude Code](https://claude.com/claude-code)
