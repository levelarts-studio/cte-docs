---
id: asset-list-pipeline
title: "Asset List & Pipeline Doc"
entity: assignment
tier: 200
status: complete
requires: ["PROD-108", "UE-206"]
standards: ["GD.18.1", "16.6", "4.5"]
evidence_for: "4.5"
portfolio: true
portfolio_section: "GAD2 U2"
est_time: 120
setting: studio
aliases: ["/a/asset-list-pipeline"]
---

## The task

Author the official **Master Asset List & Production Pipeline Document** for your team's Vertical Slice project. Following your completed greybox level layout from Module 2.3, itemize every 3D model, modular architectural piece, audio sound effect, and UI element needed to bring the 5-minute slice to finished playable visual quality.

You will establish your team's canonical naming convention taxonomy, configure Content Browser directory rules, establish polygon budgets and LOD/Nanite guardrails, define collision hull standards, and establish the pre-commit Ingestion Quality Gate to ensure seamless collaboration in Unreal Engine 5.

In real-world game development, the Master Asset Manifest is the single source of truth connecting artists, level designers, tech artists, and audio engineers. Before production artists spend weeks modeling and texturing, this document ensures that every asset has an assigned owner, strict poly budget, designated priority, and verified technical specifications.

---

## Before you start

- [Asset Management and Naming](/m/PROD-108/) (`PROD-108`)
- [Greybox the Vertical Slice](/assignments/greybox-slice/) (`greybox-slice`)
- [Art Style Guide](/assignments/art-style-guide/) (`art-style-guide`)
- [Scope and the Vertical Slice](/m/PROD-204/) (`PROD-204`)

{{< callout type="info" >}}
**Starter Template Download**:
Download the pre-formatted studio document [**`Asset_List_and_Pipeline_Template.docx`**](/resources/Asset_List_and_Pipeline_Template.docx) (or [mirror download](/downloads/Asset_List_and_Pipeline_Template.docx)) to your computer before beginning Step 1.
- **File Format:** Microsoft Word (`.docx`) — fully compatible with Microsoft Word, Google Docs, and LibreOffice.
- **Included Sections:** Metadata Block, Studio Naming Taxonomy, Content Browser Hierarchy, Technical & Poly Budgets, Master Asset Tracking Manifest (Spreadsheet Matrix), Audio & UI Standards, Ingestion Quality Gate, and Deliverable Sign-Off.
{{< /callout >}}

---

## Deliverable Overview

Your team's Master Asset List and Pipeline Document establishes technical boundaries across every discipline:

```
┌────────────────────────────────────────────────────────────────────────┐
│               MASTER ASSET LIST & PIPELINE SPECIFICATION               │
├────────────────────────────────┬───────────────────────────────────────┤
│ 1. Studio Naming Taxonomy      │ Prefixes (SM_, SK_, MI_, T_) & Suffixes│
│ 2. Content Browser Directory   │ Standardized /Game/ folder hierarchy  │
│ 3. Technical & Poly Budgets    │ LOD chains, Nanite policy & collision │
│ 4. Master Tracking Manifest    │ Min 15 items itemized with P0/P1/P2   │
│ 5. Audio & UI Specifications   │ Sample rates, 3D spatialization, UMG  │
│ 6. Ingestion Quality Gate      │ 10-point pre-commit verification list │
│ 7. Team Sign-Off & Portfolio   │ Multi-role sign-off & reflection      │
└────────────────────────────────┴───────────────────────────────────────┘
```

---

## Steps

{{% steps %}}

### Step 1 — Download and initialize the studio template

1. Download the [**`Asset_List_and_Pipeline_Template.docx`**](/resources/Asset_List_and_Pipeline_Template.docx) starter document.
2. Open the file in Microsoft Word or upload it to Google Drive as a shared collaborative Google Doc for your studio team.
3. Complete the metadata table at the top:
   - **Project Title:** Your vertical slice game title.
   - **Studio / Team Name:** Your registered production studio name.
   - **Lead Technical Artist / Asset Lead:** The student responsible for pipeline enforcement.
   - **Target Engine:** Unreal Engine 5.x.
   - **Version / Date:** `v1.0` and current date.

### Step 2 — Audit your playable greybox slice

Before adding random props to a wishlist, walk through your team's playable greybox level from Module 2.3:
1. Open your master level (`Slice_P`) in Unreal Engine 5.
2. Walk the critical path from spawn point to slice climax with a notepad or spreadsheet open.
3. Identify every placeholder cube, cylinder, and temporary mesh that must be replaced with custom production art:
   - **Modular Architecture:** How many unique wall segments, floor tiles, doorways, and ceiling trusses are needed to assemble the environment?
   - **Hero Interactive Props:** What consoles, objective levers, airlocks, and generator cores does the player interact with?
   - **Dressing & Clutter:** What crates, pipes, debris piles, and signs support the environmental storytelling from your [World Bible](/assignments/world-bible/)?
   - **Characters & Creatures:** What player models, NPC guides, or enemy combatants appear?
   - **Audio & UI:** What door mechanics, footsteps, weapon impacts, and HUD elements require bespoke sound and graphic assets?

### Step 3 — Adopt studio naming conventions & folder architecture

Review Sections 1 and 2 of the template with your team:
1. Ensure every team member commits to the canonical naming syntax:
   `[Prefix]_[Category]_[AssetName]_[Variant]_[Suffix]`
2. Verify asset prefixes: `SM_` (Static Mesh), `SK_` (Skeletal Mesh), `M_` (Master Material), `MI_` (Material Instance), `T_` (Texture Map), `BP_` (Blueprint), `WBP_` (Widget Blueprint), `A_` (Audio), and `UCX_` (Convex Collision).
3. Enforce the **Zero Spaces / No Version Tags** rule:
   - *Prohibited:* `SM Crate final v2.fbx`
   - *Required:* `SM_Prop_Crate_SciFi_01`
4. Confirm folder assignments in the Unreal Content Browser (`/Game/Art/Environment/`, `/Game/Art/Props/`, `/Game/Audio/`, etc.) and remind everyone of the **Developer Sandbox Quarantine** (never reference `/Game/Developers/` in production maps).

### Step 4 — Formulate poly budgets, LODs & Nanite policy

In Section 3 of the template:
1. Review the baseline triangle budgets for each asset tier:
   - **Hero Character:** `25,000 – 45,000 tris` (Skeletal Mesh; requires traditional LOD0–LOD3 chain).
   - **Hero Prop / Machine:** `15,000 – 30,000 tris` (Nanite enabled if rigid).
   - **Medium Prop:** `3,000 – 8,000 tris` (Nanite enabled).
   - **Modular Kit Piece:** `200 – 1,200 tris` (Nanite enabled).
   - **Small Clutter / Dressing:** `300 – 1,500 tris` (Nanite enabled or single LOD).
2. Record your team's collision standard:
   - All interactive and dressing props must have simple collision authored as custom convex hulls (`UCX_`) or box/capsule primitives.
   - Setting props to "Complex as Simple" is strictly prohibited.
3. Confirm pivot placement rules: floor props pivot at absolute base (`Z = 0`), wall props pivot at mounting surface, doors pivot at the hinge axis.

### Step 5 — Build the Master Asset Tracking Manifest

In Section 4 of the template, itemize at least **15 unique assets** required for your 5-minute slice across multiple departments:
1. **Asset ID:** Use indexed alphanumeric IDs (`AST-001`, `AST-002`, `AST-003`, etc.).
2. **Canonical Asset Name:** Full Unreal name adhering to Section 1 syntax (e.g., `SM_Prop_ReactorCore_01`, `SM_Mod_Wall_Lab_400x300`, `SK_Hero_Pilot_01`).
3. **Category / Zone:** Environment Prop, Modular Kit, Hero Character, Audio SFX, UI Widget, or VFX.
4. **Assigned Owner:** Designate the specific artist or team member responsible for delivering the asset.
5. **Priority Tagging (MoSCoW):**
   - **P0 (Blocker / Critical Path):** Core mechanics and primary route assets. The slice fails without these.
   - **P1 (Essential):** Secondary environment dressing and primary sound effects.
   - **P2 (Polish):** Decorative clutter and ambient particles (first to be cut if time runs short).
6. **Poly Budget & Texture Specs:** Target triangle budget and texture resolution (e.g., `5,000 tris`, `1x 2048 ORM + BC + N`).
7. **Collision Hull:** `UCX Convex`, `Simple Box`, `PhysicsAsset`, or `None`.
8. **Lifecycle Status:** Mark initial status (`Blockout`, `Modeling`, `Texturing`, `In-Engine`, or `Done`).

### Step 6 — Specify Audio & UI technical standards

In Section 5 of the template:
1. Itemize key audio assets (door SFX, terminal clicks, ambient hums, footstep surfaces).
2. Specify technical format: 48 kHz / 16-bit uncompressed WAV; mono for 3D spatialized sound sources; stereo for 2D UI and music beds.
3. Itemize primary UI elements (health/energy HUD, crosshairs, interaction prompt icons).
4. Specify UI canvas anchoring, power-of-two texture resolution, and 9-slice scalable borders.

### Step 7 — Review the Ingestion Quality Gate & sign off

In Sections 6 and 7 of the template:
1. Verify the 10-point **Ingestion Quality Gate Checklist** (transforms applied at 1,1,1; pivot at Z=0; ORM channel packing unchecked for sRGB; Material Instances used; collision hulls verified; redirectors fixed up).
2. Conduct a formal team sign-off review:
   - Lead Technical Artist signs off on naming and folder compliance.
   - Lead 3D Artist signs off on poly budgets and texel density.
   - Lead Level Designer signs off that all critical-path greybox proxies are represented.
   - Production Lead signs off on priority distribution (ensuring no more than 40% of assets are tagged P0).

### Step 8 — Publish to Google Sites portfolio

1. Export your completed Master Asset List & Pipeline Document as a PDF.
2. Upload the document and high-resolution screenshots of your asset manifest matrix to your portfolio under **Unit 2: Vertical Slice Pre-Production**.
3. Write your individual reflection following the prompt below.

{{% /steps %}}

---

## Submit

{{< callout type="warning" >}}
**Google Sites Portfolio Deliverable**:
Upload your documentation to your Google Sites portfolio under **Coursework > Unit 2: The Vertical Slice**:
1. **Title:** Module 2.4 — Master Asset List & Production Pipeline
2. **Embedded Artifact:** Embed your completed Master Asset List & Pipeline document (or spreadsheet) directly on the page.
3. **Visual Highlights:** Include clean screenshots of:
   - Your team's Naming Taxonomy & Folder Hierarchy table
   - The populated Master Asset Tracking Manifest (minimum 15 discrete assets with P0/P1/P2 priorities)
   - The Technical Poly Budget & Nanite guardrail table
4. **Individual Reflection (3–4 sentences):**
   - *How did auditing your playable greybox slice prevent you from budgeting unnecessary "wishlist" props?*
   - *Why is channel packing (ORM) and simple collision (UCX_) critical for maintaining 60 FPS performance in Unreal Engine 5?*
   - *If your team falls 5 days behind schedule during production, how does your P0 / P1 / P2 priority tagging guide what gets cut immediately?*
{{< /callout >}}

---

## Rubric

### Assessment Rubric

| Criteria | Proficient (4-5 pts) | Developing (2-3 pts) | Beginning (0-1 pt) |
|---|---|---|---|
| **Naming Taxonomy & Folder Architecture** (Standard `4.5`) | Canonical syntax (`[Prefix]_[Category]_[AssetName]_[Variant]_[Suffix]`) is comprehensively documented with zero spaces and no version tags. Content Browser hierarchy inside `/Game/` is clearly organized with explicit developer sandbox quarantine rules. | Naming conventions are present, but allow inconsistencies (e.g., occasional spaces or missing prefixes). Folder hierarchy is partially documented. | Inconsistent or missing naming conventions. No clear folder structure; high risk of broken asset links. |
| **Master Asset Manifest & Discipline Inventory** (Standard `16.6`) | Complete, professional manifest itemizes at least 15 discrete assets across 3D environment, modular architecture, characters, audio, and UI. Every asset has an assigned owner, clear priority (P0/P1/P2), and current lifecycle status. | Manifest contains 10–14 assets, or lacks clear priority sorting (e.g., everything marked P0). Some assigned owners or statuses are missing. | Incomplete manifest with fewer than 10 assets; lacks priority tagging or cross-discipline items. |
| **Technical Budgets, LODs & Collision Guardrails** (Standard `GD.18.1`) | Exact polygon budgets are specified by asset class. LOD reduction targets and modern UE5 Nanite rules are clearly delineated. Simple collision (`UCX_`) and pivot placement standards are strictly established. | Budgets are mentioned, but lack distinction between asset classes or omit Nanite vs. skeletal mesh LOD rules. Collision specs are vague. | Poly budgets omitted; no collision guidelines; mesh pivot standards missing. |
| **Quality Gate Protocol & Portfolio Presentation** (Standards `4.5` & `16.6`) | Pre-commit 10-point Ingestion Quality Gate is thoroughly detailed. Document is beautifully formatted, signed off across team roles, and embedded cleanly on Google Sites with thoughtful individual reflections. | Quality gate is present but lacks key technical checks (e.g., sRGB on ORM, transform freezing). Portfolio page has minor formatting issues or brief reflection. | Missing quality gate; document is unformatted or unsubmitted on portfolio. |

---

## Notes & Pro-Tips

- **Avoid the "Everything is P0" Trap:** When inexperienced teams build their asset manifest, they often mark every single prop as "P0 - Critical." If everything is top priority, nothing is prioritized. A healthy production manifest allocates approximately **30–40% P0**, **40% P1**, and **20–30% P2**. P2 assets are your schedule's shock absorber.
- **Fix Up Redirectors Every Friday:** Whenever you rename or move an asset inside the Unreal Engine Content Browser, Unreal leaves a tiny redirector file behind so existing references don't instantly break. Over time, hundreds of redirectors build up, causing slow load times and ghost dependencies. Right-click your top-level `/Game/Art/` folder once a week and click **Fix Up Redirectors in Folder**.
- **Pivot Point Discipline:** Setting an origin pivot at the bottom center (`Z = 0`) of a floor-standing asset takes 5 seconds in Blender (`Shift + S > Cursor to World Origin`, then `Object > Set Origin > Origin to 3D Cursor`). If you skip this, level designers will waste 30 seconds manually elevating every single instance of the prop so it doesn't sink into the floor. On a 500-prop level, that is over 4 hours of wasted studio time!
