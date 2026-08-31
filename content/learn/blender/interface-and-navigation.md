---
id: BLND-101
title: "Interface and Navigation"
weight: 10
entity: module
subject: blender
tier: 100
status: draft
tools: ["blender"]
prereqs: []
standards: ["4.3"]
keywords: ["viewport", "orbit", "pan", "zoom", "edit mode", "object mode", "suzanne", "shortcut", "numpad", "emulate 3 button mouse", "laptop", "g", "r", "s", "tab", "frame selected"]
duration: 10
video: ""
aliases: ["/m/BLND-101", "/gad1-docs/modules/unit-1/a1"]
---

## What you'll be able to do

- Orbit, pan, and zoom in the 3D Viewport without thinking about it
- Switch between Object Mode and Edit Mode
- Select vertices, edges, and faces
- Move, rotate, and scale, and lock those to one axis

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### Moving the camera

Three controls do almost everything. Your hand should learn these before anything else:

- **Orbit**: Hold `Middle Mouse Button` and drag
- **Pan**: Hold `Shift + Middle Mouse Button` and drag
- **Zoom**: Scroll the `Mouse Wheel`

Two keys save you constantly when you lose your object:

- `Home` frames everything in the scene
- `Numpad .` frames whatever is selected

**On a laptop?** No middle mouse button and no numpad means none of the above works. Fix it once, in **Edit → Preferences → Input**: turn on **Emulate 3 Button Mouse** and **Emulate Numpad**. Orbit becomes `Alt + Left Click`. Do this before you do anything else or you will fight the software all period.

### Object Mode and Edit Mode

Press `Tab` to switch between them. Which one you're in decides what you're editing.

- **Object Mode** treats a model as one whole thing. Move it, rotate it, scale it, duplicate it. You're arranging objects in a scene.
- **Edit Mode** opens the model up so you can change its actual shape. Now you're working on the points and surfaces the model is built from.

In Edit Mode, three keys switch what you're grabbing:

- `1` — **vertices**, the points
- `2` — **edges**, the lines between points
- `3` — **faces**, the flat surfaces between edges

Most confusion in your first week comes from being in the wrong mode. If a tool isn't doing what you expect, check the mode dropdown in the top-left corner before you check anything else.

### Moving things

Three keys, and they work in both modes:

- `G` — **grab**, which means move
- `R` — **rotate**
- `S` — **scale**

Press the key, move your mouse, click to confirm. `Right-click` or `Esc` cancels.

The important part comes next. After pressing `G`, `R`, or `S`, press `X`, `Y`, or `Z` to lock the change to that one axis. Without it you're moving in whatever direction the camera happens to be facing, which is almost never what you want. `G` then `Z` moves straight up and down no matter where you're looking.

You can also type a number: `G`, `Z`, `2`, `Enter` moves the object exactly 2 units up. That precision matters later when parts have to line up.

### The cube and the monkey

Every new Blender file starts with a cube. Delete it with `X` when you don't need it.

Suzanne, the monkey head, is Blender's test model. Add her with **Add → Mesh → Monkey**. She has eyes, ears, and an uneven shape, which makes her much better than a cube for checking whether something is working.

## Quick Check

{{< quickcheck question="You press G and drag, and your object slides off at a strange angle instead of straight up. What did you skip?" >}}

- **A.** You were in Edit Mode instead of Object Mode
- **B.** You didn't press Z to lock the movement to one axis
- **C.** The object's scale needs to be applied first
- **D.** You need to hold Shift while dragging

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> With no axis locked, Blender moves the object along the plane of your screen, so the result depends entirely on where your camera happens to be. Pressing Z after G constrains it to straight up and down. <em>A</em> is wrong because G behaves the same way in both modes.
  </div>
</details>

{{< /quickcheck >}}
