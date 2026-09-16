---
id: PROD-204
title: "Scope and the Vertical Slice"
weight: 130
entity: module
subject: production
tier: 200
status: complete
tools: []
prereqs: ["PROD-201"]
standards: ["16.9", "GD.18.3", "5.8"]
keywords: ["scope creep", "vertical slice", "horizontal slice", "moscow method", "must have", "wont have", "scope lock", "production"]
duration: 10
video: ""
aliases: ["/m/PROD-204"]
---

## What you'll be able to do

- Explain what makes a slice vertical rather than horizontal
- Sort features using Must, Should, Could, Won't
- Say why "Won't have" is the most important category, not the weakest one
- Recognize scope creep before it sinks a schedule

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### Vertical, not horizontal

A vertical slice is a small, polished, fully playable cross-section of a game that shows what the final experience actually looks and feels like. Not a rough demo you'll clean up later. A short piece finished to the standard the whole game is meant to reach.

The name comes from the contrast with horizontal slicing: building layer by layer, like installing all the plumbing in a house before any of the walls go up. A horizontal approach gives you a fully modeled level with no gameplay, or a complete combat system with no art, at every stage along the way, until the very end, when it all finally comes together for the first time. That's risky, because you don't find out whether the pieces actually fit until it's too late to change course cheaply.

A vertical slice cuts through every layer at once, in miniature. One short section with real art, real mechanics, real UI, real audio, working together end to end. It proves the whole stack fits before you commit a whole team to scaling it up.

![Horizontal vs. Vertical Slicing](/images/production/vertical-vs-horizontal-slice.svg)
<p style="font-size: 0.85rem; opacity: 0.8; margin-top: -0.5rem; margin-bottom: 1.5rem;"><em>Horizontal slicing builds layer by layer, delaying integration until the very end. Vertical slicing builds an integrated cross-section through every discipline early, proving the playable core.</em></p>

That is exactly what your studio is building this year: not a full game, and not a set of disconnected finished pieces, but one real slice of the thing, built all the way through.

### Sorting features: MoSCoW

Every project generates more feature ideas than it can build. The standard way to sort them, used across software and game development, is the MoSCoW method: four buckets, not a numbered ranking.

- **Must have** — The slice fails without this. If even one Must is cut, the slice isn't the slice anymore.
- **Should have** — Important, genuinely valuable, but the slice still works without it.
- **Could have** — Nice if time allows. First thing cut under pressure, no argument needed.
- **Won't have** — Explicitly not happening, for this slice. Not forgotten. Decided.

The value of separating these into four labeled buckets instead of one ranked list is that it forces an explicit, binary decision on every feature: which bucket, not how important on a sliding scale. A feature that's "kind of a must, kind of a should" hasn't actually been decided yet.

### Won't have is the important one

Most teams are comfortable writing a Must-have list. The list that actually protects a schedule is **Won't have**.

Saying "we are not doing this, at least not for this slice" out loud, as a group, is harder than it sounds, because it can feel like rejecting someone's idea personally. MoSCoW gives you a structured, non-personal way to say it: the feature isn't bad, it's just not in this bucket, for this slice, right now.

Write the Won't-have list down and post it somewhere visible. It is the thing you point back to in March when someone wants to add one more system.

### Scope creep

Scope creep is what happens when a project's requirements keep growing after the scope was supposedly locked, usually a small addition at a time, each one easy to justify on its own. No single addition sinks a project. The accumulation does.

The defense is not willpower. It's the Won't-have list, checked every time a new idea shows up: does this belong in the Must-have list we already agreed on, or does it belong in Won't have, for now? A written scope makes that a five-second check instead of a group debate every single time.

### Sizing a slice for real

Vertical slices in industry commonly run one to three months for a professional team with people who work full time on nothing else. Your studio has a fraction of that: lab time only, split across other coursework, with team members learning tools while they build.

That doesn't mean the same target is out of reach, it means the Must-have list has to be genuinely small. A slice with one location, one character, a handful of mechanics, and five to ten minutes of finished gameplay is not a compromise. It's the correctly sized version of the same idea, scaled to the time and team you actually have.

## Quick Check

{{< quickcheck question="Halfway through production, someone suggests adding a second playable character 'since we're already close.' The idea is good and the team is excited about it. What should happen next?" >}}

- **A.** Add it immediately since good ideas shouldn't wait
- **B.** Check it against the Must/Should/Could/Won't list the team already agreed on
- **C.** Let whoever suggested it build it in their spare time without telling the team
- **D.** Vote on it right then, whoever has the most support wins

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> A good idea showing up mid-production is exactly what scope creep looks like from the inside, since it always feels justified in the moment. The scope document exists precisely so this gets checked against an existing decision instead of relitigated from scratch every time.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Vertical slice** — A small, fully polished, end-to-end playable cross-section demonstrating the intended visual, mechanical, and audio quality of the finished game.
- **Horizontal slice** — Building a game layer by layer across all content (e.g., all levels blocked out before any mechanics or art are integrated), delaying integration until late in production.
- **MoSCoW method** — A prioritization framework dividing feature scope into four strict categories: Must have, Should have, Could have, and Won't have.
- **Scope creep** — The gradual, uncontrolled expansion of project requirements beyond original constraints, typically through small, unbudgeted additions.
- **Scope lock** — The milestone agreement where a team finalizes and freezes its feature list, committing to build only what is documented.

## Next

- [Scope & Vertical Slice Definition](/assignments/scope-and-slice/) (`scope-and-slice`)
- [Task Boards and Sprints](/m/PROD-203/) (`PROD-203`)
