---
id: BLND-103
title: "Primitive Modeling"
weight: 30
entity: module
subject: blender
tier: 100
status: complete
tools: ["blender"]
prereqs: ["BLND-102"]
standards: ["GD.17.4", "AV.17.8"]
keywords: ["primitive", "blockout", "silhouette", "proportion", "real-world scale", "cube", "cylinder", "sphere"]
duration: 10
video: ""
aliases: ["/m/BLND-103"]
---

## What you'll be able to do

- Block out an object's silhouette from primitives before adding detail
- Judge proportion against reference rather than by eye alone
- Keep an object's scale meaningful instead of arbitrary
- Recognize when a blockout is ready for the next stage

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### Silhouette before detail

Every object you'll model, however complex it ends up, starts as a blockout: a rough arrangement of primitives that nails the big proportions and reads correctly as a silhouette, with zero small detail.

This matters because detail hides proportion problems instead of fixing them. A prop with a slightly wrong overall shape looks wrong no matter how much detail you add on top. A prop with correct proportions and zero detail already looks like the thing it is. Fix the big shape first, always.

### Judging proportion

"By eye" is a trap. Human perception is bad at absolute size and decent at comparison, so the useful question is never "is this the right size," it's "is this the right size compared to that."

Hold your reference beside your viewport and ask specific comparison questions: is the handle a third of the total height, or a quarter? Is the body twice as wide as it is deep, or closer to equal? Answering those specific ratio questions, one at a time, gets you much closer than staring at the whole object and guessing.

### Scale is not arbitrary

An object's real-world size is part of its design, and Blender's default unit is the meter, so building at a believable scale from the start saves problems later. A mug modeled at 4 units tall instead of roughly 0.1m tall (about 4 inches) will cause confusing problems the moment it needs to interact with anything else, including a hand, a table, or a game character.

Check your object's real dimensions in the sidebar (N panel → Item tab) against what the object should actually measure, and adjust early rather than guessing and fixing it after detail work is already in.

### Knowing when to move on

A blockout is ready for the next stage when:

- The silhouette reads correctly from multiple angles
- The proportions match your reference within a reasonable margin
- The scale is realistic
- You're using the fewest primitives that still get the shape across

If you're not sure whether a shape is "detailed enough" yet, it isn't your call to make from vibes: go back to your reference and check a specific ratio you haven't confirmed yet.

## Quick Check

{{< quickcheck question="A student's blockout of a coffee mug looks proportionally correct in the viewport, but when they check the sidebar, it's 3 meters tall. What's the actual problem, even though it \"looks right\"?" >}}

- **A.** Nothing, if the proportions look correct the scale doesn't matter yet
- **B.** The object's real-world scale is wrong and will cause problems the moment it needs to interact with anything built at a normal scale
- **C.** The mesh needs more geometry to look correct at that size
- **D.** The material will look wrong at that scale

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> Looking correct in isolation doesn't mean the scale is usable. A 3-meter mug will be wildly incompatible with anything else in a scene built at real-world scale, and that mismatch gets much harder to fix once other objects and detail depend on it.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Blockout**
- **Silhouette**
- **Proportion**
- **Real-world scale**

## Next

- [Saving, Packing, and Exporting](/m/BLND-107/) — configure transforms and export cleanly
- [Blender First Model: Hero Prop](/assignments/blender-first-model/) — model and export your first complete hero prop
- [Primitive Form Studies](/assignments/form-studies/) — block out three props using only transformed primitives
