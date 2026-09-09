---
id: PROD-201
title: "The Game Design Document"
weight: 40
entity: module
subject: production
tier: 200
status: complete
tools: []
prereqs: []
standards: ["GD.18.2", "16.4"]
keywords: ["gdd", "design doc", "game bible", "living document", "design pillars", "core loop", "feature list", "scope", "non-goals", "decision log", "tdd"]
duration: 10
video: ""
aliases: ["/m/PROD-201"]
---

## What you'll be able to do

- Explain what a GDD is for and who actually reads it
- Name the sections a lean GDD needs and what goes in each
- Write a feature as a testable statement instead of a vague idea
- Keep a GDD alive instead of writing it once and abandoning it

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### Forget the hundred-page bible

The old idea of a GDD is a massive document written before anything is built, covering every system in exhaustive detail. That model is functionally dead in modern practice. Nobody on a working team reads a hundred pages, and the moment the build changes, the document is already wrong.

What replaced it: a lean, living GDD. Short enough that people actually keep it updated, structured enough to keep a team aligned, and disciplined enough to stop scope creep before it kills the project. For a small team, that means roughly 5 to 15 focused pages, not fifty.

The real test of a GDD is not how thorough it is. It is whether the team is still working in it, or whether it quietly became a document nobody opens.

### What it's actually for

A GDD is the shared record of what the game is and how it works: the pitch, the pillars, the core loop, the major features, the scope, and the decisions that got made along the way. Its job is to answer disagreements before they happen, so two people don't build two different games without realizing it.

### The sections that matter for a small team

1. **Pitch and pillars.** Your elevator pitch, plus two or three design pillars: short phrases that describe the core experience and get checked against every decision. *Hades* used pillars like "fast, fluid combat" and "narrative depth through repeated runs." When someone proposes a feature, you ask whether it serves a pillar. If it doesn't, that's a real reason to cut it.
2. **Target audience.** Who this is for, specifically. Covered in [Genres and Player Profiles](/learn/gamedesign/genres-and-player-profiles/) (`GAME-103`).
3. **Core loop.** What the player does, over and over. This is usually a diagram, not a paragraph: some things do not read well in prose.
4. **Feature list.** Every major system, written as a short, specific statement rather than a vague wish. Not "combat should feel good," but "the player can dodge with i-frames and chain a dodge into a light attack."
5. **Scope and non-goals.** What you are explicitly not building. This section stops arguments in March. Writing "no multiplayer" down in September is what lets you say no to it later without a fight.
6. **Asset list.** What needs to be made: characters, props, environments, UI, sound. This is the bridge between the design document and the production schedule, and it is the part your team will actually use week to week.
7. **Decision log.** A running list of major calls and why they were made. When someone asks "wait, didn't we already decide this," the answer lives here instead of in someone's memory.

That is seven sections. A one-page GDD, useful for a jam or a very early pitch, is really just the first two of these compressed onto a single page.

### Keep it alive

A GDD that does not match the actual build is worse than no GDD, because it actively misleads people. Three habits keep it honest:

- **Update it the day something changes.** Cut a feature, add a mechanic, change a rule: update the doc the same day. Five minutes now saves hours of confusion later.
- **Put it where the team already works.** A GDD in a tool nobody opens will rot no matter how well it's written.
- **Review it on a schedule, not just when something breaks.** Even a five-minute check-in each week catches drift early.

### Technical constraints belong in the same conversation

A GDD says what the game is. A related document, sometimes called a **technical design document (TDD)**, says how it gets built: engine settings, performance targets, what the hardware can actually support. For a small student team these often live in the same place.

When you write a feature, ask whether it's realistic for the engine and the machines you're using. "The player can destroy any object in the environment" is a design idea. Whether Unreal on a lab machine can handle that is a technical constraint, and the two have to agree.

## Quick Check

{{< quickcheck question="A team wrote a 40-page GDD in September covering every system in detail. By November nobody has opened it in weeks, and the actual game has drifted from what it describes. What went wrong?" >}}

- **A.** The GDD needed more sections
- **B.** It was too long to maintain and stopped being updated as the game changed
- **C.** GDDs should only be written by the lead designer
- **D.** Nothing, this is normal and the document should be rewritten at the end

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> A long document written up front and never revisited is the exact failure mode a lean, living GDD is meant to avoid. The fix is not more detail, it's less, updated more often.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Living document**
- **Design pillar**
- **Core loop**
- **Feature**
- **Scope**
- **Non-goal**
- **Decision log**
- **Technical design document (TDD)**

## Next

- [Team Game Design Document](/assignments/team-gdd/) — collaborate as a studio to write your living GDD
- [Scope and the Vertical Slice](/learn/production/scope-and-the-vertical-slice/) (`PROD-204`) — define boundaries and cut feature bloat
