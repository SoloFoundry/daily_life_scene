# Daily Life Visual Vocabulary Generator - Content Project

**Last Updated:** 2026-02-07

---

## Project Overview

### What is this project?

A **content authoring project** that creates detailed scene descriptions for 10 diverse characters going through their daily lives. These scene narratives serve as the source material for generating anime-style educational illustrations used as visual vocabulary flashcards.

### How it fits in the pipeline

```
daily_life (this project)          dev/imageGen
├── Scene narratives (.md)    →    illustrations.json (FLUX.2-dev prompts)
├── Character profiles (.json)→    Generated PNG images
└── Location configs (.json)  →    Final flashcard assets
```

- **This project** = content authoring (scene descriptions, character profiles, vocabulary, locations)
- **dev/imageGen** = image generation pipeline (FLUX.2-dev prompts, GPU scripts, generated PNGs)

This project produces **raw content only**. The transformation from scene descriptions to image generation prompts happens in `dev/imageGen`.

### Target Audience

- **Primary:** Children (ages 5-12) learning English
- **Secondary:** ESL (English as a Second Language) students of all ages
- **Distribution:** Flashcards in an existing mobile app

---

## Educational Goals & Pedagogy

### Contextual Learning Approach

**Core Principle:** "Show, don't tell" — demonstrate objects in use rather than in isolation.

- Traditional flashcard: Picture of a toothbrush on white background
- Our approach: Character brushing teeth in their bathroom — teaches "toothbrush," "bathroom," "brushing," "mirror," "sink"

### Sequential Storytelling

Following characters through their day creates a narrative arc that:
- Makes learning memorable through story
- Shows temporal relationships (breakfast before work, dinner after work)
- Demonstrates routines and sequences
- Provides natural repetition (bedroom appears multiple times)

### Diverse Representation

10 characters spanning different ages, genders, ethnicities, professions, and cultures provide:
- Multiple cultural contexts for ESL learners
- Different vocabulary sets based on character lifestyle
- Age-appropriate content for different learner groups
- Professional, student, and everyday life vocabulary

---

## Character Roster

**10 characters** (5 USA, 5 Colombia) with ~1,234 total scenes:

### United States Characters

| Character | Directory | Age | Profession | Scenes |
|-----------|-----------|-----|-----------|--------|
| Matt | matt_wm_25_yo/ | 25 | Office worker | ~310 |
| Marcus | marcus_am_45_yo/ | 45 | Firefighter (Chicago) | ~218 |
| Tyler | tyler_wm_16_yo/ | 16 | High school student (Ohio) | ~151 |
| Emily | emily_af_28_yo/ | 28 | Software engineer (SF) | ~95 |
| Rosa | rosa_hf_55_yo/ | 55 | Hospital nurse (Houston) | ~56 |

### Colombia Characters

| Character | Directory | Age | Profession | Scenes |
|-----------|-----------|-----|-----------|--------|
| Catalina | catalina_lf_21_yo/ | 21 | University student (Bogota) | ~105 |
| Jorge | jorge_lm_67_yo/ | 67 | Coffee farmer (Quindio) | ~97 |
| Isabella | isabella_lf_9_yo/ | 9 | Elementary student (Cartagena) | ~94 |
| Valentina | valentina_lf_34_yo/ | 34 | Doctor (Cali) | ~63 |
| Andres | andres_lm_42_yo/ | 42 | Tienda owner (Medellin) | ~45 |

### Demographics Summary

- **Age range:** 9 to 67
- **Gender:** 5 male, 5 female
- **Ethnicities:** White American, African American, Asian American, Mexican American, Colombian
- **Directory naming:** `{name}_{ethnicity_gender}_{age}_yo/`

---

## Content Structure

Each character directory contains:

```
{character}_xx_NN_yo/
├── {character}_daily_life_scenes.md    # Full day narrative (~50-310 scenes)
└── config/
    ├── scenes_poc.json                 # 15 POC scenes with metadata
    ├── character_profile.json          # Appearance, clothing, background
    └── locations.json                  # 3 POC locations with details
```

### Scene Descriptions (.md)

Detailed prose descriptions covering a full day (6 AM - 11 PM). Each scene includes:
- Time and lighting conditions
- Character appearance and clothing
- Character action/pose
- All visible objects with details (color, material, cultural items)
- Room/environment details
- Atmospheric details

### Config Files (.json)

**scenes_poc.json** — 15 selected scenes (5 per location: bedroom, bathroom, kitchen) with:
- Scene ID, location, time, lighting, title
- Description, character state, objects list, actions list
- Prompt template and negative prompt

**character_profile.json** — Character details:
- Demographics and appearance
- Clothing styles (sleep, work/school, casual)
- Background (family, education, hobbies)
- Prompt templates for different states
- Consistency guidelines

**locations.json** — 3 POC locations with:
- Detailed environment descriptions
- Key features and vocabulary items
- Lighting conditions by time of day
- Cultural context notes

---

## File Structure

```
daily_life/
├── CLAUDE.md                          # This file
├── STATUS.md                          # Progress tracking
├── README.md                          # Quick start guide
├── image_generation_pipeline.md       # Legacy technical planning doc
├── .gitignore
│
├── matt_wm_25_yo/                     # Matt - American office worker
│   ├── matt_daily_life_scenes.md
│   └── config/
│       ├── scenes_poc.json
│       ├── character_profile.json
│       └── locations.json
│
├── catalina_lf_21_yo/                 # Catalina - Colombian student
│   ├── catalina_daily_life_scenes.md
│   └── config/
│       ├── scenes_poc.json
│       ├── character_profile.json
│       └── locations.json
│
├── marcus_am_45_yo/                   # Marcus - Chicago firefighter
├── tyler_wm_16_yo/                    # Tyler - Ohio high school student
├── emily_af_28_yo/                    # Emily - SF software engineer
├── rosa_hf_55_yo/                     # Rosa - Houston nurse
├── jorge_lm_67_yo/                    # Jorge - Colombian coffee farmer
├── isabella_lf_9_yo/                  # Isabella - Colombian elementary student
├── valentina_lf_34_yo/                # Valentina - Colombian doctor
└── andres_lm_42_yo/                   # Andres - Colombian tienda owner
```

---

## Adding a New Character

To create a new character:

1. **Choose demographics:** Name, age, gender, ethnicity, profession, location, living situation
2. **Create directory:** `{name}_{ethnicity_gender}_{age}_yo/`
3. **Write scenes markdown:** Detailed scene descriptions covering a full day (~50-300 scenes)
   - Follow the format in existing characters' `.md` files
   - Include cultural context, vocabulary items, and object details
4. **Create config files:**
   - `config/character_profile.json` — appearance, clothing, background
   - `config/locations.json` — 3 POC locations with descriptions and vocabulary
   - `config/scenes_poc.json` — select 15 representative scenes (5 per location)

Use existing characters as templates. Match the JSON schema exactly.

---

## Notes for Future Sessions

1. **This is a content-only project** — no code, no scripts, no image generation
2. **Image generation lives in `dev/imageGen`** — that project consumes this project's content
3. **All 10 characters have complete POC configs** (scenes_poc.json, character_profile.json, locations.json)
4. **Scene descriptions vary in completeness** — some characters have full-day coverage, others are partial
5. **Cultural authenticity matters** — each character's scenes reflect their real cultural context
6. Check [STATUS.md](STATUS.md) for current progress
