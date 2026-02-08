# Project Status - Daily Life Visual Vocabulary Generator

**Last Updated:** 2026-02-08
**Phase:** Content Authoring Complete — All Scenes Expanded
**Started:** 2026-01-17

---

## Current Status

All 10 characters have complete content: expanded scene descriptions (.md) in micro-action format and POC config files (scenes_poc.json, character_profile.json, locations.json).

Image generation is handled separately in `dev/imageGen`.

---

## Character Content Status

All 10 characters have complete POC configs (3/3 config files each). All scene files have been expanded to micro-action granularity (one action per scene).

### United States Characters (5)

| Character | Directory | Scenes | scenes_poc | char_profile | locations |
|-----------|-----------|--------|------------|--------------|-----------|
| Matt | matt_wm_25_yo/ | 308 | 15 | done | done |
| Marcus | marcus_am_45_yo/ | 218 | 15 | done | done |
| Emily | emily_af_28_yo/ | 195 | 15 | done | done |
| Tyler | tyler_wm_16_yo/ | 196 | 15 | done | done |
| Rosa | rosa_hf_55_yo/ | 197 | 15 | done | done |

### Colombia Characters (5)

| Character | Directory | Scenes | scenes_poc | char_profile | locations |
|-----------|-----------|--------|------------|--------------|-----------|
| Catalina | catalina_lf_21_yo/ | 281 | 15 | done | done |
| Jorge | jorge_lm_67_yo/ | 182 | 15 | done | done |
| Isabella | isabella_lf_9_yo/ | 168 | 15 | done | done |
| Valentina | valentina_lf_34_yo/ | 172 | 15 | done | done |
| Andres | andres_lm_42_yo/ | 147 | 15 | done | done |

**Total:** 10/10 characters complete | 2,064 scenes | 150 POC scenes

---

## Scene Format

All scene files now use the standardized micro-action format:

```
### Scene NNN: [Short Title]
**Time:** H:MM AM/PM — [lighting description]
**Setting:** [location], [camera angle/framing]
**Description:** [Detailed visual description, one micro-action per scene]
```

Each scene describes exactly one action with detailed descriptions of all visible objects, lighting conditions, colors, materials, and camera framing.

---

## Scene Coverage

All characters cover a full day:

| Character | Time Span | Role |
|-----------|-----------|------|
| Matt | 6:45 AM - 11:00 PM | Office worker, USA |
| Marcus | 6:00 AM - 10:30 PM | Firefighter day off, Chicago |
| Emily | 6:30 AM - 10:50 PM | Software engineer, San Francisco |
| Tyler | 6:30 AM - 10:25 PM | High school student, Ohio |
| Rosa | 5:00 AM - 10:00 PM | Hospital nurse, Houston |
| Catalina | 6:00 AM - 10:15 PM | University student, Bogota |
| Jorge | 4:30 AM - 9:00 PM | Coffee farmer, Quindio |
| Isabella | 6:00 AM - 8:30 PM | Elementary student, Cartagena |
| Valentina | 5:30 AM - 10:30 PM | Doctor, Cali |
| Andres | 5:00 AM - 10:25 PM | Tienda owner, Medellin |

---

## Possible Next Steps

- Add new characters for additional cultural contexts (Japanese, Indian, Nigerian, etc.)
- Create full scenes configs (scenes_full.json) from complete scene markdown files
- Review and update scenes_poc.json files to reference expanded scene IDs

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

**2026-02-07 — Scene Standardization & Expansion**
- Expanded all 8 shorter characters to match Matt's micro-action format
- Before: ~1,234 scenes (many in consolidated multi-action format)
- After: 2,064 scenes (all in micro-action format, one action per scene)
- Expansion details:
  - Catalina: 105 → 281 scenes (full day coverage added)
  - Emily: 95 → 195 scenes
  - Tyler: 151 → 196 scenes
  - Jorge: 97 → 182 scenes
  - Isabella: 94 → 168 scenes
  - Valentina: 62 → 172 scenes
  - Rosa: 56 → 197 scenes
  - Andres: 45 → 147 scenes
