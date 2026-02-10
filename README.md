# Daily Life Visual Vocabulary Generator

Content authoring project for educational anime illustrations. Creates detailed daily life scene descriptions for diverse characters, used as source material for visual vocabulary flashcards.

## What's Here

Scene narratives and character profiles for **20 characters** (10 USA, 10 Colombia) spanning ages 5-75, covering **4,058 daily life scenes** total. All scenes use micro-action format (one action per scene with detailed visual descriptions).

### United States Characters (10)

| Character | Age | Role | Location | Scenes |
|-----------|-----|------|----------|--------|
| Matt | 25 | Office worker | USA | 308 |
| Aisha | 40 | Restaurant owner | Minneapolis | 260 |
| James | 22 | Culinary student | New Orleans | 232 |
| Marcus | 45 | Firefighter | Chicago | 218 |
| David | 35 | Construction foreman | Albuquerque | 206 |
| Rosa | 55 | Nurse | Houston | 197 |
| Tyler | 16 | HS student | Ohio | 196 |
| Emily | 28 | Software eng. | San Francisco | 195 |
| Raj | 72 | Retired engineer | Edison NJ | 165 |
| Sophie | 5 | Kindergartener | Portland | 155 |

### Colombia Characters (10)

| Character | Age | Role | Location | Scenes |
|-----------|-----|------|----------|--------|
| Catalina | 21 | Univ. student | Bogotá | 281 |
| Santiago | 19 | Delivery rider / DJ | Bogotá | 220 |
| Lucía | 28 | Elementary teacher | Bucaramanga | 215 |
| Camilo | 14 | Soccer student | Barranquilla | 195 |
| Marina | 45 | Fisherwoman | Tumaco | 186 |
| Jorge | 67 | Coffee farmer | Quindío | 182 |
| Valentina | 34 | Doctor | Cali | 172 |
| Isabella | 9 | Elementary student | Cartagena | 168 |
| Carmen | 75 | Artisan / grandmother | Villa de Leyva | 160 |
| Andres | 42 | Tienda owner | Medellín | 147 |

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
