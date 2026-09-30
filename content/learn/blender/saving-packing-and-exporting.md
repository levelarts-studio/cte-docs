---
id: BLND-107
title: "Saving, Packing, and Exporting"
weight: 190
entity: module
subject: blender
tier: 100
status: complete
tools: ["blender"]
prereqs: ["BLND-103"]
standards: ["4.5", "10.4"]
keywords: ["pack resources", "apply transform", "unit scale", "fbx", "apply scalings", "export", "blender"]
duration: 10
video: ""
aliases: ["/m/BLND-107"]
---

## What you'll be able to do

- Pack external resources into a .blend file so nothing goes missing
- Apply an object's transforms correctly before export
- Export a clean FBX file that a game engine will read correctly
- Recognize and fix the most common export mistakes before they cause problems

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### Packing resources

A .blend file can reference outside files, most commonly textures, without actually containing them. That's normally fine, until you move the project, share it, or open it on a different computer, and suddenly Blender can't find the file it's looking for and the texture goes missing or turns pink.

**File → External Data → Pack Resources** embeds every external file directly into the .blend, so the file becomes fully self-contained. It gets larger, but it becomes portable: you can hand it to anyone, on any computer, and everything it needs travels with it.

Get in the habit of packing before you save a version you intend to share or submit. **Unpack Resources** reverses it later if you need the raw files back out.

### Applying transforms before export

Every object carries three transform values: location, rotation, and scale. If those values aren't at their default state (scale exactly 1.0, rotation exactly 0), that leftover math travels with the object into whatever format you export to, and the receiving software has to interpret it, which is exactly where things go wrong.

**Object → Apply → All Transforms** (or **Ctrl+A → All Transforms**) bakes your current location, rotation, and scale into the mesh itself and resets the values to their defaults. The object looks and sits exactly the same. What changes is that it now behaves correctly once exported, instead of arriving rotated, flipped, or scaled 100 times too big.

Do this right before export, every time, on every object you're exporting. It's the single most common fix for an asset that "looks fine in Blender but is broken in the engine."

### Units: the most common surprise

Blender's default unit is the meter. Unreal's default unit is the centimeter. That mismatch is the source of nearly every "why is my model tiny" or "why is my model gigantic" problem a beginner runs into.

There are two ways to handle it, and either works as long as you're consistent:

- Keep Blender at 1.0 scale (meters) and let **Apply Scalings: FBX All** in the export dialog handle the conversion for you
- Set Blender's **Unit Scale to 0.01** in Scene Properties and model directly at centimeter scale to match Unreal from the start

What breaks things is mixing approaches: modeling at one scale, forgetting which one, and exporting with settings that assume the other.

### Exporting an FBX

**File → Export → FBX (.fbx)**. The defaults are closer to correct than people expect:

- **Forward / Up axis**: leave these at Blender's defaults. They already match what Unreal expects, and changing them is a common way to introduce a rotation problem rather than fix one.
- **Scale**: 1.0
- **Apply Scalings**: FBX All
- **Apply Unit**: checked

The two settings actually worth double-checking, every time, are **Apply Scalings** and whether you remembered to apply transforms on the object beforehand. Those two account for nearly every real export problem.

### A quick pre-export check

Before exporting anything:

1. Select the object
2. Check the sidebar (**N** panel): **Scale** should read `1, 1, 1` and **Rotation** should read `0, 0, 0`. If not, apply transforms (**Ctrl+A → All Transforms**).
3. Confirm textures are packed if you're sharing the file (**File → External Data → Pack Resources**)
4. Export, with **Apply Scalings** set to **FBX All**

## Quick Check

{{< quickcheck question="A student exports a prop to FBX. In Unreal, it appears rotated 90 degrees from how it looked in Blender. What is the most likely cause?" >}}

- **A.** The wrong file format was used
- **B.** The object's rotation was never applied before export
- **C.** Unreal doesn't support FBX rotation data
- **D.** The texture wasn't packed

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> An unapplied rotation value travels into the exported file as leftover transform data, and the receiving engine interprets it literally. Applying all transforms before export is the standard fix.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Pack Resources**
- **Apply Transform**
- **Unit Scale**
- **FBX**
- **Apply Scalings**

## Next

- [Blender First Model: Hero Prop](/assignments/blender-first-model/) — model and export your first complete hero prop
- [Import Your Asset](/assignments/import-your-asset/) — bring your exported FBX into Unreal Engine
