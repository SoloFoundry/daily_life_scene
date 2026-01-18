# A Day in the Life of Matt: Visual Scene Descriptions

---

## DOCUMENT CONTEXT

### Project Overview

**Purpose:** This document contains 308 detailed scene descriptions for generating realistic educational images depicting a full day in the life of Matt, a 25-year-old American office worker.

**Project Goal:** Create visual learning content that helps learners (children, ESL students, people with special learning needs, etc.) identify everyday objects and associate vocabulary with realistic images showing objects in their natural context.

**Why This Approach Works:**
- Objects shown in real-world settings (toothbrush in bathroom, not isolated)
- Logical sequence helps learners understand daily routines
- Character interactions with objects show purpose and usage
- Repetition of locations (bedroom morning + night) reinforces learning
- Cultural context embedded naturally

---

### Companion Document

**📄 `image_generation_pipeline.md`** — Contains the technical pipeline for automated image generation, including:
- Full project context and key decisions made
- Pipeline architecture diagram
- Required software and models (all free)
- Directory structure
- 19 location asset requirements (Blender scenes)
- Lighting presets for different times of day
- Automation scripts structure
- What's been completed vs. what's still needed
- Troubleshooting guide

**How These Documents Work Together:**
- This file (`matt_daily_life_scenes.md`) = **WHAT** to generate (scene content)
- Pipeline file (`image_generation_pipeline.md`) = **HOW** to generate (technical infrastructure)

**When continuing this project in a new chat:** Provide both documents to Claude for full context.

---

### This Document as a Template

This document serves as a **template structure** for generating daily life scenarios for different characters. The format, level of detail, and organization can be replicated for:

**Different Characters:**
- Different genders (female, non-binary)
- Different ages (child, teenager, middle-aged, elderly)
- Different ethnicities and cultural backgrounds
- Different careers/occupations
- Different living situations

**Example Future Character: Catalina**
| Attribute | Value |
|-----------|-------|
| Name | Catalina |
| Age | 21 |
| Gender | Female |
| Ethnicity | Colombian/Latina |
| Location | Bogotá, Colombia |
| Occupation | University student |
| Living situation | Lives with parents and siblings in family home |
| Scenarios needed | Weekday (university), Weekend (family/social) |

Catalina's daily life would include different:
- **Objects:** Colombian breakfast items, university materials, local transportation
- **Settings:** Family home (shared spaces), Colombian university campus, Bogotá streets, local tiendas
- **Routines:** Family meals together, different morning routine with shared bathroom, public transit commute
- **Cultural elements:** Colombian customs, Spanish-language signage, local food and products

---

### Scenario Variations

**This document covers:** Matt's typical weekday (work day)

**Other scenarios that could be created for Matt:**

| Scenario | Key Differences |
|----------|-----------------|
| **Weekend - Relaxed** | Sleeps in, casual breakfast, no commute, leisure activities (gym, errands, streaming), social time with friends |
| **Weekend - Active** | Morning jog, brunch at café, outdoor activities, shopping mall, evening dinner out or house party |
| **Work from Home Day** | No commute, home office setup, video calls from apartment, blurred work/home boundaries |
| **Sick Day** | Stays in bed, medicine and tissues, soup, TV all day, doctor visit or telehealth |
| **Travel Day** | Packing, airport/train station, security, waiting, boarding, hotel check-in |
| **Date Night** | Getting ready (nicer clothes), driving to restaurant, dinner scene, movie or activity |
| **Holiday** | Decorations in apartment, special meal preparation, video call with family, gift opening |
| **Moving Day** | Boxes everywhere, loading truck, new apartment, unpacking |
| **First Day at New Job** | Extra nervous morning routine, unfamiliar office, meeting new colleagues |
| **Grocery Day (Extended)** | More detailed shopping trip, farmers market, meal planning |

Each scenario would follow the same format as this document:
1. Character profile section
2. Chronological scenes with detailed descriptions
3. Time stamps and lighting notes
4. Objects and settings clearly identified
5. Appendix with location/time quick references

---

### Scene Description Format

Each scene in this document follows a consistent format for easy parsing and image generation:

```
### Scene [NUMBER]: [TITLE]
**Time:** [TIME] — [LIGHTING CONDITION]
**Setting:** [LOCATION], [CAMERA ANGLE/VIEW]
**Description:** [DETAILED PARAGRAPH INCLUDING:]
  - Character appearance and clothing
  - Character action/pose
  - All visible objects with details (color, material, brand if relevant)
  - Room/environment details
  - Lighting quality and direction
  - Atmospheric details
```

**Key principles for scene descriptions:**
- **Third-person perspective** — Character is visible in scene
- **Extremely granular** — Each small action is a separate scene
- **Object-rich** — Every visible object is mentioned
- **Sensory details** — Textures, materials, colors, lighting
- **Consistent character** — Same clothing within time periods
- **Logical flow** — Scenes connect naturally

---

### Vocabulary Categories Covered

This document naturally covers vocabulary in these categories:

| Category | Example Objects |
|----------|-----------------|
| **Bedroom** | alarm clock, nightstand, lamp, pillow, blanket, dresser, closet, mirror, hangers |
| **Bathroom** | toothbrush, toothpaste, sink, faucet, mirror, towel, shower, shampoo, soap, toilet |
| **Kitchen** | coffee maker, toaster, refrigerator, stove, pan, spatula, plate, mug, knife, cutting board |
| **Clothing** | shirt, pants, belt, shoes, socks, underwear, pajamas, t-shirt, sweatpants |
| **Electronics** | smartphone, laptop, monitor, keyboard, mouse, TV, remote, charger, earbuds |
| **Office** | desk, chair, cubicle, phone, notepad, pen, printer, elevator, conference table |
| **Car** | steering wheel, dashboard, mirror, seatbelt, cup holder, gear shift, key fob |
| **Food** | bread, butter, coffee, toast, sandwich, chips, chicken, salad, water |
| **Furniture** | bed, sofa, table, chair, stool, bookshelf, coffee table |
| **Actions** | wake up, brush teeth, pour, spread, drive, type, sit, walk, cook, eat, sleep |

---

### Adapting This Template for Other Characters

**Step 1: Define Character Profile**
- Demographics (age, gender, ethnicity, appearance)
- Location (country, city, urban/suburban/rural)
- Occupation/role
- Living situation (alone, family, roommates)
- Key personality traits affecting routine

**Step 2: Define Scenario**
- Which day type (weekday, weekend, special occasion)
- Time span (full day, partial day)
- Key activities that must be included

**Step 3: Identify Location Differences**
- What rooms/spaces will be shown?
- What's culturally specific? (furniture, appliances, decor)
- What's different from Matt's environments?

**Step 4: Identify Object Differences**
- Food and meals (culturally appropriate)
- Clothing (climate, culture, occasion appropriate)
- Transportation (car, bus, metro, walking, bike)
- Technology (same globally, but usage patterns differ)
- Work/school materials

**Step 5: Write Scenes Following Format**
- Maintain same granularity level
- Same description format
- Chronological order
- Detailed lighting and time notes

**Step 6: Create Location Asset List**
- Map new locations needed for Blender
- Identify reusable assets from existing library
- Note culturally specific objects to model

---

### Document Statistics

| Metric | Value |
|--------|-------|
| Total scenes | 308 |
| Time span covered | 6:45 AM — 11:00 PM (~16 hours) |
| Unique locations | 19 |
| Character outfit changes | 3 (sleep → work → casual) |
| Meals depicted | 3 (breakfast, lunch, dinner) |
| Major activities | Wake up, commute, office work, lunch out, grocery shopping, cook dinner, relax, sleep |

---

### File Naming Convention (When Generating Multiple Characters)

```
[character]_[scenario]_scenes.md

Examples:
- matt_weekday_office_scenes.md (this file)
- matt_weekend_relaxed_scenes.md
- matt_sick_day_scenes.md
- catalina_weekday_university_scenes.md
- catalina_weekend_family_scenes.md
- omar_weekday_construction_scenes.md
- yuki_weekday_tokyo_office_scenes.md
- grace_elderly_retirement_scenes.md
```

---

### Summary

This document provides:
1. **Complete scene descriptions** for Matt's typical weekday (308 scenes)
2. **Template structure** replicable for other characters and scenarios
3. **Vocabulary coverage** across everyday settings and objects
4. **Technical format** compatible with automated image generation pipeline

Use this document alongside `image_generation_pipeline.md` for full project context.

---

## Character Profile

- **Name:** Matt
- **Age:** 25
- **Appearance:** White male, short brown hair, average build, clean-shaven
- **Lives:** One-bedroom apartment in a suburban apartment complex outside a mid-sized American city
- **Job:** Junior marketing coordinator at a mid-sized company in a suburban business park
- **Car:** Silver Honda Civic sedan, 2019 model
- **Style:** Business casual for work (button-down shirts, chinos), casual at home (t-shirts, sweatpants)

---

## PART 1: EARLY MORNING — BEDROOM (6:45 AM - 7:00 AM)

### Scene 001: The Alarm
**Time:** 6:45 AM — dim blue pre-dawn light filtering through blinds  
**Setting:** Bedroom, viewed from foot of bed  
**Description:** A 25-year-old white man with short brown hair lies in bed under a navy blue comforter, eyes closed, face peaceful in sleep. On the wooden nightstand beside him, a smartphone screen glows brightly, displaying "6:45 AM" with an alarm interface. A simple black digital alarm clock sits behind the phone showing the same time. A glass of water is half-full next to the phone. A small brass lamp with a white shade is switched off. The window behind the bed has white horizontal blinds, slightly open, allowing thin strips of pale blue early morning light to fall across the bed. Walls are painted light gray.

### Scene 002: Reaching for the Phone
**Time:** 6:45 AM — dim blue pre-dawn light  
**Setting:** Bedroom, close-up on nightstand area  
**Description:** A man's hand emerges from under the navy comforter, reaching toward the glowing smartphone on the wooden nightstand. His fingers are about to touch the screen to dismiss the alarm. The phone screen shows the alarm with a "Dismiss" slider. The bedside lamp, water glass, and digital clock are visible in the background. Soft blue morning light from the window blinds illuminates the scene. The man's face is partially visible, eyes squinting, still groggy.

### Scene 003: Sitting Up in Bed
**Time:** 6:46 AM — dim morning light  
**Setting:** Bedroom, side view  
**Description:** Matt sits on the edge of the bed, feet touching the beige carpet floor, wearing a gray cotton t-shirt and navy pajama pants. He hunches slightly forward, rubbing his eyes with one hand. The navy comforter is pushed aside, revealing white sheets. A wooden bed frame with a simple headboard is visible. On the floor beside the bed are gray fabric slippers. The nightstand with phone, water glass, and lamp is beside him. A dresser with a mirror stands against the far wall, reflecting the dim room.

### Scene 004: Feet on the Floor
**Time:** 6:46 AM — dim morning light  
**Setting:** Bedroom, low angle close-up  
**Description:** Close-up of bare feet stepping onto beige carpet from the bed. Gray fabric slippers sit on the floor nearby. The bottom edge of navy pajama pants is visible. The wooden bed frame leg is in the foreground. Under the bed, a few dust bunnies and a single sock are barely visible in the shadows. Morning light creates soft shadows on the carpet texture.

### Scene 005: Stretching by the Window
**Time:** 6:47 AM — growing morning light  
**Setting:** Bedroom, full room view  
**Description:** Matt stands beside the window, arms raised above his head in a full-body stretch, wearing his gray t-shirt and navy pajama pants. His eyes are closed, face tilted slightly upward. The white horizontal blinds are still mostly closed. The bed is unmade behind him, navy comforter bunched to one side. A full-length mirror on a closet door reflects his stretching figure. A laundry basket with some clothes sits in the corner near a white six-drawer dresser.

### Scene 006: Opening the Blinds
**Time:** 6:47 AM — morning light flooding in  
**Setting:** Bedroom, view toward window  
**Description:** Matt's hand pulls the cord of white horizontal blinds, twisting them open. Bright morning sunlight streams through, casting horizontal striped shadows across the room. Through the window, a suburban view is visible: a parking lot with several cars, green grass, and another apartment building across the way. Matt's face is lit by the warm morning sun, eyes slightly squinted against the brightness. The room is transformed from dim blue to warm golden light.

### Scene 007: Making the Bed
**Time:** 6:48 AM — bright morning light  
**Setting:** Bedroom, view of bed  
**Description:** Matt leans over the bed, pulling the navy comforter up and straightening it. White sheets are partially visible. Two pillows in white pillowcases sit against the wooden headboard. The nightstand is visible with the phone now dark, water glass, lamp, and digital clock showing 6:48. Warm morning sunlight illuminates the scene from the window. A small framed photograph of a mountain landscape hangs on the light gray wall above the bed.

### Scene 008: Picking Out Clothes
**Time:** 6:50 AM — bright morning light  
**Setting:** Bedroom, open closet  
**Description:** Matt stands before an open sliding closet door with mirrored panels. Inside the closet, button-down shirts hang on wooden hangers — light blue, white, pale pink, striped patterns. Below them, several pairs of chinos and dress pants hang. On the closet floor are three pairs of shoes: brown leather dress shoes, white sneakers, and black loafers. A shelf above holds folded sweaters and a few boxes. Matt's hand reaches toward a light blue oxford shirt. The room is reflected in the closet mirror.

### Scene 009: Clothes Laid on Bed
**Time:** 6:51 AM — bright morning light  
**Setting:** Bedroom, view of bed  
**Description:** On top of the made bed with navy comforter, a work outfit is laid out neatly: a light blue button-down oxford shirt, khaki chinos, a brown leather belt, and navy blue socks. A pair of brown leather dress shoes sits on the carpet beside the bed. The morning sun casts warm light across the fabric. Matt is not visible in the frame — just the prepared outfit waiting on the bed.

---

## PART 2: BATHROOM (7:00 AM - 7:25 AM)

### Scene 010: Entering the Bathroom
**Time:** 7:00 AM — bright bathroom light  
**Setting:** Bathroom doorway  
**Description:** Matt walks through the bathroom doorway, hand reaching for the light switch on the wall. He still wears his gray t-shirt and navy pajama pants. The bathroom is small but clean: white tile floor, white walls, a single vanity with a white sink and chrome faucet, a large mirror above, and a white toilet beside it. A glass-enclosed shower stall is visible in the background. Beige towels hang on a chrome bar. The light is just flickering on, transitioning from dim to bright.

### Scene 011: Looking in the Mirror
**Time:** 7:00 AM — bright fluorescent light  
**Setting:** Bathroom, facing mirror  
**Description:** Matt stands before the bathroom mirror, examining his face. His reflection shows slightly messy brown hair, a bit of stubble, tired eyes. Both hands rest on the white porcelain sink edge. The chrome faucet gleams under the bright vanity lights above the mirror — three round bulbs in frosted glass. A toothbrush holder with a blue toothbrush and white toothpaste tube sits to the right. A soap dispenser and small succulent plant in a white pot are on the left side of the sink.

### Scene 012: Turning on the Faucet
**Time:** 7:01 AM — bright bathroom light  
**Setting:** Bathroom, close-up on sink  
**Description:** Close-up of Matt's hands turning the chrome faucet handle. Water begins to flow from the faucet into the white porcelain sink. His fingers are on the cold water handle. The sink basin reflects the vanity lights. Water droplets splash slightly. A bar of white soap sits in a ceramic dish nearby. The drain has a chrome stopper.

### Scene 013: Splashing Face with Water
**Time:** 7:01 AM — bright bathroom light  
**Setting:** Bathroom, side view at sink  
**Description:** Matt leans over the sink, cupping water in both hands, splashing it onto his face. Water drips from his chin and nose back into the basin. His eyes are closed, face wet. The mirror reflects his hunched back. Small water droplets are scattered on the counter surface around the sink. A white hand towel hangs on a small ring beside the mirror.

### Scene 014: Drying Face with Towel
**Time:** 7:02 AM — bright bathroom light  
**Setting:** Bathroom, facing mirror  
**Description:** Matt presses a white hand towel against his face, drying off the water. His eyes are hidden behind the towel. His reflection is visible in the mirror. The sink faucet is now off, water droplets on the porcelain. The toothbrush and toothpaste wait on the counter. His gray t-shirt has a few wet spots near the collar.

### Scene 015: Applying Toothpaste
**Time:** 7:02 AM — bright bathroom light  
**Setting:** Bathroom, close-up on hands  
**Description:** Extreme close-up of Matt's hands holding a blue toothbrush in one hand and a white tube of Colgate toothpaste in the other. He squeezes a strip of blue-and-white striped toothpaste onto the bristles. The bathroom counter is blurred in the background. His thumb presses the tube. A small curl of toothpaste sits perfectly on the brush bristles.

### Scene 016: Brushing Teeth
**Time:** 7:03 AM — bright bathroom light  
**Setting:** Bathroom, facing mirror  
**Description:** Matt brushes his teeth, the blue toothbrush in his right hand, moving it across his teeth. His mouth is slightly open, foamy white toothpaste visible. His reflection in the mirror shows the brushing motion. His left hand rests on the counter. The toothpaste tube lies on its side near the sink. His expression is neutral, eyes looking at his own reflection.

### Scene 017: Spitting into Sink
**Time:** 7:05 AM — bright bathroom light  
**Setting:** Bathroom, side angle  
**Description:** Matt leans over the sink, spitting white foamy toothpaste into the basin. The water runs, washing the foam down toward the drain. His hand holds the toothbrush aside. His mouth is open, mid-spit. The chrome drain catches the white foam. Water swirls in the basin.

### Scene 018: Rinsing Mouth
**Time:** 7:05 AM — bright bathroom light  
**Setting:** Bathroom, close-up  
**Description:** Matt cups water in his right hand, bringing it to his mouth to rinse. Water dribbles between his fingers. His head is tilted back slightly. The faucet runs behind his hand. His cheeks are slightly puffed, swishing the water. The mirror reflects the back of his head.

### Scene 019: Rinsing Toothbrush
**Time:** 7:06 AM — bright bathroom light  
**Setting:** Bathroom, close-up on sink  
**Description:** Close-up of the blue toothbrush being held under running water from the chrome faucet. White toothpaste residue washes off the bristles and swirls down into the sink. Matt's fingers hold the brush handle. Water streams off the bristles in small rivulets.

### Scene 020: Putting Toothbrush Away
**Time:** 7:06 AM — bright bathroom light  
**Setting:** Bathroom, view of counter  
**Description:** Matt places the blue toothbrush back into a white ceramic toothbrush holder that has two slots. The holder sits on the counter beside the sink. The toothpaste tube stands upright nearby. A small potted succulent adds a touch of green. The soap dispenser and other toiletries are arranged neatly.

### Scene 021: Undressing for Shower
**Time:** 7:07 AM — bright bathroom light  
**Setting:** Bathroom, full view  
**Description:** Matt pulls his gray t-shirt over his head, revealing his bare back and torso. The shirt is bunched around his arms and head mid-removal. His navy pajama pants are still on. The glass shower enclosure is visible behind him. A white bath mat sits on the tile floor in front of the shower. The toilet with its lid down is to the left.

### Scene 022: Adjusting Shower Temperature
**Time:** 7:08 AM — bright bathroom light with steam beginning  
**Setting:** Bathroom, inside shower view  
**Description:** Matt's hand reaches into the glass-enclosed shower, turning the chrome shower handle. Water sprays from the rainfall showerhead mounted on the wall. His arm is extended, testing the water temperature with his fingers. Steam begins to rise. The glass shower door is open. White subway tiles line the shower walls. A shelf holds a bottle of blue shampoo and a bar of soap.

### Scene 023: Stepping into Shower
**Time:** 7:08 AM — steamy bathroom  
**Setting:** Bathroom, view of shower entrance  
**Description:** Matt steps into the shower, one foot on the white non-slip shower floor, the other still on the bath mat outside. The glass door is held open with one hand. Steam fills the shower enclosure. Water streams down from the showerhead. His bare back and shoulders are visible, slightly blurred by the steam and glass.

### Scene 024: Under the Showerhead
**Time:** 7:10 AM — steamy shower  
**Setting:** Inside shower  
**Description:** Matt stands directly under the rainfall showerhead, eyes closed, face tilted up toward the water. Water streams down over his hair, face, and shoulders. His short brown hair is wet and slicked back. Water droplets cover his skin. Steam fills the space. The white subway tile walls glisten with moisture. The chrome shower fixtures gleam.

### Scene 025: Shampooing Hair
**Time:** 7:12 AM — steamy shower  
**Setting:** Inside shower  
**Description:** Matt's hands are in his hair, working blue shampoo into a white lather. His eyes are closed to avoid suds. Foam covers his head and drips slightly down his forehead. The shampoo bottle sits on the built-in tile shelf. Water continues to spray from the showerhead onto his shoulders. Steam swirls around him.

### Scene 026: Rinsing Shampoo
**Time:** 7:13 AM — steamy shower  
**Setting:** Inside shower  
**Description:** Matt tilts his head back under the showerhead, rinsing shampoo from his hair. White foam streams down his back and swirls toward the drain. His hands run through his hair, helping clear the suds. Water cascades over his face and closed eyes. The drain catches the soapy water.

### Scene 027: Using Body Wash
**Time:** 7:14 AM — steamy shower  
**Setting:** Inside shower  
**Description:** Matt holds a blue loofah sponge, squeezing body wash onto it from a bottle. The clear gel sits on the loofah mesh. His other hand holds the body wash bottle. The shower spray falls on his back. The tile shelf holds the shampoo bottle beside him.

### Scene 028: Washing Body
**Time:** 7:15 AM — steamy shower  
**Setting:** Inside shower  
**Description:** Matt scrubs his arm with the soapy blue loofah, white suds covering his skin. His other arm is raised. The loofah creates patterns of foam. Water and soap stream down his torso. The glass shower walls are fogged with steam. His face shows a neutral, routine expression.

### Scene 029: Rinsing Body
**Time:** 7:17 AM — steamy shower  
**Setting:** Inside shower  
**Description:** Matt stands under the shower spray, rinsing soap from his body. Water streams down his chest and arms, washing away the white suds. His arms are slightly raised, letting water reach everywhere. The drain is visible at his feet, soapy water swirling into it. Steam continues to fill the shower.

### Scene 030: Turning Off Shower
**Time:** 7:19 AM — steam-filled bathroom  
**Setting:** Inside shower  
**Description:** Matt's wet hand turns the chrome shower handle to the off position. The last drops of water fall from the showerhead. His arm is extended toward the fixture. Water droplets cling to the chrome and tile. The steam begins to slowly clear. The glass door is still closed, fogged with condensation.

### Scene 031: Reaching for Towel
**Time:** 7:19 AM — steamy bathroom  
**Setting:** Bathroom, shower area  
**Description:** Matt opens the glass shower door, reaching out for a beige bath towel hanging on a chrome bar. His wet arm extends from the shower. Water drips from his body onto the white bath mat. Steam escapes from the open shower door into the bathroom. His face is visible, wet hair pushed back.

### Scene 032: Drying Off
**Time:** 7:20 AM — clearing steam  
**Setting:** Bathroom, full view  
**Description:** Matt stands on the white bath mat outside the shower, wrapping the large beige towel around his waist. His torso is still wet with water droplets. His hair is damp and disheveled. The glass shower door is open behind him, water droplets on the glass. The bathroom mirror is fogged up. He tucks the towel corner to secure it.

### Scene 033: Wiping Mirror
**Time:** 7:21 AM — bathroom with clearing steam  
**Setting:** Bathroom, at mirror  
**Description:** Matt's hand wipes a clear streak across the fogged bathroom mirror with a small towel. His partial reflection becomes visible through the cleared section — wet face, damp hair. Condensation drips down the glass around the cleared area. The vanity lights glow above. His towel is wrapped around his waist.

### Scene 034: Combing Hair
**Time:** 7:22 AM — bright bathroom light  
**Setting:** Bathroom, facing mirror  
**Description:** Matt runs a black plastic comb through his wet brown hair, looking at his reflection in the partially cleared mirror. His free hand holds the hair at the front. The comb teeth pull through damp strands. A few toiletries are visible on the counter — deodorant, hair product, toothbrush holder. His bare shoulders are visible above the towel at his waist.

### Scene 035: Applying Deodorant
**Time:** 7:23 AM — bright bathroom light  
**Setting:** Bathroom, side view  
**Description:** Matt holds a stick of deodorant (white container with blue cap) in one hand, applying it under his raised arm. His face is reflected in the mirror, focused on the task. The towel remains around his waist. Other toiletries are visible on the counter. His arm pit is exposed as he applies the product.

### Scene 036: Applying Hair Product
**Time:** 7:24 AM — bright bathroom light  
**Setting:** Bathroom, close-up  
**Description:** Matt squeezes a small amount of hair styling paste from a small black container onto his fingertips. The product is a matte gray color. His other hand holds the open container. The bathroom counter and mirror are in the soft background. Water droplets still cling to the mirror edges.

### Scene 037: Styling Hair
**Time:** 7:24 AM — bright bathroom light  
**Setting:** Bathroom, facing mirror  
**Description:** Matt runs his product-coated fingers through his damp hair, styling it into a neat side part. He looks at his reflection in the mirror, making adjustments. His hair is taking shape — neat, professional, slightly textured. The bathroom is now clear of steam. His expression is focused, evaluating the result.

### Scene 038: Exiting Bathroom
**Time:** 7:25 AM — bright hallway light  
**Setting:** Bathroom doorway to hallway  
**Description:** Matt walks out of the bathroom into a short hallway, towel around his waist, hair neatly styled. His hand reaches to switch off the bathroom light. The hallway has beige carpet and light gray walls. A framed abstract print hangs on the wall. Light from the bedroom window illuminates the hallway ahead.

---

## PART 3: GETTING DRESSED (7:25 AM - 7:35 AM)

### Scene 039: Back in the Bedroom
**Time:** 7:25 AM — bright morning light  
**Setting:** Bedroom, full view  
**Description:** Matt enters the bedroom with the towel around his waist. The outfit he laid out earlier — light blue shirt, khaki chinos, belt, socks — remains on the neatly made bed. Morning sunlight fills the room through the open blinds. His body is dry now, hair styled. He walks toward the bed. The dresser with mirror is visible against the wall.

### Scene 040: Opening Underwear Drawer
**Time:** 7:26 AM — bright morning light  
**Setting:** Bedroom, at dresser  
**Description:** Matt's hand pulls open the top drawer of the white six-drawer dresser. Inside, neatly folded boxer briefs are visible in various dark colors — black, navy, gray. White undershirts are also folded on one side. His toweled waist is at drawer level. The dresser mirror reflects the bright window behind him.

### Scene 041: Putting on Underwear
**Time:** 7:26 AM — bright morning light  
**Setting:** Bedroom, side view  
**Description:** Matt steps into a pair of gray boxer briefs, pulling them up. The towel has been removed and lies on the floor beside him. One leg is through, he's pulling them up over the other. The bed with laid-out clothes is behind him. His back is partially to the viewer, maintaining modesty while showing the action.

### Scene 042: Putting on Undershirt
**Time:** 7:27 AM — bright morning light  
**Setting:** Bedroom, front view  
**Description:** Matt pulls a white crew-neck undershirt over his head, arms raised through the arm holes. The shirt is halfway down, his face emerging from the neck hole. The fabric stretches as he pulls it down over his torso. He wears gray boxer briefs. The dressed bed is visible behind him.

### Scene 043: Putting on Dress Shirt
**Time:** 7:28 AM — bright morning light  
**Setting:** Bedroom, at bed  
**Description:** Matt picks up the light blue oxford button-down shirt from the bed, slipping his right arm into the sleeve. The shirt is partially on, draped over one shoulder. The khaki chinos, belt, and socks remain on the bed. He wears the white undershirt and gray boxer briefs. Morning light catches the cotton fabric of the shirt.

### Scene 044: Buttoning Dress Shirt
**Time:** 7:29 AM — bright morning light  
**Setting:** Bedroom, facing mirror  
**Description:** Matt stands before the full-length mirror on the closet door, buttoning his light blue shirt from bottom to top. His fingers work on a middle button. The shirt is mostly buttoned, collar still open. He wears the white undershirt beneath and gray boxer briefs. His expression is focused, routine. The mirror reflects the bright room.

### Scene 045: Putting on Chinos
**Time:** 7:30 AM — bright morning light  
**Setting:** Bedroom, side view  
**Description:** Matt steps into the khaki chinos, pulling them up one leg at a time. He balances on one foot, the other leg entering the pant leg. The pants are mid-thigh, being pulled up. His blue shirt is buttoned and untucked. The bed with the remaining items — belt, socks — is beside him.

### Scene 046: Zipping and Buttoning Pants
**Time:** 7:31 AM — bright morning light  
**Setting:** Bedroom, close-up on waist  
**Description:** Close-up of Matt's hands zipping up the khaki chinos and fastening the button at the waist. The metal zipper and brass button are visible. The light blue shirt is untucked, partially covering the waistband. His fingers pinch the button through the hole. Belt loops are empty and visible.

### Scene 047: Threading the Belt
**Time:** 7:31 AM — bright morning light  
**Setting:** Bedroom, close-up on waist  
**Description:** Matt threads a brown leather belt through the belt loops of his khaki chinos. His hands guide the belt through each loop, moving around his waist. The silver buckle hangs waiting. The blue shirt is still untucked. The belt is classic brown leather with a simple rectangular buckle.

### Scene 048: Buckling the Belt
**Time:** 7:32 AM — bright morning light  
**Setting:** Bedroom, close-up on waist  
**Description:** Close-up of Matt's hands fastening the brown leather belt buckle. The prong goes through a worn hole in the leather. The buckle is secured at his waist. The khaki chinos and blue shirt (still untucked) frame the belt. His fingers adjust the fit.

### Scene 049: Tucking in Shirt
**Time:** 7:32 AM — bright morning light  
**Setting:** Bedroom, facing mirror  
**Description:** Matt tucks the light blue oxford shirt into his khaki chinos, hands pushing the fabric down around his waist. He looks at his reflection in the closet mirror, adjusting the tuck to be neat and even. The brown belt is visible at his waist. His movements are practiced, making sure the shirt lies flat without bunching.

### Scene 050: Sitting to Put on Socks
**Time:** 7:33 AM — bright morning light  
**Setting:** Bedroom, edge of bed  
**Description:** Matt sits on the edge of the made bed, picking up the navy blue dress socks. He lifts one foot, ankle resting on opposite knee, about to pull the sock on. The brown leather dress shoes sit on the carpet beside his feet. His outfit is nearly complete — blue shirt tucked into khakis with brown belt. Morning light from the window illuminates him.

### Scene 051: Pulling on Socks
**Time:** 7:33 AM — bright morning light  
**Setting:** Bedroom, close-up on feet  
**Description:** Close-up of Matt's hands pulling a navy blue sock onto his foot. The sock stretches over his toes and heel. His other foot already has a sock on. The carpet beneath is beige. The brown leather shoes wait nearby.

### Scene 052: Putting on Dress Shoes
**Time:** 7:34 AM — bright morning light  
**Setting:** Bedroom, at bed  
**Description:** Matt slides his right foot into a brown leather oxford dress shoe, using a finger at the heel to help it in. He's still seated on the bed edge. His left foot is already in its shoe. The shoes are polished and professional. His khaki pants leg rises slightly, showing the navy sock above the shoe.

### Scene 053: Tying Shoelaces
**Time:** 7:34 AM — bright morning light  
**Setting:** Bedroom, close-up on shoes  
**Description:** Close-up of Matt's hands tying the brown laces of his dress shoe in a neat bow. His fingers loop and pull the laces tight. The polished brown leather shoe gleams. The khaki pant leg is visible above. The beige carpet is beneath.

### Scene 054: Final Mirror Check
**Time:** 7:35 AM — bright morning light  
**Setting:** Bedroom, full-length mirror  
**Description:** Matt stands before the full-length closet mirror, doing a final check of his appearance. He wears the complete outfit: light blue oxford shirt tucked into khaki chinos, brown leather belt, brown leather dress shoes. His hair is neatly styled. He adjusts his collar slightly, turning to check the side view. His reflection shows a polished, professional young man ready for work.

---

## PART 4: BREAKFAST AND KITCHEN (7:35 AM - 7:55 AM)

### Scene 055: Walking to Kitchen
**Time:** 7:35 AM — bright morning light  
**Setting:** Hallway/living area  
**Description:** Matt walks from the bedroom through a short hallway into the open-concept living and kitchen area. He's fully dressed for work. The hallway opens into a modest living room with a gray fabric sofa, coffee table, and TV on a stand. Beyond it, the kitchen is visible with white cabinets and a breakfast bar. Morning light comes through sliding glass doors leading to a small balcony.

### Scene 056: Entering the Kitchen
**Time:** 7:36 AM — bright morning light  
**Setting:** Kitchen, full view  
**Description:** Matt enters the kitchen area, a modest galley-style kitchen with white cabinets, gray countertops, and stainless steel appliances. A coffee maker sits on the counter near the sink. A toaster is next to it. The refrigerator is stainless steel with a few magnets and a calendar. A microwave is mounted above the stove. Sunlight streams in from the adjacent living room windows.

### Scene 057: Opening Cabinet for Coffee Mug
**Time:** 7:36 AM — bright kitchen light  
**Setting:** Kitchen, at cabinets  
**Description:** Matt opens an upper white cabinet door, reaching for a coffee mug. Inside the cabinet, several mugs are visible — various colors and styles. His hand selects a plain white ceramic mug. Plates and bowls are stacked on other shelves. The cabinet hinges gleam. His blue shirt sleeve is visible as he reaches up.

### Scene 058: Setting Mug by Coffee Maker
**Time:** 7:37 AM — bright kitchen light  
**Setting:** Kitchen, counter area  
**Description:** Matt places the white ceramic mug on the gray countertop next to the black coffee maker. The coffee maker is a standard drip machine with a glass carafe. A bag of coffee grounds sits nearby, slightly open. The toaster is visible to the right. The counter also holds a small wooden knife block and a fruit bowl with two bananas and an apple.

### Scene 059: Opening Coffee Bag
**Time:** 7:37 AM — bright kitchen light  
**Setting:** Kitchen, close-up on counter  
**Description:** Close-up of Matt's hands opening a bag of ground coffee, pulling apart the resealable top. The brown coffee grounds are visible inside, aromatic. The bag label shows a generic coffee brand. The white mug and coffee maker are in the soft background. Coffee grounds are dark and rich in color.

### Scene 060: Scooping Coffee Grounds
**Time:** 7:38 AM — bright kitchen light  
**Setting:** Kitchen, at coffee maker  
**Description:** Matt uses a plastic measuring scoop to take coffee grounds from the bag, transferring them to the coffee maker's filter basket. The scoop is filled with dark brown grounds. The filter basket is pulled out from the machine. His other hand holds the bag. Some grounds scatter slightly on the counter.

### Scene 061: Adding Water to Coffee Maker
**Time:** 7:38 AM — bright kitchen light  
**Setting:** Kitchen, at sink  
**Description:** Matt fills the glass coffee carafe with water from the kitchen sink's chrome faucet. Water streams into the carafe, level rising. The sink is stainless steel with a few dishes in it. Through the window above the sink, the parking lot and another building are visible. His hand holds the carafe handle under the flowing water.

### Scene 062: Pouring Water into Coffee Maker
**Time:** 7:39 AM — bright kitchen light  
**Setting:** Kitchen, at coffee maker  
**Description:** Matt pours water from the glass carafe into the reservoir at the top of the coffee maker. The water level rises in the reservoir. Steam begins to wisp as the machine starts warming. The filter basket with grounds is closed. The machine's digital display shows the time.

### Scene 063: Starting the Coffee Maker
**Time:** 7:39 AM — bright kitchen light  
**Setting:** Kitchen, close-up on coffee maker  
**Description:** Matt's finger presses the "Brew" button on the coffee maker. A small red light illuminates, indicating the brewing cycle has started. The digital display shows "BREWING." The machine begins to hum. The glass carafe sits on the warming plate below, empty but waiting.

### Scene 064: Opening Refrigerator
**Time:** 7:40 AM — bright kitchen light with fridge glow  
**Setting:** Kitchen, at refrigerator  
**Description:** Matt opens the stainless steel refrigerator door, the interior light illuminating its contents. Inside, the shelves hold various items: a carton of milk, a carton of orange juice, a package of deli meat, cheese, condiments in the door, leftover containers, vegetables in the crisper. The cold air creates a slight mist. Matt looks inside, deciding what to grab.

### Scene 065: Taking Out Butter
**Time:** 7:40 AM — bright kitchen light  
**Setting:** Kitchen, at refrigerator  
**Description:** Matt reaches into the refrigerator door shelf, taking out a stick of butter in its paper wrapper on a small dish. The butter dish is white ceramic. His other hand holds the fridge door open. The interior light illuminates the action. Condiment bottles line the door shelves — ketchup, mustard, mayonnaise.

### Scene 066: Getting Bread from Bread Box
**Time:** 7:41 AM — bright kitchen light  
**Setting:** Kitchen, at counter  
**Description:** Matt lifts the wooden lid of a bread box on the counter, revealing a loaf of sliced white bread in its plastic bag inside. His hand reaches in to pull out the bag. The bread box is light oak wood with a curved top. The kitchen counter shows the coffee maker now dripping coffee into the carafe.

### Scene 067: Taking Bread Slices
**Time:** 7:41 AM — bright kitchen light  
**Setting:** Kitchen, close-up on counter  
**Description:** Close-up of Matt's hands opening the plastic bread bag with a twist tie, pulling out two slices of white bread. The bread is soft and fresh. The twist tie is between his fingers. The bread bag lies on the gray counter. Crumbs scatter slightly.

### Scene 068: Placing Bread in Toaster
**Time:** 7:42 AM — bright kitchen light  
**Setting:** Kitchen, at toaster  
**Description:** Matt drops two slices of white bread into the slots of a silver two-slice toaster. His fingers release the bread into the wide slots. The toaster is chrome with a black base and a dial for darkness settings. The lever on the side is in the up position. The counter behind shows the coffee maker steadily brewing.

### Scene 069: Pushing Toaster Lever Down
**Time:** 7:42 AM — bright kitchen light  
**Setting:** Kitchen, close-up on toaster  
**Description:** Close-up of Matt's hand pushing down the lever on the side of the chrome toaster. The bread slices descend into the slots as the lever clicks into place. The heating elements begin to glow orange inside. A slight mechanical click sounds. The darkness dial is set to medium.

### Scene 070: Coffee Brewing
**Time:** 7:43 AM — bright kitchen light  
**Setting:** Kitchen, view of coffee maker  
**Description:** The coffee maker actively brews, dark coffee streaming from the filter basket into the glass carafe below. Steam rises from the fresh coffee. The carafe is about one-third full with dark brown liquid. The aroma of fresh coffee fills the space. The red brewing light glows on the machine's panel. Matt is visible in the background, preparing other things.

### Scene 071: Getting a Plate
**Time:** 7:44 AM — bright kitchen light  
**Setting:** Kitchen, at cabinets  
**Description:** Matt opens a lower cabinet, pulling out a white ceramic plate. Stacks of matching plates are visible inside the cabinet. He holds the plate in one hand, closing the cabinet door with the other. The kitchen shows morning activity — coffee brewing, toaster glowing.

### Scene 072: Taking Butter Knife from Drawer
**Time:** 7:44 AM — bright kitchen light  
**Setting:** Kitchen, at drawer  
**Description:** Matt opens a drawer below the counter, revealing a utensil organizer with various silverware — forks, knives, spoons in separate compartments. His hand selects a butter knife from the knife section. The drawer is neatly organized. Other items like a can opener and measuring spoons are in separate sections.

### Scene 073: Toast Popping Up
**Time:** 7:46 AM — bright kitchen light  
**Setting:** Kitchen, at toaster  
**Description:** The toaster lever pops up with a mechanical snap, ejecting two golden-brown toast slices that rise above the slots. Steam wisps from the hot toast. The bread is perfectly toasted — golden brown with slightly darker edges. The chrome toaster reflects the kitchen light. Matt turns toward the sound.

### Scene 074: Removing Toast from Toaster
**Time:** 7:46 AM — bright kitchen light  
**Setting:** Kitchen, at toaster  
**Description:** Matt carefully picks the hot toast slices out of the toaster slots, fingers gripping the edges that protrude above. The toast is warm, slight steam rising. His fingers carefully avoid the hot metal. He transfers them toward the white plate on the counter.

### Scene 075: Placing Toast on Plate
**Time:** 7:47 AM — bright kitchen light  
**Setting:** Kitchen, close-up on plate  
**Description:** Matt sets the two slices of golden-brown toast onto the white ceramic plate. The toast is arranged neatly, slightly overlapping. The plate sits on the gray counter. Toast crumbs scatter slightly. The warm toast glistens with a slight sheen.

### Scene 076: Spreading Butter on Toast
**Time:** 7:47 AM — bright kitchen light  
**Setting:** Kitchen, close-up on plate  
**Description:** Close-up of Matt's hand using the butter knife to spread butter on a slice of toast. The knife drags across the golden surface, leaving a trail of melting yellow butter. A curl of butter sits on the knife blade. The butter dish is beside the plate. The butter melts into the warm bread, darkening slightly where absorbed.

### Scene 077: Coffee Maker Finished
**Time:** 7:48 AM — bright kitchen light  
**Setting:** Kitchen, at coffee maker  
**Description:** The coffee maker's red light has turned off, indicating brewing is complete. The glass carafe is full of dark, fresh coffee. Steam rises from the carafe. The warming plate keeps it hot. The machine displays "READY." Matt approaches with his white mug in hand.

### Scene 078: Pouring Coffee into Mug
**Time:** 7:48 AM — bright kitchen light  
**Setting:** Kitchen, at coffee maker  
**Description:** Matt lifts the glass carafe from the coffee maker and pours hot black coffee into the white ceramic mug. The dark liquid streams from the carafe spout. Steam rises from the mug. His other hand steadies the mug on the counter. The coffee level rises in the mug, nearly filling it.

### Scene 079: Opening Refrigerator for Milk
**Time:** 7:49 AM — bright kitchen light  
**Setting:** Kitchen, at refrigerator  
**Description:** Matt opens the refrigerator again, reaching for a carton of milk on the top shelf. The carton is white with blue labeling — 2% milk. His hand grips the carton. The fridge interior light illuminates the scene. Other items are visible on surrounding shelves.

### Scene 080: Adding Milk to Coffee
**Time:** 7:49 AM — bright kitchen light  
**Setting:** Kitchen, close-up on mug  
**Description:** Matt pours a splash of milk from the carton into the mug of black coffee. The white milk swirls into the dark coffee, creating beautiful tan patterns as it mixes. His hand tilts the milk carton. The mug sits on the counter. The milk cloud expands and lightens the coffee.

### Scene 081: Stirring Coffee
**Time:** 7:50 AM — bright kitchen light  
**Setting:** Kitchen, close-up on mug  
**Description:** Matt stirs the coffee with a small spoon, mixing the milk throughout. The liquid swirls in the mug, color evening out to a medium brown. The spoon clinks softly against the ceramic. His fingers grip the spoon handle. The coffee is now a uniform light brown color.

### Scene 082: Carrying Breakfast to Counter
**Time:** 7:50 AM — bright morning light  
**Setting:** Kitchen, view of breakfast bar  
**Description:** Matt carries the plate of buttered toast in one hand and the mug of coffee in the other, walking to the breakfast bar — a raised countertop with two bar stools. The plate is set down, then the mug. The kitchen is behind him. Morning light comes through the living room windows. A phone sits on the counter.

### Scene 083: Sitting at Breakfast Bar
**Time:** 7:51 AM — bright morning light  
**Setting:** Kitchen, at breakfast bar  
**Description:** Matt sits on a gray upholstered bar stool at the breakfast bar, his plate of toast and coffee mug before him. He reaches for a slice of toast. His posture is relaxed but alert for the morning. The living room is visible beyond — gray sofa, TV. Sunlight streams through the sliding glass doors.

### Scene 084: Taking a Bite of Toast
**Time:** 7:51 AM — bright morning light  
**Setting:** Kitchen, close-up  
**Description:** Matt bites into the buttered toast, the bread crunching slightly. His mouth is open, taking a bite from the corner. Crumbs fall slightly. The golden toast with visible butter is in his hands. The coffee mug steams beside the plate. His expression is neutral, routine.

### Scene 085: Sipping Coffee
**Time:** 7:52 AM — bright morning light  
**Setting:** Kitchen, at breakfast bar  
**Description:** Matt lifts the white mug of coffee to his lips, taking a sip. Both hands wrap around the warm mug. His eyes look slightly down. Steam rises near his face. The plate with remaining toast sits on the counter. The morning light creates a warm atmosphere.

### Scene 086: Checking Phone While Eating
**Time:** 7:53 AM — bright morning light  
**Setting:** Kitchen, at breakfast bar  
**Description:** Matt looks at his smartphone while eating breakfast, the phone in one hand, a half-eaten slice of toast in the other. The phone screen shows notifications — emails, news headlines. The coffee mug and plate are on the counter. His eyes scan the screen. Morning routine multitasking.

### Scene 087: Finishing Breakfast
**Time:** 7:55 AM — bright morning light  
**Setting:** Kitchen, at breakfast bar  
**Description:** Matt takes the last bite of toast, the plate now empty except for crumbs. The coffee mug is nearly empty, just a bit of liquid remaining. He chews, looking at the window. The morning light is bright. He's almost ready to leave.

### Scene 088: Carrying Dishes to Sink
**Time:** 7:56 AM — bright morning light  
**Setting:** Kitchen, at sink  
**Description:** Matt carries the empty plate and mug to the kitchen sink. He places them in the stainless steel basin, which has a few other dishes from previous days. The window above the sink shows the parking lot outside. Water droplets are on some of the dishes. He doesn't wash them — no time.

---

## PART 5: LEAVING THE APARTMENT (7:55 AM - 8:05 AM)

### Scene 089: Walking to Living Room
**Time:** 7:57 AM — bright morning light  
**Setting:** Living room  
**Description:** Matt walks through the living room, passing the gray fabric sofa with throw pillows, a wooden coffee table with a few magazines and a remote control, and a TV on a black stand against the wall. The sliding glass doors to the balcony let in bright sunlight. A small bookshelf with books and some framed photos is against one wall.

### Scene 090: Getting Bag from Chair
**Time:** 7:57 AM — bright morning light  
**Setting:** Living room, near door  
**Description:** Matt picks up a black messenger bag / laptop bag from where it sits on an armchair near the front door. The bag has a shoulder strap and buckle closure. A laptop shape is visible through the fabric. He lifts it by the strap, swinging it over his shoulder. The front door is visible nearby — white with a deadbolt and chain.

### Scene 091: Putting on Bag
**Time:** 7:58 AM — bright morning light  
**Setting:** Living room, near door  
**Description:** Matt adjusts the black messenger bag across his body, the strap diagonal across his chest, bag resting at his hip. He adjusts the strap length with a buckle. His blue shirt and khaki pants are neat. He's ready to go.

### Scene 092: Getting Keys from Bowl
**Time:** 7:58 AM — bright morning light  
**Setting:** Entryway, near door  
**Description:** Matt reaches into a small ceramic bowl on a narrow entry table near the door, grabbing his car keys. The keys are on a silver ring with a Honda key fob, house keys, and a small keychain. The bowl also contains some loose change and a few receipts. A small mirror hangs on the wall above the table.

### Scene 093: Patting Pockets to Check
**Time:** 7:59 AM — bright morning light  
**Setting:** Entryway  
**Description:** Matt pats his pockets — front pants pocket for phone, back pocket for wallet — checking he has everything. His expression is routine concentration. Keys are in his hand. The messenger bag is over his shoulder. The front door is beside him. He feels the reassuring shapes in his pockets.

### Scene 094: Unlocking Front Door
**Time:** 7:59 AM — bright morning light  
**Setting:** Entryway, at front door  
**Description:** Matt's hand turns the deadbolt lock on the white front door. The brass deadbolt knob turns from horizontal to vertical. The door is a standard apartment door with a peephole at eye level. The door handle is brass. His other hand is ready to open the door.

### Scene 095: Opening Front Door
**Time:** 8:00 AM — bright light from hallway  
**Setting:** Doorway, view into apartment hallway  
**Description:** Matt opens the front door, revealing the apartment building hallway. The hallway has beige carpet, off-white walls, and evenly spaced doors to other apartments. Overhead fluorescent lights illuminate the corridor. A door number "207" is visible on his door. He steps through the doorway, bag on shoulder.

### Scene 096: Pulling Door Shut
**Time:** 8:00 AM — bright hallway light  
**Setting:** Apartment hallway  
**Description:** Matt pulls his apartment door shut behind him, hand on the brass handle. He's standing in the hallway, looking back at the closing door. Other apartment doors line the hallway. The carpet muffles sound. A small decorative table with a fake plant is near the elevator.

### Scene 097: Locking Door from Outside
**Time:** 8:01 AM — bright hallway light  
**Setting:** Apartment hallway  
**Description:** Matt inserts his apartment key into the deadbolt lock on the outside of his door, turning it to lock. Door number "207" is clearly visible on the door. His messenger bag hangs at his side. The hallway stretches behind him. The key turns with a click.

### Scene 098: Walking to Elevator
**Time:** 8:01 AM — bright hallway light  
**Setting:** Apartment hallway  
**Description:** Matt walks down the apartment hallway toward the elevator, passing several other apartment doors. The hallway is quiet, morning light coming from a window at the end. His footsteps are soft on the beige carpet. He holds his keys loosely in one hand. The elevator doors are visible ahead — silver metal.

### Scene 099: Pressing Elevator Button
**Time:** 8:02 AM — bright hallway light  
**Setting:** Apartment hallway, at elevator  
**Description:** Matt's finger presses the down arrow button beside the silver elevator doors. The button illuminates with a soft glow. He waits, looking at the floor indicator above the doors. The display shows the elevator is on floor 4, coming down. His reflection is visible in the polished elevator doors.

### Scene 100: Elevator Doors Opening
**Time:** 8:02 AM — bright elevator light  
**Setting:** Apartment hallway, at elevator  
**Description:** The silver elevator doors slide open, revealing the interior of a small apartment elevator — beige walls, a handrail, mirrored back wall, buttons panel on the side. The interior light is bright. The elevator is empty. Matt steps forward to enter.

### Scene 101: Inside Elevator
**Time:** 8:02 AM — elevator interior light  
**Setting:** Inside elevator  
**Description:** Matt stands inside the small elevator, pressing the "1" button on the panel. The button lights up. The elevator panel shows floors 1-4 and buttons for door open/close, alarm. His reflection is visible in the mirrored back wall. The elevator begins to descend, a slight sensation of movement. He watches the floor indicator change.

### Scene 102: Elevator Doors Opening at Ground Floor
**Time:** 8:03 AM — bright lobby light  
**Setting:** Elevator opening to lobby  
**Description:** The elevator doors open on the ground floor, revealing the apartment building lobby. The lobby has tiled floors, a few chairs, a row of mailboxes on one wall, glass front doors showing the parking lot outside. Bright morning light comes through the glass. Matt steps out of the elevator.

### Scene 103: Walking Through Lobby
**Time:** 8:03 AM — bright lobby light  
**Setting:** Building lobby  
**Description:** Matt walks through the apartment lobby, passing the mailboxes (small metal doors with numbers and keyholes), a bulletin board with community notices, and a fake potted plant. The glass front doors are ahead. Through them, the parking lot and parked cars are visible. The tiled floor is clean, light gray.

### Scene 104: Pushing Open Glass Door
**Time:** 8:04 AM — bright outdoor light  
**Setting:** Building entrance  
**Description:** Matt pushes open the glass front door of the apartment building, stepping outside. The door has a metal handle and a "PUSH" sign. Bright morning sunlight hits him. The parking lot is ahead — asphalt with painted lines, various cars parked. Trees and bushes landscape the building perimeter.

### Scene 105: Walking to Parking Lot
**Time:** 8:04 AM — bright morning outdoor light  
**Setting:** Apartment building exterior  
**Description:** Matt walks along a concrete sidewalk from the building entrance toward the parking lot. The apartment building is visible behind him — a three-story beige stucco building with balconies. Cars are parked in the lot ahead. A few trees provide shade. The sky is bright blue with a few clouds. Morning shadows are still long.

### Scene 106: Approaching His Car
**Time:** 8:05 AM — bright morning outdoor light  
**Setting:** Parking lot  
**Description:** Matt walks toward his car — a silver Honda Civic sedan parked in a spot. The car is a few years old but clean. Other cars are parked nearby — various makes and colors. The asphalt parking lot has white painted lines marking spaces. His keys are in his hand, thumb on the key fob.

### Scene 107: Unlocking Car with Key Fob
**Time:** 8:05 AM — bright outdoor light  
**Setting:** Parking lot, near car  
**Description:** Matt points the key fob at his silver Honda Civic and presses the unlock button. The car's lights flash briefly, and a soft beep sounds. The door handles click unlocked. He walks closer to the driver's door. The car's chrome trim gleams in the morning sun. His reflection is visible in the car window.

---

## PART 6: THE COMMUTE — DRIVING TO WORK (8:05 AM - 8:35 AM)

### Scene 108: Opening Car Door
**Time:** 8:05 AM — bright outdoor light  
**Setting:** Parking lot, at car  
**Description:** Matt opens the driver's side door of his silver Honda Civic. The door swings open, revealing the gray interior — cloth seats, steering wheel, dashboard. The car interior is reasonably clean with a phone mount on the dashboard. He ducks his head to get in, messenger bag shifting on his shoulder.

### Scene 109: Getting into Driver's Seat
**Time:** 8:06 AM — interior car light  
**Setting:** Inside car  
**Description:** Matt slides into the driver's seat, placing his messenger bag on the passenger seat beside him. The car's interior has gray cloth seats, a black dashboard with digital display, and a center console with cup holders. He settles in, adjusting his position. The door is still open, letting in outside light.

### Scene 110: Closing Car Door
**Time:** 8:06 AM — interior car light  
**Setting:** Inside car  
**Description:** Matt pulls the driver's door closed with a solid thunk. The interior light begins to dim. Through the window, the parking lot is visible. His hand grips the interior door handle to pull it shut. The door seals with a satisfying sound.

### Scene 111: Putting on Seatbelt
**Time:** 8:06 AM — interior car with morning light  
**Setting:** Inside car, driver's seat  
**Description:** Matt reaches over his shoulder for the seatbelt, pulling it across his chest and clicking it into the buckle at his hip. The gray seatbelt crosses his light blue shirt. The buckle clicks securely. The car's dashboard warning light for seatbelt turns off.

### Scene 112: Inserting Key / Pressing Start Button
**Time:** 8:07 AM — interior car light  
**Setting:** Inside car, dashboard area  
**Description:** Matt presses the start button on the dashboard, his foot on the brake. The engine comes to life, the dashboard illuminating with gauges and displays. The radio automatically turns on at low volume. The car hums with readiness. The digital display shows time, fuel level, and temperature.

### Scene 113: Checking Mirrors
**Time:** 8:07 AM — interior car light  
**Setting:** Inside car, mirror views  
**Description:** Matt adjusts the rearview mirror, his eyes checking it. The mirror shows the view out the back window — parked cars behind him. He then glances at the side mirror, checking for obstacles. His hand touches the mirror's adjustment. His expression is focused, routine driver checks.

### Scene 114: Putting Car in Reverse
**Time:** 8:08 AM — interior car light  
**Setting:** Inside car, center console  
**Description:** Matt moves the gear shifter from Park to Reverse. His right hand grips the shifter knob, moving it down. The dashboard display shows "R" for reverse. The rearview camera activates on the center screen, showing the view behind the car. He looks over his shoulder as well.

### Scene 115: Backing Out of Parking Space
**Time:** 8:08 AM — view from inside car  
**Setting:** Inside car, looking out  
**Description:** View from inside the car as Matt backs out of the parking space. Through the rear window and rearview camera screen, the parking lot is visible — other parked cars, the apartment building in the background. His hands are on the steering wheel, turning it to guide the car. The car moves slowly backward.

### Scene 116: Putting Car in Drive
**Time:** 8:09 AM — interior car light  
**Setting:** Inside car, center console  
**Description:** Matt shifts the gear from Reverse to Drive. His hand moves the shifter. The dashboard display shows "D" for drive. He takes his foot off the brake and presses lightly on the gas. The car begins to move forward through the parking lot.

### Scene 117: Driving Through Parking Lot
**Time:** 8:09 AM — view from inside car  
**Setting:** Inside car, looking through windshield  
**Description:** View through the windshield as Matt drives through the apartment parking lot toward the exit. Parked cars line both sides. A speed bump is ahead. The parking lot exit gate or driveway is visible. Trees and landscaping border the lot. The morning sun is ahead and slightly to the left.

### Scene 118: Exiting Parking Lot onto Street
**Time:** 8:10 AM — view from inside car  
**Setting:** Inside car, at parking lot exit  
**Description:** Matt stops at the parking lot exit, looking both ways at the suburban street. Through the windshield, a residential street is visible — houses, trees, parked cars along the curb. He turns right onto the street. The car's turn signal ticks. A stop sign or yield sign is at the exit.

### Scene 119: Driving on Residential Street
**Time:** 8:11 AM — view from inside car  
**Setting:** Inside car, suburban street  
**Description:** View through the windshield as Matt drives down a quiet suburban residential street. Single-family homes with front lawns line both sides. Trees create dappled shadows on the road. Parked cars are along curbs. A person walks a dog on the sidewalk. The speed limit is 25 mph. Morning light filters through the trees.

### Scene 120: Approaching Stop Sign
**Time:** 8:12 AM — view from inside car  
**Setting:** Inside car, at intersection  
**Description:** View through the windshield approaching a four-way stop sign at a residential intersection. The red octagonal stop sign is clearly visible. Matt's hands are on the steering wheel, preparing to stop. Another car is waiting at the cross street. Houses are on each corner of the intersection.

### Scene 121: Stopped at Stop Sign
**Time:** 8:12 AM — view from inside car  
**Setting:** Inside car, at stop sign  
**Description:** The car is fully stopped at the stop sign. Through the windshield, the intersection is visible. Matt looks left and right, checking for traffic. His foot is on the brake pedal. The dashboard is visible at the bottom of the frame. The stop sign is immediately to the left.

### Scene 122: Turning onto Main Road
**Time:** 8:13 AM — view from inside car  
**Setting:** Inside car, turning  
**Description:** Matt turns right from the residential street onto a larger suburban main road. Through the windshield, the wider road is visible — two lanes in each direction, retail and commercial buildings along the sides. A gas station is on the corner. Traffic is moderate for morning commute. The turn signal clicks.

### Scene 123: Driving on Main Road
**Time:** 8:14 AM — view from inside car  
**Setting:** Inside car, suburban commercial road  
**Description:** View through the windshield driving along a suburban main road. Commercial strips line both sides — strip malls, fast food restaurants, a grocery store, a bank. Traffic moves steadily. Other cars are ahead and in adjacent lanes. Traffic lights are visible ahead. Signs for various businesses are prominent.

### Scene 124: Stopped at Red Light
**Time:** 8:16 AM — view from inside car  
**Setting:** Inside car, at traffic light  
**Description:** Matt's car is stopped at a red traffic light. Through the windshield, the traffic light shows red. Cross traffic passes through the intersection. A pedestrian walks in the crosswalk. The dashboard shows the car is in Drive but stationary. Matt's hands rest on the steering wheel. A Starbucks is visible on the corner.

### Scene 125: Turning into Coffee Shop Drive-Through
**Time:** 8:17 AM — view from inside car  
**Setting:** Inside car, approaching drive-through  
**Description:** After the light turns green, Matt turns right into a Starbucks parking lot, following signs for the drive-through. The Starbucks building is a typical suburban design with the green logo visible. A few cars are in the drive-through line ahead. The menu board is visible in the distance.

### Scene 126: Waiting in Drive-Through Line
**Time:** 8:18 AM — view from inside car  
**Setting:** Inside car, in drive-through lane  
**Description:** Matt's car waits behind two other vehicles in the Starbucks drive-through line. Through the windshield, the car ahead and the drive-through lane winding around the building are visible. The brick exterior of the Starbucks is to the left. Morning sunlight creates shadows. Matt checks his phone while waiting.

### Scene 127: At the Drive-Through Menu Board
**Time:** 8:20 AM — view from inside car  
**Setting:** Inside car, at menu/speaker  
**Description:** Matt's car is at the drive-through menu board and speaker. The large menu board shows drinks and food items with prices. A speaker box with a screen is at driver's window height. Through the window, Matt speaks his order. His window is rolled down. The morning air comes into the car.

### Scene 128: Ordering Coffee at Speaker
**Time:** 8:20 AM — close-up through car window  
**Setting:** At drive-through speaker  
**Description:** Close-up of Matt leaning slightly toward the open car window, speaking into the drive-through speaker. The menu board with coffee options is visible in the background. The speaker box has a small screen showing the order being entered. His mouth is open, mid-speech. Morning light illuminates his face.

### Scene 129: Driving to Pickup Window
**Time:** 8:21 AM — view from inside car  
**Setting:** Inside car, drive-through lane  
**Description:** Matt drives forward along the drive-through lane, rounding the corner of the building toward the pickup window. Through the windshield, the pickup window is visible ahead with a car already there receiving their order. A barista's figure is visible in the window. The lane is narrow, brick walls on one side.

### Scene 130: At the Pickup Window
**Time:** 8:23 AM — view from inside car  
**Setting:** Inside car, at pickup window  
**Description:** Matt's car is at the drive-through pickup window. A barista in a green apron and black cap leans out, handing a paper coffee cup toward Matt. Matt reaches out through his open window to take the cup. The window shows the interior of the coffee shop — espresso machines, other workers. Steam rises from the cup.

### Scene 131: Receiving Coffee Cup
**Time:** 8:23 AM — close-up at window  
**Description:** Close-up of the exchange at the pickup window. Matt's hand takes a white paper cup with a Starbucks logo and a brown cardboard sleeve from the barista's hand. The barista is smiling. The cup lid is black. A straw or napkins are also being offered. Morning light illuminates the transaction.

### Scene 132: Placing Coffee in Cup Holder
**Time:** 8:24 AM — inside car, center console  
**Setting:** Inside car, close-up  
**Description:** Matt places the Starbucks cup in the cup holder of his car's center console. The cup fits snugly in the round holder. The console also has a phone charging cable, some coins, and a sunglasses case. He steadies the cup before letting go. The brown sleeve and green logo are visible.

### Scene 133: Driving out of Drive-Through
**Time:** 8:24 AM — view from inside car  
**Setting:** Inside car, leaving drive-through  
**Description:** View through the windshield as Matt drives out of the Starbucks drive-through lane, back toward the main road. The Starbucks building is behind him. The parking lot connects to the main road. He signals left to re-enter traffic. The coffee cup is visible in the cup holder at the edge of the frame.

### Scene 134: Merging onto Road
**Time:** 8:25 AM — view from inside car  
**Setting:** Inside car, entering traffic  
**Description:** Matt merges back onto the main suburban road, checking mirrors and waiting for a gap in traffic. Through the windshield, traffic is visible — cars in both directions. He accelerates to match traffic speed. The shopping areas continue along the road. A traffic light is ahead.

### Scene 135: Taking a Sip of Coffee While Driving
**Time:** 8:26 AM — inside car  
**Setting:** Inside car, driver's perspective  
**Description:** At a red light, Matt reaches for the Starbucks cup in the cup holder, bringing it to his lips for a sip. One hand stays on the steering wheel. The cup lid is visible near his mouth. The traffic light ahead is red. Other cars are stopped around him. Steam wisps from the cup opening.

### Scene 136: Driving Toward Highway Entrance
**Time:** 8:28 AM — view from inside car  
**Setting:** Inside car, approaching highway  
**Description:** View through the windshield as Matt drives toward a highway entrance ramp. Green highway signs are visible overhead indicating "Interstate 78 East" and "Downtown." The ramp curves ahead. Traffic increases near the highway entrance. The suburban commercial area gives way to highway infrastructure.

### Scene 137: On Highway On-Ramp
**Time:** 8:29 AM — view from inside car  
**Setting:** Inside car, highway on-ramp  
**Description:** View through the windshield as Matt accelerates up the curved highway on-ramp. The ramp rises and curves to the right. Concrete barriers line the ramp edge. Ahead, the main highway is visible with traffic flowing. He checks his side mirror for merging. The speedometer shows increasing speed.

### Scene 138: Merging onto Highway
**Time:** 8:30 AM — view from inside car  
**Setting:** Inside car, highway  
**Description:** Matt merges from the on-ramp into highway traffic. Through the windshield, multiple lanes of traffic are visible — cars, a few trucks, all moving at highway speed. He enters the middle lane. Overpasses and highway infrastructure surround the road. The sky is bright blue above. The coffee cup vibrates slightly in its holder.

### Scene 139: Highway Driving
**Time:** 8:32 AM — view from inside car  
**Setting:** Inside car, highway  
**Description:** View through the windshield while cruising on the highway at 65 mph. Multiple lanes of traffic stretch ahead, taillights visible on cars ahead. Highway signs indicate upcoming exits. Suburban commercial areas are visible on both sides — office buildings, shopping centers. The dashboard shows speed and navigation.

### Scene 140: Taking Highway Exit
**Time:** 8:34 AM — view from inside car  
**Setting:** Inside car, highway exit  
**Description:** Matt takes a highway exit, following signs for "Industrial Parkway / Business Park." The exit curves to the right, descending from the highway. Through the windshield, the off-ramp leads toward an intersection below. Office buildings and business park structures are visible in the distance.

### Scene 141: Driving in Business Park Area
**Time:** 8:35 AM — view from inside car  
**Setting:** Inside car, business park  
**Description:** View through the windshield driving through a suburban business park area. Modern office buildings — three to five stories, glass and concrete — line a landscaped parkway. Trees and green spaces separate parking lots. Signs show various company names. Traffic is light. Well-maintained medians divide the road.

### Scene 142: Turning into Office Parking Lot
**Time:** 8:37 AM — view from inside car  
**Setting:** Inside car, entering work parking lot  
**Description:** Matt turns right into the parking lot of his office building — a modern three-story glass and brick structure with "PLAZA BUSINESS CENTER" on a sign. The parking lot is partially filled with employee cars. Landscaped islands with trees are throughout. He drives slowly, looking for a space.

### Scene 143: Finding a Parking Space
**Time:** 8:38 AM — view from inside car  
**Setting:** Inside car, parking lot  
**Description:** View through the windshield as Matt approaches an empty parking spot between two cars. He signals and begins turning into the space. Painted white lines mark the spot. The office building entrance is visible in the distance — glass doors, an awning. Other employees walk from cars toward the building.

### Scene 144: Parking the Car
**Time:** 8:38 AM — inside car  
**Setting:** Inside car, parking  
**Description:** Matt carefully pulls into the parking space, straightening the wheel. Through the windshield, the car ahead's trunk is visible. He shifts into Park. The engine idles. He checks his position using side mirrors. The car is centered in the space.

### Scene 145: Turning Off Engine
**Time:** 8:39 AM — inside car, center console  
**Setting:** Inside car, close-up  
**Description:** Close-up of Matt pressing the engine start/stop button, turning off the car. The dashboard displays go dark. The engine falls silent. His finger presses the button. The car is now parked and off. The coffee cup still sits in the cup holder, nearly empty.

### Scene 146: Gathering Belongings
**Time:** 8:39 AM — inside car  
**Setting:** Inside car, passenger seat  
**Description:** Matt reaches over to the passenger seat to grab his black messenger bag. His hand grips the strap. The coffee cup is also grabbed from the cup holder — he'll dispose of it inside. His seatbelt is already unbuckled. He prepares to exit.

### Scene 147: Opening Driver's Door to Exit
**Time:** 8:40 AM — car exterior  
**Setting:** Parking lot, at car  
**Description:** Matt opens the driver's side door, stepping out of the silver Honda Civic into the parking lot. He has his messenger bag over his shoulder and the empty coffee cup in one hand. The door swings open. Asphalt is beneath his brown dress shoes. Other parked cars surround his vehicle.

### Scene 148: Standing Next to Car
**Time:** 8:40 AM — bright outdoor light  
**Setting:** Parking lot  
**Description:** Matt stands next to his car, closing the door with his hip while adjusting his messenger bag strap. His full outfit is visible — light blue oxford, khaki chinos, brown belt and shoes. The silver Civic is beside him. The office building is visible in the background. Morning sunlight is bright. He holds the empty coffee cup.

### Scene 149: Locking Car with Key Fob
**Time:** 8:40 AM — bright outdoor light  
**Setting:** Parking lot  
**Description:** Matt presses the lock button on his key fob, pointed back at his car. The car's lights flash and horn gives a short beep, confirming it's locked. His thumb is on the fob button. The car is behind him. He begins walking toward the building.

### Scene 150: Walking Across Parking Lot
**Time:** 8:41 AM — bright outdoor light  
**Setting:** Office parking lot  
**Description:** Matt walks across the parking lot toward the office building entrance. His messenger bag bounces slightly at his side. Other employees walk nearby — people in business casual, carrying bags and coffees. The glass entrance of the building is ahead. Landscaped shrubs line the walkway. Shadows are still moderately long.

---

## PART 7: THE OFFICE — MORNING (8:45 AM - 12:00 PM)

### Scene 151: Approaching Building Entrance
**Time:** 8:42 AM — bright outdoor light  
**Setting:** Office building entrance  
**Description:** Matt approaches the glass front doors of the office building. The entrance has a modern design — large glass panels, metal framing, an awning over the doors. A company logo or "PLAZA BUSINESS CENTER" is on the glass. Through the doors, the lobby is visible. He reaches for the door handle. Potted plants flank the entrance.

### Scene 152: Entering Lobby
**Time:** 8:43 AM — bright lobby light  
**Setting:** Office building lobby  
**Description:** Matt walks into the building lobby, a modern space with polished floors, a reception desk, a seating area with chairs and a small table, and a directory board on the wall. Elevators are visible in the back. A security guard or receptionist sits at the desk. Other employees cross the lobby toward elevators. Indoor plants add greenery.

### Scene 153: Throwing Away Coffee Cup
**Time:** 8:43 AM — lobby light  
**Setting:** Office building lobby  
**Description:** Matt drops his empty Starbucks cup into a trash bin near the lobby entrance. The trash bin is sleek silver metal with a swing top. His hand releases the cup. The lobby is active behind him with people walking. A recycling bin is beside the trash.

### Scene 154: Walking to Elevators
**Time:** 8:44 AM — lobby light  
**Setting:** Office building lobby  
**Description:** Matt walks across the lobby toward the elevator bank — two or three elevator doors in a row. Other employees wait there, some looking at phones. He joins the group waiting. The elevator indicator shows numbers changing as elevators move between floors. His bag hangs at his side.

### Scene 155: Pressing Elevator Button
**Time:** 8:44 AM — lobby light  
**Setting:** Office building lobby, at elevators  
**Description:** Matt presses the "Up" elevator button, which illuminates. He stands waiting with a few other employees — a woman in business attire checking her phone, a man with a laptop bag. The elevator doors are brushed metal. The floor indicator above shows an elevator approaching.

### Scene 156: Elevator Doors Opening
**Time:** 8:45 AM — bright elevator light  
**Setting:** Office building lobby, elevators  
**Description:** The elevator doors slide open, revealing the interior — larger than the apartment elevator, with carpeted floor, mirrored back wall, and a panel of buttons. A few people exit. Matt and others step forward to enter. The elevator chimes softly.

### Scene 157: Inside Office Elevator
**Time:** 8:45 AM — elevator light  
**Setting:** Inside elevator  
**Description:** Matt stands in the elevator with several other people, facing forward. He's pressed the button for floor 3. The elevator button panel shows multiple floors lit up. Other passengers look at phones or stare ahead. The mirrored wall shows reflections. Soft elevator music plays. The elevator ascends.

### Scene 158: Exiting Elevator on Third Floor
**Time:** 8:46 AM — bright office light  
**Setting:** Third floor elevator area  
**Description:** The elevator doors open on the third floor, and Matt steps out into the office floor lobby area. A small waiting area with chairs is to one side. A frosted glass door with a company logo — "VERTEX MARKETING" — is ahead. A few other employees exit with him, heading toward the office door.

### Scene 159: Opening Office Door
**Time:** 8:46 AM — bright office light  
**Setting:** Office entrance  
**Description:** Matt opens the frosted glass door to the office suite, holding it with one hand. Through the door, the open office space is visible — cubicles, desks, computer monitors, people starting their workday. The company logo "VERTEX MARKETING" is on the glass. A reception desk is just inside. The office hums with morning activity.

### Scene 160: Walking Through Office
**Time:** 8:47 AM — bright office light  
**Setting:** Open office floor  
**Description:** Matt walks through the open-plan office, passing rows of cubicles with low gray partitions, shared desks, and employees settling in for the day. Computer monitors glow. People sip coffee, check emails, chat quietly. Large windows let in natural light. The carpet is gray industrial. Ceiling lights are bright fluorescent. He waves to a colleague.

### Scene 161: Arriving at His Cubicle
**Time:** 8:48 AM — bright office light  
**Setting:** Matt's cubicle  
**Description:** Matt arrives at his cubicle — a workstation with a desk, dual computer monitors, keyboard, mouse, and phone. The cubicle walls are low gray fabric. A few personal items decorate the space — a small plant, a photo of a mountain, a company mug. His chair is a black ergonomic office chair. Papers and folders are stacked neatly.

### Scene 162: Putting Down Bag
**Time:** 8:48 AM — bright office light  
**Setting:** Matt's cubicle  
**Description:** Matt places his black messenger bag on the floor next to his desk, leaning it against the cubicle wall. The bag slumps slightly with the weight of the laptop inside. His desk is at a comfortable sitting height. The chair is pushed back, ready for him to sit.

### Scene 163: Sitting Down at Desk
**Time:** 8:49 AM — bright office light  
**Setting:** Matt's cubicle  
**Description:** Matt pulls out his black office chair and sits down, rolling forward toward the desk. He adjusts his position, getting comfortable. The dual monitors are in front of him, currently dark or showing login screens. His keyboard and mouse are within reach. He loosens his shoulders and settles in.

### Scene 164: Moving Mouse to Wake Computer
**Time:** 8:49 AM — bright office light, screen glow  
**Setting:** Matt's cubicle, close-up on desk  
**Description:** Close-up of Matt's hand on the mouse, moving it to wake the computer from sleep. The screens begin to illuminate, displaying a Windows login screen with a user icon and password field. The mouse is black, sleek design. The keyboard is standard office black. His hand rests on the mouse.

### Scene 165: Typing Password
**Time:** 8:50 AM — screen glow  
**Setting:** Matt's cubicle, close-up on keyboard  
**Description:** Close-up of Matt's fingers typing his password on the keyboard. The keys press down as he types — only asterisks or dots appear in the password field on the screen. His fingers move confidently across the keys. The login screen is reflected in his eyes. The dual monitors glow.

### Scene 166: Desktop Loading
**Time:** 8:50 AM — screen glow  
**Setting:** Matt's cubicle, view of monitors  
**Description:** The computer desktop loads on Matt's dual monitors. Icons appear — Outlook, Chrome, Excel, internal company apps. The desktop background is a default landscape image. A taskbar at the bottom shows time and notifications. Matt watches the screen, waiting for programs to load. The screens illuminate his face.

### Scene 167: Opening Email Application
**Time:** 8:51 AM — screen glow  
**Setting:** Matt's cubicle, view of monitor  
**Description:** Matt clicks to open Microsoft Outlook on his computer. The application window fills the main monitor. His inbox appears — a list of unread emails from colleagues, newsletters, meeting notifications. A red badge shows 12 unread emails. He leans slightly forward, scanning the subjects.

### Scene 168: Reading an Email
**Time:** 8:52 AM — screen glow  
**Setting:** Matt's cubicle, view of monitor  
**Description:** Close-up of the monitor showing an open email. The email is from a manager, subject line "Q1 Marketing Review - Please Review Attached." The body text is visible — professional email requesting review of a document before a meeting. Matt's face is partially reflected in the screen, reading intently.

### Scene 169: Replying to an Email
**Time:** 8:55 AM — screen glow, keyboard sound  
**Setting:** Matt's cubicle  
**Description:** Matt types a reply email, fingers moving over the keyboard. The compose window is open on the screen — "RE: Q1 Marketing Review" in the subject. He types a professional response in the body. The cursor blinks at the end of his sentences. His expression is focused, professional.

### Scene 170: Taking a Sip from Office Mug
**Time:** 9:00 AM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt picks up a ceramic mug with a company logo from his desk, taking a sip. The mug contains water or cold coffee from a previous day. He holds it with one hand while looking at the screen with the other hand on the mouse. The mug is dark blue with "VERTEX" in white letters.

### Scene 171: Colleague Stopping By
**Time:** 9:15 AM — office light  
**Setting:** Matt's cubicle  
**Description:** A colleague — a woman in her 30s wearing a blouse and slacks, holding a tablet — stops by Matt's cubicle. She leans against the cubicle partition, smiling. They're in conversation — she asks a question or makes a comment. Matt swivels in his chair to face her, smiling back. The office bustles behind her.

### Scene 172: Brief Conversation with Colleague
**Time:** 9:16 AM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt and his colleague continue their brief conversation. She gestures with her hand while explaining something. Matt nods, listening. Other employees pass by in the background. The tone is friendly and professional. Coffee cups and paperwork are visible on nearby desks.

### Scene 173: Colleague Walking Away
**Time:** 9:18 AM — office light  
**Setting:** Office floor, view from cubicle  
**Description:** The colleague walks away from Matt's cubicle, heading back to her own workspace. Matt watches briefly, then turns back to his computer. The open office floor is visible — rows of cubicles, people working, natural light from windows. He refocuses on his monitors.

### Scene 174: Working on Spreadsheet
**Time:** 9:30 AM — screen glow  
**Setting:** Matt's cubicle, monitor view  
**Description:** Matt works on an Excel spreadsheet, the application filling his main monitor. The spreadsheet shows columns of data — marketing metrics, budget numbers, dates. His hand is on the mouse, clicking cells. Numbers and formulas fill the cells. The cursor moves across rows. His brow is slightly furrowed in concentration.

### Scene 175: Highlighting Data in Spreadsheet
**Time:** 9:35 AM — screen glow  
**Setting:** Matt's cubicle, close-up on monitor  
**Description:** Close-up of the Excel spreadsheet on the monitor. Matt uses the mouse to highlight a column of data, which turns blue when selected. Numbers are visible in the cells — sales figures, percentages. He's about to create a chart or perform a calculation. The toolbar ribbon is visible at the top.

### Scene 176: Making a Phone Call
**Time:** 10:00 AM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt picks up his desk phone — a standard black office phone with multiple buttons. He holds the handset to his ear while dialing numbers with his other hand. The phone cord curls below. His screen shows an email with a phone number visible. His expression is neutral, professional, preparing to speak.

### Scene 177: On the Phone
**Time:** 10:02 AM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt speaks on the phone, the handset to his ear, his free hand gesturing slightly or holding a pen. He looks at his screen while talking, referencing information. His tone is professional. Notes are scribbled on a notepad beside his keyboard. A colleague passes behind him.

### Scene 178: Taking Notes While on Call
**Time:** 10:05 AM — office light  
**Setting:** Matt's cubicle, close-up on desk  
**Description:** Close-up of Matt's hand writing notes on a yellow legal pad while on the phone. The handset is cradled between his shoulder and ear. The pen moves quickly, jotting down points. Words like "timeline," "budget," and "deliverables" are visible in handwriting. The desk surface shows keyboard, mouse, and papers.

### Scene 179: Ending Phone Call
**Time:** 10:10 AM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt says goodbye on the phone and places the handset back in its cradle. His hand releases the handset. He leans back in his chair slightly, processing the call. The notepad with notes is beside the keyboard. He takes a breath before returning to his computer work.

### Scene 180: Walking to Water Cooler
**Time:** 10:30 AM — office light  
**Setting:** Office break area  
**Description:** Matt walks through the office toward a water cooler in a small break area. The cooler is white and blue with a large water jug on top. A small counter with supplies — cups, coffee maker — is beside it. He holds an empty glass or gets a paper cup. Another employee is nearby, chatting.

### Scene 181: Filling Glass at Water Cooler
**Time:** 10:30 AM — office light  
**Setting:** Break area  
**Description:** Matt fills his glass with water from the cooler, pressing the blue lever. Water streams into the clear glass. Air bubbles rise in the large water jug above. The break area has a small refrigerator, microwave, and a table with a few chairs. A motivational poster is on the wall.

### Scene 182: Brief Chat at Water Cooler
**Time:** 10:32 AM — office light  
**Setting:** Break area  
**Description:** Matt stands near the water cooler chatting with a colleague — a man in his 40s with glasses, also holding a cup. They share a casual conversation — perhaps about the weekend or a work project. Both are relaxed, taking a short break. The office continues behind them through a doorway.

### Scene 183: Walking Back to Desk
**Time:** 10:35 AM — office light  
**Setting:** Office floor  
**Description:** Matt walks back through the office toward his cubicle, carrying his glass of water. He passes colleagues at their desks, some on phones, others typing. The open office layout shows rows of workstations. Natural light from windows creates a pleasant work environment. He sips the water as he walks.

### Scene 184: Attending a Meeting (Walking to Conference Room)
**Time:** 11:00 AM — office light  
**Setting:** Office hallway  
**Description:** Matt walks down an office hallway toward a conference room, carrying a laptop and notepad. The hallway has offices with name plates on doors, and meeting rooms with glass walls. Other colleagues walk alongside him or toward other destinations. A sign on a door reads "Conference Room B."

### Scene 185: Entering Conference Room
**Time:** 11:01 AM — bright conference room light  
**Setting:** Conference room entrance  
**Description:** Matt opens the glass door of the conference room, entering with his laptop and notepad. The room has a long rectangular table surrounded by office chairs, a large TV screen on the wall for presentations, and a whiteboard. Several colleagues are already seated, laptops open, chatting before the meeting starts. Natural light comes from windows.

### Scene 186: Sitting at Conference Table
**Time:** 11:02 AM — bright conference room light  
**Setting:** Conference room  
**Description:** Matt takes a seat at the conference table, pulling out a chair and sitting. He sets his laptop on the table and opens it, the screen facing him. His notepad and pen are beside it. Five or six colleagues sit around the table in various positions. Coffee cups and water bottles are scattered about. A projector screen or TV displays a title slide.

### Scene 187: Meeting in Progress
**Time:** 11:10 AM — conference room light  
**Setting:** Conference room  
**Description:** The meeting is in progress. A colleague stands at the front, presenting slides on the large screen — marketing charts and bullet points visible. Matt and others look at the presentation, some taking notes. A few colleagues have laptops open, others just notepads. The atmosphere is professional but collegial.

### Scene 188: Matt Speaking in Meeting
**Time:** 11:25 AM — conference room light  
**Setting:** Conference room  
**Description:** Matt speaks during the meeting, making a point or asking a question. His hand gestures slightly as he talks. Colleagues look toward him, listening. The presenter at the front pauses. Matt's laptop and notepad are in front of him. His expression is engaged, articulate. The presentation slide is visible on screen behind.

### Scene 189: Taking Notes in Meeting
**Time:** 11:35 AM — conference room light  
**Setting:** Conference room  
**Description:** Matt writes notes on his notepad during the meeting, pen moving across the yellow paper. The presenter continues in the background. His eyes glance between the notepad and the screen. Colleagues around him are similarly engaged — some typing on laptops, others listening. Coffee cups create rings on the table.

### Scene 190: Meeting Ending — People Standing
**Time:** 11:55 AM — conference room light  
**Setting:** Conference room  
**Description:** The meeting concludes. Colleagues push back chairs and stand, gathering laptops and notepads. Some chat in small groups. Matt closes his laptop and picks up his notepad. The presenter thanks everyone. The TV screen shows an ending slide with "Thank You" or "Questions?" The room transitions from focused meeting to casual dispersal.

---

## PART 8: LUNCH (12:00 PM - 1:00 PM)

### Scene 191: Back at Desk Before Lunch
**Time:** 12:00 PM — bright office light  
**Setting:** Matt's cubicle  
**Description:** Matt returns to his cubicle from the meeting, setting down his laptop. He checks his phone for the time. A colleague appears nearby, suggesting lunch. Matt nods, agreeing. He grabs his wallet from his desk drawer. The office is buzzing with pre-lunch energy. People are standing, moving toward exits.

### Scene 192: Walking with Colleagues Through Office
**Time:** 12:05 PM — bright office light  
**Setting:** Office floor  
**Description:** Matt walks through the office with two colleagues — a man and a woman, all in business casual. They chat and laugh as they head toward the exit. Others around them are also leaving for lunch. The mood is light, social. Jacket is grabbed from chair backs. The exit door is ahead.

### Scene 193: Exiting Office Building
**Time:** 12:08 PM — bright outdoor midday light  
**Setting:** Office building entrance  
**Description:** Matt and his two colleagues push through the glass front doors of the office building, stepping outside into the bright midday sun. The parking lot and surrounding business park are visible. The sun is high overhead, casting short shadows. The three walk together along the sidewalk, deciding where to eat.

### Scene 194: Walking on Business Park Sidewalk
**Time:** 12:10 PM — bright outdoor light  
**Setting:** Business park area  
**Description:** Matt and colleagues walk along a landscaped sidewalk in the business park. Modern office buildings line both sides. Trees provide shade. Other professionals walk in groups or alone. The group heads toward a cluster of restaurants visible in the distance — a small retail strip within the business park.

### Scene 195: Approaching Sandwich Shop
**Time:** 12:12 PM — bright outdoor light  
**Setting:** Business park retail strip  
**Description:** The group approaches a casual sandwich shop — a storefront with large windows and outdoor seating with tables and umbrellas. The shop sign reads something like "FRESH MARKET DELI." A few customers sit at outdoor tables. The menu is posted in the window. The door is open, inviting. Matt and colleagues head toward the entrance.

### Scene 196: Entering Sandwich Shop
**Time:** 12:13 PM — bright indoor lunch lighting  
**Setting:** Sandwich shop interior  
**Description:** Matt and colleagues enter the sandwich shop. The interior has a counter where sandwiches are made, a display case with salads and sides, a menu board above, and tables and chairs for seating. The lunch rush is active — a line at the counter, customers eating at tables. The smell of fresh bread and deli meat fills the air. They join the line.

### Scene 197: Waiting in Line
**Time:** 12:15 PM — sandwich shop light  
**Setting:** Sandwich shop counter  
**Description:** Matt stands in line at the counter with his colleagues, looking up at the menu board. Choices include various sandwiches, salads, soups, and sides with prices. The person ahead of him orders. Workers in aprons and gloves prepare food behind the counter. The line moves steadily. Matt decides what to order.

### Scene 198: Ordering at Counter
**Time:** 12:18 PM — sandwich shop light  
**Setting:** Sandwich shop counter  
**Description:** Matt reaches the front of the line and places his order with a worker behind the counter. He points at the menu and speaks. The worker nods, beginning to prepare his sandwich. Behind the counter, ingredients are visible in a display case — meats, cheeses, vegetables, condiments. A bread loaf is sliced. Matt watches his sandwich being made.

### Scene 199: Watching Sandwich Being Made
**Time:** 12:19 PM — sandwich shop light  
**Setting:** Sandwich shop counter  
**Description:** Close-up scene of the sandwich being assembled. Hands in plastic gloves place turkey slices on fresh bread, add lettuce, tomato, and cheese, apply mayo with a knife. The sandwich is being built layer by layer on the counter workspace. Ingredients are colorful and fresh. Matt watches from across the counter.

### Scene 200: Paying at Register
**Time:** 12:21 PM — sandwich shop light  
**Setting:** Sandwich shop register  
**Description:** Matt stands at the cash register, pulling his wallet from his back pocket. He hands over a credit card or taps his phone for contactless payment. The cashier completes the transaction. A paper receipt is offered. The wrapped sandwich and a bag of chips sit on the counter. His colleagues are nearby, also completing their purchases.

### Scene 201: Picking Up Food Tray
**Time:** 12:22 PM — sandwich shop light  
**Setting:** Sandwich shop counter  
**Description:** Matt picks up his tray with the wrapped sandwich, a bag of chips, and a fountain drink cup. He balances the tray with both hands. His colleagues have similar trays. They look around for an open table. The restaurant is moderately crowded. They spot a table near the window.

### Scene 202: Sitting at Table
**Time:** 12:23 PM — lunch lighting  
**Setting:** Sandwich shop seating area  
**Description:** Matt and his two colleagues sit down at a small square table near the window. They set down their trays. The table has napkin holder and condiment bottles. Through the window, the sunny business park is visible. They settle into chairs, unwrapping sandwiches, beginning casual conversation.

### Scene 203: Unwrapping Sandwich
**Time:** 12:24 PM — lunch lighting  
**Setting:** Table, close-up  
**Description:** Close-up of Matt's hands unwrapping his sandwich from the paper wrapping. The sandwich is revealed — fresh bread with layers of turkey, cheese, lettuce, tomato visible. The paper crinkles as it's pulled away. His fountain drink and chips are beside him. The table surface is visible.

### Scene 204: Taking First Bite
**Time:** 12:24 PM — lunch lighting  
**Setting:** Sandwich shop table  
**Description:** Matt brings the sandwich to his mouth and takes a bite. His mouth opens wide to accommodate the thick sandwich. His colleagues are similarly eating across the table. The sandwich compresses slightly as he bites. His expression is satisfied — good food. Crumbs fall slightly.

### Scene 205: Lunch Conversation
**Time:** 12:30 PM — lunch lighting  
**Setting:** Sandwich shop table  
**Description:** Matt and his colleagues are mid-lunch, chatting and laughing around the table. Sandwiches are half-eaten. One colleague gestures while telling a story. Matt listens, smiling. Chip bags are open. Drinks are sipped. The conversation is casual — weekend plans, sports, office gossip. Natural light fills the shop.

### Scene 206: Checking Phone During Lunch
**Time:** 12:40 PM — lunch lighting  
**Setting:** Sandwich shop table  
**Description:** Matt glances at his phone while at the table, checking a message or notification. His sandwich is nearly finished. His colleagues chat across from him. The phone screen shows a text message or app notification. He looks briefly, then puts it down to rejoin the conversation. The phone lies face-up on the table.

### Scene 207: Finishing Lunch
**Time:** 12:50 PM — lunch lighting  
**Setting:** Sandwich shop table  
**Description:** Matt finishes his sandwich, crumpling up the paper wrapping. His chip bag is empty. He takes a final sip of his drink through a straw. His colleagues are similarly wrapping up. Napkins are used. The table has remnants of the meal. They prepare to leave.

### Scene 208: Throwing Away Trash
**Time:** 12:52 PM — lunch lighting  
**Setting:** Sandwich shop trash area  
**Description:** Matt carries his tray to the trash and recycling area. He dumps wrappers, napkins, and the empty chip bag into the trash bin, places the drink cup in the recycling slot, and stacks the tray on top of the trash bin. His colleagues do the same beside him. The bins are marked "Trash" and "Recycling."

### Scene 209: Walking Back to Office
**Time:** 12:55 PM — bright outdoor midday light  
**Setting:** Business park sidewalk  
**Description:** Matt and his colleagues walk back along the sunny sidewalk toward the office building. They chat casually as they walk. The sun is high, shadows short. Other workers are also returning from lunch breaks. The office building looms ahead. Trees line the path.

### Scene 210: Re-Entering Office Building
**Time:** 12:58 PM — lobby light  
**Setting:** Office building lobby  
**Description:** Matt pushes through the glass doors, re-entering the office building lobby. The cool air-conditioning contrasts with the outdoor warmth. Colleagues behind him also enter. The lobby is quieter now — most people already back at work or still at lunch. He heads toward the elevators for the afternoon session.

---

## PART 9: THE OFFICE — AFTERNOON (1:00 PM - 5:30 PM)

### Scene 211: Back at Desk After Lunch
**Time:** 1:00 PM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt settles back into his chair at his cubicle, refreshed from lunch. He moves the mouse to wake his computer. The screens illuminate with his open programs. The office has a post-lunch calm. Colleagues are back at desks, the pace resuming. His notepad from the morning meeting sits nearby with his afternoon tasks.

### Scene 212: Afternoon Email Check
**Time:** 1:05 PM — screen glow  
**Setting:** Matt's cubicle, monitor view  
**Description:** Matt's Outlook inbox is displayed on the monitor, with new emails received during lunch. He scrolls through the list — new messages from colleagues, a calendar invite, a newsletter. He clicks on an important-looking email to read it. His hand is on the mouse. The afternoon work begins.

### Scene 213: Working on a Presentation
**Time:** 1:30 PM — screen glow  
**Setting:** Matt's cubicle, monitor view  
**Description:** Matt works on a PowerPoint presentation, the application open on his monitor. The slide displayed shows a marketing chart with bullet points. He edits text, moving between slides in the thumbnail view on the left. The toolbar shows design and animation options. His face is focused on the work.

### Scene 214: Adding Images to Presentation
**Time:** 1:45 PM — screen glow  
**Setting:** Matt's cubicle, close-up on monitor  
**Description:** Close-up of the monitor showing a PowerPoint slide with an image being inserted. Matt drags a product image into place on the slide. The image shows a marketing graphic — a product photo or infographic. He resizes it with corner handles. The slide layout improves as he adjusts elements.

### Scene 215: Desk Interaction with Colleague
**Time:** 2:00 PM — office light  
**Setting:** Matt's cubicle  
**Description:** A colleague approaches Matt's cubicle, leaning on the partition. They have a work-related conversation — the colleague asks a question about a project, Matt explains something while pointing at his screen. Both look at the monitor. The interaction is collaborative. Papers and sticky notes are visible on the cubicle wall.

### Scene 216: Afternoon Snack from Desk Drawer
**Time:** 2:30 PM — office light  
**Setting:** Matt's cubicle, close-up  
**Description:** Matt opens his desk drawer and pulls out a small snack — a granola bar in its wrapper. The drawer contains other items: pens, sticky notes, charger cables, maybe other snacks. He unwraps the granola bar while looking at his screen, a quick energy boost for the afternoon. The wrapper crinkles quietly.

### Scene 217: Eating Snack at Desk
**Time:** 2:31 PM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt takes a bite of the granola bar while continuing to look at his computer screen. He holds the bar in one hand, mouse in the other. Multitasking during a busy afternoon. Crumbs fall slightly onto the desk. He brushes them away absently. The office continues around him.

### Scene 218: Video Call Setup
**Time:** 3:00 PM — screen glow  
**Setting:** Matt's cubicle  
**Description:** Matt sets up for a video call. On his monitor, a Zoom or Teams window is open, showing the meeting about to start. He adjusts his webcam at the top of the monitor, checks his appearance briefly in the preview window. His background shows the office cubicle. He puts in earbuds, the cord trailing down.

### Scene 219: On Video Call
**Time:** 3:05 PM — screen glow  
**Setting:** Matt's cubicle, view of monitor  
**Description:** Matt is on a video call, his face visible in a small self-view window in the corner of the screen. The main window shows multiple video feeds — remote colleagues in their home offices or other locations. Matt speaks, looking at the camera. The earbuds are in his ears. The video gallery shows 4-6 participants.

### Scene 220: Speaking During Video Call
**Time:** 3:15 PM — screen glow  
**Setting:** Matt's cubicle  
**Description:** Matt speaks animatedly during the video call, gesturing slightly. His eyes look at the camera, simulating eye contact with remote participants. The screen shows the other participants listening. His self-view shows his professional appearance — blue shirt, office background. He makes a point with hand movement.

### Scene 221: Taking Notes During Video Call
**Time:** 3:25 PM — screen glow  
**Setting:** Matt's cubicle  
**Description:** Matt writes notes on his notepad while participating in the video call. He glances between the screen and his notes. His pen moves quickly, jotting down action items. The video call continues on screen — another participant is speaking. The earbuds stay in his ears. Multitasking on the call.

### Scene 222: Video Call Ending
**Time:** 3:45 PM — screen glow  
**Setting:** Matt's cubicle  
**Description:** The video call ends. Participants wave goodbye on screen. Matt clicks to leave the meeting, the window closing. He removes his earbuds, stretching slightly after sitting focused for the call. The main desktop reappears on his monitor. He takes a breath, transitioning back to independent work.

### Scene 223: Stretch at Desk
**Time:** 3:50 PM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt stretches in his chair — arms raised above his head, back arching slightly, releasing tension. His eyes close briefly. The chair creaks. The afternoon has been long. He rolls his shoulders and neck. The office continues bustling around him. The stretch feels good after hours of sitting.

### Scene 224: Walking to Get Afternoon Coffee
**Time:** 4:00 PM — office light  
**Setting:** Office floor to break area  
**Description:** Matt walks through the office toward the break area for afternoon coffee. He carries his mug — the company mug from his desk. Other employees are at their desks, the afternoon pushing toward end of day. The break area with the coffee maker is visible ahead. An afternoon energy boost is needed.

### Scene 225: Pouring Coffee from Office Coffee Maker
**Time:** 4:02 PM — break area light  
**Setting:** Office break area  
**Description:** Matt pours coffee from the office coffee maker into his company mug. The coffee maker is a standard office model — carafe half-full with dark coffee. Steam rises from the pour. The break area has a counter with sugar, creamer, stirrers. A small refrigerator, microwave, and sink are nearby. He adds a splash of creamer.

### Scene 226: Afternoon Work Push
**Time:** 4:15 PM — screen glow  
**Setting:** Matt's cubicle  
**Description:** Matt is deep in focused work at his computer. His coffee mug sits nearby, steam rising. He types rapidly on the keyboard, eyes on the screen showing a document or email. The office has the quiet intensity of afternoon productivity. He's trying to finish tasks before end of day. Papers are shuffled beside him.

### Scene 227: Printing a Document
**Time:** 4:30 PM — office light  
**Setting:** Matt's cubicle and office printer  
**Description:** Matt clicks to print a document, then gets up and walks to the office printer — a large multifunction machine in a corner of the office floor. The printer hums, pages emerging from the output tray. He waits briefly, then picks up the printed pages — a report or presentation. He taps them on the printer to align the stack.

### Scene 228: Reviewing Printed Document
**Time:** 4:32 PM — office light  
**Setting:** Matt's cubicle  
**Description:** Back at his desk, Matt reviews the printed document, flipping through pages. He holds a pen, occasionally marking corrections or notes in the margins. His screen shows the digital version. Comparing print to screen, making final edits. His expression is analytical, detail-oriented.

### Scene 229: Calendar Reminder Pop-up
**Time:** 5:00 PM — screen glow  
**Setting:** Matt's cubicle, close-up on monitor  
**Description:** Close-up of Matt's monitor showing a calendar reminder pop-up. The notification shows "End of Day — Submit Report" or similar. He clicks to dismiss it. The clock in the corner shows 5:00 PM. End of day is approaching. He begins wrapping up his work, saving files.

### Scene 230: Saving and Closing Programs
**Time:** 5:15 PM — screen glow  
**Setting:** Matt's cubicle, monitor view  
**Description:** Matt saves his work, clicking through save dialogs. He closes applications — Excel closes, PowerPoint closes, Outlook minimized. The desktop becomes visible as programs exit. He shuts down or locks the computer. The screens go dark. The workday is ending.

### Scene 231: Organizing Desk Before Leaving
**Time:** 5:20 PM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt tidies his desk — straightening papers, putting pens in a holder, pushing in his chair. The notepad is aligned with the keyboard. Personal items remain — the small plant, photo. His mug is empty, set aside. The workspace is neat for tomorrow. Ready to leave.

### Scene 232: Putting Laptop in Bag (If Taking Home)
**Time:** 5:22 PM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt unplugs his laptop from the monitors and power, sliding it into his black messenger bag. The laptop fits into a padded sleeve inside the bag. Cables are also packed. He zips or buckles the bag closed. Taking work home or just bringing the laptop for security. The bag is ready.

### Scene 233: Picking Up Bag to Leave
**Time:** 5:25 PM — office light  
**Setting:** Matt's cubicle  
**Description:** Matt picks up his messenger bag, slinging it over his shoulder. He takes one last look at his desk — everything in order. He pushes his chair in. The bag settles at his hip. He's ready to leave for the day. The office is emptying as others also pack up.

### Scene 234: Saying Goodbye to Colleagues
**Time:** 5:27 PM — office light  
**Setting:** Office floor  
**Description:** Matt walks through the office, waving or nodding goodbye to colleagues still at their desks. "Have a good night" exchanges happen. Some colleagues are also packing up, others staying late. The office has end-of-day energy — people logging off, conversations about evening plans. Matt heads toward the exit.

### Scene 235: Leaving the Office Floor
**Time:** 5:28 PM — office light  
**Setting:** Office entrance  
**Description:** Matt pushes through the frosted glass door of the office suite, leaving the work floor behind. The "VERTEX MARKETING" logo is on the door. He steps into the elevator lobby area on the third floor. Others wait for the elevator or head for stairs. The workday is complete.

### Scene 236: Elevator Ride Down
**Time:** 5:29 PM — elevator light  
**Setting:** Inside elevator  
**Description:** Matt rides the elevator down, standing with a few other end-of-day employees. Everyone looks tired but relieved. Someone checks their phone. The floor numbers decrease on the display. Soft elevator music plays. The doors open at the lobby. Workers exit toward the main doors.

### Scene 237: Walking Through Lobby (Evening)
**Time:** 5:30 PM — lobby light transitioning to outdoor light  
**Setting:** Office building lobby  
**Description:** Matt walks through the building lobby toward the exit. The lobby is busier now with end-of-day departures. He pushes through the glass doors, stepping outside into the late afternoon sun. The workday is officially over. The parking lot and his car await.

---

## PART 10: AFTER WORK — COMMUTE & ERRANDS (5:30 PM - 6:30 PM)

### Scene 238: Walking to Car (Evening)
**Time:** 5:32 PM — late afternoon outdoor light  
**Setting:** Office parking lot  
**Description:** Matt walks across the parking lot to his silver Honda Civic. The sun is lower in the sky, casting long shadows. His bag swings at his side. Other employees walk to their cars. The air is warm. Trees cast shadows across the asphalt. He approaches his car, keys in hand.

### Scene 239: Getting into Car to Go Home
**Time:** 5:33 PM — inside car  
**Setting:** Car interior  
**Description:** Matt gets into his car, tossing his messenger bag onto the passenger seat. He closes the door and starts the car. The air conditioning kicks on. He connects his phone to the car audio via Bluetooth. Music or a podcast starts playing through the speakers. He puts on his seatbelt and prepares to drive.

### Scene 240: Driving Out of Work Parking Lot
**Time:** 5:35 PM — inside car, view through windshield  
**Setting:** Inside car, parking lot  
**Description:** View through the windshield as Matt drives out of the office parking lot. Other cars are also leaving. He waits to turn onto the main road. The business park buildings are behind him. The late afternoon sun creates golden light. He checks mirrors, signals, and turns.

### Scene 241: Driving on Highway (Evening)
**Time:** 5:45 PM — inside car  
**Setting:** Inside car, highway  
**Description:** Matt drives on the highway heading home. Traffic is heavier now — rush hour. Through the windshield, many cars fill the lanes, taillights visible in the flow. He's in the middle lane, moving at moderate speed. Music plays from the speakers. The sun is lower, creating glare. His sunglasses are on.

### Scene 242: Taking Exit Toward Home
**Time:** 5:55 PM — inside car  
**Setting:** Inside car, highway exit  
**Description:** Matt takes the highway exit toward his suburban neighborhood. The exit ramp curves down. Suburban commercial areas come into view. The traffic is still busy but moving. He follows signs toward his area. The end-of-day commute continues.

### Scene 243: Pulling into Grocery Store Parking Lot
**Time:** 6:00 PM — inside car, parking lot  
**Setting:** Grocery store parking lot  
**Description:** Matt turns into a grocery store parking lot — a typical suburban supermarket with a large sign, shopping carts in corrals, and a busy parking lot. He finds a spot and parks. The store entrance with automatic doors is visible. Other shoppers push carts to their cars. He'll make a quick stop for groceries.

### Scene 244: Getting Out at Grocery Store
**Time:** 6:02 PM — bright outdoor light  
**Setting:** Grocery store parking lot  
**Description:** Matt gets out of his car at the grocery store, leaving his messenger bag inside. He walks toward the store entrance, passing shopping carts and other customers. The store facade is visible — large windows, promotional signs for sales. The automatic doors ahead. He grabs a hand basket or small cart just inside.

### Scene 245: Entering Grocery Store
**Time:** 6:03 PM — bright grocery store lighting  
**Setting:** Grocery store entrance  
**Description:** Matt walks through the automatic doors into the grocery store. The interior opens up — produce section immediately visible with colorful fruits and vegetables, aisles stretching back, overhead signs indicating departments. Soft store music plays. The temperature is cool. He grabs a red plastic shopping basket.

### Scene 246: Walking Through Produce Section
**Time:** 6:05 PM — bright store lighting  
**Setting:** Grocery store produce section  
**Description:** Matt walks through the produce section, looking at fruits and vegetables. Tables and bins hold apples, oranges, bananas, lettuce, tomatoes. He picks up a bag of salad greens, examining it. Misting sprays keep vegetables fresh. Other shoppers select produce nearby. Price signs are visible. The area smells fresh.

### Scene 247: Selecting Produce
**Time:** 6:06 PM — bright store lighting  
**Setting:** Produce section, close-up  
**Description:** Close-up of Matt's hand selecting a ripe tomato from a pile, gently squeezing to test firmness. The tomatoes are red and round. He places it in a plastic produce bag with others. His basket already has salad greens. The produce display is colorful — green peppers, yellow squash nearby.

### Scene 248: Walking Down Grocery Aisle
**Time:** 6:08 PM — bright store lighting  
**Setting:** Grocery store aisle  
**Description:** Matt walks down a grocery aisle — shelves lined with products on both sides. This could be the pasta aisle, cereal aisle, or canned goods. Colorful packages and boxes line the shelves. He scans the products, looking for something specific. His basket hangs from his arm. Other shoppers are in the aisle.

### Scene 249: Picking Item off Shelf
**Time:** 6:09 PM — bright store lighting  
**Setting:** Grocery aisle, close-up  
**Description:** Close-up of Matt reaching for a box of pasta on the shelf. His hand pulls a blue box of spaghetti from among various pasta options. Price tags are visible on the shelf edge. His basket contains his other selections — produce, maybe a jar of sauce. He places the pasta in the basket.

### Scene 250: At the Meat Counter
**Time:** 6:12 PM — bright store lighting  
**Setting:** Grocery store meat department  
**Description:** Matt stands at the meat counter, looking at packaged meats in the refrigerated case. Chicken breasts, ground beef, steaks are arranged with price labels. He selects a package of chicken breasts, checking the date and appearance. A butcher in white works behind the counter. He places the chicken in his basket.

### Scene 251: Checking Out at Register
**Time:** 6:18 PM — bright store lighting  
**Setting:** Grocery store checkout  
**Description:** Matt stands at a checkout lane, placing items from his basket onto the conveyor belt — produce, pasta, sauce, chicken, a few other items. The cashier scans each item. The register displays the running total. A bagging area is at the end. He pulls out his wallet to pay. The line moves efficiently.

### Scene 252: Paying at Checkout
**Time:** 6:20 PM — bright store lighting  
**Setting:** Grocery checkout, close-up  
**Description:** Close-up of Matt's hand tapping a credit card on the payment terminal. The screen shows "Approved" or a checkmark. The cashier bags his groceries in a paper bag. Receipt paper prints. The transaction completes. He takes his bagged groceries, ready to leave.

### Scene 253: Carrying Groceries to Car
**Time:** 6:22 PM — warm evening light  
**Setting:** Grocery store parking lot  
**Description:** Matt walks through the grocery store parking lot carrying a paper grocery bag in one arm. The bag shows the tops of items — celery sticking out, the box of pasta visible. The evening sun is warm and golden. He approaches his silver Civic. Other shoppers load cars nearby.

### Scene 254: Putting Groceries in Car
**Time:** 6:23 PM — warm evening light  
**Setting:** At his car  
**Description:** Matt opens the back door of his Civic and places the grocery bag on the back seat. He ensures it won't tip over. The bag sits securely. His messenger bag is visible on the front passenger seat. He closes the back door. Time to head home.

### Scene 255: Driving Home — Suburban Streets
**Time:** 6:28 PM — inside car, golden hour light  
**Setting:** Inside car, suburban streets  
**Description:** View through the windshield as Matt drives the final stretch home on suburban residential streets. The evening light is golden, casting long shadows. Familiar streets pass — houses with lawns, parked cars, kids playing. He turns onto his street. The apartment complex comes into view ahead.

---

## PART 11: EVENING AT HOME (6:30 PM - 11:00 PM)

### Scene 256: Pulling into Apartment Parking
**Time:** 6:32 PM — warm evening light  
**Setting:** Inside car, apartment parking lot  
**Description:** Matt pulls into the apartment complex parking lot, finding a spot near his building. Through the windshield, the familiar apartment building is visible. He parks, turns off the car. The day is winding down. He gathers his belongings — messenger bag from passenger seat, grocery bag from back seat.

### Scene 257: Walking to Apartment with Groceries
**Time:** 6:34 PM — warm evening outdoor light  
**Setting:** Apartment complex exterior  
**Description:** Matt walks from his car toward the apartment building entrance, carrying his messenger bag over one shoulder and the paper grocery bag in his arms. The evening is pleasant. A few neighbors are visible — someone walking a dog, others coming home. The building entrance is ahead. Keys are in his hand.

### Scene 258: Entering Apartment Building
**Time:** 6:35 PM — lobby light  
**Setting:** Apartment building lobby  
**Description:** Matt pushes through the glass front door into the apartment building lobby. He carries his bags, heading toward the elevator. The lobby is quiet — a few pieces of mail on the floor by the mailboxes. He presses the elevator button, balancing bags.

### Scene 259: Unlocking Apartment Door
**Time:** 6:37 PM — hallway light  
**Setting:** Outside apartment 207  
**Description:** Matt stands at his apartment door, balancing the grocery bag while unlocking the deadbolt. The key turns. He pushes the door open. The interior of his apartment is visible — the familiar living room and kitchen. He steps inside, relieved to be home.

### Scene 260: Entering Apartment with Groceries
**Time:** 6:38 PM — warm interior light  
**Setting:** Apartment entryway  
**Description:** Matt enters his apartment, nudging the door closed behind him with his foot. He carries bags inside. The apartment is as he left it — neat, lived-in. Evening light streams through the windows. He sets down his messenger bag on the armchair near the door, heads to the kitchen with groceries.

### Scene 261: Setting Groceries on Kitchen Counter
**Time:** 6:39 PM — kitchen light  
**Setting:** Kitchen  
**Description:** Matt sets the paper grocery bag on the kitchen counter. He begins unpacking — produce, pasta, sauce, chicken. Each item comes out and goes either on the counter or into the refrigerator. The kitchen is familiar — white cabinets, gray counters. The evening cooking ritual begins.

### Scene 262: Changing Clothes — Entering Bedroom
**Time:** 6:42 PM — bedroom light  
**Setting:** Bedroom  
**Description:** Matt enters the bedroom, ready to change out of his work clothes. The bed is neatly made from the morning. Evening light is softer now, coming through the blinds. He loosens his collar, begins unbuttoning his shirt. Time to get comfortable.

### Scene 263: Taking Off Dress Shirt
**Time:** 6:43 PM — bedroom light  
**Setting:** Bedroom  
**Description:** Matt pulls off his light blue dress shirt, tossing it into the laundry basket in the corner. He's in his white undershirt and khakis. The shirt lands in the basket with other clothes. He unbuckles his belt, kicks off his dress shoes near the closet.

### Scene 264: Putting on Comfortable Clothes
**Time:** 6:45 PM — bedroom light  
**Setting:** Bedroom  
**Description:** Matt pulls on a casual gray t-shirt and navy sweatpants from his dresser. He's barefoot or puts on comfortable socks. The transformation from work mode to home mode is complete. Comfortable and relaxed. He heads back to the kitchen to make dinner.

### Scene 265: Starting Dinner — Washing Hands
**Time:** 6:48 PM — kitchen light  
**Setting:** Kitchen sink  
**Description:** Matt washes his hands at the kitchen sink, preparing to cook. Water runs, soap bubbles. He rinses and dries with a dish towel. The groceries are out on the counter — chicken, vegetables, pasta. The stove and pots await. Dinner preparation begins.

### Scene 266: Preparing Vegetables
**Time:** 6:50 PM — kitchen light  
**Setting:** Kitchen counter  
**Description:** Matt stands at the kitchen counter with a cutting board and knife, slicing tomatoes. The knife moves through the ripe red tomato, creating neat slices. Lettuce and other salad vegetables are nearby. A salad bowl waits. He's making a simple dinner — chicken and salad.

### Scene 267: Unwrapping Chicken
**Time:** 6:55 PM — kitchen light  
**Setting:** Kitchen counter  
**Description:** Close-up of Matt unwrapping the package of chicken breasts. The plastic is pulled away, revealing the pink raw chicken. He places the chicken on a clean plate. Seasonings — salt, pepper, garlic powder — are nearby. A pan waits on the stove.

### Scene 268: Seasoning Chicken
**Time:** 6:56 PM — kitchen light  
**Setting:** Kitchen counter, close-up  
**Description:** Matt sprinkles seasoning onto the raw chicken breasts. Salt falls from his fingers, pepper is shaken from a grinder. The seasonings coat the meat. He pats them in slightly. The preparation for cooking is complete.

### Scene 269: Heating Pan on Stove
**Time:** 6:58 PM — kitchen light  
**Setting:** Kitchen stove  
**Description:** Matt turns on the stove burner, a blue gas flame or red electric element igniting. A pan sits on the burner. He adds a splash of olive oil from a bottle, tilting the pan to spread it. The oil begins to shimmer with heat. He waits for it to be hot enough for the chicken.

### Scene 270: Placing Chicken in Pan
**Time:** 7:00 PM — kitchen light  
**Setting:** Kitchen stove  
**Description:** Matt carefully places the seasoned chicken breasts into the hot pan. A sizzle erupts as the meat hits the oil. Steam and a small amount of smoke rise. He uses tongs or a spatula to position the chicken. The cooking begins. The kitchen fills with the sound and smell of searing meat.

### Scene 271: Chicken Cooking in Pan
**Time:** 7:05 PM — kitchen light  
**Setting:** Kitchen stove, close-up  
**Description:** Close-up of the chicken breasts cooking in the pan. The meat is browning on the bottom, sizzling sounds audible. Oil bubbles around the edges. The heat creates a golden crust. Steam rises. Matt watches the progress. A spatula rests nearby.

### Scene 272: Flipping Chicken
**Time:** 7:08 PM — kitchen light  
**Setting:** Kitchen stove  
**Description:** Matt uses tongs to flip the chicken breasts in the pan. The cooked side is golden brown. He carefully turns each piece. Sizzle continues as the uncooked side hits the hot pan. Oil splatters slightly. The cooking continues toward completion.

### Scene 273: Setting Table for One
**Time:** 7:12 PM — warm living/dining light  
**Setting:** Kitchen/living area  
**Description:** Matt sets a plate, fork, knife, and napkin at the small dining table near the kitchen or on the breakfast bar. A glass of water is poured. The table is simple — one place setting for himself. The apartment is quiet, peaceful. He prepares to enjoy his dinner.

### Scene 274: Plating Dinner
**Time:** 7:15 PM — kitchen light  
**Setting:** Kitchen counter  
**Description:** Matt plates his dinner — the cooked chicken breast is placed on a white plate, sliced to show it's cooked through. The fresh salad is added beside it, colorful with tomatoes and greens. Maybe some pasta on the side. The plate looks appetizing. Home cooking complete.

### Scene 275: Carrying Plate to Table
**Time:** 7:16 PM — warm interior light  
**Setting:** Kitchen to dining area  
**Description:** Matt carries his plate of food from the kitchen counter to the small dining table. The plate steams slightly. His glass of water is already on the table. The evening is calm. He's ready to eat and relax after the workday.

### Scene 276: Sitting Down to Eat
**Time:** 7:17 PM — warm interior light  
**Setting:** Dining area  
**Description:** Matt sits down at the table, pulling in his chair. His plate of chicken and salad is before him. Fork and knife in hand. He takes a moment before eating, perhaps looking at his phone briefly. The apartment is quiet — just him, his dinner, and the evening ahead.

### Scene 277: Eating Dinner
**Time:** 7:20 PM — warm interior light  
**Setting:** Dining area  
**Description:** Matt cuts into his chicken breast, bringing a piece to his mouth. He chews, enjoying the home-cooked meal. The salad is eaten with forks full of greens. He takes sips of water between bites. Alone but content. The meal is satisfying after a long day.

### Scene 278: Checking Phone While Eating
**Time:** 7:25 PM — warm interior light, phone glow  
**Setting:** Dining area  
**Description:** Matt scrolls through his phone while eating dinner — reading news, checking social media, or responding to a text. His fork holds a bite of salad. The phone screen shows an app interface. Multitasking during a solo dinner. The plate is half-finished.

### Scene 279: Finishing Dinner
**Time:** 7:35 PM — warm interior light  
**Setting:** Dining area  
**Description:** Matt's plate is now mostly empty — just remnants of salad and smears of sauce. He sets down his fork, takes a final drink of water. Dinner is complete. He sits back, satisfied. The evening stretches ahead. Time to clean up and relax.

### Scene 280: Carrying Dishes to Sink
**Time:** 7:37 PM — kitchen light  
**Setting:** Kitchen  
**Description:** Matt carries his empty plate and glass to the kitchen sink. He sets them in the basin with the dishes from breakfast. The sink now has plates, mugs, and cooking implements. He decides whether to wash them now or later. A quick rinse for now.

### Scene 281: Washing Dishes
**Time:** 7:40 PM — kitchen light  
**Setting:** Kitchen sink  
**Description:** Matt stands at the sink washing dishes — warm water running, dish soap bubbles, a sponge in hand. He scrubs the plate, rinses it, places it in the drying rack. The pan from cooking is soaked in the sink. Methodical cleanup. The window above the sink shows the darkening evening outside.

### Scene 282: Putting Dishes in Drying Rack
**Time:** 7:45 PM — kitchen light  
**Setting:** Kitchen sink area  
**Description:** Close-up of Matt placing clean dishes in a drying rack beside the sink. Plates stand upright, glasses inverted. Water drips into the sink. The drying rack is chrome with a drip tray. The dishes are clean, kitchen restored to order.

### Scene 283: Walking to Living Room
**Time:** 7:50 PM — warm living room light  
**Setting:** Living room  
**Description:** Matt walks from the kitchen into the living room, ready to relax. The gray fabric sofa beckons. The TV is off but waiting. The coffee table has the remote. Evening light fades outside the sliding glass doors, room lights are now on — a floor lamp, overhead light. He's in comfortable clothes, ready to unwind.

### Scene 284: Sitting on Couch
**Time:** 7:51 PM — warm living room light  
**Setting:** Living room  
**Description:** Matt settles onto the gray sofa, sinking into the cushions. He grabs a throw pillow, adjusts his position. His feet go up on the coffee table. The remote is within reach. The TV is ahead. A comfortable, familiar evening ritual. He exhales, relaxing.

### Scene 285: Turning on TV
**Time:** 7:52 PM — TV glow in living room  
**Setting:** Living room  
**Description:** Matt points the remote at the TV and presses the power button. The TV comes to life — a large flat screen on a stand. The screen shows a streaming service menu with rows of shows and movies. The room is now lit by TV glow and lamps. He browses for something to watch.

### Scene 286: Browsing Netflix/Streaming Service
**Time:** 7:53 PM — TV glow  
**Setting:** Living room, TV view  
**Description:** The TV screen shows a streaming service interface — Netflix, Hulu, or similar. Rows of thumbnail images for shows and movies scroll as Matt navigates with the remote. "Continue Watching" row shows partially finished series. His hand holds the remote, thumb on the navigation buttons. He decides what to watch.

### Scene 287: Watching TV
**Time:** 8:00 PM — TV glow  
**Setting:** Living room  
**Description:** Matt watches TV, a show or movie playing on screen. His face is illuminated by the TV light. He's reclined on the couch, pillow behind his head. The scene shows him engaged with the content — maybe smiling at something funny or focused on drama. The coffee table has the remote, maybe a glass of water.

### Scene 288: Getting a Snack from Kitchen
**Time:** 8:30 PM — kitchen light  
**Setting:** Kitchen  
**Description:** Matt walks back to the kitchen during a break in watching TV. He opens a cabinet, grabbing a bag of chips or a chocolate bar. The snack is simple — evening munchies. He also might grab a can of soda or beer from the refrigerator. Carrying snacks back to the couch.

### Scene 289: Snacking While Watching TV
**Time:** 8:35 PM — TV glow  
**Setting:** Living room  
**Description:** Matt is back on the couch with his snacks. He eats chips from a bowl on his lap while watching TV. The show continues playing. His feet are up, totally relaxed. Crumbs may fall. A drink is on the coffee table within reach. Evening relaxation in full mode.

### Scene 290: Playing Video Games — Setting Up
**Time:** 9:00 PM — TV glow  
**Setting:** Living room  
**Description:** Matt switches from streaming to gaming. He picks up a video game controller from beside the TV — a PlayStation or Xbox controller. He navigates to the gaming input. The screen shows a game startup or selection menu. He settles back, controller in hand, ready to play.

### Scene 291: Playing Video Games
**Time:** 9:15 PM — dynamic TV glow  
**Setting:** Living room  
**Description:** Matt plays a video game, focused on the screen. The game graphics are visible — could be action, sports, adventure. His thumbs work the controller, pressing buttons and moving joysticks. His face shows concentration, reactions to gameplay — excitement at a good play, frustration at failure. Immersed in the game.

### Scene 292: Intense Gaming Moment
**Time:** 9:30 PM — dynamic TV glow  
**Setting:** Living room, close-up  
**Description:** Close-up of Matt's hands on the controller during an intense gaming moment. His thumbs press rapidly. The TV screen reflects in his eyes. His expression is focused, in the zone. The game sounds are audible. A competitive or challenging moment in the game.

### Scene 293: Taking a Break from Gaming
**Time:** 10:00 PM — TV glow and lamp light  
**Setting:** Living room  
**Description:** Matt sets down the controller, taking a break from gaming. He stretches on the couch, rubs his eyes. The game is paused on screen. He looks at the time on his phone — 10:00 PM. The evening is winding down. He decides to start getting ready for bed.

### Scene 294: Checking Phone Before Bed
**Time:** 10:05 PM — phone glow in dim light  
**Setting:** Living room/hallway  
**Description:** Matt sits on the couch scrolling through his phone one more time before bed. Social media feeds, texts, emails. The phone screen illuminates his face in the dim room. The TV is now off. He yawns, tired from the day. Last check before sleep.

### Scene 295: Turning Off Living Room Lights
**Time:** 10:10 PM — dimming light  
**Setting:** Living room  
**Description:** Matt stands and walks around the living room turning off lights. The floor lamp clicks off. He switches off the main light. The room goes dark except for ambient light from outside through the blinds. He walks toward the bedroom hallway. The day is almost over.

### Scene 296: Entering Bathroom to Prepare for Bed
**Time:** 10:12 PM — bathroom light  
**Setting:** Bathroom  
**Description:** Matt enters the bathroom for his nighttime routine. He flicks on the light. The mirror, sink, and toiletries are familiar. He's in his casual clothes — t-shirt and sweatpants. Time to brush teeth and prepare for sleep.

### Scene 297: Brushing Teeth at Night
**Time:** 10:13 PM — bathroom light  
**Setting:** Bathroom  
**Description:** Matt brushes his teeth at the sink, toothbrush moving in his mouth. He looks tired in the mirror — end of day fatigue. The routine is quick but thorough. Toothpaste foam at his lips. His reflection shows a man ready for sleep.

### Scene 298: Washing Face at Night
**Time:** 10:15 PM — bathroom light  
**Setting:** Bathroom  
**Description:** Matt splashes water on his face at the sink, a nighttime refresh. The water is cool. He pats his face dry with a towel. His eyes are a bit red from screen time. He looks at his reflection briefly — ready for bed.

### Scene 299: Using Bathroom (Tasteful)
**Time:** 10:17 PM — bathroom light  
**Setting:** Bathroom  
**Description:** Matt uses the toilet — shown from side or back angle, tasteful. He finishes, flushes. The toilet handle is pressed. The flush sounds. He moves to wash hands at the sink. Normal nighttime routine.

### Scene 300: Exiting Bathroom, Turning Off Light
**Time:** 10:20 PM — dimming to dark  
**Setting:** Bathroom doorway  
**Description:** Matt exits the bathroom, his hand reaching back to switch off the light. The bathroom goes dark. He walks through the dim hallway toward the bedroom. The apartment is now mostly dark and quiet. Sleep awaits.

### Scene 301: Entering Bedroom at Night
**Time:** 10:21 PM — dim bedroom  
**Setting:** Bedroom  
**Description:** Matt enters the dark bedroom, the only light coming from a nightstand lamp still on. The bed is made from the morning, inviting. His phone is in hand. He moves toward the bed, ready to end the day.

### Scene 302: Plugging in Phone to Charge
**Time:** 10:22 PM — dim bedroom, phone glow  
**Setting:** Bedroom, nightstand  
**Description:** Close-up of Matt plugging his phone into a charging cable on the nightstand. The phone screen shows charging indicator. He sets it down on the nightstand face-down or face-up. The charger is a white cable. The alarm is likely already set for tomorrow.

### Scene 303: Setting Alarm (If Not Already Set)
**Time:** 10:23 PM — phone glow  
**Setting:** Bedroom, nightstand  
**Description:** Matt picks up his phone to confirm his alarm is set. The alarm app shows 6:45 AM set for weekdays. He swipes to check, then sets the phone down. Tomorrow will start the cycle again.

### Scene 304: Pulling Back Bed Covers
**Time:** 10:24 PM — dim bedroom  
**Setting:** Bedroom, bed  
**Description:** Matt pulls back the navy comforter and white sheets on his bed, revealing the inviting sleep space. The pillow is fluffed. The bed is made but being unmade for sleep. He sits on the edge of the bed.

### Scene 305: Getting into Bed
**Time:** 10:25 PM — dim bedroom  
**Setting:** Bedroom  
**Description:** Matt slides into bed, under the covers. He adjusts the pillow, finding a comfortable position. The comforter is pulled up to his chest. He lies on his back, settling in. The nightstand lamp is still on. He's almost ready for sleep.

### Scene 306: Reaching to Turn Off Lamp
**Time:** 10:26 PM — dim bedroom  
**Setting:** Bedroom, nightstand  
**Description:** Matt reaches from the bed to turn off the nightstand lamp. His hand finds the switch. The room goes dark except for faint light through the window blinds — streetlights or moonlight creating soft stripes.

### Scene 307: Lying in Dark Room
**Time:** 10:27 PM — dark bedroom  
**Setting:** Bedroom  
**Description:** The bedroom is dark. Matt lies in bed, eyes closed or staring at the ceiling. The only light is ambient from outside through the blinds. His breathing slows. The room is quiet. The day is done.

### Scene 308: Final Scene — Sleeping
**Time:** 11:00 PM — dark bedroom with soft ambient light  
**Setting:** Bedroom, from foot of bed  
**Description:** Matt is asleep, lying peacefully under the navy comforter. His face is relaxed, eyes closed. The pillow cradles his head. Soft moonlight or streetlight creates gentle illumination through the blinds. The nightstand shows the phone charging, the water glass. The alarm clock shows 11:00. Another day complete. Rest until morning.

---

## APPENDIX: Scene Categories Quick Reference

### By Location:
- **Bedroom (Morning):** Scenes 001-009, 039-054
- **Bathroom:** Scenes 010-038, 296-300
- **Kitchen:** Scenes 055-088, 265-282
- **Living Room:** Scenes 089-094, 283-295
- **Apartment Hallway/Lobby:** Scenes 095-104, 257-259
- **Parking Lot (Apartment):** Scenes 105-107, 256
- **Car Interior:** Scenes 108-149, 239-242, 254-255
- **Coffee Shop Drive-Through:** Scenes 125-133
- **Office Building Lobby:** Scenes 151-157, 236-237
- **Office Floor/Cubicle:** Scenes 158-179, 211-234
- **Conference Room:** Scenes 184-190
- **Office Break Area:** Scenes 180-183, 224-225
- **Sandwich Shop (Lunch):** Scenes 196-208
- **Business Park Exterior:** Scenes 193-195, 209, 238
- **Grocery Store:** Scenes 243-253
- **Bedroom (Night):** Scenes 262-264, 301-308

### By Time Period:
- **Early Morning (6:45-7:00):** Scenes 001-009
- **Morning Routine (7:00-8:00):** Scenes 010-094
- **Commute to Work (8:00-8:45):** Scenes 095-150
- **Office Morning (8:45-12:00):** Scenes 151-190
- **Lunch (12:00-1:00):** Scenes 191-210
- **Office Afternoon (1:00-5:30):** Scenes 211-237
- **Commute Home + Errands (5:30-6:30):** Scenes 238-255
- **Evening at Home (6:30-11:00):** Scenes 256-308

---

## Usage Notes for Image Generation

Each scene description is designed to work as a detailed prompt for Stable Diffusion or similar AI image generation tools. For best results:

1. **Character Consistency:** Always include "a 25-year-old white man with short brown hair" or reference to Matt's established appearance.

2. **Lighting:** Pay attention to time-of-day lighting cues — pre-dawn blue, bright morning, midday, golden hour, artificial indoor lighting.

3. **Environment Details:** Include the described objects and setting details for realism.

4. **Clothing Consistency:** Track what Matt is wearing for each time period (pajamas, work clothes, casual evening clothes).

5. **Perspective:** All scenes are third-person POV — Matt is visible in the scene or his body parts are visible performing actions.

---

*Total Scenes: 308*
