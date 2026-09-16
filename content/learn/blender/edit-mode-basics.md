---
id: BLND-104
title: "Edit Mode Basics"
weight: 40
entity: module
subject: blender
tier: 100
status: complete
tools: ["blender"]
prereqs: ["BLND-103"]
standards: ["GD.17.4", "4.3"]
keywords: ["extrude", "inset", "bevel", "loop cut", "merge by distance", "non-destructive"]
duration: 10
video: ""
aliases: ["/m/BLND-104"]
---

## What you'll be able to do

- Extrude, inset, and bevel geometry
- Add loop cuts to control where a surface can bend or stay sharp
- Merge vertices cleanly, without leaving holes
- Choose the right tool for a hard surface shape

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### You already know the moves

Last module you built props from whole primitives, moved and scaled, nothing cut. Edit mode is where you start reshaping the mesh itself: pushing out new geometry, cutting it, and merging it back together.

Same three keys as before: **1 / 2 / 3** for vertex, edge, face select. Everything below works on whichever you have selected.

### Extrude

**E** pulls a new face out from whatever you've selected, keeping it connected to the mesh.

Extrude a face and you get a rectangular box growing off a surface: a vent, a bolt head, a raised panel. Extrude an edge and you get a new face bridging the old position to the new one. It is the single most useful tool for building hard surface shapes, because almost every mechanical form is extrusions stacked on each other.

Like Move, Extrude respects axis locks. `E`, `Z` extrudes straight up regardless of your camera angle.

### Inset

**I** shrinks a new face inward from the one you've selected, leaving a border of geometry around it.

This is how panel lines get made. Select a face, inset it, and you have a smaller face sitting inside a frame. Extrude that inset face down slightly and you have a recessed panel; up, and you have a raised one. Most sci-fi and mechanical detailing is inset and extrude, repeated.

### Loop cuts

**Ctrl + R** adds a ring of edges running around a shape, following its existing topology. Move your mouse to preview where the cut lands, scroll to add more than one at once, click to place, then either drag to slide it or right-click to leave it centered.

Loop cuts do not change a shape's silhouette. What they do is add control: more edges to select, move, or use to keep a bevel from spreading too far. A cylinder with no loop cuts can only bend at its two end caps. Add a loop cut in the middle and it can bend there too.

### Bevel: tool and modifier

Two different things share the name, and mixing them up costs time.

**The Bevel tool**, `Ctrl + B`, works on a selection in edit mode. Confirm it, and the new geometry is baked permanently into the mesh. Move your mouse to set the width, scroll to add segments.

**The Bevel modifier** sits in the modifier stack and does the same visual job, but non-destructively. Adjust its width or segment count any time, or delete it, without the underlying mesh ever changing. That flexibility is why studio pipelines lean on the modifier for production work: you can keep iterating without starting over.

**Rule of thumb:** use the modifier while a shape might still change. Use the tool only once you are certain and want to hand-edit the result afterward. Everything in this course defaults to the modifier unless a step says otherwise, because iteration is the whole point of a block-out.

Real hard surface objects are almost never perfectly sharp. A slightly beveled edge catches light the way a real manufactured part does; a perfectly sharp edge reads as digital and flat. A small bevel on every visible hard edge is one of the fastest ways to make a block-out look intentional.

### Merging vertices

**M** opens the merge menu: **At Center**, **At Last**, **At Cursor**, or **By Distance**.

**By Distance** is the one you'll use constantly. It collapses any vertices within a set range of each other into one, which is exactly what you need after moving parts of a mesh close together and ending up with doubles sitting on top of each other. Unnoticed doubled vertices are a common cause of shading errors and export problems later, so it's worth running a **By Distance** merge on a finished mesh as a habit, not just when something looks wrong.

### Choosing the right tool

| You want to... | Use |
|---|---|
| Add a new raised or recessed shape | Extrude |
| Add a panel line or frame | Inset, then Extrude |
| Control where a shape can bend | Loop Cut |
| Soften an edge, might still change it | Bevel modifier |
| Soften an edge, final and certain | Bevel tool |
| Clean up doubled vertices | Merge by Distance |

## Quick Check

{{< quickcheck question="You bevel an edge with Ctrl+B, then realize the width is wrong. What's the easiest fix?" >}}

- **A.** Undo, then redo the bevel with the correct width
- **B.** Select the new faces and delete them
- **C.** Nothing can be changed once a bevel tool is confirmed
- **D.** Switch to object mode and scale the whole object

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>A.</strong> The Bevel tool bakes geometry permanently, so there's no live width to adjust afterward. The width has to be redone from scratch, which is exactly the case for reaching for the Bevel modifier instead whenever a shape might still change.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Extrude** (`E`) — Extends new faces, edges, or vertices outward or inward from existing geometry while maintaining mesh connectivity.
- **Inset** (`I`) — Offsets and scales a new face inward from the perimeter of the selected face, creating a bordering frame.
- **Loop Cut** (`Ctrl + R`) — Inserts a continuous ring of edges around a mesh along quad topology, adding local resolution and control.
- **Bevel Tool** (`Ctrl + B`) — Manually rounds or chamfers selected edges in Edit Mode, baking the newly created polygons permanently into the base mesh.
- **Bevel Modifier** — Applies parametric edge rounding or chamfering across an object non-destructively in the modifier stack.
- **Merge by Distance** (`M` → *By Distance*) — Automatically fuses overlapping or nearby vertices within a specified tolerance threshold.
- **Non-destructive** — A modeling workflow where geometry changes remain procedural and live in a stack, leaving original base geometry intact.

## Next

- [Modifiers Introduction](/m/BLND-105/) (`BLND-105`)
- [Hard Surface Prop 1: Blockout](/assignments/hard-surface-prop/) (`hard-surface-prop`)
