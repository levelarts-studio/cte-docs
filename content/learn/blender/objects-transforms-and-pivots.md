---
id: BLND-102
title: "Objects, Transforms, and Pivots"
weight: 20
entity: module
subject: blender
tier: 100
status: draft
tools: ["blender"]
prereqs: ["BLND-101"]
standards: ["4.3"]
keywords: ["origin point", "3d cursor", "transforms", "sidebar", "n panel", "dimensions", "scale", "apply transform", "pivot point", "median point", "bounding box center"]
duration: 10
video: ""
aliases: ["/m/BLND-102"]
---

## What you'll be able to do

- Read and type exact transform values in the sidebar
- Explain what an object's origin is and move it deliberately
- Place and use the 3D cursor
- Choose the right pivot point for a rotation

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### An object is a container

An object has a location, a rotation, and a scale. The mesh inside it is separate data. Move the object and the mesh comes along, but the mesh has its own coordinates relative to the object.

The connecting point is the **origin**: the small orange dot. Every transform is measured from it. When you rotate an object, it rotates around its origin unless you tell Blender otherwise.

An origin does not have to sit inside the mesh. A door's origin belongs at its hinge, not its center, and that one choice is the difference between a door that swings and a door that spins in place.

### The sidebar is where precision lives

Press **N** to open the sidebar. The Item tab shows Location, Rotation, Scale, and Dimensions for whatever is selected.

You can type into any of these. Click a field, type a number, press Enter. This is how professionals place things, and dragging is the exception rather than the rule.

Two fields that look similar and are not:

- **Dimensions** is the object's actual size in meters
- **Scale** is a multiplier applied to the mesh

Set a cube's dimensions to 2m and its scale becomes 2. Both describe the same result, but scale carries baggage.

### Applying transforms

Non-1.0 scale causes problems later: textures stretch, modifiers behave oddly, physics misreads size, and exports arrive in the wrong dimensions.

**Ctrl+A → Scale** bakes the current scale into the mesh and resets the value to 1.0. The object looks identical and now behaves properly. Apply scale before exporting, before rigging, and any time something is acting strangely for no visible reason.

You can also apply Location and Rotation the same way.

### The 3D cursor

The red and white ringed target is the **3D cursor**. It is a point in space with a position and a rotation, and it does two jobs: it marks where new objects appear, and it can act as a pivot.

- **Shift + Right Click** places it under your mouse
- **Shift + S** opens the Snap pie menu, including Cursor to Selected and Cursor to World Origin
- **Shift + C** returns it to the world origin
- Its exact coordinates are in the sidebar under the View tab

### Pivot points

The pivot is the point a rotation or scale happens around. The selector sits in the middle of the 3D viewport header, and the default is **Median Point**.

| Pivot | What it uses |
|---|---|
| **Median Point** | The average of everything selected. Default. |
| **Bounding Box Center** | The center of a box drawn around the extremes of the selection |
| **3D Cursor** | Wherever you put the cursor |
| **Individual Origins** | Each object rotates around its own origin |
| **Active Element** | The last thing you selected |

Median and bounding box sound the same and are not. Median averages, so it gets pulled toward wherever more objects are clustered. Bounding box only cares about the outermost extents, so three objects at -10, 0, and 20 give a median near 3 but a bounding box center at 5.

In object mode, both of these use object **origins**, not geometry. If an origin sits somewhere odd, your pivot will too.

**Press `.` (period)** to open the pivot pie menu. Careful with older tutorials: `.` used to switch straight to 3D Cursor, and now it opens the menu. `,` (comma) opens the transform orientation menu, which used to jump to bounding box.

### Units

Blender's default unit is the meter. One Blender unit is one meter, and the default cube is 2m across.

Worth knowing now because Unreal measures in centimeters. That conversion is handled on export, but "why is my model 100 times too big" is the most common first-import problem, and it starts here.

## Quick Check

{{< quickcheck question="You rotate a door object and it spins around its middle instead of swinging on its hinge. What is the fix?" >}}

- **A.** Switch the pivot point to Bounding Box Center
- **B.** Move the object's origin to the hinge edge
- **C.** Apply rotation with Ctrl+A
- **D.** Place the 3D cursor at the door's center

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> The origin is where the object rotates from, so a hinge means the origin belongs at the hinge. D is backwards, and A would move the pivot to the middle of the bounding box, which is where it already effectively is.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Object**
- **Origin**
- **Transform**
- **Sidebar (N panel)**
- **Dimensions vs Scale**
- **Apply Transform**
- **3D cursor**
- **Pivot point**
- **Median point**
- **Bounding box center**

## Next

- [Navigating 3D Space](/assignments/navigating-3d-space/) — generate and assemble the tiny house with snapping and hinge pivots
- [Primitive Modeling](/learn/blender/primitive-modeling/) — build block-outs using simple 3D primitives
