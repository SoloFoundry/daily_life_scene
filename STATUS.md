# Project Status - Daily Life Visual Vocabulary Generator

**Last Updated:** 2026-02-10
**Phase:** Content Authoring Complete — 20 Characters
**Started:** 2026-01-17

---

## Current Status

All 20 characters have complete content: expanded scene descriptions (.md) in micro-action format and POC config files (scenes_poc.json, character_profile.json, locations.json).

Image generation is handled separately in `dev/imageGen`.

---

## Character Content Status

All 20 characters have complete POC configs (3/3 config files each). All scene files use micro-action granularity (one action per scene).

### United States Characters (10)

| Character | Directory | Age | Profession | Scenes | scenes_poc | char_profile | locations |
|-----------|-----------|-----|-----------|--------|------------|--------------|-----------|
| Matt | matt_wm_25_yo/ | 25 | Office worker | 308 | 15 | done | done |
| Marcus | marcus_am_45_yo/ | 45 | Firefighter (Chicago) | 218 | 15 | done | done |
| Emily | emily_af_28_yo/ | 28 | Software engineer (SF) | 195 | 15 | done | done |
| Tyler | tyler_wm_16_yo/ | 16 | HS student (Ohio) | 196 | 15 | done | done |
| Rosa | rosa_hf_55_yo/ | 55 | Nurse (Houston) | 197 | 15 | done | done |
| Sophie | sophie_wf_5_yo/ | 5 | Kindergartener (Portland) | 155 | 15 | done | done |
| Raj | raj_im_72_yo/ | 72 | Retired engineer (Edison NJ) | 165 | 15 | done | done |
| James | james_am_22_yo/ | 22 | Culinary student (New Orleans) | 232 | 15 | done | done |
| Aisha | aisha_sf_40_yo/ | 40 | Restaurant owner (Minneapolis) | 260 | 15 | done | done |
| David | david_nm_35_yo/ | 35 | Construction foreman (Albuquerque) | 206 | 15 | done | done |

### Colombia Characters (10)

| Character | Directory | Age | Profession | Scenes | scenes_poc | char_profile | locations |
|-----------|-----------|-----|-----------|--------|------------|--------------|-----------|
| Catalina | catalina_lf_21_yo/ | 21 | University student (Bogotá) | 281 | 15 | done | done |
| Jorge | jorge_lm_67_yo/ | 67 | Coffee farmer (Quindío) | 182 | 15 | done | done |
| Isabella | isabella_lf_9_yo/ | 9 | Elementary student (Cartagena) | 168 | 15 | done | done |
| Valentina | valentina_lf_34_yo/ | 34 | Doctor (Cali) | 172 | 15 | done | done |
| Andres | andres_lm_42_yo/ | 42 | Tienda owner (Medellín) | 147 | 15 | done | done |
| Camilo | camilo_lm_14_yo/ | 14 | Student / soccer player (Barranquilla) | 195 | 15 | done | done |
| Lucía | lucia_lf_28_yo/ | 28 | Elementary teacher (Bucaramanga) | 215 | 15 | done | done |
| Marina | marina_af_45_yo/ | 45 | Fisherwoman (Tumaco) | 186 | 15 | done | done |
| Carmen | carmen_lf_75_yo/ | 75 | Artisan / grandmother (Villa de Leyva) | 160 | 15 | done | done |
| Santiago | santiago_lm_19_yo/ | 19 | Delivery rider / DJ (Bogotá) | 220 | 15 | done | done |

**Total:** 20/20 characters complete | 4,058 scenes | 300 POC scenes

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
| Sophie | 6:30 AM - 8:00 PM | Kindergartener, Portland |
| Raj | 6:30 AM - 9:00 PM | Retired engineer, Edison NJ |
| James | 7:00 AM - 11:30 PM | Culinary student / line cook, New Orleans |
| Aisha | 5:30 AM - 11:00 PM | Restaurant owner, Minneapolis |
| David | 5:00 AM - 9:30 PM | Construction foreman, Albuquerque |
| Catalina | 6:00 AM - 10:15 PM | University student, Bogotá |
| Jorge | 4:30 AM - 9:00 PM | Coffee farmer, Quindío |
| Isabella | 6:00 AM - 8:30 PM | Elementary student, Cartagena |
| Valentina | 5:30 AM - 10:30 PM | Doctor, Cali |
| Andres | 5:00 AM - 10:25 PM | Tienda owner, Medellín |
| Camilo | 6:00 AM - 10:00 PM | Student / soccer player, Barranquilla |
| Lucía | 5:30 AM - 10:00 PM | Elementary teacher, Bucaramanga |
| Marina | 4:30 AM - 9:00 PM | Fisherwoman, Tumaco |
| Carmen | 5:00 AM - 8:30 PM | Artisan / grandmother, Villa de Leyva |
| Santiago | 8:00 AM - 1:00 AM | Delivery rider / DJ, Bogotá |

---

## Possible Next Steps

- Create full scenes configs (scenes_full.json) from complete scene markdown files
- Review and update scenes_poc.json files to reference expanded scene IDs
- Add characters from additional countries beyond US/Colombia

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

**2026-02-10 — 10 New Characters Added**
- Added 10 new characters (5 USA, 5 Colombia) for expanded diversity
- New USA characters: Sophie (5, kindergartener, Portland), Raj (72, retired engineer, Edison NJ), James (22, culinary student, New Orleans), Aisha (40, restaurant owner, Minneapolis), David (35, construction foreman, Albuquerque)
- New Colombia characters: Camilo (14, soccer student, Barranquilla), Lucía (28, teacher, Bucaramanga), Marina (45, fisherwoman, Tumaco), Carmen (75, artisan, Villa de Leyva), Santiago (19, delivery rider/DJ, Bogotá)
- 1,994 new scenes across 10 characters (all micro-action format)
- Project total: 20 characters, 4,058 scenes, 300 POC scenes
- Age range expanded: 5 to 75
- New ethnicities: Somali American, Indian American, Native American (Navajo), Afro-Colombian
