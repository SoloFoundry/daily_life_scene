# Daily Life Visual Vocabulary Generator

Content authoring project for educational anime illustrations. Creates detailed daily life scene descriptions for diverse characters, used as source material for visual vocabulary flashcards.

## What's Here

Scene narratives and character profiles for **10 characters** (5 USA, 5 Colombia) spanning ages 9-67, covering **2,016 daily life scenes** total. All scenes use micro-action format (one action per scene with detailed visual descriptions).

| Character | Age | Role | Location | Scenes |
|-----------|-----|------|----------|--------|
| Matt | 25 | Office worker | USA | 308 |
| Catalina | 21 | Univ. student | Bogota | 281 |
| Marcus | 45 | Firefighter | Chicago | 218 |
| Emily | 28 | Software eng. | San Francisco | 195 |
| Tyler | 16 | HS student | Ohio | 183 |
| Jorge | 67 | Coffee farmer | Quindio | 182 |
| Isabella | 9 | Elementary student | Cartagena | 171 |
| Valentina | 34 | Doctor | Cali | 166 |
| Rosa | 55 | Nurse | Houston | 165 |
| Andres | 42 | Tienda owner | Medellin | 147 |

## Project Structure

Each character has their own directory:

```
{character}_xx_NN_yo/
├── {character}_daily_life_scenes.md    # Full day narrative
└── config/
    ├── scenes_poc.json                 # 15 POC scenes
    ├── character_profile.json          # Appearance & background
    └── locations.json                  # 3 POC locations
```

## Image Generation

Image generation is handled by a separate project: `dev/imageGen`. That project consumes this content and produces anime illustrations using FLUX.2-dev.

## Documentation

- [CLAUDE.md](CLAUDE.md) — Full project context
- [STATUS.md](STATUS.md) — Current progress

---

**Created with** [Claude Code](https://claude.com/claude-code)
