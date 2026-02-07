# Project Status - Daily Life Visual Vocabulary Generator

**Last Updated:** 2026-02-07
**Phase:** Content Authoring Complete
**Started:** 2026-01-17

---

## Current Status

All 10 characters have complete content: scene descriptions (.md) and POC config files (scenes_poc.json, character_profile.json, locations.json).

Image generation is handled separately in `dev/imageGen`.

---

## Character Content Status

All 10 characters have complete POC configs (3/3 config files each).

### United States Characters (5)

| Character | Directory | Scenes | scenes_poc | char_profile | locations |
|-----------|-----------|--------|------------|--------------|-----------|
| Matt | matt_wm_25_yo/ | ~310 | 15 | done | done |
| Marcus | marcus_am_45_yo/ | ~218 | 15 | done | done |
| Tyler | tyler_wm_16_yo/ | ~151 | 15 | done | done |
| Emily | emily_af_28_yo/ | ~95 | 15 | done | done |
| Rosa | rosa_hf_55_yo/ | ~56 | 15 | done | done |

### Colombia Characters (5)

| Character | Directory | Scenes | scenes_poc | char_profile | locations |
|-----------|-----------|--------|------------|--------------|-----------|
| Catalina | catalina_lf_21_yo/ | ~105 | 15 | done | done |
| Jorge | jorge_lm_67_yo/ | ~97 | 15 | done | done |
| Isabella | isabella_lf_9_yo/ | ~94 | 15 | done | done |
| Valentina | valentina_lf_34_yo/ | ~63 | 15 | done | done |
| Andres | andres_lm_42_yo/ | ~45 | 15 | done | done |

**Total:** 10/10 characters complete | ~1,234 scenes | 150 POC scenes

---

## Scene Completeness

Scene markdown files vary in coverage. Some cover a full day (6 AM - 11 PM), others cover partial days:

| Character | Coverage | Notes |
|-----------|----------|-------|
| Matt | Full day | Most detailed, ~310 scenes |
| Marcus | Full day | Firefighter day off |
| Tyler | Full day | School day |
| Catalina | Morning only (~6 AM - 1 PM) | Template shows 103 scenes, full day would be ~280 |
| Jorge | Full day | Coffee farm routine |
| Emily | Full day | Tech worker day |
| Isabella | Full day | School day |
| Valentina | Full day | Doctor's day |
| Rosa | Full day | Nurse's shift |
| Andres | Full day | Tienda owner's day |

---

## Possible Next Steps

- Expand Catalina's scenes to cover full day (afternoon, evening, bedtime — currently ~105, target ~280)
- Expand scene descriptions for shorter characters (Rosa ~56, Andres ~45) if more detail needed
- Add new characters for additional cultural contexts (Japanese, Indian, Nigerian, etc.)
- Create full scenes configs (scenes_full.json) from complete scene markdown files

---

## Session Notes

**2026-01-17 — Initial Setup**
- Created project structure, documentation, Matt's config files, RunPod API wrapper

**2026-01-17 — Multi-Character Expansion**
- Created Catalina template demonstrating cultural adaptation
- Reorganized into character-specific subdirectories

**2026-01-19 — 8 New Characters**
- Created Marcus, Tyler, Emily, Rosa, Jorge, Isabella, Valentina, Andres
- All with complete scene descriptions and POC configs

**2026-02-07 — Project Refocus & Cleanup**
- Clarified project scope: content authoring only, image generation in dev/imageGen
- Completed Catalina's missing config files (character_profile.json, locations.json)
- Removed scripts/ directory (RunPod automation moved to imageGen)
- Rewrote CLAUDE.md, STATUS.md, README.md to reflect content-only focus
- Removed requirements.txt (no Python code in this project)
- Simplified .gitignore
