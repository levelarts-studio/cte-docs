---
id: GAME-107
title: "Narrative in Games"
weight: 130
entity: module
subject: gamedesign
tier: 100
status: complete
tools: []
prereqs: ["GAME-101"]
standards: ["GD.17.3", "15.1", "15.3"]
keywords: ["narrative design", "embedded narrative", "emergent narrative", "audio logs", "environmental text", "branching narrative", "diegetic narrative", "ludonarrative consistency", "authentic representation"]
duration: 12
video: ""
aliases: ["/m/GAME-107", "/m/game-107", "/game-107"]
---

## What you'll be able to do

- Differentiate narrative design (authoring systems and delivery) from traditional linear scriptwriting
- Contrast embedded narrative with emergent narrative and balance both in a game space
- Author concise, diegetic audio logs and environmental text adhering to modern industry constraints
- Structure player agency using the sustainable "branch-and-bottleneck" narrative architecture
- Develop authentic, multidimensional factions that avoid monolithic tropes and cultural caricatures

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### Narrative design is not screenwriting

Many writers enter game development imagining they will write fifty-page scripts filled with cinematic dialogue and dramatic cutscenes. In modern game production, that role is a fraction of the process.

**Game writing** is the craft of writing words: dialogue scripts, quest prompts, menu text, and item descriptions.

**Narrative design** is the discipline of shaping *how the player experiences the story through gameplay mechanics, level architecture, player choices, and engine systems*.

In a film or novel, the audience sits outside the story watching events unfold. In a video game, **the player's agency is the engine that drives the narrative forward**. If a player stops pressing forward on the thumbstick, the story halts. Therefore, a narrative designer must collaborate constantly with systems designers, level designers, and audio programmers to weave storytelling directly into the player's hands.

---

### The two core pillars: Embedded vs. emergent narrative

Game narrative operates across two distinct modes identified by game scholars Katie Salen and Eric Zimmerman:

```
                    ┌────────────────────────────────────────────────────────┐
                    │                   GAMEPLAY EXPERIENCE                  │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                     ┌──────────────────────────┴──────────────────────────┐
                     ▼                                                     ▼
        ┌─────────────────────────┐                           ┌─────────────────────────┐
        │   EMBEDDED NARRATIVE    │                           │   EMERGENT NARRATIVE    │
        │   (Pre-authored story)  │                           │   (Player-driven story) │
        ├─────────────────────────┤                           ├─────────────────────────┤
        │ • Scripted cutscenes    │                           │ • Unpredictable AI bots │
        │ • Audio logs & radios   │                           │ • Physics chain events  │
        │ • Written terminal lore │                           │ • Clutch 1 HP escapes   │
        │ • Environmental set-ups │                           │ • Self-directed routes  │
        └─────────────────────────┘                           └─────────────────────────┘
```

#### 1. Embedded narrative (The author's hand)
Embedded narrative consists of pre-authored, fixed story content crafted deliberately by developers and placed into the game world for players to discover or trigger.
- **Examples**: Cutscenes in *The Last of Us*, audio logs in *BioShock*, lore plaques in *Dark Souls*, linear dialogue trees in *Mass Effect*.
- **Strengths**: Emotional precision, thematic depth, character development, and carefully choreographed pacing.
- **Vulnerabilities**: If overused, it strips player control. It also risks **ludonarrative dissonance** — when the story told in the cutscene directly contradicts what the player does during gameplay (for example, a protagonist who expresses horror at violence in dialogue, but casually eliminates hundreds of henchmen five seconds later).

#### 2. Emergent narrative (The player's journey)
Emergent narrative arises organically from the dynamic interaction between game systems, player choices, physics simulations, and AI behaviors.
- **Examples**: The unscripted panic of surviving a swarm in *Left 4 Dead* with zero ammunition, building a precarious fortress in *Minecraft*, accidentally detonating a fuel barrel that launches an enemy into a hazard in *Dishonored*.
- **Strengths**: Unmatched player investment. When players tell their friends about a game, they rarely recount the writer's dialogue; they say, *"Let me tell you what happened to me last night in Sector 4."*
- **Vulnerabilities**: Developers cannot script emotional climaxes with precision. It requires robust, interconnected mechanics to work without feeling flat.

#### The industry sweet spot
The most memorable games use embedded narrative as a **scaffolding**: setting up clear stakes, evocative factions, and emotional motivation, while designing spaces that leave generous breathing room for emergent player drama to erupt.

---

### Diegetic narrative tools: Audio logs, terminals, and environmental text

When games avoid taking control away from the player with cutscenes, they rely on **diegetic narrative tools** — storytelling devices that exist physically inside the game world.

#### The rise and fall of the "Audio Log"
Pioneered by games like *System Shock* and perfected by *BioShock*, audio logs became the default storytelling tool in the 2000s and 2010s because they solved a major production challenge: they delivered high-quality voice acting without requiring expensive 3D facial capture, and allowed the player to keep walking.

However, modern players and critics have grown fatigued by poorly integrated audio logs. Who records their intimate personal secrets onto a tape recorder and leaves it on a sewer crate next to an ammo box?

To design modern, believable audio logs:
1. **The 15-to-25 Second Rule**: Audio logs must be punchy, urgent, and focused. If a log exceeds 30 seconds, players will either tune it out or become frustrated standing in an empty hallway waiting for it to finish.
2. **Contextual Verisimilitude**: Provide a believable in-world reason for the recording: an emergency dispatcher call, a military black-box cockpit recording, a shift supervisor's voice memo reprimanding an employee, or a radio transmission interception.
3. **Non-blocking / Spatial Playback**: In engine (Unreal Engine 5), configure audio logs to play over a radio channel or 3D spatialized speaker so the player can continue parkouring or exploring while listening. If combat erupts, duck the log's volume or queue a pause rather than allowing gunfire to swallow critical dialogue.

#### Environmental text and graphic design
Signage, warning placards, transit maps, and street graffiti are among the most cost-effective worldbuilding tools in 3D production:
- **Official Signage**: Reflects the governing authority or corporate power (rigid sans-serif typography, high-contrast hazard stripes, formal legal warnings, branded logos).
- **Subversive Graffiti**: Reflects citizen resistance, panic, or survival tips (hand-sprayed stencils, jagged lettering, scrawled directional arrows, crossed-out propaganda).

A clean corporate poster stating *"Report Unsanctioned Biometric Scans to Security"* with a red spray-painted *"THEY ARE LYING"* scrawled across it does more narrative work than three paragraphs of text in a pause menu.

---

### Branching narratives and the "Branch-and-Bottleneck" (GD.17.3)

Standard `GD.17.3` asks designers to give players agency over narrative outcomes. However, true open branching — where every choice creates two completely separate storylines — quickly becomes impossible for a small team to build:

```
Exponential Branching (Production Nightmare):
Choice 1 ──► 2 paths ──► Choice 2 ──► 4 paths ──► Choice 3 ──► 8 unique levels to build!
```

To deliver meaningful choice without exploding scope, the industry uses **Branch-and-Bottleneck** architecture:

```
            ┌── Route A (Sneak through maintenance vents, find worker diary) ──┐
[Start] ──► │                                                                  ├──► [Bottleneck: Security Hub]
            └── Route B (Overload generator, trigger alarms, hack door) ────────┘
```

1. **The Branch**: The player faces a choice (e.g., divert power to the transit tram vs. override the cryo-vault security). Each choice yields distinct gameplay challenges, unique lore clues, or different NPC reactions.
2. **The Bottleneck**: Both paths eventually reconvene at a shared major milestone or physical transition point (e.g., the elevator to the surface).
3. **The Consequence**: While the physical path reconvenes, the game's system state remembers the choice: an NPC references the decision, a faction's hostility changes, or an alternate weapon variant unlocks.

The player feels their choice had genuine weight, but the art and engineering teams only have to build one master level pipeline.

---

### Authentic representation and avoiding stereotypes (Standard 15.3)

Fictional worldbuilding often mirrors real-world human history, social structures, and cultural identities. Standard `15.3` emphasizes creating authentic representation of diverse communities and viewpoints while actively eliminating stereotypes.

When authoring game factions and communities:
- **Avoid the "Monolithic Culture" Trap**: No culture in human history has ever been monolithic. If every member of your rebel faction is an aggressive, hot-headed brawler, or every member of your tech syndicate is a cold, emotionless cyborg, you have written caricatures rather than people. Give factions internal dissent, varied moral compasses, differing age groups, and competing philosophical factions within their own ranks.
- **Ground Motivations in Real Needs**: Villains and rival factions should not exist merely to be "evil." Give them grounded, recognizable motivations: scarce water resources, historical generational trauma, conflicting economic survival pressures, or fear of external annihilation.
- **Respect Cultural Source Material**: If your fictional civilization draws inspiration from real-world cultural aesthetics (e.g., Mesoamerican architecture, Polynesian navigation, or West African textiles), research the cultural context deeply. Integrate those influences with respect and nuance rather than treating them as superficial exotic decoration.

---

## Try it

{{< quickcheck question="A student narrative designer writes a 4-minute audio log containing a character explaining the political history of the last fifty years. When the player picks it up in Unreal Engine, all player movement is locked until the audio clip finishes playing. What is the primary design flaw here?" >}}

- **A.** Audio logs must always be voiced by professional actors from the Screen Actors Guild.
- **B.** It treats interactive game narrative like passive cinema, destroys gameplay flow with an excessive duration, and locks player agency for a text-heavy lore dump.
- **C.** 4 minutes is too short; real RPG audio logs should be at least ten minutes long.
- **D.** Narrative designers are not permitted to use audio logs in Unreal Engine 5.

<details>
<summary>Show answer</summary>

**B.** Video games are an interactive medium. Locking a player's movement for four minutes while forcing them to listen to a monologue breaks pacing and causes immediate frustration. Modern best practice dictates breaking that information into short, 15–25 second contextual audio bites that play while the player remains in control, while trusting environmental clues and visual architecture to convey the world's history naturally.

</details>
{{< /quickcheck >}}

---

## Terms

- **Narrative Design**: The craft of structuring how a story is experienced through gameplay mechanics, player agency, level environments, and systems.
- **Embedded Narrative**: Pre-authored story content (dialogue, cutscenes, scripted events, written lore) deliberately placed into the game by creators.
- **Emergent Narrative**: Storylines and moments that arise unpredictably through the systemic interaction of gameplay rules, physics, AI, and player choices.
- **Ludonarrative Dissonance**: A conflict between what a game's story says through cutscenes/dialogue and what the player actually does during gameplay mechanics.
- **Diegetic**: Elements that exist directly inside the fictional game world and can be perceived by the characters within that world (e.g., an in-world radio vs. background orchestral score).
- **Branch-and-Bottleneck**: A narrative branching technique that offers meaningful local choices before funneling back into shared major story beats to manage production scope.
- **Monolithic Culture**: An oversimplified, stereotypical depiction where every member of a group or faction shares identical beliefs, personalities, and behaviors.

---

## Next

- [Worldbuilding and Environmental Storytelling](/m/GAME-205/) (`GAME-205`) — discover how architectural styles, palimpsest decay, and set dressing turn spaces into visual lore
- [World Bible & Environmental Storytelling](/assignments/world-bible/) — collaborate as a studio to write your official World Bible document
- [Team Game Design Document](/assignments/team-gdd/) (`team-gdd`) — ensure your world lore aligns with your project's living GDD and core gameplay loop
