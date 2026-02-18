# Daily Life Visual Vocabulary Generator - Content Project

**Last Updated:** 2026-02-17

---

## Project Overview

### What is this project?

A **content authoring project** that creates detailed scene descriptions for 20 diverse characters going through their daily lives. These scene narratives serve as the source material for generating anime-style educational illustrations used as visual vocabulary flashcards.

### How it fits in the pipeline

```
daily_life (this project)          dev/imageGen
├── Scene narratives (.md)    →    illustrations.json (FLUX.2-dev prompts)
└── (source content)          →    Generated PNG images
```

- **This project** = content authoring (scene descriptions, vocabulary)
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

20 characters spanning different ages, genders, ethnicities, professions, and cultures provide:
- Multiple cultural contexts for ESL learners
- Different vocabulary sets based on character lifestyle
- Age-appropriate content for different learner groups
- Professional, student, and everyday life vocabulary

---

## Character Roster

**20 characters** (10 USA, 10 Colombia) with ~4,058 total scenes:

### United States Characters (10)

| Character | Directory | Age | Profession | Scenes |
|-----------|-----------|-----|-----------|--------|
| Matt | matt_wm_25_yo/ | 25 | Office worker | 308 |
| Marcus | marcus_am_45_yo/ | 45 | Firefighter (Chicago) | 218 |
| Tyler | tyler_wm_16_yo/ | 16 | High school student (Ohio) | 196 |
| Emily | emily_af_28_yo/ | 28 | Software engineer (SF) | 195 |
| Rosa | rosa_hf_55_yo/ | 55 | Hospital nurse (Houston) | 197 |
| Sophie | sophie_wf_5_yo/ | 5 | Kindergartener (Portland) | 155 |
| Raj | raj_im_72_yo/ | 72 | Retired engineer (Edison NJ) | 165 |
| James | james_am_22_yo/ | 22 | Culinary student (New Orleans) | 232 |
| Aisha | aisha_sf_40_yo/ | 40 | Restaurant owner (Minneapolis) | 260 |
| David | david_nm_35_yo/ | 35 | Construction foreman (Albuquerque) | 206 |

### Colombia Characters (10)

| Character | Directory | Age | Profession | Scenes |
|-----------|-----------|-----|-----------|--------|
| Catalina | catalina_lf_21_yo/ | 21 | University student (Bogotá) | 281 |
| Jorge | jorge_lm_67_yo/ | 67 | Coffee farmer (Quindío) | 182 |
| Isabella | isabella_lf_9_yo/ | 9 | Elementary student (Cartagena) | 168 |
| Valentina | valentina_lf_34_yo/ | 34 | Doctor (Cali) | 172 |
| Andres | andres_lm_42_yo/ | 42 | Tienda owner (Medellín) | 147 |
| Camilo | camilo_lm_14_yo/ | 14 | Student / soccer player (Barranquilla) | 195 |
| Lucía | lucia_lf_28_yo/ | 28 | Elementary teacher (Bucaramanga) | 215 |
| Marina | marina_af_45_yo/ | 45 | Fisherwoman (Tumaco) | 186 |
| Carmen | carmen_lf_75_yo/ | 75 | Artisan / grandmother (Villa de Leyva) | 160 |
| Santiago | santiago_lm_19_yo/ | 19 | Delivery rider / DJ (Bogotá) | 220 |

### Demographics Summary

- **Age range:** 5 to 75
- **Gender:** 10 male, 10 female
- **Ethnicities:** White American, African American, Indian American, Somali American, Native American (Navajo), Mexican American, Colombian, Afro-Colombian
- **Directory naming:** `{name}_{ethnicity_gender}_{age}_yo/`

---

## Content Structure

Each character directory contains:

```
{character}_xx_NN_yo/
└── {character}_daily_life_scenes.md    # Full day narrative (~147-308 scenes)
```

### Scene Descriptions (.md)

Detailed prose descriptions covering a full day (6 AM - 11 PM). Each scene includes:
- Time and lighting conditions
- Character appearance and clothing
- Character action/pose
- All visible objects with details (color, material, cultural items)
- Room/environment details
- Atmospheric details

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
│   └── matt_daily_life_scenes.md
│
├── catalina_lf_21_yo/                 # Catalina - Colombian student
│   └── catalina_daily_life_scenes.md
│
├── marcus_am_45_yo/                   # Marcus - Chicago firefighter
├── tyler_wm_16_yo/                    # Tyler - Ohio high school student
├── emily_af_28_yo/                    # Emily - SF software engineer
├── rosa_hf_55_yo/                     # Rosa - Houston nurse
├── jorge_lm_67_yo/                    # Jorge - Colombian coffee farmer
├── isabella_lf_9_yo/                  # Isabella - Colombian elementary student
├── valentina_lf_34_yo/                # Valentina - Colombian doctor
├── andres_lm_42_yo/                   # Andres - Colombian tienda owner
├── sophie_wf_5_yo/                    # Sophie - Portland kindergartener
├── raj_im_72_yo/                      # Raj - Retired Indian American engineer
├── james_am_22_yo/                    # James - New Orleans culinary student
├── aisha_sf_40_yo/                    # Aisha - Minneapolis restaurant owner
├── david_nm_35_yo/                    # David - Navajo construction foreman
├── camilo_lm_14_yo/                   # Camilo - Barranquilla soccer student
├── lucia_lf_28_yo/                    # Lucía - Bucaramanga teacher
├── marina_af_45_yo/                   # Marina - Tumaco fisherwoman
├── carmen_lf_75_yo/                   # Carmen - Villa de Leyva artisan
└── santiago_lm_19_yo/                 # Santiago - Bogotá delivery rider / DJ
```

---

## Adding a New Character

To create a new character:

1. **Choose demographics:** Name, age, gender, ethnicity, profession, location, living situation
2. **Create directory:** `{name}_{ethnicity_gender}_{age}_yo/`
3. **Write scenes markdown:** Detailed scene descriptions covering a full day (~150-310 scenes)
   - Follow the format in existing characters' `.md` files
   - Include cultural context, vocabulary items, and object details

Use existing characters as templates.

---

## Notes for Future Sessions

1. **This is a content-only project** — no code, no scripts, no image generation
2. **Image generation lives in `dev/imageGen`** — that project consumes this project's content
3. **All 20 characters have full-day scene coverage** in micro-action format (one action per scene)
4. **Cultural authenticity matters** — each character's scenes reflect their real cultural context
5. Check [STATUS.md](STATUS.md) for current progress
