---
id: UE-206
title: "Level Blockout Workflow"
weight: 50
entity: module
subject: unreal
tier: 200
status: complete
tools: []
prereqs: []
standards: ["GD.17.6", "GD.18.4"]
keywords: ["greybox", "geometry brushes", "modeling mode", "blockout", "scale reference", "critical path", "pacing", "text actor"]
duration: 10
video: ""
aliases: ["/m/UE-206"]
---

## What you'll be able to do

- Set a player-scale reference before building anything else
- Label spaces by function instead of relying on memory
- Pace a level as a rhythm of tension and rest, not a straight line
- Playtest a blockout honestly, before any art exists

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### Scale first, always

Before placing a single wall, put a player-scale reference in your level: a capsule or simple character mesh at 180cm tall, the standard human reference, and a door opening at 100cm wide. Keep both visible in the scene the whole time you're building.

Every other dimension gets judged against these two numbers. A hallway that looks fine in an empty viewport can read as cramped or oversized the moment a player-sized shape walks through it, and you won't catch that mistake until it's expensive to fix unless the reference is sitting there the entire time.

Unreal works in centimeters: 100cm equals 1 meter. A typical standing human is about 180cm. A standard doorway is about 100cm wide. Build everything relative to those two numbers and your level will feel consistent, even before any art exists.

### Label every space

As you block out each area, drop a text actor naming what it's for: `COMBAT`, `PUZZLE`, `SAFE ZONE`, `REWARD`. This sounds unnecessary and is not. The moment someone other than you plays the blockout, labels are the difference between "I can tell what this space wants me to do" and total confusion. Even playing it yourself a week later, you'll be glad the label is there.

### Pacing is a rhythm, not a straight line

A level that's intense the whole way through exhausts a player. A level that's slow the whole way through bores one. Good pacing alternates: build tension, release it, build it again. A short rest after a demanding stretch is what makes the next demanding stretch land.

Think in terms of beats: set up what's expected, deliver a challenge or moment that pays it off, then give a brief lull before the next beat starts. Your five-minute slice doesn't need a complicated structure, but it does need at least one real shift in intensity. Five minutes of flat, identical pacing feels longer than five minutes with one deliberate peak and one deliberate rest.

### Building order

Work roughly in this sequence:

1. **Place your scale references** and leave them in the scene.
2. **Block the critical path** — the route a player has to take to get through the slice at all.
3. **Block the spaces off that path** — combat arenas, optional areas, anything that branches.
4. **Label everything.**
5. **Walk it yourself**, in first or third person, at actual player speed. Not flying around in the editor.

Simple shapes only at this stage: cubes for walls, cylinders for pillars, ramps for elevation changes. Nothing textured, nothing detailed. The entire point of a blockout is answering gameplay questions cheaply, before anyone spends real time on art that might have to be redone if the space doesn't work.

### Playtest the grey version

A blockout is meant to be played, not just looked at. Walk your own level repeatedly as you build. Specific things to check:

- **Can the player actually get lost**, in a way you didn't intend?
- **Does a combat space give the player enough room to move**, given the 180cm reference you placed?
- **Does the critical path read clearly**, or does it take real effort to figure out where to go?
- **Is there an actual shift in pacing somewhere**, or does the whole slice feel the same the entire way through?

Fixing a pacing or scale problem now, in grey boxes, costs you an afternoon. Fixing it after your team has built and placed finished art costs considerably more, because now finished work has to move or get rebuilt around the correction.

## Quick Check

{{< quickcheck question="A hallway in a student's level looks fine from the editor's default fly-camera view, but feels cramped the moment they walk through it with their character. What's the most likely explanation?" >}}

- **A.** The textures haven't been applied yet
- **B.** The hallway was built without a player-scale reference in the scene to judge against
- **C.** The lighting hasn't been baked
- **D.** The level needs more detail geometry

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> The fly-camera view doesn't give you an honest read on scale, because you're not experiencing the space the way a player at 180cm actually would. A scale reference left in the scene the whole time is what catches this before it becomes a real problem.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Blockout / greybox** — A preliminary playable level layout constructed entirely with simple geometric shapes (cubes, cylinders, ramps) without textures or final art to test scale, movement, and mechanics cheaply.
- **Scale reference** — Standardized reference actors (such as a 180cm character capsule and 100cm doorway) kept visible in the scene while building to evaluate spatial dimensions accurately against player perspective.
- **Critical path** — The primary, mandatory route a player must traverse to progress from the beginning to the completion of the level or vertical slice.
- **Pacing** — The deliberate rhythm and tempo of gameplay intensity, alternating between demanding moments of tension or challenge and brief lulls of rest.
- **Text actor label** — In-editor 3D text placed directly in the scene to mark each area's intended design function (e.g., `COMBAT`, `PUZZLE`, `SAFE ZONE`, `REWARD`) for clear playtester and team communication.

## Next

- [Greybox the Vertical Slice](/assignments/greybox-slice/) (`greybox-slice`) — construct the full playable layout of your studio's slice using blockout geometry
- [Greybox a Level from a Floor Plan](/assignments/blockout-level/) (`blockout-level`) — translate a 2D floor plan into a playable blockout layout in Unreal Engine
