# Project Status - Daily Life Visual Vocabulary Generator

**Last Updated:** 2026-01-19
**Phase:** POC Setup - Multi-Character Expansion Complete
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

## Multi-Character Expansion

### Character Templates Created

**Total Characters: 10** (2 original + 8 new)

#### United States Characters (5)

**Matt (Original Primary Character):**
- **Directory:** matt_wm_25_yo/
- **Profile:** 30-year-old American white male, office professional
- **Location:** American suburban
- **Scenes:** ~308 total (15 selected for POC)
- **POC Config:** ✅ Complete
- **Images Path:** matt_wm_25_yo/images/{poc,full}/

**Marcus (Firefighter):**
- **Directory:** marcus_am_45_yo/
- **Profile:** 45-year-old African American male, Chicago firefighter
- **Location:** Chicago suburb (Oak Park area)
- **Scenes:** ~218 total (15 selected for POC)
- **POC Config:** ✅ Complete
- **Key Features:** Firefighter profession, family with teens, suburban family home

**Tyler (High School Student):**
- **Directory:** tyler_wm_16_yo/
- **Profile:** 16-year-old white male, high school student
- **Location:** Small town, Ohio
- **Scenes:** ~151 total (15 selected for POC)
- **POC Config:** ✅ Complete
- **Key Features:** Teen life, school bus, homework, sports

**Emily (Software Engineer):**
- **Directory:** emily_af_28_yo/
- **Profile:** 28-year-old Asian American female, software engineer
- **Location:** San Francisco, CA (Mission District)
- **Scenes:** ~94 total (15 selected for POC)
- **POC Config:** ✅ Complete
- **Key Features:** Tech startup, bike commute, apartment with roommate, Asian cooking

**Rosa (Hospital Nurse):**
- **Directory:** rosa_hf_55_yo/
- **Profile:** 55-year-old Mexican American female, registered nurse
- **Location:** Houston, TX (Pasadena suburb)
- **Scenes:** ~55 total (15 selected for POC)
- **POC Config:** ✅ Complete
- **Key Features:** 12-hour shifts, multigenerational home, Catholic faith, Mexican American culture

#### Colombia Characters (5)

**Catalina (Original Second Character):**
- **Directory:** catalina_lf_21_yo/
- **Profile:** 21-year-old Colombian female university student
- **Location:** Bogotá, Colombia
- **Scenes:** ~103 detailed scenes
- **POC Config:** ❌ Not yet created
- **Key Features:** University life, TransMilenio transit, family home

**Jorge (Coffee Farmer):**
- **Directory:** jorge_lm_67_yo/
- **Profile:** 67-year-old Colombian male, coffee farmer
- **Location:** Rural Quindío (coffee region)
- **Scenes:** ~97 total (15 selected for POC)
- **POC Config:** ✅ Complete
- **Key Features:** Coffee cultivation, traditional finca, rural Colombian life

**Isabella (Elementary Student):**
- **Directory:** isabella_lf_9_yo/
- **Profile:** 9-year-old Colombian female, elementary student
- **Location:** Cartagena, Colombia
- **Scenes:** ~94 total (15 selected for POC)
- **POC Config:** ✅ Complete
- **Key Features:** School uniform, Caribbean coastal culture, family life

**Valentina (Doctor):**
- **Directory:** valentina_lf_34_yo/
- **Profile:** 34-year-old Colombian female, general practitioner
- **Location:** Cali, Colombia
- **Scenes:** ~62 total (15 selected for POC)
- **POC Config:** ✅ Complete
- **Key Features:** Hospital and private clinic, morning running, salsa dancing

**Andrés (Tienda Owner):**
- **Directory:** andres_lm_42_yo/
- **Profile:** 42-year-old Colombian male, neighborhood tienda owner
- **Location:** Medellín, Colombia (Laureles)
- **Scenes:** ~44 total (15 selected for POC)
- **POC Config:** ✅ Complete
- **Key Features:** Small business, apartment above store, community pillar

### Multi-Character Strategy

**Approach:**
1. Validate image generation approach with Matt's POC (15 images)
2. If successful, expand to other characters
3. All 10 characters now have POC configs ready (except Catalina)
4. Total potential images: ~1,500+ across all characters

**Character Demographics Summary:**
- **Age range:** 9 to 67 years old
- **Genders:** 5 male, 5 female
- **Ethnicities:** White American, African American, Asian American, Mexican American, Colombian
- **Professions:** Office worker, firefighter, student (high school, elementary, university), software engineer, nurse, doctor, coffee farmer, tienda owner
- **Countries:** 5 USA, 5 Colombia

**Scalability:**
- ✅ Template structure supports unlimited characters
- ✅ Each character gets their own directory: {name}_{ethnicity_gender}_{age}_yo/
- ✅ Each character gets their own scenes markdown file
- ✅ Each character gets their own config files (character_profile.json, scenes_poc.json, locations.json)
- ✅ Each character gets their own assets directory (location_refs, character_refs, lora_weights)
- ✅ Each character gets their own images directory (images/{poc,full})
- ✅ Each character gets their own LoRA model for consistency
- ✅ Same automation pipeline works for all characters
- ✅ 8 new characters created with complete POC configs (2026-01-19)

**Benefits:**
- Diverse representation in educational materials
- Multiple cultural contexts for ESL learners
- Different vocabulary sets based on character lifestyle
- Age-appropriate content for different learner groups
- Professional, student, and everyday life vocabulary

---

## File Inventory

### Character Files

**US Characters (5):**

| Character | Directory | Scenes MD | scenes_poc.json | character_profile.json | locations.json |
|-----------|-----------|-----------|-----------------|----------------------|----------------|
| Matt | matt_wm_25_yo/ | ✅ ~308 | ✅ 15 | ✅ | ✅ |
| Marcus | marcus_am_45_yo/ | ✅ ~218 | ✅ 15 | ✅ | ✅ |
| Tyler | tyler_wm_16_yo/ | ✅ ~151 | ✅ 15 | ✅ | ✅ |
| Emily | emily_af_28_yo/ | ✅ ~94 | ✅ 15 | ✅ | ✅ |
| Rosa | rosa_hf_55_yo/ | ✅ ~55 | ✅ 15 | ✅ | ✅ |

**Colombia Characters (5):**

| Character | Directory | Scenes MD | scenes_poc.json | character_profile.json | locations.json |
|-----------|-----------|-----------|-----------------|----------------------|----------------|
| Catalina | catalina_lf_21_yo/ | ✅ ~103 | ❌ | ❌ | ❌ |
| Jorge | jorge_lm_67_yo/ | ✅ ~97 | ✅ 15 | ✅ | ✅ |
| Isabella | isabella_lf_9_yo/ | ✅ ~94 | ✅ 15 | ✅ | ✅ |
| Valentina | valentina_lf_34_yo/ | ✅ ~62 | ✅ 15 | ✅ | ✅ |
| Andrés | andres_lm_42_yo/ | ✅ ~44 | ✅ 15 | ✅ | ✅ |

**Total:** 9/10 characters have complete POC configs

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

**Matt (matt_wm_25_yo/assets/):**
| Asset Type | Count | Path | Status |
|------------|-------|------|--------|
| Location references | 0/9 | location_refs/ | Not generated |
| Character references | 0 | character_refs/ | Not needed (using existing LoRA) |
| LoRA weights | 0 | lora_weights/ | Not downloaded |

**Catalina (catalina_lf_21_yo/assets/):**
| Asset Type | Count | Path | Status |
|------------|-------|------|--------|
| Location references | 0 | location_refs/ | Not generated |
| Character references | 0 | character_refs/ | Not generated |
| LoRA weights | 0 | lora_weights/ | Not downloaded |

### Generated Images

**Matt (matt_wm_25_yo/images/):**
| Type | Count | Path | Status |
|------|-------|------|--------|
| POC images | 0/15 | poc/ | Not generated |
| Full project images | 0/308 | full/ | Future work |

**Catalina (catalina_lf_21_yo/images/):**
| Type | Count | Path | Status |
|------|-------|------|--------|
| POC images | 0/15 | poc/ | Not generated |
| Full project images | 0/~280 | full/ | Future work |

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
  - Animagine XL 3.1 (anime SDXL): ❌ No
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

**2026-01-17 - Multi-Character Expansion**
- ✅ **Created catalina_daily_life_scenes.md** - Template for second character (Colombian university student)
- ✅ **Demonstrated scalability** - Template can be adapted for different characters, cultures, demographics
- Character profile: 21-year-old Colombian female university student living in Bogotá
- ~103 detailed scenes created showing cultural adaptation (Spanish language, Colombian products, family home, TransMilenio transit, Universidad Nacional)
- Template includes different daily routine (student vs working professional), different culture (Latin American vs American), different gender (female vs male), different living situation (family home vs solo apartment)
- **Project now supports multiple characters** - Ready to scale to many people's daily lives

**2026-01-17 - Directory Structure Reorganization**
- ✅ **Reorganized project with character-specific subdirectories**
- Created `matt_wm_25_yo/` directory for Matt (white male, 25 years old)
- Created `catalina_lf_21_yo/` directory for Catalina (latina female, 21 years old)
- Each character now has their own:
  - Scenes markdown file: `{character}/{character}_daily_life_scenes.md`
  - Config directory: `{character}/config/` with scenes_poc.json, character_profile.json, locations.json
  - Assets directory: `{character}/assets/` with location_refs/, character_refs/, lora_weights/
  - Images directory: `{character}/images/` with poc/ and full/ subdirectories
- Moved Matt's files to matt_wm_25_yo/
- Updated all config files to use new paths
- Updated .gitignore to reflect new character-specific structure
- Updated all documentation (README.md, STATUS.md, CLAUDE.md) with new structure
- Removed deprecated output/ and assets/ directories
- **Directory naming convention:** `{name}_{gender}_{age}_yo/` for clear organization

**Next Session:**
- Get RunPod API key and test connection
- Create remaining automation scripts (remote_generate.py, generate_location_refs.py)
- Update automation scripts to work with character-specific directories
- Generate location references for Matt's POC (matt_wm_25_yo/assets/location_refs/)
- Download character LoRA from CivitAI
- Begin ComfyUI workflow testing

**2026-01-19 - Multi-Character Expansion Complete**
- ✅ Created 8 new character directories with full structure
- ✅ **Marcus (marcus_am_45_yo/):** African American firefighter, 45, Chicago - 218 scenes, complete POC config
- ✅ **Tyler (tyler_wm_16_yo/):** White male high school student, 16, Ohio - 151 scenes, complete POC config
- ✅ **Emily (emily_af_28_yo/):** Asian American software engineer, 28, San Francisco - 94 scenes, complete POC config
- ✅ **Rosa (rosa_hf_55_yo/):** Mexican American nurse, 55, Houston - 55 scenes, complete POC config
- ✅ **Jorge (jorge_lm_67_yo/):** Colombian coffee farmer, 67, Quindío - 97 scenes, complete POC config
- ✅ **Isabella (isabella_lf_9_yo/):** Colombian elementary student, 9, Cartagena - 94 scenes, complete POC config
- ✅ **Valentina (valentina_lf_34_yo/):** Colombian doctor, 34, Cali - 62 scenes, complete POC config
- ✅ **Andrés (andres_lm_42_yo/):** Colombian tienda owner, 42, Medellín - 44 scenes, complete POC config

**Character creation summary:**
- All 8 new characters have daily_life_scenes.md with detailed scene descriptions
- All 8 new characters have config/character_profile.json with appearance and prompts
- All 8 new characters have config/locations.json with 3 POC locations each
- All 8 new characters have config/scenes_poc.json with 15 POC scenes each
- Project now has 10 total characters (5 USA, 5 Colombia)
- Total estimated scenes: ~1,300+ across all characters
- Total POC scenes ready for generation: 135 (9 characters × 15 scenes)

**Next steps:**
- Generate Matt's POC images first to validate workflow
- If successful, can generate POC for any of the 9 ready characters
- Create Catalina's POC configs (only remaining character without POC config)

### Learnings

- Character diversity requires careful cultural research and authentic representation
- Each character benefits from unique vocabulary tied to their profession/lifestyle
- Age-appropriate scenes are important (Isabella's child-friendly content, Tyler's teen life)

### Improvements for Next Time

- TBD (will be filled based on POC results)

---

**End of STATUS.md** - Updated 2026-01-19
