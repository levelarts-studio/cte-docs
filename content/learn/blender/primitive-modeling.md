---
id: BLND-103
title: "Primitive Modeling"
weight: 30
entity: module
subject: blender
tier: 100
status: draft
tools: ["blender"]
prereqs: ["BLND-102"]
standards: ["GD.17.4", "AV.17.8"]
keywords: ["primitive", "cube", "cylinder", "sphere", "cone", "torus", "blocking", "block-out", "adjust last operation", "f9", "vertex count", "proportion", "silhouette", "snapping"]
duration: 10
video: ""
aliases: ["/m/BLND-103"]
---

## What you'll be able to do

- Add and configure the mesh primitives
- Set segment and vertex counts at creation, when it still matters
- Judge proportion against reference
- Explain why silhouette decides whether a prop reads

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### The primitives

**Shift + A → Mesh** adds a starting shape. The ones you will use constantly:

| Primitive | Good for |
|---|---|
| **Cube** | Boxes, buildings, anything with flat faces |
| **Cylinder** | Cans, poles, barrels, limbs, wheels |
| **UV Sphere** | Heads, balls, domes |
| **Cone** | Tips, spikes, funnels |
| **Plane** | Ground, walls, flat panels |
| **Torus** | Rings, tires, handles |

**Ico Sphere** is a sphere built from triangles instead of rings. It deforms more evenly, but UV Sphere is easier to unwrap and is the usual choice for props.

### Set the count at creation

When you add a primitive, a small **Add Cylinder** panel appears in the bottom-left corner. Click it, or press **F9**, and you get options: vertices, radius, depth, segments, rings.

This matters because **it only works right after you add the object.** Click somewhere else and the panel is gone. Changing a cylinder from 32 sides to 12 later means deleting it and starting over.

A default cylinder has 32 sides. For a small background prop that is often more than you need. Fewer sides means fewer triangles, and in a game those add up fast.

### Proportion before detail

The first pass on any model is a **block-out**: the object described in a handful of simple shapes with correct proportions and nothing else.

The temptation is to start adding detail early. Resist it. A prop with beautiful bolts and wrong proportions looks wrong. A prop with correct proportions and no detail already looks like the thing it is.

Measure against reference. Not "the lantern is tall" but "the lantern is about twice as tall as it is wide, and the handle is about a third of the total height."

### Silhouette decides everything

Fill any well-designed prop in with flat black and you can still tell what it is.

That matters because of how players see. A player identifies objects in a fraction of a second, at distance, often while moving, often in bad lighting. The outline does that work. Texture and detail arrive later, if at all.

So the test for a block-out is not "does it look good." It is **can you recognize it from the outline alone.** If not, the fix is proportion or arrangement, never more detail.

This is also why silhouettes should be distinct from each other. Three props with similar outlines make a cluttered scene, no matter how different their textures are.

### Working without edit mode

You can build a surprising amount from transformed primitives alone. A vise is a couple of cubes and a cylinder. A lantern is a cylinder, a cone, a torus, and a thin box.

Working this way forces you to solve problems with placement and proportion instead of cutting geometry, and that habit is worth building before you learn the tools that let you avoid it.

**Snapping** helps: **Shift + Tab** toggles it, and increment snapping moves things in clean steps so parts meet cleanly.

## Quick Check

{{< quickcheck question="Your block-out of a kettle is unrecognizable when you view it as a flat silhouette. What should you fix first?" >}}

- **A.** Add a texture so the material reads
- **B.** Add more geometry detail to the spout and handle
- **C.** Adjust the proportions and placement of the existing shapes
- **D.** Increase the cylinder's vertex count for a smoother curve

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>C.</strong> Silhouette is decided by proportion and arrangement. Texture is invisible in a silhouette, extra detail does not change an outline that is already wrong, and vertex count only affects smoothness.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Primitive**
- **Block-out**
- **Adjust Last Operation (F9)**
- **Vertex count**
- **Proportion**
- **Silhouette**
- **Snapping**

## Next

- [Primitive Form Studies](/assignments/form-studies/) — block out three props using only transformed primitives
- [Edit Mode Basics](/learn/blender/edit-mode-basics/) — move into mesh editing with extrusions and loop cuts
