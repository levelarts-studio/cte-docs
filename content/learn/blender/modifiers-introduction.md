---
id: BLND-105
title: "Modifiers Introduction"
weight: 60
entity: module
subject: blender
tier: 100
status: complete
tools: ["blender"]
prereqs: ["BLND-104"]
standards: ["4.3", "GD.17.4"]
keywords: ["mirror", "subdivision surface", "subd", "boolean", "solidify", "modifier", "non-destructive"]
duration: 10
video: ""
aliases: ["/m/BLND-105"]
---

## What you'll be able to do

- Explain what a modifier is and why it's non-destructive
- Use Mirror to build symmetric shapes from half the geometry
- Use Subdivision Surface to smooth a low-poly base
- Use Solidify and Boolean for thickness and combining shapes

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### What a modifier actually is

A modifier is an operation that happens on top of your mesh without changing the mesh itself. The underlying vertices stay exactly as you placed them; the modifier recalculates its effect live, every time you edit. Turn it off and your original geometry is sitting there unchanged.

That single property, **non-destructive**, is why modifiers matter. Committing to a change with a regular edit tool means starting over if you're wrong. A modifier means changing a number instead.

Modifiers live in the wrench-icon tab of the Properties panel, stack in order from top to bottom, and can be reordered by dragging.

### Mirror

Model half a symmetric object, add a **Mirror** modifier, and Blender builds the other half live. Move a vertex on one side and the mirrored vertex updates instantly on the other.

This is standard practice for anything roughly symmetric: most props, most characters, most vehicles. Model half, mirror it, and you've cut your modeling time and guaranteed the two sides actually match, which is nearly impossible by hand.

The modifier mirrors across an axis of the object's **origin**, so origin placement matters here too. Set the origin on the center line before adding the modifier, or the mirror will happen in the wrong place.

### Subdivision Surface

**Subdivision Surface** (often shortened to "SubD" or "Subsurf") smooths a low-poly cage into a much denser, rounder surface, the same way a low-resolution blocky shape can preview as a smooth one.

This is how a lot of hard surface and character work actually gets built: model a simple, low-poly cage, and let Subdivision Surface preview the smooth final result without you ever having to place the smoothing geometry by hand. Edge loops placed close together on the cage keep an area sharp where the surface would otherwise round off too much, which is the main technique for controlling where a subdivided shape stays crisp.

Subdivision Surface adds geometry only for preview and render by default; your actual mesh stays light until you choose to apply it.

### Solidify

Model a single flat surface, like a piece of sheet metal or a leaf, and it has no thickness; view it from the edge and it disappears. **Solidify** gives it thickness by generating a second surface offset from the first, turning a flat plane into a real, thin, three-dimensional shell.

### Boolean

**Boolean** combines two separate objects using set operations:

- **Union** merges them into one shape
- **Difference** cuts one shape out of another, like drilling a hole
- **Intersect** keeps only the overlapping volume

Difference is the one you'll reach for constantly: model a cube, model a cylinder positioned where you want a hole, set the cylinder as a Boolean Difference on the cube, and the cylinder cuts a clean hole through it.

Boolean is powerful and also the modifier most likely to produce messy geometry: overlapping faces, ugly triangulation at the cut line, results that look correct in the viewport but are broken underneath. Check the result in edit mode after applying, not just how it looks shaded.

### Order matters

Modifiers process top to bottom, and the same two modifiers in a different order can produce different results. Mirror, then Subdivision Surface smooths across the seam correctly. Subdivision Surface, then Mirror can leave a visible crease down the centerline. When something looks wrong, check the stack order before you check anything else.

### When to apply

A modifier stays live and editable until you **apply** it, which bakes its effect permanently into the mesh, same tradeoff as the Bevel tool versus the Bevel modifier. Keep modifiers live for as long as a shape might change. Apply only when you're finished with that part, and usually right before export, since some destinations expect the final geometry rather than a stack of instructions.

## Quick Check

{{< quickcheck question="A model built with Mirror looks correct in the viewport, but after the modifier is applied, one vertex on the seam is doubled and causes a shading error. What is the most likely cause?" >}}

- **A.** Subdivision Surface was added after Mirror
- **B.** The object's origin was not centered on the mirror axis before modeling
- **C.** Boolean Difference was used instead of Union
- **D.** The mesh had too few loop cuts

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> Mirror reflects across the object's origin. If the centerline geometry was not built exactly on that axis, the two halves don't meet cleanly and a doubled or gapped vertex shows up right at the seam once applied.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Modifier** — A procedural operation applied non-destructively to an object's geometry stack in Blender.
- **Non-destructive** — An editing system where calculations happen on the fly without overwriting underlying vertex data.
- **Mirror** — Generates a duplicate half of a mesh reflected across an axis anchored to the object's origin.
- **Subdivision Surface (SubD)** — Subdivides and smooths low-polygon cages for high-resolution shape preview and curvature.
- **Solidify** — Extrudes a flat surface or shell to give it measurable physical thickness.
- **Boolean** — Employs constructive solid geometry (Union, Difference, Intersect) between two meshes.
- **Apply** — Converts a live modifier's procedural effect into permanent, editable vertices on the mesh.

## Next

- [Hard Surface Prop 1: Blockout](/assignments/hard-surface-prop/) (`hard-surface-prop`)
- [Topology and Edge Flow](/m/BLND-201/) (`BLND-201`)
