import os, re

courses_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses"

# Clean IMC template
imc_content = """---
description: "Intro to Media Careers course map outlining units, modules, and assignments."
summary: "Intro to Media Careers course map outlining units, modules, and assignments."
title: Intro to Media Careers
course_code: IMC
---

Intro to Media Careers (IMC) explores digital literacy, design principles, media production, intellectual property, and career pathways in the Arts, Entertainment, and Design cluster.

<details class="unit-accordion">
<summary class="unit-summary">Unit 1: Digital Foundations</summary>
<div class="unit-items-container">
<a href="/learn/computing/what-a-computer-is-doing/" class="unit-item-button">
<div>
<div class="unit-item-title">What a Computer Is Doing</div>
<div class="unit-item-desc">Hardware, CPU, RAM, storage, and GPU fundamentals.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/learn/computing/operating-systems-and-why-they-differ/" class="unit-item-button">
<div>
<div class="unit-item-title">Operating Systems</div>
<div class="unit-item-desc">Windows, macOS, Linux, and OS file management differences.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/learn/career/the-arts-entertainment-design-cluster/" class="unit-item-button">
<div>
<div class="unit-item-title">CAREER-101: The AME Cluster</div>
<div class="unit-item-desc">CTE pathways, industry sectors, and focus area career maps.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/build-your-portfolio/" class="unit-item-button">
<div>
<div class="unit-item-title">Build Your Portfolio</div>
<div class="unit-item-desc">Set up your Google Sites portfolio homepage and bio.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 2: Design & The Creative Process</summary>
<div class="unit-items-container">
<a href="/learn/design/elements-of-art/" class="unit-item-button">
<div>
<div class="unit-item-title">Elements of Art</div>
<div class="unit-item-desc">Line, shape, form, value, space, color, and texture.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/learn/design/principles-of-design/" class="unit-item-button">
<div>
<div class="unit-item-title">Principles of Design</div>
<div class="unit-item-desc">Balance, contrast, emphasis, movement, pattern, and rhythm.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/mood-board/" class="unit-item-button">
<div>
<div class="unit-item-title">Mood Board Gathering</div>
<div class="unit-item-desc">Reference board assembly using PureRef and Google Sites.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 3: Storytelling Across Media</summary>
<div class="unit-items-container">
<a href="/learn/media/what-makes-a-story/" class="unit-item-button">
<div>
<div class="unit-item-title">MEDIA-101: What Makes a Story</div>
<div class="unit-item-desc">Storytelling premises, theme, character motivation, and conflict.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/learn/media/shot-types-and-framing/" class="unit-item-button">
<div>
<div class="unit-item-title">MEDIA-105: Shot Types & Framing</div>
<div class="unit-item-desc">Wide shots, medium shots, close-ups, and camera positioning.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/storyboard-sequence/" class="unit-item-button">
<div>
<div class="unit-item-title">Storyboard Sequence</div>
<div class="unit-item-desc">Create a 6-panel storyboard sequence with shot notes.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 4: Careers & Media Literacy</summary>
<div class="unit-items-container">
<a href="/learn/career/reading-an-onet-entry/" class="unit-item-button">
<div>
<div class="unit-item-title">CAREER-102: Reading an O*NET Entry</div>
<div class="unit-item-desc">O*NET codes, median salaries, and career outlook data.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/onet-career-report/" class="unit-item-button">
<div>
<div class="unit-item-title">O*NET Research Report</div>
<div class="unit-item-desc">Investigate 2 AME pathway careers and publish to portfolio.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 5: Law, Ethics & AI</summary>
<div class="unit-items-container">
<a href="/learn/law/copyright-basics/" class="unit-item-button">
<div>
<div class="unit-item-title">Copyright Basics</div>
<div class="unit-item-desc">Original authorship, copyright protections, and public domain.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/learn/law/fair-use-the-four-factors/" class="unit-item-button">
<div>
<div class="unit-item-title">Fair Use: The 4 Factors</div>
<div class="unit-item-desc">Transformative use, market impact, and parody analysis.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/fair-use-case/" class="unit-item-button">
<div>
<div class="unit-item-title">Fair Use Case Analysis</div>
<div class="unit-item-desc">Evaluate copyright scenarios using the 4 factors.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 6: Production & The Pitch</summary>
<div class="unit-items-container">
<a href="/learn/production/production-phases/" class="unit-item-button">
<div>
<div class="unit-item-title">Production Phases</div>
<div class="unit-item-desc">Pre-production, production, post-production, and launch.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/learn/production/pitching-a-concept/" class="unit-item-button">
<div>
<div class="unit-item-title">Pitching a Concept</div>
<div class="unit-item-desc">Pitch decks, elevator pitches, and presentation craft.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/concept-pitch/" class="unit-item-button">
<div>
<div class="unit-item-title">Concept Deck Pitch</div>
<div class="unit-item-desc">Present a final project concept deck to the class.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>
"""

with open(os.path.join(courses_dir, "imc.md"), "w", encoding="utf-8") as f:
    f.write(imc_content.strip())
print("Wrote clean unindented HTML for imc.md!")

# Clean GAD1 template
gad1_content = """---
description: "Game Art & Design 1 course map outlining units, modules, and assignments."
summary: "Game Art & Design 1 course map outlining units, modules, and assignments."
title: Game Art & Design 1
course_code: GAD1
---

Game Art & Design 1 (GAD1) develops core competencies in 3D hard-surface modeling, PBR material creation, Unreal Engine 5 interactive environments, and game mechanics prototyping.

<details class="unit-accordion">
<summary class="unit-summary">Unit 1: 3D Modeling Foundations</summary>
<div class="unit-items-container">
<a href="/learn/blender/interface-and-navigation/" class="unit-item-button">
<div>
<div class="unit-item-title">BLND-101: Interface & Navigation</div>
<div class="unit-item-desc">Blender viewport, outliner, properties, and transform gizmos.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/learn/blender/edit-mode-basics/" class="unit-item-button">
<div>
<div class="unit-item-title">BLND-104: Edit Mode Basics</div>
<div class="unit-item-desc">Vertices, edges, faces, extrude, inset, and loop cuts.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/blender-first-model/" class="unit-item-button">
<div>
<div class="unit-item-title">First 3D Model</div>
<div class="unit-item-desc">Model a complete low-poly prop using primitive primitives and edit mode tools.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 2: Modular Assets & UV Unwrapping</summary>
<div class="unit-items-container">
<a href="/learn/blender/uv-unwrapping/" class="unit-item-button">
<div>
<div class="unit-item-title">BLND-107: UV Unwrapping</div>
<div class="unit-item-desc">Seams, texel density, UV packing, and unwrap unwrapping.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/uv-unwrap-drill/" class="unit-item-button">
<div>
<div class="unit-item-title">UV Unwrap Drill</div>
<div class="unit-item-desc">Mark seams, unwrap 3 hard-surface props, and pack UV islands cleanly.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 3: PBR Texturing & Shading</summary>
<div class="unit-items-container">
<a href="/learn/blender/texturing-and-pbr-maps/" class="unit-item-button">
<div>
<div class="unit-item-title">BLND-205: PBR Textures & Maps</div>
<div class="unit-item-desc">Base color, roughness, metallic, normal, and ambient occlusion channels.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/pbr-texture-set/" class="unit-item-button">
<div>
<div class="unit-item-title">PBR Texture Set</div>
<div class="unit-item-desc">Author a complete PBR material set for a 3D asset.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 4: Unreal Engine 5 Environment & Lighting</summary>
<div class="unit-items-container">
<a href="/learn/unreal/interface-and-navigation/" class="unit-item-button">
<div>
<div class="unit-item-title">UE-101: Unreal Interface & Navigation</div>
<div class="unit-item-desc">Viewport controls, content browser, outliner, and actor details.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/engine-orientation/" class="unit-item-button">
<div>
<div class="unit-item-title">Engine Orientation & Graybox</div>
<div class="unit-item-desc">Set up a new UE5 project, organize folders, and build a graybox level blockout.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 5: Blueprint Interactive Logic</summary>
<div class="unit-items-container">
<a href="/learn/unreal/collision-and-triggers/" class="unit-item-button">
<div>
<div class="unit-item-title">UE-203: Collision & Trigger Volumes</div>
<div class="unit-item-desc">Box triggers, overlap events, object channels, and physics responses.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/interactive-door/" class="unit-item-button">
<div>
<div class="unit-item-title">Interactive Door Blueprint</div>
<div class="unit-item-desc">Construct a functional interactive sliding or swinging door actor with audio.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 6: Capstone Vertical Slice</summary>
<div class="unit-items-container">
<a href="/learn/production/scope-and-the-vertical-slice/" class="unit-item-button">
<div>
<div class="unit-item-title">PROD-205: Vertical Slice Scope</div>
<div class="unit-item-desc">Defining a complete, playable 5-minute gameplay slice.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/capstone-vertical-slice/" class="unit-item-button">
<div>
<div class="unit-item-title">Solo Vertical Slice</div>
<div class="unit-item-desc">Package and publish a complete interactive environment with custom 3D models and lighting.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>
"""

with open(os.path.join(courses_dir, "gad1.md"), "w", encoding="utf-8") as f:
    f.write(gad1_content.strip())
print("Wrote clean unindented HTML for gad1.md!")

# Clean GAD2 template
gad2_content = """---
description: "Game Art & Design 2 course map outlining units, modules, and assignments."
summary: "Game Art & Design 2 course map outlining units, modules, and assignments."
title: Game Art & Design 2
course_code: GAD2
---

Game Art & Design 2 (GAD2) focuses on advanced technical art pipelines: character sculpting, retopology, game animation blendspaces, team production sprints, and capstone publishing.

<details class="unit-accordion">
<summary class="unit-summary">Unit 1: Character Blockout & Anatomy</summary>
<div class="unit-items-container">
<a href="/learn/character/character-concept-and-proportions/" class="unit-item-button">
<div>
<div class="unit-item-title">CHAR-101: Character Proportions & Concept</div>
<div class="unit-item-desc">Human anatomy landmarks, heroic proportions, and reference silhouettes.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/character-bust-sculpt/" class="unit-item-button">
<div>
<div class="unit-item-title">Character Bust Sculpt</div>
<div class="unit-item-desc">Sculpt a character bust focusing on facial planes and primary forms.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 2: Retopology & Deformation Edge Flow</summary>
<div class="unit-items-container">
<a href="/learn/character/character-topology-and-deform-flow/" class="unit-item-button">
<div>
<div class="unit-item-title">CHAR-201: Character Topology & Edge Flow</div>
<div class="unit-item-desc">Facial edge loops, shoulder/elbow deformation rings, and quad optimization.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/retopology-practice/" class="unit-item-button">
<div>
<div class="unit-item-title">Low-Poly Retopology Pass</div>
<div class="unit-item-desc">Retopologize a high-poly sculpt to a clean animatable mesh under 15k triangles.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 3: Biped Rigging & Weight Painting</summary>
<div class="unit-items-container">
<a href="/learn/animation/biped-rigging-and-weight-painting/" class="unit-item-button">
<div>
<div class="unit-item-title">ANIM-201: Biped Rigging & Weight Painting</div>
<div class="unit-item-desc">Armature creation, IK/FK bone constraints, vertex weight gradients, and test poses.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/biped-rigging-pass/" class="unit-item-button">
<div>
<div class="unit-item-title">Biped Rig & Weighting Pass</div>
<div class="unit-item-desc">Rig a humanoid character mesh with clean joint deformation.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 4: Locomotion & Gameplay Cycles</summary>
<div class="unit-items-container">
<a href="/learn/animation/idle-and-locomotion-cycles/" class="unit-item-button">
<div>
<div class="unit-item-title">ANIM-301: Walk & Run Cycles</div>
<div class="unit-item-desc">Contact, down, passing, and up poses, hip swaying, and loop timing.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/walk-cycle-animation/" class="unit-item-button">
<div>
<div class="unit-item-title">Walk & Run Cycle Set</div>
<div class="unit-item-desc">Animate a looped walk and run cycle matching game locomotion specs.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 5: Team Production Sprints & Agile Pipeline</summary>
<div class="unit-items-container">
<a href="/learn/production/task-boards-and-sprints/" class="unit-item-button">
<div>
<div class="unit-item-title">PROD-203: Agile Sprints & Task Boards</div>
<div class="unit-item-desc">Kanban boards, burndown velocity, sprint milestones, and peer code reviews.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/team-sprint-milestone/" class="unit-item-button">
<div>
<div class="unit-item-title">Team Sprint Milestone 1</div>
<div class="unit-item-desc">Execute Sprint 1 deliverables on the class collaborative capstone repo.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">Unit 6: Capstone Showcase & Portfolio Defense</summary>
<div class="unit-items-container">
<a href="/learn/career/interviews-and-portfolio-review/" class="unit-item-button">
<div>
<div class="unit-item-title">CAREER-204: Portfolio Review & Interview Prep</div>
<div class="unit-item-desc">Technical art breakdown reels, live project defense, and industry presentation.</div>
</div>
<span class="unit-item-badge badge-module">MODULE</span>
</a>
<a href="/assignments/capstone-final-defense/" class="unit-item-button">
<div>
<div class="unit-item-title">Capstone Showcase & Defense</div>
<div class="unit-item-desc">Present a completed game project and defend technical art contributions.</div>
</div>
<span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
</a>
</div>
</details>
"""

with open(os.path.join(courses_dir, "gad2.md"), "w", encoding="utf-8") as f:
    f.write(gad2_content.strip())
print("Wrote clean unindented HTML for gad2.md!")