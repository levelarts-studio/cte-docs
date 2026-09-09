---
id: team-gdd
title: "Team Game Design Document"
entity: assignment
tier: 300
status: complete
requires: ["PROD-201"]
standards: ["GD.18.2", "16.4", "2.5"]
evidence_for: "GD.18.2"
portfolio: true
portfolio_section: "GAD2 U1"
est_time: 180
setting: lab
aliases: ["/a/team-gdd"]
---

## The task

Write the Game Design Document (GDD) for the game the studio just greenlit. This becomes the shared reference the whole team builds from for the rest of the year, and it is expected to change as the project changes.

This is a team deliverable, written together, not assembled from separate parts written alone.

**Deliverable**: Studio living GDD document (5 to 15 pages in a shared workspace) + individual portfolio reflection entries.

## Before you start

Read [The Game Design Document](/learn/production/the-game-design-document/) (`PROD-201`).

## Steps

{{% steps %}}

### Step 1 — Assign a document owner

One person, usually the producer or creative director, owns the document: keeps it organized, makes sure edits get made, and flags when it has drifted from the build.

> *Owning the document does not mean writing it alone. Every department lead contributes their sections.*

### Step 2 — Write the seven sections

As a studio, collaborate to write the seven core sections:

1. **Pitch and pillars**: The elevator pitch from the greenlit concept, plus two or three design pillars everyone can recite from memory.
2. **Target audience**: Who this game is for, specifically (pulled from the winning pitch and player taxonomy).
3. **Core loop**: A clear diagram showing what the player does, over and over.
4. **Feature list**: Every major system, each written as a specific, testable statement (e.g., *"The player can dodge with i-frames and chain a dodge into a light attack"*).
5. **Scope and non-goals**: What you are explicitly building, and an explicit list of what you are **not** building.
6. **Asset list**: A first-pass inventory of every character, prop, environment module, UI element, and audio asset the vertical slice requires.
7. **Decision log**: Start it now, even with just today's date and *"Greenlit concept: [Name]"*.

Keep the whole document to roughly **5 to 15 pages**. If a section begins running long, that is a sign it belongs in a dedicated sub-document (like an Art Bible or Technical Spec) linked from the GDD, not that the main GDD should balloon.

### Step 3 — Pressure-test the scope section

As a group, go through your feature list and ask two questions of each item:

1. **Does this serve one of our design pillars?**
2. **Can this class realistically build and polish it in the time we have?**

Anything that fails either question moves directly to the **Non-Goals** list. This is the moment to be honest, not encouraging. A disciplined feature list now is what makes April survivable.

### Step 4 — Check it against reality

Read your feature list against what you actually know about Unreal Engine 5 and your lab machines.

Flag anything that represents high technical risk (heavy physics simulations, massive open-world areas, complex multi-state AI) so it can be prototyped and tested early instead of discovering performance bottlenecks in March.

### Step 5 — Put it where the team works

Post the GDD somewhere every team member can open and edit: a shared Google Doc, Notion workspace, or project wiki. Link it directly from your team's task board.

### Step 6 — Set your update habit

As a team, agree on two working rules and write them into the document itself:
- Who is responsible for updating the document when a mechanic, rule, or asset changes
- When you will hold a standing five-minute weekly review to catch document drift early

### Step 7 — Document on your portfolio

Each team member must publish a short individual entry to their portfolio **Coursework** page using the standard write-up format:
- A link to the studio's shared living GDD
- Which specific section(s) you personally contributed to and wrote
- One design pillar or non-goal you personally pushed for, and why

{{% /steps %}}

## Submit

{{< callout type="info" >}}
**Team Submission**: The producer submits the live link to the studio's shared living GDD document, once, in Google Classroom.

**Individual Submission**: Each team member submits the link to their published Google Sites portfolio Coursework page containing their individual reflection.
{{< /callout >}}

## Rubric

| Criteria | Approaching | Proficient | Advanced |
| :--- | :--- | :--- | :--- |
| **Pitch & Pillars** | Elevator pitch is missing or vague; pillars are generic slogans | Clear elevator pitch; 2–3 specific, memorable design pillars that establish clear decision criteria | Pillars provide sharp, actionable creative direction; clearly referenced throughout all features |
| **Core Loop & Feature List** | Core loop missing or unclear; features written as vague wishes | Core loop diagrammed clearly; major gameplay systems written as concrete, testable statements | Systems breakdown is rigorous, detailing player inputs, engine responses, and feedback states |
| **Scope & Non-Goals** | Non-goals list omitted; features exceed realistic lab timeline | Explicit non-goals list recorded; features pressure-tested against team bandwidth and timeline | Aggressively scoped; proactive identification of high-risk features with defined fallback positions |
| **Asset List & Technical Reality** | Asset list is vague ("props", "enemies"); ignores hardware limits | Itemized inventory of characters, props, environment pieces, UI, and audio; realistic for UE5 lab machines | Assets categorized with reuse/modularity notes; clear technical constraints (polycounts, texture budgets) |
| **Living Document & Ownership** | Document owner unassigned; no update cadence; portfolio missing | Designated owner, shared accessible location, agreed weekly review cadence; individual portfolio reflections complete | Document setup includes an active decision log, change protocol, and mature individual reflections |

## Notes

- **This document will be wrong by October, and that is fine**: What matters is that it gets corrected instead of ignored. A GDD that drifts from the build and never gets fixed has failed even if it was well-written in September.
- **Non-goals are not a failure of ambition**: Writing down what you are **not** building is one of the most useful things a small team can do. It is the sentence you point to in March when someone wants to add multiplayer or branching narratives.
- **The asset list feeds the pipeline doc directly**: What you write here becomes the starting point for planning who builds what, so vague entries here cause confusion later. *"Enemy type"* is not useful. *"Small ranged enemy, one attack pattern, reuses the base rig"* is.
