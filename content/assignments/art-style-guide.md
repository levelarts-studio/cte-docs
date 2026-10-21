---
id: art-style-guide
title: "Art Style Guide"
entity: assignment
tier: 200
status: complete
requires: ["DESN-201", "DESN-116"]
standards: ["GD.17.4", "13.3", "10.3"]
evidence_for: "GD.17.4"
portfolio: true
portfolio_section: "GAD2 U2"
est_time: 90
setting: lab
aliases: ["/a/art-style-guide"]
---

## The task

Author the official **Art Style Guide (Studio Art Bible)** for your team's Vertical Slice project. You will define the 3 non-negotiable visual pillars, establish shape language rules, architect a 60-30-10 color palette, map a beat-by-beat environmental color script, specify PBR material and edge wear standards, and author visual "Do's and Don'ts" to eliminate stylistic drift across team artists.

In game production, the Art Bible is the visual constitution. Before a single blockout mesh or 3D prop is authored for the 5-minute slice, this document establishes the aesthetic law so assets built by multiple artists look like they belong to the exact same game world.

---

## Before you start

- [World Bible](/assignments/world-bible/) (`world-bible`)
- [Color Scripting and Mood](/m/DESN-201/) (`DESN-201`)
- [Brand Identity and Style Guides](/m/DESN-116/) (`DESN-116`)

{{< callout type="info" >}}
**Starter Template Download**:
Download the pre-formatted studio document [**`Art_Style_Guide_Template.docx`**](/resources/Art_Style_Guide_Template.docx) (or [mirror download](/downloads/Art_Style_Guide_Template.docx)) to your computer before beginning Step 1.
- **File Format:** Microsoft Word (`.docx`) — compatible with Microsoft Word, Google Docs, and LibreOffice.
- **Included Sections:** Visual Pillars, Shape Language Matrix, 60-30-10 Palette Table, Color Script Progression, PBR Standards, Technical Guardrails, and Visual Do's & Don'ts.
{{< /callout >}}

---

## Deliverable Overview

Your team's Art Style Guide will establish the visual boundaries for your entire game slice:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      STUDIO ART BIBLE DECK                             │
├────────────────────────────────┬───────────────────────────────────────┤
│ 1. Core Visual Pillars         │ 3 defining aesthetic principles       │
│ 2. Shape Language Rules        │ Friendly (■) vs Hostile (▲) vs Nat (●)│
│ 3. Palette & 60-30-10 Rules    │ Base (60%) / Trim (30%) / Accent (10%)│
│ 4. Narrative Color Script Arc  │ Beat 1 (Entry) to Beat 4 (Climax)     │
│ 5. Material & PBR Treatment    │ Roughness boundaries & edge wear logic│
│ 6. Technical Asset Metrics     │ Texel density & Unreal grid snapping  │
│ 7. Visual Do's & Don'ts        │ Explicit acceptable vs prohibited art │
└────────────────────────────────┴───────────────────────────────────────┘
```

---

## Steps

{{% steps %}}

### Step 1 — Download and set up your template

1. Download the [**`Art_Style_Guide_Template.docx`**](/resources/Art_Style_Guide_Template.docx) starter document.
2. Open the file in Microsoft Word or upload it to Google Drive as a collaborative Google Doc for your team.
3. Fill out the header metadata block:
   - Project Title
   - Team / Studio Name
   - Lead Artist(s) / Author(s)
   - Target Engine (*Unreal Engine 5*)
   - Version number (`v1.0`) and Date

### Step 2 — Formulate your 3 Visual Pillars

In Section 1 of the template:
1. Brainstorm and select **three actionable visual pillars** that define your game's aesthetic personality.
2. *Avoid weak, generic buzzwords* (e.g., "dark," "fun," "cool"). Choose evocative, concrete terms like:
   - *Industrial Utilitarian*
   - *Atmospheric Overgrowth*
   - *Brutalist Monolithic*
   - *Whimsical Chunky*
   - *Weathered Retro-Futurism*
3. For each pillar, write:
   - A clear **Definition** explaining what the pillar means to the team.
   - An **In-Game Art Application** explaining how 3D modelers and texture artists will reflect it in real assets.

### Step 3 — Define Shape Language rules

In Section 2 of the template:
1. Define how geometric primitives convey narrative alignment, faction identity, and gameplay function:
   - **Rectangles / Boxes (■):** What faction, structure, or defensive cover uses sturdy, grounded box forms?
   - **Triangles / Diagonals (▲):** What enemy elements, hazard zones, or lethal traps use sharp, aggressive angles?
   - **Circles / Cylinders (●):** What interactive resource nodes, conduits, or friendly NPC elements use soft, curved forms?
2. Provide at least two concrete 3D prop or environmental examples for each shape primitive.

### Step 4 — Architect the 60-30-10 color palette

In Section 3 (Part A) of the template:
1. Establish the color balance for your game's primary environment:
   - **60% Dominant Base:** The broad structural background (concrete, rock, terrain, metal panels). Keep this desaturated to prevent visual fatigue.
   - **30% Secondary Material:** Props, doors, support trusses, and secondary trim.
   - **10% Focal Pop:** Reserved exclusively for gameplay navigation, interactive objective levers, and lethal hazards.
2. Provide hex color codes (`#RRGGBB`) and material names for each tier.
3. Identify your project's **Affordance Colors**:
   - What color marks *traversable ledges* (e.g., weathered yellow)?
   - What color marks *interactive mechanisms* (e.g., high-vis amber)?
   - What color marks *immediate lethal hazard* (e.g., saturated red)?

### Step 5 — Construct the beat-by-beat Color Script arc

In Section 3 (Part B) of the template:
1. Review your team's narrative beats from your [World Bible](/assignments/world-bible/) and level walkthrough.
2. Fill out the **Color Script Progression Table** mapping the emotional lighting across all 4 beats of your 5-minute slice:
   - **Beat 1: Infiltration / Entry Zone** (Grounding, natural state, tension building)
   - **Beat 2: Interior Transit / Encounter Setup** (Claustrophobia, shadow deepening, shift in light temperature)
   - **Beat 3: Climax / Main Objective Arena** (Peak adrenaline, high value contrast, saturated focal lighting)
   - **Beat 4: Escape / Extraction / Aftermath** (Catharsis, relief, dawn/horizon lighting)
3. For each beat, specify the dominant hue, Kelvin light temperature (e.g., `2700K` warm sodium vs `7500K` cool sky), and shadow contrast.

### Step 6 — Specify PBR materials and technical guardrails

In Sections 4 and 5 of the template:
1. **Material Standards:** Document the base color value ranges, roughness ranges, and metallic rules for your world's four primary surface types (e.g., concrete/stone, painted metal, treated wood, glass).
2. **Edge Wear Logic:** Document where wear and tear accumulates (e.g., *only on exposed convex corners and contact points, never as uniform cloudy noise*).
3. **Texel Density Budget:** Record your team's texel density target (e.g., `10.24 px/cm` for hero weapons/characters, `5.12 px/cm` for environmental props).
4. **Grid Snapping Metrics:** Specify modular wall and doorway dimensions (e.g., `100cm / 200cm / 400cm` walls; `120cm W × 240cm H` doors) to ensure all modular pieces snap cleanly in Unreal Engine.

### Step 7 — Author visual Do's and Don'ts

In Section 6 of the template:
1. Write at least **four explicit pairs of Do's and Don'ts**.
2. Make them concrete, enforceable rules:
   - *✓ DO ground every machine with real-world cables, mounting bolts, and physical power feeds.*
   - *✗ DON'T float technological devices in mid-air without visible structural mounting.*
   - *✓ DO bevel all mechanical hard edges so light catches specular highlights in UE5.*
   - *✗ DON'T leave razor-sharp 90-degree polygon edges that look artificial.*

### Step 8 — Review and publish to Google Sites

1. Conduct a peer-review session with your team: verify that all artists understand and agree to follow these rules.
2. Export your completed Art Style Guide as a PDF or save it as a slide deck.
3. Post the document and a brief reflection to your Google Sites portfolio under **Unit 2: Vertical Slice Pre-Production**.

{{% /steps %}}

---

## Submit

{{< callout type="warning" >}}
**Google Sites Portfolio Deliverable**:
Upload your documentation to your Google Sites portfolio under **Coursework > Unit 2: The Vertical Slice**:
1. **Title:** Module 2.2 — Studio Art Style Guide
2. **Embedded Artifact:** Embed your completed Art Style Guide document (or slide deck) directly on the page.
3. **Visual Highlights:** Include images of your 3 Visual Pillars, 60-30-10 palette swatches, and Color Script table.
4. **Team Reflection (3–4 sentences):**
   - *How do your 3 visual pillars reflect the gameplay mechanics of your vertical slice?*
   - *Which affordance colors did your team choose to guide player navigation, and why?*
   - *How will your technical guardrails (texel density, grid snapping) prevent visual clashes during production?*
{{< /callout >}}

---

## Rubric

### Assessment Rubric

| Criteria | Proficient (4-5 pts) | Developing (2-3 pts) | Beginning (0-1 pt) |
|---|---|---|---|
| **Visual Pillars & Artistic Identity** | Three actionable, evocative visual pillars are established with clear definitions and specific in-game 3D modeling/texturing applications. Zero generic buzzwords. | Three pillars are named, but descriptions are somewhat generic or lack specific 3D art applications. | Missing pillars or vague, cliché descriptions that provide no actionable guidance to artists. |
| **Shape Language & Form Rules** | Comprehensive shape rules differentiate friendly, hostile, and neutral factions using clear geometric primitives (■, ▲, ●) with concrete prop examples. | Basic shape rules established, but examples are vague or lack clear connection to gameplay affordances. | Shape language is omitted or contradicts the established world narrative. |
| **Color Script & 60-30-10 Palette** | Full 60-30-10 environment palette defined with exact hex codes. Beat-by-beat color script progression maps emotional pacing from entry to climax. Clear affordance colors. | Palette is provided, but lacks strict 60-30-10 ratios or color script table has missing beats. | Palette is incomplete; no color script arc or affordance rules established. |
| **PBR Standards & Technical Guardrails** | Surface roughness ranges, edge wear logic, texel density budgets, and modular grid snapping metrics are explicitly documented for team consistency. | Technical specs are partially documented, but missing texel density targets or modular grid metrics. | Technical guardrails omitted; no PBR or scale rules defined. |
| **Visual Do's & Don'ts & Presentation** | Concrete, actionable Do's and Don'ts matrix eliminates ambiguity. Document is polished, well-formatted, and embedded cleanly on Google Sites with reflection. | Do's and Don'ts are included but vague; document formatting has minor inconsistencies. | Incomplete document or unsubmitted assignment. |

---

## Notes & Pro-Tips

- **The Art Bible is a Living Document:** Do not treat your style guide as a tombstone. As you greybox your vertical slice in Module 2.3 and run early lighting tests, return to this document and adjust roughness values or light temperatures as you see what looks best in-engine.
- **Readability Trumps Cinematic Fidelity:** GDC art directors emphasize that if a color script looks cinematic but an enemy or climbable ledge blends invisibly into the background, the color script has failed. Gameplay clarity always comes first.
- **Enforce the Rules Early:** The earlier you catch an asset that violates your visual pillars, the less time your team wastes on rework. Use your Do's and Don'ts during every weekly peer review.
