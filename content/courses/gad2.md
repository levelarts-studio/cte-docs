---
title: "Game Art & Design 2 (GAD2)"
course_code: GAD2
entity: course
units:
  - name: U1 Studio Formation, Concept & Greenlight
    assignments:
      - team-role-charter
      - studio-concept-pitches
      - team-gdd
      - scope-and-slice
      - schedule-and-taskboard
      - greenlight-pitch
    reference:
      - PROD-104
      - PROD-206
      - GAME-208
  - name: U2 Worldbuilding, Blockout & Art Bible
    assignments:
      - world-bible
      - art-style-guide
      - greybox-slice
      - asset-list-pipeline
      - milestone-review-1
    reference:
      - DESN-202
      - UE-207
      - BLND-302
  - name: "U3 Production Sprint: Custom Assets"
    assignments:
      - hero-character
      - environment-props
      - fab-license-audit
      - standups-and-handoff
      - milestone-review-2
    reference:
      - CHAR-201
      - CHAR-202
      - CHAR-301
      - CHAR-302
      - CHAR-401
      - DESN-203
      - ANIM-201
      - BLND-209
      - PROD-108
  - name: U4 Systems, UI & Interaction
    assignments:
      - core-loop-prototype
      - ui-ux-pass
      - accessibility-audit
      - feedback-systems-pass
      - animation-integration
    reference:
      - GAME-202
      - GAME-104
      - UE-302
      - ANIM-102
      - ANIM-202
      - ANIM-301
      - BLND-210
      - GAME-207
  - name: U5 Playtest, Iterate & Optimize
    assignments:
      - external-playtest
      - playtest-data-report
      - iteration-sprint
      - optimization-pass
      - milestone-review-3
    reference:
      - BLND-212
  - name: U6 Ship, Showcase & Industry
    assignments:
      - release-build
      - marketing-beat
      - monetization-analysis
      - showcase-event
      - careers-capstone
      - postmortem-capstone
      - xr-briefing
    reference:
      - MEDIA-114
      - LAW-201
      - CAREER-202
      - PROD-207
---

Welcome to Game Art & Design 2. In this advanced capstone course, you and your classmates will operate as a collaborative indie studio to build and publish an original Vertical Slice game. Working with open-ended creative briefs, you will sculpt custom hero characters, build modular 3D environments, engineer gameplay mechanics in Unreal Engine 5, conduct external playtesting, and release your game.

**Course Scope:** 6 Units · 34 Modules & Assignments · 100 Standards Covered

---

## Unit 1: Studio Formation, Concept & Greenlight

> **What you will learn:** In this unit, you will form our studio department teams, pitch original game concepts, vote as a studio to select our title, author the master Game Design Document (GDD), set up Git source control, and defend the project at the Greenlight Milestone.
>
> <span class="unit-stats">6 Modules · 17 Standards Covered</span>

<details class="unit-accordion" open>
<summary class="unit-summary">
  <span><strong>Module 1.1:</strong> Studio Roles & Team Charter</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will choose paired department roles (art lead, technical artist, level designer) and sign the studio charter.</div>
  <a href="/m/PROD-102/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Roles on a Creative Team</div>
      <div class="unit-item-desc">Code: <code>PROD-102</code> · Studio hierarchy, paired ownership, and team accountability</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/team-role-charter/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Studio Roles & Team Charter</div>
      <div class="unit-item-desc">ID: <code>team-role-charter</code> · Deliverable: Signed studio team charter document</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>16.2</code> <code>8.1</code> <code>9.1</code> <code>8.5</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 1.2:</strong> Concept Pitches (Individual, Class Votes)</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will pitch a 90-second vertical slice concept to the class, and the studio will vote on our greenlight title.</div>
  <a href="/m/GAME-103/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Genres and Player Profiles</div>
      <div class="unit-item-desc">Code: <code>GAME-103</code> · Bartle player taxonomy, target demographics, and genre mechanics</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/PROD-105/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Pitching a Concept</div>
      <div class="unit-item-desc">Code: <code>PROD-105</code> · High-concept elevator hook, core mechanic, and visual style</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/studio-concept-pitches/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Concept Pitches</div>
      <div class="unit-item-desc">ID: <code>studio-concept-pitches</code> · Deliverable: Pitch slide deck & vote log</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.18.3</code> <code>13.2</code> <code>2.3</code> <code>10.2</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 1.3:</strong> Team Game Design Document</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will collaborate with your team to author the living GDD detailing gameplay loops, narrative, and asset lists.</div>
  <a href="/m/PROD-201/" class="unit-item-button">
    <div>
      <div class="unit-item-title">The Game Design Document</div>
      <div class="unit-item-desc">Code: <code>PROD-201</code> · Living GDDs, technical constraints, and feature tables</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/team-gdd/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Team Game Design Document</div>
      <div class="unit-item-desc">ID: <code>team-gdd</code> · Deliverable: Studio living GDD document</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.18.2</code> <code>16.4</code> <code>2.5</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 1.4:</strong> Scope & Vertical Slice Definition</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will define the precise boundaries of our 5-minute playable slice and cut feature bloat.</div>
  <a href="/m/PROD-204/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Scope and the Vertical Slice</div>
      <div class="unit-item-desc">Code: <code>PROD-204</code> · Must-have vs nice-to-have features, vertical vs horizontal slices</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/scope-and-slice/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Scope & Vertical Slice Definition</div>
      <div class="unit-item-desc">ID: <code>scope-and-slice</code> · Deliverable: Vertical slice scope contract</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>16.9</code> <code>GD.18.3</code> <code>5.8</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 1.5:</strong> Production Schedule & Task Board</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will set up the team Kanban board (Trello/GitHub Projects) and initialize the Git LFS project repository.</div>
  <a href="/m/PROD-203/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Task Boards and Sprints</div>
      <div class="unit-item-desc">Code: <code>PROD-203</code> · Kanban workflow, estimating task duration, and sprint cycles</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/PROD-202/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Version Control for Teams</div>
      <div class="unit-item-desc">Code: <code>PROD-202</code> · Git LFS, branching strategies, conflict resolution, and pull requests</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/schedule-and-taskboard/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Production Schedule & Task Board</div>
      <div class="unit-item-desc">ID: <code>schedule-and-taskboard</code> · Deliverable: Live project task board and repo setup</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>16.5</code> <code>16.7</code> <code>2.8</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 1.6:</strong> GREENLIGHT: Pitch to Approve the Project</span>
  <span class="unit-item-badge badge-assignment">GREENLIGHT MILESTONE</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will present the studio's greenlight defense to approve budget, pipeline, and commence production.</div>
  <a href="/m/PROD-103/" class="unit-item-button">
    <div>
      <div class="unit-item-title">The Creative Brief</div>
      <div class="unit-item-desc">Code: <code>PROD-103</code> · Stakeholder signoff criteria and milestone deliverables</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/greenlight-pitch/" class="unit-item-button">
    <div>
      <div class="unit-item-title">GREENLIGHT: Pitch to Approve the Project</div>
      <div class="unit-item-desc">ID: <code>greenlight-pitch</code> · Deliverable: Greenlight presentation recording & signoff</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>13.2</code> <code>2.3</code> <code>16.8</code></div>
</div>
</details>

<div class="unit-ref-shelf">
  <div class="unit-ref-shelf-title">Unit 1 Reference Shelf (Supplemental Reading)</div>
  <div class="unit-ref-shelf-items">
    <a href="/m/PROD-104/" class="unit-ref-pill"><code>PROD-104</code> Project Planning & Milestones</a>
    <a href="/m/PROD-206/" class="unit-ref-pill"><code>PROD-206</code> Budgets & Resources</a>
    <a href="/m/GAME-208/" class="unit-ref-pill"><code>GAME-208</code> Rapid Prototyping</a>
  </div>
</div>

---

## Unit 2: Worldbuilding, Blockout & Art Bible

> **What you will learn:** In this unit, you will develop the game's world lore, author the official Art Style Bible so all team assets look unified, greybox the entire 5-minute slice in Unreal Engine, and build our master asset pipeline registry.
>
> <span class="unit-stats">5 Modules · 14 Standards Covered</span>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 2.1:</strong> World Bible & Environmental Storytelling</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will author world history, factions, environmental visual clues, and lore guidelines for level artists.</div>
  <a href="/m/GAME-205/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Worldbuilding and Environmental Storytelling</div>
      <div class="unit-item-desc">Code: <code>GAME-205</code> · Visual lore, architectural styles, and environmental decay</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/GAME-107/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Narrative in Games</div>
      <div class="unit-item-desc">Code: <code>GAME-107</code> · Embedded vs emergent narrative, audio logs, and environmental text</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/world-bible/" class="unit-item-button">
    <div>
      <div class="unit-item-title">World Bible & Environmental Storytelling</div>
      <div class="unit-item-desc">ID: <code>world-bible</code> · Deliverable: Published studio World Bible document</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.18.4</code> <code>15.1</code> <code>15.3</code> <code>GD.17.3</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 2.2:</strong> Art Style Guide</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will create our Art Style Guide specifying color keys, shape language, texel density, and material rules.</div>
  <a href="/m/DESN-201/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Color Scripting and Mood</div>
      <div class="unit-item-desc">Code: <code>DESN-201</code> · Emotional color progression, lighting keys, and mood palettes</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/DESN-116/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Brand Identity and Style Guides</div>
      <div class="unit-item-desc">Code: <code>DESN-116</code> · Style guides, art bible rules, material consistency</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/art-style-guide/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Art Style Guide</div>
      <div class="unit-item-desc">ID: <code>art-style-guide</code> · Deliverable: Studio Art Bible deck</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.17.4</code> <code>13.3</code> <code>10.3</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 2.3:</strong> Greybox the Vertical Slice</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will construct the entire playable 5-minute slice in Unreal Engine using blockout geometry.</div>
  <a href="/m/UE-206/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Level Blockout Workflow</div>
      <div class="unit-item-desc">Code: <code>UE-206</code> · Scale metrics, combat arenas, and pacing blockouts</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/greybox-slice/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Greybox the Vertical Slice</div>
      <div class="unit-item-desc">ID: <code>greybox-slice</code> · Deliverable: Master greybox level commit in Git repo</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.18.4</code> <code>GD.17.6</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 2.4:</strong> Asset List & Pipeline Doc</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will itemize every model, audio effect, and UI asset with assigned artists, LODs, and file prefixes.</div>
  <a href="/m/PROD-108/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Asset Management and Naming</div>
      <div class="unit-item-desc">Code: <code>PROD-108</code> · Asset registries, prefixes (`SM_`, `M_`, `T_`), and LOD poly budgets</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/asset-list-pipeline/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Asset List & Pipeline Doc</div>
      <div class="unit-item-desc">ID: <code>asset-list-pipeline</code> · Deliverable: Complete master asset manifest spreadsheet</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.18.1</code> <code>16.6</code> <code>4.5</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 2.5:</strong> Milestone Review 1</span>
  <span class="unit-item-badge badge-assignment">MILESTONE REVIEW</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will conduct Sprint Review 1: playable greybox walkthrough, style guide review, and blocker resolution.</div>
  <a href="/m/PROD-106/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Meetings, Standups, and Notes</div>
      <div class="unit-item-desc">Code: <code>PROD-106</code> · Retrospectives, unblocking dependencies, and action logs</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/milestone-review-1/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Milestone Review 1</div>
      <div class="unit-item-desc">ID: <code>milestone-review-1</code> · Deliverable: Milestone signoff document</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>16.8</code> <code>8.4</code> <code>10.5</code></div>
</div>
</details>

<div class="unit-ref-shelf">
  <div class="unit-ref-shelf-title">Unit 2 Reference Shelf (Supplemental Reading)</div>
  <div class="unit-ref-shelf-items">
    <a href="/m/DESN-202/" class="unit-ref-pill"><code>DESN-202</code> Silhouette & Readability</a>
    <a href="/m/UE-207/" class="unit-ref-pill"><code>UE-207</code> Landscape & Environment</a>
    <a href="/m/BLND-302/" class="unit-ref-pill"><code>BLND-302</code> Modular Kit Building</a>
  </div>
</div>

---

## Unit 3: Production Sprint: Custom Assets

> **What you will learn:** In this unit, you will build our game's custom 3D assets: sculpt and retopologize the hero character, model at least 3 original environment props per student, integrate Fab assets with legal license audits, and run daily paired standups.
>
> <span class="unit-stats">5 Modules · 18 Standards Covered</span>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 3.1:</strong> Hero Character (Custom, Required)</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will sculpt, retopologize, and texture our project's hero character with game-ready topology.</div>
  <a href="/m/CHAR-101/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Character Proportions & Silhouette</div>
      <div class="unit-item-desc">Code: <code>CHAR-101</code> · Anatomical landmarks, heroic proportions, and silhouette clarity</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/CHAR-102/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Sculpt Blockout & Base Meshes</div>
      <div class="unit-item-desc">Code: <code>CHAR-102</code> · Primary facial planes, dynamic topology sculpting, and symmetry</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/hero-character/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Hero Character (Custom, Required)</div>
      <div class="unit-item-desc">ID: <code>hero-character</code> · Deliverable: Game-ready rigged character model</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.17.5</code> <code>AV.17.2</code> <code>AV.17.4</code> <code>GD.17.4</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 3.2:</strong> Environment Props (Custom, 3 Minimum)</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">Each student will model, unwrap, and texture at least 3 custom environment props adhering to the Art Bible.</div>
  <a href="/m/BLND-301/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Retopology</div>
      <div class="unit-item-desc">Code: <code>BLND-301</code> · Quad remeshing, Shrinkwrap modifier, poly-strips, and clean edge flow</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/environment-props/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Environment Props (3 Minimum)</div>
      <div class="unit-item-desc">ID: <code>environment-props</code> · Deliverable: 3-prop asset package integrated into level</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.17.4</code> <code>AV.17.8</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 3.3:</strong> Fab Integration & License Audit</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will source marketplace/Fab environment assets and conduct an attribution license audit.</div>
  <a href="/m/LAW-105/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Licenses: CC, Royalty-Free, Commercial</div>
      <div class="unit-item-desc">Code: <code>LAW-105</code> · Marketplace commercial redistribution rules and license compliance</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/fab-license-audit/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Fab Integration & License Audit</div>
      <div class="unit-item-desc">ID: <code>fab-license-audit</code> · Deliverable: Completed asset license audit registry</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>14.5</code> <code>14.1</code> <code>11.6</code> <code>4.5</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 3.4:</strong> Standups & Handoff Protocol</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will run daily 3-minute standups and document paired code/asset handoff notes to prevent blockers.</div>
  <a href="/m/PROD-205/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Handoff and Documentation</div>
      <div class="unit-item-desc">Code: <code>PROD-205</code> · Blueprint comments, material naming, and prefab grouping</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/PROD-106/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Meetings, Standups, and Notes</div>
      <div class="unit-item-desc">Code: <code>PROD-106</code> · Async standup logs, tracking sprint velocity</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/standups-and-handoff/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Standups & Handoff Protocol</div>
      <div class="unit-item-desc">ID: <code>standups-and-handoff</code> · Deliverable: Standup minutes & handoff doc</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>16.8</code> <code>9.3</code> <code>2.9</code> <code>2.5</code> <code>6.4</code> <code>6.5</code> <code>6.6</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 3.5:</strong> Milestone Review 2</span>
  <span class="unit-item-badge badge-assignment">MILESTONE REVIEW</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will participate in Sprint 2 review: inspect assets in engine, verify texel density, and test performance.</div>
  <a href="/m/PROD-107/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Giving and Receiving Feedback</div>
      <div class="unit-item-desc">Code: <code>PROD-107</code> · Constructive critique during sprint reviews</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/milestone-review-2/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Milestone Review 2</div>
      <div class="unit-item-desc">ID: <code>milestone-review-2</code> · Deliverable: Sprint 2 milestone signoff log</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>16.8</code> <code>8.4</code> <code>5.3</code></div>
</div>
</details>

<div class="unit-ref-shelf">
  <div class="unit-ref-shelf-title">Unit 3 Reference Shelf (Supplemental Reading)</div>
  <div class="unit-ref-shelf-items">
    <a href="/m/CHAR-201/" class="unit-ref-pill"><code>CHAR-201</code> Facial Structure</a>
    <a href="/m/CHAR-202/" class="unit-ref-pill"><code>CHAR-202</code> Character Topology</a>
    <a href="/m/CHAR-301/" class="unit-ref-pill"><code>CHAR-301</code> Clothing & Armor</a>
    <a href="/m/CHAR-302/" class="unit-ref-pill"><code>CHAR-302</code> Hair Cards & Alpha</a>
    <a href="/m/CHAR-401/" class="unit-ref-pill"><code>CHAR-401</code> Skin Texturing</a>
    <a href="/m/DESN-203/" class="unit-ref-pill"><code>DESN-203</code> Shape Language</a>
    <a href="/m/ANIM-201/" class="unit-ref-pill"><code>ANIM-201</code> Biped Rigging</a>
    <a href="/m/BLND-209/" class="unit-ref-pill"><code>BLND-209</code> Rigging Basics</a>
    <a href="/m/PROD-108/" class="unit-ref-pill"><code>PROD-108</code> Asset Management</a>
  </div>
</div>

---

## Unit 4: Systems, UI & Interaction

> **What you will learn:** In this unit, you will make the vertical slice fully playable: program the core loop win/loss conditions, author UI menus and HUDs, implement required accessibility options (subtitles, colorblind modes, remapping), and build animation blendspaces.
>
> <span class="unit-stats">5 Modules · 12 Standards Covered</span>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 4.1:</strong> Core Loop Implementation</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will script win/loss triggers, scoring, and primary gameplay systems in Blueprints.</div>
  <a href="/m/GAME-201/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Systems and Balancing</div>
      <div class="unit-item-desc">Code: <code>GAME-201</code> · Balancing math curves, difficulty scaling, and risk vs reward</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/core-loop-prototype/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Core Loop Implementation</div>
      <div class="unit-item-desc">ID: <code>core-loop-prototype</code> · Deliverable: Playable core loop demo commit in repo</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.17.7</code> <code>GD.17.1</code> <code>10.7</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 4.2:</strong> UI & UX Pass</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will build start menus, pause screens, HUD widgets, and audio feedback on button interactions.</div>
  <a href="/m/GAME-108/" class="unit-item-button">
    <div>
      <div class="unit-item-title">UX and UI Principles</div>
      <div class="unit-item-desc">Code: <code>GAME-108</code> · Visual weight, button states, and screen layout</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/UE-205/" class="unit-item-button">
    <div>
      <div class="unit-item-title">UI Widgets and HUD</div>
      <div class="unit-item-desc">Code: <code>UE-205</code> · Widget Blueprints, event dispatchers, and focus navigation</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/ui-ux-pass/" class="unit-item-button">
    <div>
      <div class="unit-item-title">UI & UX Pass</div>
      <div class="unit-item-desc">ID: <code>ui-ux-pass</code> · Deliverable: Full UI menu flow gameplay clip</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.18.7</code> <code>GD.17.8</code> <code>12.4</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 4.3:</strong> Accessibility Audit & Fixes</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will implement colorblind shaders, readable subtitle font sizing, and remappable inputs.</div>
  <a href="/m/GAME-109/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Accessibility in Games</div>
      <div class="unit-item-desc">Code: <code>GAME-109</code> · Motor, visual, auditory, and cognitive accessibility guidelines</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/accessibility-audit/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Accessibility Audit & Fixes</div>
      <div class="unit-item-desc">ID: <code>accessibility-audit</code> · Deliverable: Accessibility demonstration video</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.20.2</code> <code>7.6</code> <code>12.3</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 4.4:</strong> Audio & Feedback Integration</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will integrate MetaSounds, audio attenuation volumes, camera shakes, and particle impact effects.</div>
  <a href="/m/GAME-203/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Game Feel and Feedback</div>
      <div class="unit-item-desc">Code: <code>GAME-203</code> · Game juiciness, camera shakes, hit stops, and impact cues</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/UE-208/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Audio in Engine</div>
      <div class="unit-item-desc">Code: <code>UE-208</code> · Sound cues, spatial attenuation radii, and ambient sound zones</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/feedback-systems-pass/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Audio & Feedback Integration</div>
      <div class="unit-item-desc">ID: <code>feedback-systems-pass</code> · Deliverable: Audio & feedback gameplay clip</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>15.7</code> <code>GD.17.8</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 4.5:</strong> Animation Integration</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will configure Animation Blueprints, 1D/2D blendspaces, and locomotion state machines.</div>
  <a href="/m/ANIM-401/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Anim Blueprints & Blendspaces</div>
      <div class="unit-item-desc">Code: <code>ANIM-401</code> · State machines, transition conditions, and movement blendspaces</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/ANIM-101/" class="unit-item-button">
    <div>
      <div class="unit-item-title">12 Principles in 3D</div>
      <div class="unit-item-desc">Code: <code>ANIM-101</code> · Anticipation, staging, squash & stretch in 3D game animation</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/animation-integration/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Animation Integration</div>
      <div class="unit-item-desc">ID: <code>animation-integration</code> · Deliverable: Animated character gameplay demonstration</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>AV.17.7</code> <code>AV.18.4</code></div>
</div>
</details>

<div class="unit-ref-shelf">
  <div class="unit-ref-shelf-title">Unit 4 Reference Shelf (Supplemental Reading)</div>
  <div class="unit-ref-shelf-items">
    <a href="/m/GAME-202/" class="unit-ref-pill"><code>GAME-202</code> Economy & Progression</a>
    <a href="/m/GAME-104/" class="unit-ref-pill"><code>GAME-104</code> Mechanics, Dynamics, Aesthetics</a>
    <a href="/m/UE-302/" class="unit-ref-pill"><code>UE-302</code> Data Tables & Save Systems</a>
    <a href="/m/ANIM-102/" class="unit-ref-pill"><code>ANIM-102</code> Graph Editor</a>
    <a href="/m/ANIM-202/" class="unit-ref-pill"><code>ANIM-202</code> Walk & Run Cycles</a>
    <a href="/m/ANIM-301/" class="unit-ref-pill"><code>ANIM-301</code> Action Poses</a>
    <a href="/m/BLND-210/" class="unit-ref-pill"><code>BLND-210</code> Keyframe Animation</a>
    <a href="/m/GAME-207/" class="unit-ref-pill"><code>GAME-207</code> Multiplayer Concepts</a>
  </div>
</div>

---

## Unit 5: Playtest, Iterate & Optimize

> **What you will learn:** In this unit, you will host playtest sessions with guest students, analyze telemetry and feedback data, execute a targeted iteration sprint, optimize Nanite/Lumen performance for 60 FPS, and lock the Beta build.
>
> <span class="unit-stats">5 Modules · 13 Standards Covered</span>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 5.1:</strong> External Playtest (Other Classes)</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will run external playtesting with IMC and guest students, logging player confusion points and bugs.</div>
  <a href="/m/GAME-204/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Playtesting Methods</div>
      <div class="unit-item-desc">Code: <code>GAME-204</code> · Blind playtests, quantitative metrics, and qualitative feedback surveys</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/external-playtest/" class="unit-item-button">
    <div>
      <div class="unit-item-title">External Playtest</div>
      <div class="unit-item-desc">ID: <code>external-playtest</code> · Deliverable: Playtest observation logs & video clips</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.18.6</code> <code>12.4</code> <code>13.6</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 5.2:</strong> Playtest Data Report</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will analyze completion rates, survey metrics, and death heatmaps into an actionable report.</div>
  <a href="/m/GAME-204/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Playtesting Methods</div>
      <div class="unit-item-desc">Code: <code>GAME-204</code> · Data analysis, filtering feedback, and triaging bug priority</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/playtest-data-report/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Playtest Data Report</div>
      <div class="unit-item-desc">ID: <code>playtest-data-report</code> · Deliverable: Published playtest findings report</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>5.1</code> <code>11.1</code> <code>10.8</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 5.3:</strong> Iteration Sprint from Findings</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will execute a 1-week sprint fixing the top usability issues and gameplay bugs revealed by the data.</div>
  <a href="/m/DESN-115/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Iteration and Revision</div>
      <div class="unit-item-desc">Code: <code>DESN-115</code> · Prioritizing high-impact player fixes over adding new features</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/iteration-sprint/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Iteration Sprint from Findings</div>
      <div class="unit-item-desc">ID: <code>iteration-sprint</code> · Deliverable: Git changelog and before/after comparison video</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>10.5</code> <code>5.3</code> <code>9.6</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 5.4:</strong> Performance & Optimization Pass</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will profile draw calls, tune Lumen settings, and virtualize geometry with Nanite to maintain 60 FPS.</div>
  <a href="/m/UE-210/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Performance and Profiling</div>
      <div class="unit-item-desc">Code: <code>UE-210</code> · Unreal Insights, GPU visualizer, and draw call batching</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/UE-301/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Nanite and Lumen</div>
      <div class="unit-item-desc">Code: <code>UE-301</code> · Nanite virtualization, raytracing scalability, and lighting optimization</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/optimization-pass/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Performance & Optimization Pass</div>
      <div class="unit-item-desc">ID: <code>optimization-pass</code> · Deliverable: Profiler benchmark report</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.18.8</code> <code>GD.20.1</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 5.5:</strong> Milestone Review 3</span>
  <span class="unit-item-badge badge-assignment">MILESTONE REVIEW</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will participate in Milestone 3 review: Beta build freeze, feature completion, and final bug triage.</div>
  <a href="/m/PROD-107/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Giving and Receiving Feedback</div>
      <div class="unit-item-desc">Code: <code>PROD-107</code> · QA issue tracking and release candidate signoff</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/milestone-review-3/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Milestone Review 3</div>
      <div class="unit-item-desc">ID: <code>milestone-review-3</code> · Deliverable: Beta feature freeze signoff document</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>16.8</code> <code>8.4</code></div>
</div>
</details>

<div class="unit-ref-shelf">
  <div class="unit-ref-shelf-title">Unit 5 Reference Shelf (Supplemental Reading)</div>
  <div class="unit-ref-shelf-items">
    <a href="/m/BLND-212/" class="unit-ref-pill"><code>BLND-212</code> Poly Budget and LODs</a>
  </div>
</div>

---

## Unit 6: Ship, Showcase & Industry

> **What you will learn:** In this capstone unit, you will ship the game two weeks before finals. You will build a 45-second launch trailer, design capsule key art for an Itch.io/Steam-style store page, host the public arcade showcase, author your studio postmortem, and defend your senior portfolio.
>
> <span class="unit-stats">7 Modules · 34 Standards Covered</span>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 6.1:</strong> Release Build & QA Checklist</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will run the final smoke test, verify installer packages, and tag the Gold Master release in the repository.</div>
  <a href="/m/UE-209/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Packaging a Build</div>
      <div class="unit-item-desc">Code: <code>UE-209</code> · Shipping build configuration, debug removal, and pak compression</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/release-build/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Release Build & QA Checklist</div>
      <div class="unit-item-desc">ID: <code>release-build</code> · Deliverable: Packaged master game build</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.18.8</code> <code>15.9</code> <code>4.5</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 6.2:</strong> Marketing Beat: Trailer, Key Art, Store Page</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will produce a 45-second launch trailer, capsule key art, and an Itch.io / Steam store page.</div>
  <a href="/m/MEDIA-116/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Trailers, Key Art, and Store Pages</div>
      <div class="unit-item-desc">Code: <code>MEDIA-116</code> · Capsule art sizes, first 5 seconds hook, and store metadata</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/MEDIA-108/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Editing: Cuts and Transitions</div>
      <div class="unit-item-desc">Code: <code>MEDIA-108</code> · Rhythmic cutting to music, match cuts, and title cards</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/marketing-beat/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Marketing Beat: Trailer, Key Art, Store Page</div>
      <div class="unit-item-desc">ID: <code>marketing-beat</code> · Deliverable: Itch.io store page link & embedded trailer</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>13.1</code> <code>13.3</code> <code>15.4</code> <code>15.8</code> <code>13.8</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 6.3:</strong> Monetization & Content Ecosystem Analysis</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will analyze premium, free-to-play, battle pass, DLC, and UGC creator economy monetization models.</div>
  <a href="/m/GAME-206/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Monetization Models</div>
      <div class="unit-item-desc">Code: <code>GAME-206</code> · Ethical monetization vs predatory dark patterns, and DLC scoping</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/monetization-analysis/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Monetization Analysis</div>
      <div class="unit-item-desc">ID: <code>monetization-analysis</code> · Deliverable: Monetization strategy paper on your portfolio</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.18.9</code> <code>13.4</code> <code>13.9</code> <code>12.5</code> <code>13.7</code> <code>12.8</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 6.4:</strong> Public Showcase Event</span>
  <span class="unit-item-badge badge-assignment">PUBLIC SHOWCASE</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will run a live arcade station showcasing the game to parents, industry guests, and the school community.</div>
  <a href="/m/CAREER-117/" class="unit-item-button">
    <div>
      <div class="unit-item-title">CTSOs, Leadership, and Community</div>
      <div class="unit-item-desc">Code: <code>CAREER-117</code> · Live demo presentation skills, event setup, and answering player questions</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/showcase-event/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Public Showcase Event</div>
      <div class="unit-item-desc">ID: <code>showcase-event</code> · Deliverable: Showcase station photo & feedback log</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>2.3</code> <code>7.8</code> <code>16.3</code> <code>13.6</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 6.5:</strong> Careers, Freelancing & Entrepreneurship</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READINGS</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will build your professional demo reel, create contract and invoice templates, and map your industry entry route.</div>
  <a href="/m/CAREER-204/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Entrepreneurship and Freelancing</div>
      <div class="unit-item-desc">Code: <code>CAREER-204</code> · Client contracts, pricing creative work, and business basics</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/m/CAREER-203/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Cross-Sector Careers for Game Skills</div>
      <div class="unit-item-desc">Code: <code>CAREER-203</code> · Technical art in architecture, aerospace simulation, and virtual production</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/careers-capstone/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Careers, Freelancing & Entrepreneurship</div>
      <div class="unit-item-desc">ID: <code>careers-capstone</code> · Deliverable: Demo reel link & freelance business package</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.19.3</code> <code>GD.19.4</code> <code>GD.19.5</code> <code>3.9</code> <code>14.8</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 6.6:</strong> Postmortem & Portfolio Capstone</span>
  <span class="unit-item-badge badge-assignment">CAPSTONE DEFENSE</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will write a studio postmortem (what went right, what went wrong, lessons learned) and defend your portfolio.</div>
  <a href="/m/PROD-207/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Sustainability in Production</div>
      <div class="unit-item-desc">Code: <code>PROD-207</code> · Sustainable development pace, avoiding crunch, and postmortem analysis</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/postmortem-capstone/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Postmortem & Portfolio Capstone</div>
      <div class="unit-item-desc">ID: <code>postmortem-capstone</code> · Deliverable: Published postmortem essay & portfolio defense</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>5.3</code> <code>3.8</code> <code>10.8</code> <code>GD.20.5</code> <code>12.3</code> <code>12.2</code> <code>12.9</code></div>
</div>
</details>

<details class="unit-accordion">
<summary class="unit-summary">
  <span><strong>Module 6.7:</strong> Emerging Tech Briefing: XR, Real-Time & Multiplayer</span>
  <span class="unit-item-badge badge-assignment">ASSIGNMENT & READING</span>
</summary>
<div class="unit-items-container">
  <div class="module-block-desc">You will research spatial computing (VR/AR/XR), real-time virtual production, and networked gameplay systems.</div>
  <a href="/m/GAME-301/" class="unit-item-button">
    <div>
      <div class="unit-item-title">XR and Real-Time Production</div>
      <div class="unit-item-desc">Code: <code>GAME-301</code> · Spatial tracking, foveated rendering, and virtual production LED stages</div>
    </div>
    <span class="unit-item-badge badge-module">MODULE</span>
  </a>
  <a href="/assignments/xr-briefing/" class="unit-item-button">
    <div>
      <div class="unit-item-title">Emerging Tech Briefing</div>
      <div class="unit-item-desc">ID: <code>xr-briefing</code> · Deliverable: XR & real-time tech briefing paper</div>
    </div>
    <span class="unit-item-badge badge-assignment">ASSIGNMENT</span>
  </a>
  <div class="module-standards-row"><strong>Standards:</strong> <code>GD.20.4</code> <code>GD.20.1</code> <code>GD.17.9</code> <code>4.8</code> <code>12.1</code></div>
</div>
</details>

<div class="unit-ref-shelf">
  <div class="unit-ref-shelf-title">Unit 6 Reference Shelf (Supplemental Reading)</div>
  <div class="unit-ref-shelf-items">
    <a href="/m/MEDIA-114/" class="unit-ref-pill"><code>MEDIA-114</code> Exporting & Delivery</a>
    <a href="/m/LAW-201/" class="unit-ref-pill"><code>LAW-201</code> Contracts & Terms</a>
    <a href="/m/CAREER-202/" class="unit-ref-pill"><code>CAREER-202</code> Esports Careers</a>
    <a href="/m/PROD-207/" class="unit-ref-pill"><code>PROD-207</code> Sustainability in Production</a>
  </div>
</div>
