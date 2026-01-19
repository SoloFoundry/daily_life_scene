# Automated Image Generation Pipeline

---

## PROJECT CONTEXT (For Continuation)

### What This Project Is

This is an **educational visual content generation project** aimed at helping learners become familiar with everyday settings, objects, and associated vocabulary through realistic images. The learner should be able to:

1. **Identify objects visually** — See a toothbrush, coffee maker, steering wheel, office desk, etc.
2. **Associate words with objects** — Learn vocabulary tied to real-world items
3. **Understand context** — See objects in their natural environment (toothbrush in bathroom, not floating in space)

### Target Audience

- Children learning vocabulary
- Adults learning a new language (ESL, etc.)
- People with special learning needs
- Anyone needing visual-vocabulary association

### Content Strategy

The project generates **realistic images depicting a full day in the life of a character**, showing them interacting with everyday objects in familiar settings. This provides:

- **Natural context** for each object
- **Logical sequence** (morning routine → commute → work → evening)
- **Repetition of locations** (bedroom appears morning and night, reinforcing learning)

### Scope & Scalability

**Starting point:** One character (Matt, 25-year-old white male American office worker)

**Future expansion planned:**
- Different age groups (children, elderly)
- Different genders (female characters)
- Different careers (street vendor, musician, tourist guide, nurse, construction worker, etc.)
- Different cultural contexts (European, Asian, Latin American settings)
- Different scenarios (weekends, holidays, special occasions)

The pipeline is designed so that once built, adding new characters/scenarios requires only:
1. Training a new character LoRA (if appearance changes)
2. Creating new scene descriptions
3. Running the generation script

Location assets can be reused across many character variants.

---

## KEY DECISIONS MADE

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Image style | **High-quality anime** | Child-friendly, faster development, clear object identification |
| Perspective | **Third-person POV** | Character visible interacting with objects |
| Geographic setting | **American suburban** | Starting point; will diversify later |
| Scene granularity | **Extremely detailed** | Every small action gets its own image |
| Scene count | **308 scenes** for first character | Comprehensive day coverage |
| Generation method | **Stable Diffusion (local)** | Free, scalable to thousands of images |
| Automation | **Fully automated pipeline** | No manual intervention during generation |
| Cost | **$0** | All free/open-source tools |
| Location consistency | **Blender 3D renders + ControlNet** | Same room looks the same across all scenes |
| Character consistency | **LoRA training** | Same person looks the same across all scenes |

---

## COMPANION DOCUMENT

This pipeline document works together with:

**📄 `matt_daily_life_scenes.md`** — Contains 308 detailed scene descriptions for Matt's full day

That document includes:
- Character profile (Matt's appearance, home, job, car, etc.)
- Scene-by-scene descriptions organized by time of day
- Each scene has: time, setting, lighting, detailed description, objects present
- Appendix with scenes organized by location and time period
- Usage notes for Stable Diffusion prompt optimization

**Relationship between documents:**
- `matt_daily_life_scenes.md` = **WHAT** to generate (content)
- `image_generation_pipeline.md` (this file) = **HOW** to generate (infrastructure)

---

## CURRENT CHARACTER: MATT

| Attribute | Value |
|-----------|-------|
| Name | Matt |
| Age | 25 |
| Gender | Male |
| Ethnicity | White |
| Hair | Short brown |
| Build | Average |
| Facial hair | Clean-shaven |
| Home | One-bedroom apartment, suburban complex |
| Location | Suburbs of mid-sized American city |
| Job | Junior marketing coordinator |
| Workplace | "Vertex Marketing" in suburban business park |
| Car | Silver 2019 Honda Civic sedan |
| Lives with | Alone, no pets |
| Work attire | Business casual (oxford shirts, chinos, brown leather shoes) |
| Home attire | Gray t-shirt, navy sweatpants |
| Sleep attire | Gray t-shirt, navy pajama pants |

---

## WHAT HAS BEEN COMPLETED

✅ **Scene descriptions** — 308 scenes fully written in `matt_daily_life_scenes.md`
✅ **Pipeline architecture** — Designed and documented (this file)
✅ **Tool selection** — All free tools identified
✅ **Directory structure** — Defined
✅ **Location requirements** — 19 locations with camera angles and objects listed
✅ **Lighting presets** — Time-of-day modifiers defined

---

## WHAT STILL NEEDS TO BE DONE

### Files to Create (Claude can help with these)

| File | Description | Status |
|------|-------------|--------|
| `scenes.json` | Structured data version of all 308 scenes | ❌ Not created |
| `locations.json` | Metadata for all 19 locations | ❌ Not created |
| `lighting_presets.json` | Time-of-day prompt modifiers | ❌ Not created |
| `prompts.json` | Prompt templates and negative prompts | ❌ Not created |
| `generate_all.py` | Main automation script | ❌ Not created |
| `comfyui_api.py` | ComfyUI API wrapper | ❌ Not created |
| `comfyui_workflow.json` | Base ComfyUI workflow template | ❌ Not created |
| `requirements.txt` | Python dependencies | ❌ Not created |

### Manual Setup Required (User must do)

| Task | Description |
|------|-------------|
| Install software | ComfyUI, Blender, Kohya_ss, Python |
| Download models | RealVisXL, IP-Adapter, ControlNet |
| Create Blender scenes | Model 19 locations, render base images + depth maps |
| Train Matt LoRA | Generate reference images, train with Kohya_ss |
| Test pipeline | Run single scene before full batch |

---

## HOW TO CONTINUE THIS PROJECT

When starting a new chat with Claude, provide:

1. **This file** (`image_generation_pipeline.md`) — for pipeline context
2. **Scene file** (`matt_daily_life_scenes.md`) — for scene content
3. **Your request** — e.g., "Create the scenes.json file" or "Write the generate_all.py script"

Claude will have full context to continue building the automation infrastructure.

---

## QUICK REFERENCE: SCENE COUNTS BY LOCATION

| Location | Scene Count | Notes |
|----------|-------------|-------|
| Bedroom | ~25 | Morning + night |
| Bathroom | ~30 | Morning + night routines |
| Kitchen | ~35 | Breakfast + dinner |
| Living room | ~15 | Evening relaxation |
| Apartment hallway/lobby | ~10 | Coming and going |
| Parking lot | ~10 | Apartment complex |
| Car interior | ~40 | Commute both ways |
| Coffee drive-through | ~10 | Morning stop |
| Office cubicle | ~50 | Main work scenes |
| Conference room | ~8 | Meeting |
| Break room | ~5 | Water cooler, coffee |
| Sandwich shop | ~15 | Lunch |
| Grocery store | ~12 | Evening errand |
| Other (streets, highways, exteriors) | ~20+ | Transitions |

---

## END OF CONTEXT SECTION

---

## Overview

A fully free, fully automated pipeline for generating thousands of consistent educational images depicting daily life scenes. Once set up, the entire generation process runs unattended.

---

## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            ONE-TIME SETUP PHASE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │    BLENDER      │    │    KOHYA_SS     │    │    COMFYUI      │         │
│  │                 │    │                 │    │                 │         │
│  │  Create 3D      │    │  Train LoRA     │    │  Build reusable │         │
│  │  locations      │    │  for character  │    │  workflow       │         │
│  │  Render depth   │    │  consistency    │    │  template       │         │
│  │  maps + base    │    │                 │    │                 │         │
│  │  images         │    │                 │    │                 │         │
│  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘         │
│           │                      │                      │                   │
│           ▼                      ▼                      ▼                   │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │                      REFERENCE ASSETS                            │       │
│  │                                                                  │       │
│  │   /assets/locations/          /assets/character/                 │       │
│  │   ├── bedroom/                ├── matt_lora.safetensors         │       │
│  │   │   ├── base.png            └── reference_images/             │       │
│  │   │   ├── depth.png                                             │       │
│  │   │   └── angles/                                               │       │
│  │   ├── bathroom/                                                 │       │
│  │   ├── kitchen/                                                  │       │
│  │   ├── car_interior/                                             │       │
│  │   ├── office_cubicle/                                           │       │
│  │   └── ...                                                       │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         AUTOMATED GENERATION PHASE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐                                                        │
│  │  scenes.json    │ ◄── Structured data for all 308 scenes                │
│  │                 │     - scene_id                                        │
│  │  [              │     - location_id                                     │
│  │    {            │     - time_of_day                                     │
│  │      scene_001  │     - lighting                                        │
│  │    },           │     - camera_angle                                    │
│  │    ...          │     - prompt                                          │
│  │  ]              │     - objects                                         │
│  └────────┬────────┘                                                        │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │                    generate_all.py                               │       │
│  │                                                                  │       │
│  │   1. Load scenes.json                                           │       │
│  │   2. For each scene:                                            │       │
│  │      a. Select location reference + depth map                   │       │
│  │      b. Build full prompt with lighting/time modifiers          │       │
│  │      c. Modify ComfyUI workflow template                        │       │
│  │      d. Send to ComfyUI API                                     │       │
│  │      e. Poll for completion                                     │       │
│  │      f. Save output image                                       │       │
│  │      g. Log progress                                            │       │
│  │   3. Handle errors, retries, resume from checkpoint             │       │
│  │                                                                  │       │
│  └────────┬────────────────────────────────────────────────────────┘       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │                      ComfyUI (API Mode)                          │       │
│  │                                                                  │       │
│  │   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐        │       │
│  │   │  Load   │──▶│  LoRA   │──▶│ IP-Adapt│──▶│ Control │        │       │
│  │   │  Model  │   │ (Matt)  │   │ (Locat.)│   │   Net   │        │       │
│  │   └─────────┘   └─────────┘   └─────────┘   └─────────┘        │       │
│  │                                                   │              │       │
│  │                                                   ▼              │       │
│  │   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐        │       │
│  │   │  Save   │◀──│  VAE    │◀──│ KSample │◀──│ Prompt  │        │       │
│  │   │  Image  │   │ Decode  │   │   r     │   │ Encode  │        │       │
│  │   └─────────┘   └─────────┘   └─────────┘   └─────────┘        │       │
│  │                                                                  │       │
│  └──────────────────────────────────────────────────────────────────┘       │
│                                                                             │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │                         OUTPUT                                   │       │
│  │                                                                  │       │
│  │   /output/                                                       │       │
│  │   ├── scene_001_bedroom_alarm.png                               │       │
│  │   ├── scene_002_bedroom_reaching_phone.png                      │       │
│  │   ├── scene_003_bedroom_sitting_up.png                          │       │
│  │   ├── ...                                                        │       │
│  │   └── scene_308_bedroom_sleeping.png                            │       │
│  │                                                                  │       │
│  │   /logs/                                                         │       │
│  │   ├── generation.log                                            │       │
│  │   ├── errors.log                                                │       │
│  │   └── checkpoint.json  (for resume capability)                  │       │
│  │                                                                  │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Required Software (All Free)

| Software | Version | Purpose | Source |
|----------|---------|---------|--------|
| **Python** | 3.10+ | Automation scripting | python.org |
| **ComfyUI** | Latest | Image generation engine | github.com/comfyanonymous/ComfyUI |
| **Blender** | 3.6+ | 3D modeling & rendering | blender.org |
| **Kohya_ss** | Latest | LoRA training | github.com/bmaltais/kohya_ss |
| **Git** | Latest | Repository cloning | git-scm.com |

### Required ComfyUI Extensions (Free)

| Extension | Purpose |
|-----------|---------|
| **ComfyUI-Manager** | Easy extension installation |
| **ComfyUI_IPAdapter_plus** | Location reference consistency |
| **ComfyUI-ControlNet** | Depth/structure consistency |
| **ComfyUI-AnimateDiff** | Optional: for future animation |

### Required Models (Free Downloads)

| Model | Type | Source |
|-------|------|--------|
| **Animagine XL 3.1** or **CounterfeitXL** | Base anime model | CivitAI |
| **IP-Adapter Plus SDXL** | Style/location consistency | Hugging Face |
| **ControlNet Depth SDXL** | Spatial consistency | Hugging Face |

**Why Anime Style?**
- Faster development time (less demanding consistency requirements)
- Child-friendly aesthetic that appeals to target audience
- Clean lines make vocabulary objects clearly identifiable
- Large community of free anime models and LoRAs
- More forgiving of minor character inconsistencies

---

## Directory Structure

```
project_root/
│
├── assets/
│   ├── locations/
│   │   ├── bedroom/
│   │   │   ├── base_wide.png           # Hero image of empty room
│   │   │   ├── base_closeup.png        # Closeup angle
│   │   │   ├── depth_wide.png          # Depth map for wide angle
│   │   │   ├── depth_closeup.png       # Depth map for closeup
│   │   │   └── blender/
│   │   │       └── bedroom.blend       # Source Blender file
│   │   │
│   │   ├── bathroom/
│   │   │   ├── base_sink.png
│   │   │   ├── base_shower.png
│   │   │   ├── base_full.png
│   │   │   ├── depth_sink.png
│   │   │   ├── depth_shower.png
│   │   │   ├── depth_full.png
│   │   │   └── blender/
│   │   │       └── bathroom.blend
│   │   │
│   │   ├── kitchen/
│   │   ├── living_room/
│   │   ├── apartment_hallway/
│   │   ├── apartment_lobby/
│   │   ├── parking_lot/
│   │   ├── car_interior/
│   │   ├── suburban_street/
│   │   ├── highway/
│   │   ├── coffee_drive_through/
│   │   ├── office_lobby/
│   │   ├── office_elevator/
│   │   ├── office_cubicle/
│   │   ├── office_hallway/
│   │   ├── conference_room/
│   │   ├── break_room/
│   │   ├── business_park_exterior/
│   │   ├── sandwich_shop/
│   │   └── grocery_store/
│   │
│   └── character/
│       ├── matt_lora.safetensors       # Trained LoRA
│       ├── matt_reference.png          # Primary reference image
│       └── training_images/            # Images used to train LoRA
│           ├── 01.png
│           ├── 02.png
│           └── ...
│
├── config/
│   ├── scenes.json                     # All scene definitions
│   ├── locations.json                  # Location metadata
│   ├── prompts.json                    # Prompt templates
│   ├── lighting_presets.json           # Time-of-day lighting modifiers
│   └── comfyui_workflow.json           # Base workflow template
│
├── scripts/
│   ├── generate_all.py                 # Main generation script
│   ├── comfyui_api.py                  # ComfyUI API wrapper
│   ├── scene_processor.py              # Scene data processing
│   ├── prompt_builder.py               # Dynamic prompt construction
│   ├── blender_render.py               # Blender automation (optional)
│   └── utils.py                        # Helper functions
│
├── output/
│   ├── images/                         # Generated images
│   └── metadata/                       # Image metadata JSONs
│
├── logs/
│   ├── generation.log                  # Full generation log
│   ├── errors.log                      # Error tracking
│   └── checkpoint.json                 # Resume state
│
└── requirements.txt                    # Python dependencies
```

---

## Phase 1: One-Time Setup

### Step 1.1: Install Software

```bash
# Clone ComfyUI
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
pip install -r requirements.txt

# Clone Kohya_ss for LoRA training
git clone https://github.com/bmaltais/kohya_ss.git
cd kohya_ss
pip install -r requirements.txt

# Download Blender from blender.org (manual install)

# Install Python dependencies for automation
pip install requests websocket-client pillow numpy
```

### Step 1.2: Download Models

```bash
# Create model directories
mkdir -p ComfyUI/models/checkpoints
mkdir -p ComfyUI/models/loras
mkdir -p ComfyUI/models/controlnet
mkdir -p ComfyUI/models/ipadapter

# Download from CivitAI (manual - requires browser):
# - RealVisXL V5.0 → ComfyUI/models/checkpoints/
# - IP-Adapter models → ComfyUI/models/ipadapter/
# - ControlNet Depth → ComfyUI/models/controlnet/
```

### Step 1.3: Create Location Assets in Blender

For each location, create:
1. **3D scene** with all required objects
2. **Multiple camera angles** as needed
3. **Render outputs:**
   - Base image (for IP-Adapter reference)
   - Depth map (for ControlNet)

See [Location Asset Requirements](#location-asset-requirements) below.

### Step 1.4: Train Character LoRA

1. **Generate reference images** of Matt using Stable Diffusion:
   - 15-20 images
   - Various angles (front, side, 3/4)
   - Consistent appearance
   - Neutral background

2. **Train LoRA using Kohya_ss:**
   ```bash
   # Example training command (adjust paths)
   accelerate launch train_network.py \
     --pretrained_model_name_or_path="realvisxl_v5.safetensors" \
     --train_data_dir="./training_images" \
     --output_dir="./output" \
     --output_name="matt_lora" \
     --resolution=1024 \
     --train_batch_size=1 \
     --max_train_epochs=10 \
     --network_module=networks.lora \
     --network_dim=32 \
     --network_alpha=16
   ```

### Step 1.5: Build ComfyUI Workflow

Create a workflow that includes:
- Checkpoint loader
- LoRA loader (for Matt)
- IP-Adapter (for location reference)
- ControlNet (for depth map)
- KSampler
- VAE Decode
- Save Image

Export as API-compatible JSON.

---

## Phase 2: Automated Generation

### Step 2.1: Scene Data Structure

Each scene in `scenes.json`:

```json
{
  "scene_id": "001",
  "scene_name": "the_alarm",
  "location_id": "bedroom",
  "location_angle": "wide",
  "time_of_day": "6:45 AM",
  "lighting": "dim_blue_predawn",
  "camera_angle": "from_foot_of_bed",
  "character_action": "lying_in_bed_sleeping",
  "character_clothing": "gray_tshirt_navy_pajama_pants",
  "objects_focus": ["smartphone_alarm", "nightstand", "digital_clock", "water_glass", "lamp"],
  "prompt_base": "A 25-year-old white man with short brown hair lies in bed under a navy blue comforter, eyes closed, face peaceful in sleep. On the wooden nightstand beside him, a smartphone screen glows brightly displaying 6:45 AM alarm.",
  "prompt_environment": "Bedroom with light gray walls, white horizontal blinds slightly open, thin strips of pale blue early morning light falling across the bed.",
  "negative_prompt": "bad anatomy, blurry, low quality, distorted face, extra limbs"
}
```

### Step 2.2: Generation Script Flow

```python
# Simplified flow (generate_all.py)

def main():
    # Load configurations
    scenes = load_json("config/scenes.json")
    locations = load_json("config/locations.json")
    workflow_template = load_json("config/comfyui_workflow.json")
    checkpoint = load_checkpoint()
    
    # Start from last checkpoint if resuming
    start_index = checkpoint.get("last_completed", -1) + 1
    
    for i, scene in enumerate(scenes[start_index:], start=start_index):
        try:
            # Get location assets
            location = locations[scene["location_id"]]
            reference_image = location["angles"][scene["location_angle"]]["base"]
            depth_map = location["angles"][scene["location_angle"]]["depth"]
            
            # Build full prompt
            prompt = build_prompt(scene)
            
            # Modify workflow
            workflow = customize_workflow(
                template=workflow_template,
                prompt=prompt,
                negative_prompt=scene["negative_prompt"],
                reference_image=reference_image,
                depth_map=depth_map,
                lora_strength=0.8,
                controlnet_strength=0.7,
                ip_adapter_strength=0.6
            )
            
            # Generate image
            image = generate_image(workflow)
            
            # Save
            output_path = f"output/images/scene_{scene['scene_id']}_{scene['scene_name']}.png"
            save_image(image, output_path)
            
            # Update checkpoint
            save_checkpoint({"last_completed": i})
            
            log_progress(i, len(scenes), scene["scene_id"])
            
        except Exception as e:
            log_error(scene["scene_id"], e)
            continue

if __name__ == "__main__":
    main()
```

### Step 2.3: Running Generation

```bash
# Start ComfyUI in API mode
cd ComfyUI
python main.py --listen 127.0.0.1 --port 8188

# In another terminal, run generation
cd project_root
python scripts/generate_all.py
```

### Step 2.4: Monitoring Progress

The script creates:
- `logs/generation.log` — Real-time progress
- `logs/errors.log` — Any failed generations
- `logs/checkpoint.json` — Resume point if interrupted

---

## Location Asset Requirements

### Required Locations (19 Total)

| Location ID | Angles Needed | Objects to Model |
|-------------|---------------|------------------|
| `bedroom` | wide, closeup_nightstand, at_closet, mirror_view | bed, nightstand, lamp, phone, blinds, dresser, closet, mirror, laundry basket |
| `bathroom` | full, at_sink, at_shower, mirror_view | sink, toilet, shower, mirror, towel bar, bath mat, toiletries |
| `kitchen` | full, at_counter, at_stove, at_fridge, at_breakfast_bar | cabinets, counter, stove, fridge, coffee maker, toaster, sink, breakfast bar, stools |
| `living_room` | full, at_couch, at_tv, at_door | sofa, coffee table, TV, bookshelf, sliding doors, armchair |
| `apartment_hallway` | corridor, at_elevator, at_door | carpet, doors, light fixtures, small table |
| `apartment_lobby` | full, at_mailboxes, at_entrance | mailboxes, chairs, front desk, glass doors |
| `parking_lot` | wide, at_car, walking | asphalt, parking lines, cars, building exterior, trees |
| `car_interior` | driver_seat, dashboard, rearview | steering wheel, dashboard, seats, mirrors, cup holders |
| `suburban_street` | driving_pov | houses, trees, parked cars, sidewalks |
| `highway` | driving_pov, on_ramp | multiple lanes, signs, barriers, other cars |
| `coffee_drive_through` | at_menu, at_window | menu board, speaker, pickup window, building |
| `office_lobby` | full, at_elevator | reception desk, seating, directory, elevators |
| `office_elevator` | interior | buttons, handrail, mirror |
| `office_cubicle` | at_desk, wide | desk, monitors, chair, partitions, phone, personal items |
| `office_hallway` | corridor | doors, nameplates, carpet |
| `conference_room` | full, at_table | table, chairs, screen/TV, whiteboard |
| `break_room` | full, at_counter | water cooler, coffee maker, fridge, microwave, table |
| `sandwich_shop` | full, at_counter, at_table | counter, menu board, tables, chairs |
| `grocery_store` | entrance, produce, aisle, checkout | shelves, products, carts, registers |

### Blender Workflow for Each Location

1. **Model the space** — Use simple geometry, focus on recognizable shapes
2. **Add materials** — Basic colors and textures (don't need photorealism)
3. **Set up cameras** — One for each required angle
4. **Configure depth output** — Enable Z-depth pass in render settings
5. **Render both outputs** — Color render + depth map for each angle

### Free 3D Asset Sources

| Source | URL | Best For |
|--------|-----|----------|
| BlenderKit | blenderkit.com | Furniture, props |
| Sketchfab | sketchfab.com (filter: downloadable) | Various |
| Polyhaven | polyhaven.com | HDRIs, textures |
| CGTrader | cgtrader.com (filter: free) | Furniture |
| TurboSquid | turbosquid.com (filter: free) | Various |
| Blend Swap | blendswap.com | Blender-ready files |

---

## Lighting Presets

Time-of-day affects prompt modifiers:

```json
{
  "dim_blue_predawn": {
    "time_range": "6:00-7:00",
    "prompt_modifier": "dim blue pre-dawn light filtering through blinds, soft shadows",
    "negative_modifier": "bright sunlight, harsh shadows"
  },
  "bright_morning": {
    "time_range": "7:00-9:00",
    "prompt_modifier": "bright warm morning sunlight streaming through windows, golden hour glow",
    "negative_modifier": "dim, dark, blue light"
  },
  "midday_indoor": {
    "time_range": "10:00-14:00",
    "prompt_modifier": "bright even indoor lighting, fluorescent office lights, neutral white light",
    "negative_modifier": "dramatic shadows, warm sunset"
  },
  "midday_outdoor": {
    "time_range": "10:00-14:00",
    "prompt_modifier": "bright midday sun overhead, short shadows, clear blue sky",
    "negative_modifier": "long shadows, golden hour"
  },
  "afternoon_golden": {
    "time_range": "16:00-18:00",
    "prompt_modifier": "warm golden afternoon light, long shadows, sunset approaching",
    "negative_modifier": "harsh midday sun, blue light"
  },
  "evening_indoor": {
    "time_range": "19:00-22:00",
    "prompt_modifier": "warm indoor lamp light, cozy evening ambiance, soft artificial lighting",
    "negative_modifier": "bright sunlight, daylight"
  },
  "night_indoor": {
    "time_range": "22:00-6:00",
    "prompt_modifier": "dim bedroom, nightstand lamp glow, ambient darkness",
    "negative_modifier": "bright light, daylight"
  }
}
```

---

## Estimated Generation Time

| Hardware | Time per Image | 308 Images | 1000 Images |
|----------|----------------|------------|-------------|
| RTX 3060 (12GB) | ~45 sec | ~4 hours | ~12.5 hours |
| RTX 3080 (10GB) | ~30 sec | ~2.5 hours | ~8.3 hours |
| RTX 4090 (24GB) | ~15 sec | ~1.3 hours | ~4.2 hours |
| RTX 3050 (8GB) | ~90 sec | ~7.7 hours | ~25 hours |

*Times assume SDXL model at 1024x1024 resolution*

---

## Error Handling & Recovery

The automation script includes:

1. **Automatic retry** — Failed generations retry up to 3 times
2. **Checkpoint system** — Progress saved after each image; resume from any point
3. **Error logging** — Detailed logs for debugging
4. **Batch validation** — Post-generation check for missing/corrupted images

---

## Scaling to Other Characters

To add new character variants (female, different careers, etc.):

1. **Train new LoRA** for each character appearance
2. **Update `scenes.json`** with character-specific details:
   - Clothing appropriate to character
   - Actions/poses appropriate to context
3. **Run generation** with new LoRA selected

The location assets remain unchanged — only the character LoRA and prompts need updating.

---

## Future Enhancements

| Enhancement | Benefit | Complexity |
|-------------|---------|------------|
| Add AnimateDiff | Generate short video clips | Medium |
| Multiple characters in scene | More realistic scenarios | High |
| Weather variations | Rainy day, snowy day | Low |
| Regional variations | European, Asian settings | Medium (new location assets) |
| Voice narration | Audio descriptions | Low (separate tool) |

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Character looks different across images | LoRA not applied consistently | Increase LoRA strength (0.7-0.9) |
| Location changes between scenes | IP-Adapter weight too low | Increase IP-Adapter strength (0.6-0.8) |
| Composition doesn't match | ControlNet not working | Check depth map quality, increase strength |
| Out of VRAM | Image too large or batch size | Reduce resolution or use tiled VAE |
| ComfyUI API not responding | Server not started | Ensure ComfyUI running with `--listen` flag |
| Generation hangs | Workflow error | Check ComfyUI console for errors |

---

## Quick Start Checklist

- [ ] Install Python 3.10+
- [ ] Clone and set up ComfyUI
- [ ] Install ComfyUI extensions (Manager, IPAdapter, ControlNet)
- [ ] Download base model (RealVisXL or Realistic Vision)
- [ ] Download IP-Adapter and ControlNet models
- [ ] Install Blender
- [ ] Clone Kohya_ss for LoRA training
- [ ] Create location assets in Blender (start with bedroom, bathroom, kitchen)
- [ ] Generate and train character LoRA
- [ ] Set up project directory structure
- [ ] Configure scenes.json
- [ ] Build ComfyUI workflow template
- [ ] Test single scene generation
- [ ] Run full batch generation

---

## Summary

This pipeline enables fully automated generation of thousands of consistent educational images:

- **One-time setup:** ~1-2 days (modeling locations, training LoRA, configuring workflow)
- **Ongoing generation:** Fully automated, runs unattended
- **Cost:** $0 (all free tools)
- **Scalability:** Easy to add new characters, locations, scenarios
- **Consistency:** Location references + LoRA ensure visual continuity

Once the initial setup is complete, generating images for new characters or expanded scenarios requires only updating the scene data and running the script.
