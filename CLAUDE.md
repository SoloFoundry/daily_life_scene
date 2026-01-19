# Daily Life Visual Vocabulary Generator - Project Context

**Last Updated:** 2026-01-17
**Current Phase:** POC Setup
**Status:** See [STATUS.md](STATUS.md) for real-time progress

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Educational Goals & Pedagogy](#educational-goals--pedagogy)
3. [Technical Architecture](#technical-architecture)
4. [Content Specification](#content-specification)
5. [Current Phase & Status](#current-phase--status)
6. [Key Decisions & Constraints](#key-decisions--constraints)
7. [File Structure & Organization](#file-structure--organization)
8. [Common Tasks & Commands](#common-tasks--commands)
9. [Troubleshooting](#troubleshooting)

---

## Project Overview

### What is this project?

An automated pipeline to generate **308 high-quality anime illustrations** depicting a character named "Matt" going through a typical workday. These images will be used as **visual vocabulary flashcards** for children and ESL students learning English.

### Why does this exist?

**Problem:** Traditional vocabulary flashcards show objects in isolation (e.g., a toothbrush on a white background).

**Solution:** Show objects in their natural context - a toothbrush in a bathroom, being used during a morning routine. This **contextual learning** approach:
- Helps learners associate words with real-world situations
- Provides cultural context automatically
- Creates narrative coherence that aids memory retention
- Demonstrates object usage and purpose

### Target Audience

- **Primary:** Children (ages 5-12) learning English
- **Secondary:** ESL (English as a Second Language) students of all ages
- **Distribution:** Flashcards in an existing mobile app (already built by user)

### Educational Outcomes

Students will learn:
- **Vocabulary:** 200+ everyday objects (toothbrush, coffee mug, car keys, etc.)
- **Actions:** Common daily activities (brushing teeth, making coffee, driving, etc.)
- **Context:** When and where objects are used
- **Cultural norms:** Western daily routines and living spaces

---

## Educational Goals & Pedagogy

### Contextual Learning Approach

**Core Principle:** "Show, don't tell" - demonstrate objects in use rather than in isolation.

**Example:**
- ❌ **Traditional flashcard:** Picture of a toothbrush on white background → "toothbrush"
- ✅ **Our approach:** Matt brushing his teeth in his bathroom → "toothbrush," "bathroom," "brushing," "mirror," "sink"

### Sequential Storytelling

Following Matt through his day creates a **narrative arc** that:
- Makes learning memorable through story
- Shows temporal relationships (breakfast before work, dinner after work)
- Demonstrates routines and sequences
- Provides natural repetition (bedroom appears multiple times)

### Repetition with Variation

**Key locations appear multiple times** in different contexts:
- Bedroom: Morning (waking up), evening (getting ready for bed)
- Kitchen: Breakfast, dinner, cleanup
- Bathroom: Morning routine, evening routine

This reinforces learning while showing different uses and states.

### Vocabulary Categories Covered

- **Bedroom:** bed, pillow, alarm clock, closet, dresser, nightstand
- **Bathroom:** sink, toilet, shower, mirror, toothbrush, towel, shampoo
- **Kitchen:** stove, refrigerator, coffee maker, microwave, dishes, table
- **Living room:** sofa, TV, remote, coffee table, lamp
- **Office:** desk, computer, chair, phone, papers, pen
- **Car:** steering wheel, keys, seatbelt, dashboard
- **Clothing:** shirt, pants, shoes, jacket, tie, watch
- **Food:** breakfast, lunch, dinner, snacks, drinks
- **Actions:** walking, sitting, standing, eating, drinking, driving, working, sleeping

---

## Technical Architecture

### Infrastructure

**GPU Provider:** RunPod (cloud GPU rental)
**GPU Type:** RTX 4090 or RTX 3090 (recommended)
**Image Generation:** Stable Diffusion via ComfyUI
**Automation:** Python scripts + RunPod API
**Version Control:** Git

### Image Generation Stack

```
Stable Diffusion (Animagine XL 3.1 - high-quality anime SDXL model)
    ↓
Character LoRA (for Matt's consistency)
    ↓
IP-Adapter (for location consistency)
    ↓
Optional: ControlNet Depth (for spatial control)
    ↓
Final Image
```

**Why Anime Style?**
- **Faster development** - Less demanding consistency requirements than photorealism
- **Child-friendly aesthetic** - Appeals strongly to target audience (ages 5-12)
- **Highly expressive characters** - Actions and emotions clearly conveyed
- **Objects remain identifiable** - Clean lines make vocabulary items clear
- **Large community support** - Many free anime models and LoRAs available on CivitAI
- **Reduced uncanny valley** - Stylized characters are more forgiving of minor inconsistencies

### Character Consistency Strategy

**Approach:** Use existing character LoRA from CivitAI (recommended for POC)

**Alternatives:**
1. **Option A (Current):** Download pre-trained character LoRA from CivitAI
   - Pros: Fast, no training, proven quality
   - Cons: Won't match exact vision of Matt
   - Time: ~30 minutes

2. **Option B:** IP-Adapter with reference images
   - Pros: No training, can iterate quickly
   - Cons: Slightly less consistent
   - Time: 2-3 hours

3. **Option C:** Train custom LoRA for Matt
   - Pros: Best consistency, full control
   - Cons: Most time-consuming
   - Time: 6-12 hours (can automate via RunPod API)

### Location Consistency Strategy

**Approach:** AI-generated location references + IP-Adapter

**How it works:**
1. Generate 2-3 reference images of each location (bedroom, bathroom, kitchen)
2. Use these as IP-Adapter references during scene generation
3. IP-Adapter ensures new images match the reference location style

**Why not Blender 3D?**
- Would take 20-40 hours to model 19 locations
- AI-generated references are faster and equally effective
- Can always upgrade to Blender later if needed

### Automation via RunPod API

**Key Feature:** Fully automated GPU work - no manual interaction required

**What's automated:**
- Starting/stopping RunPod pods
- Uploading prompts and configs
- Running ComfyUI workflows remotely
- Downloading generated images
- Cost optimization (auto-stop when done)

**Scripts:**
- `scripts/runpod_manager.py` - Core API wrapper
- `scripts/remote_generate.py` - Automated image generation
- `scripts/remote_train_lora.py` - Optional LoRA training

**Workflow:**
```bash
python scripts/remote_generate.py \
  --config config/scenes_poc.json \
  --output output/poc/ \
  --gpu-type "RTX 4090" \
  --auto-stop
```

**What happens:**
1. Script starts RunPod pod
2. Uploads ComfyUI workflow and prompts
3. Generates all images
4. Downloads results
5. Stops pod automatically
6. You just wait for results!

---

## Content Specification

### Character Profile: Matt

**Basic Info:**
- Age: ~30 years old
- Gender: Male
- Ethnicity: Caucasian (can adapt for diversity later)
- Build: Average/athletic
- Hair: Short brown hair
- Profession: Office worker/professional

**Appearance Details:** (See config/character_profile.json for full prompt)

**Warrants:**
- Matt should look like a relatable, everyday person
- Not a model or actor - just a normal professional
- Consistent appearance across all 308 images is critical
- Neutral expressions (slight smile OK, but not overly emotive)

### Scene Structure

**Total Scenes:** 308 (full project)
**POC Scenes:** 10-15 (proof of concept)
**Time span:** 6:45 AM to 11:00 PM (one weekday)
**Locations:** 19 unique locations

### Location Inventory (Full Project)

1. **Matt's Bedroom** (morning and evening)
2. **Matt's Bathroom** (morning and evening)
3. **Matt's Kitchen** (breakfast, dinner, cleanup)
4. **Matt's Living Room** (evening relaxation)
5. **Matt's Home Office** (optional scenes)
6. **Matt's Car Interior** (commute)
7. **Office Parking Lot**
8. **Office Building Lobby**
9. **Office Elevator**
10. **Office Hallway**
11. **Matt's Cubicle/Desk**
12. **Office Conference Room**
13. **Office Break Room**
14. **Office Cafeteria**
15. **Office Bathroom**
16. **Outdoor Coffee Shop**
17. **City Street** (walking)
18. **Restaurant Interior** (lunch)
19. **Gym** (optional evening scenes)

### POC Locations (Phase 1)

For the proof-of-concept, we're focusing on **3 locations:**
1. **Bedroom** - Morning routine scenes
2. **Bathroom** - Personal hygiene scenes
3. **Kitchen** - Breakfast preparation scenes

This represents ~10-15 scenes total and covers the highest-value vocabulary.

---

## Multi-Character Expansion

### Overview

The project now supports **multiple characters** with diverse backgrounds, cultures, and demographics. Each character gets their own complete daily life narrative with culturally-appropriate scenes, vocabulary, and contexts.

### Character Templates Created

**1. Matt (Primary Character) - American Professional**
- **Directory:** matt_wm_25_yo/
- **Age:** ~30 years old
- **Gender:** Male
- **Ethnicity:** Caucasian
- **Profession:** Office worker/professional
- **Living Situation:** Solo apartment
- **Culture:** American suburban
- **Transportation:** Personal car
- **Total Scenes:** ~308
- **File:** [matt_wm_25_yo/matt_daily_life_scenes.md](matt_wm_25_yo/matt_daily_life_scenes.md)
- **Config Files:** matt_wm_25_yo/config/{scenes_poc.json, character_profile.json, locations.json}
- **Images:** matt_wm_25_yo/images/{poc,full}/
- **POC Status:** ✅ Complete (config files ready)

**2. Catalina - Colombian University Student**
- **Directory:** catalina_lf_21_yo/
- **Age:** 21 years old
- **Gender:** Female
- **Ethnicity:** Colombian/Latina
- **Profession:** University student (Communications)
- **Living Situation:** Family home with parents and younger brother
- **Culture:** Colombian/Latin American (Bogotá)
- **Transportation:** Public transit (TransMilenio)
- **Total Scenes:** ~280 (103 detailed scenes created)
- **File:** [catalina_lf_21_yo/catalina_daily_life_scenes.md](catalina_lf_21_yo/catalina_daily_life_scenes.md)
- **Config Files:** catalina_lf_21_yo/config/ (to be created)
- **Images:** catalina_lf_21_yo/images/{poc,full}/
- **POC Status:** ⏳ Not yet created (will follow Matt's validation)
- **Language:** Bilingual vocabulary (Spanish-English)

### Multi-Character Strategy

**Phase 1: Validate with Matt**
1. Generate Matt's POC (15 images)
2. Evaluate character consistency, quality, cost
3. If successful → proceed to full Matt set (308 images)

**Phase 2: Expand to Catalina**
1. Create Catalina's POC config (15 images from her scenes)
2. Generate Catalina's POC images
3. If successful → generate full Catalina set (~280 images)

**Phase 3: Scale to Additional Characters**
- Same template can be adapted for unlimited characters
- Examples: Japanese salaryman, Indian family, Nigerian teacher, etc.
- Each character provides different cultural context and vocabulary

### Technical Implications

**Character-Specific Requirements:**
- Each character gets their own directory: `{name}_{gender}_{age}_yo/`
  - Example: `matt_wm_25_yo/` for Matt (white male, 25 years old)
  - Example: `catalina_lf_21_yo/` for Catalina (latina female, 21 years old)
- Each character needs their own LoRA model for visual consistency
- Each character has their own config directory:
  - `{character}/config/character_profile.json`
  - `{character}/config/scenes_poc.json`
  - `{character}/config/locations.json`
- Each character has their own assets directory:
  - `{character}/assets/location_refs/`
  - `{character}/assets/character_refs/`
  - `{character}/assets/lora_weights/`
- Each character has their own images directory:
  - `{character}/images/poc/`
  - `{character}/images/full/`

**Shared Infrastructure:**
- Same RunPod automation scripts work for all characters
- Same ComfyUI workflow with different parameters
- Same base Stable Diffusion model

**Total Project Scope (If All Characters Generated):**
- Matt: 308 images (~$7.50-$10 GPU cost)
- Catalina: ~280 images (~$7-$9 GPU cost)
- **Total: ~588 images, ~$14.50-$19 GPU cost**

### Educational Benefits

**Diverse Representation:**
- Multiple genders, ages, ethnicities, cultures
- Different socioeconomic contexts
- Various professions and living situations

**Cultural Context:**
- Western vs Latin American vs Asian vs African contexts
- Different daily routines and cultural norms
- Bilingual/multilingual vocabulary support

**Vocabulary Variety:**
- Student vs professional vocabulary
- Public transit vs car vocabulary
- Family vs solo living vocabulary
- Cultural-specific objects and customs

### Scalability Approach

**Template Adaptation Guide:**

To create a new character, adapt the template with:
1. **Demographics:** Age, gender, ethnicity, profession
2. **Living Situation:** Solo, family, roommates, dormitory
3. **Culture:** Country, city, cultural norms
4. **Daily Routine:** Student, professional, retiree, parent, etc.
5. **Transportation:** Car, public transit, bike, walking
6. **Language:** Monolingual, bilingual, regional vocabulary
7. **Locations:** Adapt to cultural context (e.g., TransMilenio vs subway vs car)
8. **Objects:** Cultural-specific items (e.g., Colombian products, Japanese appliances)

**Example Variations:**
- **Yuki (Japanese Salaryman):** Tokyo apartment, train commute, office life, Japanese culture
- **Amara (Nigerian Teacher):** Lagos home, school environment, African context
- **Raj (Indian Family Man):** Delhi joint family, scooter commute, Indian cultural norms
- **Emma (American Student):** College dormitory, campus life, cafeteria, library

Each character provides hundreds of unique vocabulary items in authentic cultural contexts.

---

## Current Phase & Status

**Phase:** POC Configuration Complete - Ready for Generation

See [STATUS.md](STATUS.md) for real-time progress tracking.

### Completed Steps

1. ✅ Create project structure
2. ✅ Initialize git repository and make first commit
3. ✅ Create documentation (CLAUDE.md, STATUS.md, README.md)
4. ✅ Select 15 POC scenes for Matt (5 bedroom, 5 bathroom, 5 kitchen)
5. ✅ Create config files for Matt:
   - scenes_poc.json (15 scenes with detailed prompts)
   - character_profile.json (Matt's appearance and settings)
   - locations.json (3 POC locations with generation params)
6. ✅ Write RunPod API wrapper (scripts/runpod_manager.py)
7. ✅ Create multi-character template (catalina_daily_life_scenes.md)
   - ~103 detailed scenes for Colombian university student
   - Demonstrates cultural adaptation (Spanish language, Colombian products, Bogotá setting)
   - Shows gender, age, profession, culture, living situation variations

### Immediate Next Steps

8. ⏳ Get RunPod API key and test connection
9. ⏳ Write additional automation scripts (remote_generate.py, generate_location_refs.py)
10. ⏳ Generate 9 location reference images for Matt (3 per location)
11. ⏳ Download/test character LoRA from CivitAI for Matt
12. ⏳ Set up ComfyUI workflow on RunPod
13. ⏳ Generate 15 POC images for Matt
14. ⏳ Evaluate results and decide on full implementation
15. ⏳ If successful, create Catalina POC configs and repeat process

### Success Criteria for POC

- [ ] Matt is recognizable across 70%+ of images
- [ ] Objects are clearly identifiable for vocabulary learning
- [ ] Images look natural (minimal AI artifacts)
- [ ] Workflow is repeatable and can scale to 308 images
- [ ] Total cost < $5 for POC

### Decision Point After POC

If POC succeeds:
→ Scale to all 308 images using same automation approach

If POC fails:
→ Iterate on prompts, try different LoRA, or reconsider approach

---

## Key Decisions & Constraints

### Hard Constraints

✅ **No Blender** - Using AI-generated locations instead (saves 20-40 hours)
✅ **No paid AI services** - Stable Diffusion only, no DALL-E/Midjourney
✅ **Free/open-source tools only** - ComfyUI, RunPod, Python
✅ **POC before full implementation** - Validate approach with 10-15 images first
✅ **RunPod API automation** - Minimize manual GPU work

### Design Decisions

**Character Consistency:**
- Using existing LoRA from CivitAI for POC
- Can train custom LoRA later if needed

**Location Consistency:**
- AI-generated reference images + IP-Adapter
- 2-3 reference images per location

**Image Specifications:**
- Resolution: 1024x1024 or 1024x768 (landscape/portrait as needed)
- Format: PNG (high quality)
- Style: High-quality anime illustration, clean lines, vibrant colors

**Vocabulary Prioritization:**
- POC focuses on bedroom, bathroom, kitchen (highest value)
- Full project covers all 19 locations

### Budget & Timeline

**POC:**
- Cost: $1.50-$3.50 (GPU time)
- Time: 7-11 hours total (3.5-5.5 hours your time, rest automated)
- Timeline: 1-2 days

**Full Project (if POC succeeds):**
- Cost: $7.50-$10.00 (GPU time)
- Time: 15-20 hours GPU time (mostly automated)
- Your effort: ~2-4 hours (mostly quality review)

---

## File Structure & Organization

```
daily_life/
├── CLAUDE.md                    ← You are here
├── STATUS.md                    ← Real-time progress tracking
├── README.md                    ← Quick start guide
├── requirements.txt             ← Python dependencies
├── .gitignore                   ← Git ignore rules
├── image_generation_pipeline.md ← Original technical planning doc
│
├── scripts/                     ← Automation scripts (shared across all characters)
│   ├── runpod_manager.py        ← RunPod API wrapper
│   ├── remote_generate.py       ← Remote image generation
│   ├── remote_train_lora.py     ← Remote LoRA training (optional)
│   ├── generate_location_refs.py ← Location reference generator
│   ├── prepare_lora_dataset.py  ← LoRA dataset prep utilities
│   └── check_consistency.py     ← Quality checking utilities
│
├── matt_wm_25_yo/               ← Matt's character directory
│   ├── matt_daily_life_scenes.md ← ~308 scene descriptions
│   ├── config/                  ← Matt's configuration files
│   │   ├── scenes_poc.json      ← 15 POC scenes with metadata
│   │   ├── scenes_full.json     ← All 308 scenes (created later)
│   │   ├── character_profile.json ← Matt's appearance details
│   │   └── locations.json       ← Location metadata
│   ├── assets/                  ← Matt's generated assets (not committed)
│   │   ├── location_refs/       ← AI-generated location references
│   │   ├── character_refs/      ← Character reference images
│   │   └── lora_weights/        ← Trained LoRA model files
│   └── images/                  ← Matt's generated images (not committed)
│       ├── poc/                 ← POC images (15)
│       └── full/                ← Full project images (308)
│
└── catalina_lf_21_yo/           ← Catalina's character directory
    ├── catalina_daily_life_scenes.md ← ~280 scene descriptions
    ├── config/                  ← Catalina's configuration files (to be created)
    │   ├── scenes_poc.json      ← 15 POC scenes (to be created)
    │   ├── scenes_full.json     ← All ~280 scenes (created later)
    │   ├── character_profile.json ← Catalina's appearance details
    │   └── locations.json       ← Location metadata
    ├── assets/                  ← Catalina's generated assets (not committed)
    │   ├── location_refs/       ← AI-generated location references
    │   ├── character_refs/      ← Character reference images
    │   └── lora_weights/        ← Trained LoRA model files
    └── images/                  ← Catalina's generated images (not committed)
        ├── poc/                 ← POC images (15)
        └── full/                ← Full project images (~280)
```

### Config Files

Each character has their own config directory with the following files:

**{character}/config/scenes_poc.json**
- Contains 10-15 selected scenes for POC
- Each scene has: scene_id, location, time, lighting, description, objects, prompt

**{character}/config/character_profile.json**
- Character's detailed appearance description
- Prompt templates for consistency
- Negative prompts (what to avoid)
- LoRA settings

**{character}/config/locations.json**
- Metadata for each location
- Reference image paths (pointing to {character}/assets/location_refs/)
- IP-Adapter strength settings

**{character}/config/scenes_full.json** (created later)
- All scenes for the character
- Generated from scenes markdown file

**Shared:** config/comfyui_workflow.json (if needed)
- Exported ComfyUI workflow
- Node configuration
- Model paths and parameters

---

## Common Tasks & Commands

### Setup (One-time)

```bash
# Install Python dependencies
pip install -r requirements.txt

# Set RunPod API key (REQUIRED)
export RUNPOD_API_KEY="your-api-key-here"
# Or create a .env file with:
# RUNPOD_API_KEY=your-api-key-here

# Verify setup
python scripts/runpod_manager.py --test
```

### Generate Images (Automated)

```bash
# Generate Matt's POC images (15 scenes)
python scripts/remote_generate.py \
  --config matt_wm_25_yo/config/scenes_poc.json \
  --output matt_wm_25_yo/images/poc/ \
  --gpu-type "RTX 4090" \
  --auto-stop

# Generate Catalina's POC images (15 scenes)
python scripts/remote_generate.py \
  --config catalina_lf_21_yo/config/scenes_poc.json \
  --output catalina_lf_21_yo/images/poc/ \
  --gpu-type "RTX 4090" \
  --auto-stop

# Generate with specific LoRA
python scripts/remote_generate.py \
  --config matt_wm_25_yo/config/scenes_poc.json \
  --output matt_wm_25_yo/images/poc/ \
  --lora matt_wm_25_yo/assets/lora_weights/matt_lora.safetensors \
  --lora-strength 0.8

# Dry run (test without actually generating)
python scripts/remote_generate.py \
  --config matt_wm_25_yo/config/scenes_poc.json \
  --dry-run
```

### Generate Location References

```bash
# Generate Matt's location reference images
python scripts/generate_location_refs.py \
  --config matt_wm_25_yo/config/locations.json \
  --output matt_wm_25_yo/assets/location_refs/ \
  --count 3  # 3 variations per location

# Generate Catalina's location reference images
python scripts/generate_location_refs.py \
  --config catalina_lf_21_yo/config/locations.json \
  --output catalina_lf_21_yo/assets/location_refs/ \
  --count 3  # 3 variations per location
```

### Train LoRA (Optional)

```bash
# Train custom LoRA for Matt
python scripts/remote_train_lora.py \
  --dataset matt_wm_25_yo/assets/character_refs/ \
  --output matt_wm_25_yo/assets/lora_weights/ \
  --epochs 10 \
  --gpu-type "RTX 4090"

# Train custom LoRA for Catalina
python scripts/remote_train_lora.py \
  --dataset catalina_lf_21_yo/assets/character_refs/ \
  --output catalina_lf_21_yo/assets/lora_weights/ \
  --epochs 10 \
  --gpu-type "RTX 4090"
```

### Quality Checks

```bash
# Check consistency of Matt's generated images
python scripts/check_consistency.py \
  --input matt_wm_25_yo/images/poc/ \
  --report matt_consistency_report.json

# Check consistency of Catalina's generated images
python scripts/check_consistency.py \
  --input catalina_lf_21_yo/images/poc/ \
  --report catalina_consistency_report.json

# Validate config files for a character
python scripts/check_consistency.py \
  --validate-configs matt_wm_25_yo/config/
```

### Manual ComfyUI Testing (Local)

If you want to test locally before automating:

```bash
# Export your ComfyUI workflow to JSON
# Save to: config/comfyui_workflow.json (shared)
# Or character-specific: {character}/config/comfyui_workflow.json

# Test workflow with sample prompt from Matt's config
# (This would be manual in ComfyUI interface using matt_wm_25_yo/config/scenes_poc.json)
```

---

## Troubleshooting

### Common Issues

**1. RunPod API key not found**
```
Error: RUNPOD_API_KEY environment variable not set
```
**Fix:** Set the environment variable or create a .env file:
```bash
export RUNPOD_API_KEY="your-key-here"
# OR
echo "RUNPOD_API_KEY=your-key-here" > .env
```

**2. Character inconsistency**
```
Matt looks different in each image
```
**Fix:**
- Increase LoRA strength (try 0.9 instead of 0.7)
- Use more detailed character prompts
- Try different character LoRA
- Add negative prompts (e.g., "multiple people, crowd")

**3. Location inconsistency**
```
Bedroom/bathroom looks different each time
```
**Fix:**
- Increase IP-Adapter strength (try 0.7 instead of 0.5)
- Generate more consistent location references
- Use ControlNet Depth for spatial consistency
- Add location-specific details to prompts

**4. AI artifacts**
```
Images have weird hands, distorted faces, etc.
```
**Fix:**
- Use negative prompts: "deformed, distorted, disfigured, bad anatomy"
- Lower CFG scale (try 6-7 instead of 8-9)
- Increase steps (try 30-40 instead of 20)
- Use different seed

**5. RunPod pod won't start**
```
Error: No pods available with requested GPU type
```
**Fix:**
- Try different GPU type (RTX 3090 instead of RTX 4090)
- Wait and retry (GPUs may be temporarily unavailable)
- Choose different datacenter region

**6. Out of memory errors**
```
CUDA out of memory
```
**Fix:**
- Reduce batch size (generate 1 image at a time)
- Lower resolution (try 768x768 instead of 1024x1024)
- Use GPU with more VRAM (RTX 4090 has 24GB)

### Getting Help

- Check [STATUS.md](STATUS.md) for current blockers
- Review [image_generation_pipeline.md](image_generation_pipeline.md) for technical details
- Review [matt_daily_life_scenes.md](matt_daily_life_scenes.md) for scene specifications
- Ask Claude Code for help (I can troubleshoot issues)

---

## Notes for Future Sessions

**If you're Claude Code in a future session**, here's what you need to know:

1. **Check STATUS.md first** - It has the most current state
2. **This project uses RunPod API automation** - Don't suggest manual GPU work
3. **POC before full implementation** - Always validate with 10-15 images first
4. **Character consistency is critical** - Each character must look the same across all their images
5. **Target audience is children/ESL** - Keep explanations simple, images clear
6. **Cost awareness** - Keep GPU costs low ($1.50-$3.50 per POC, $7.50-$10 per full character set)
7. **No Blender** - User decided against it due to time investment
8. **Existing app** - These images will be integrated into a flashcard app already built
9. **Multi-character project** - Currently 2 characters (Matt, Catalina), can expand to more
10. **Cultural diversity** - Each character represents different culture, age, gender, profession

**Current blockers/questions:**
- See STATUS.md "Blockers" section

**Next decision point:**
- After POC: Evaluate quality and decide whether to proceed to full 308 images

---

**End of CLAUDE.md** - See STATUS.md for real-time progress.
