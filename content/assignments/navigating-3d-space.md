---
id: navigating-3d-space
title: "Navigating 3D Space"
entity: assignment
tier: 100
status: complete
requires: ["BLND-102"]
standards: ["4.3", "1.2", "5.7"]
evidence_for: "4.3"
portfolio: true
portfolio_section: "GAD1 U1"
est_time: 60
setting: lab
aliases: ["/a/navigating-3d-space"]
---

## The task

**Blender Exercise: Coordinates, Scale, and Pivot Points**

Complete a precision coordinate, scale, and pivot point exercise in Blender. Place, rotate, and scale objects at exact coordinates using typed values instead of dragging, understand the difference between scale and dimensions, master both the 3D cursor and median pivot points, and prove your accuracy with orthographic screenshots.

### What this exercise teaches

By the end, you should understand:

- **Exact coordinate placement**: How to place objects using exact numbers instead of dragging
- **Scale vs. dimensions**: The difference between an object's scale and its dimensions
- **Pivot points**: How the pivot point setting changes what happens when you rotate something

Work through the steps in order. Don't skip the "why" notes—they explain what you're actually supposed to be learning at each stage.

## Before you start

Read [Objects, Transforms, and Pivots](/learn/blender/objects-transforms-and-pivots/) (`BLND-102`).

## Steps

{{% steps %}}

### Step 1 — Set up your file

1. Open Blender: **File > New > General**.
2. Click the default cube to select it, press `X`, and choose **Delete**.
3. Save the file as `LASTNAME_NavCourse_v01.blend` inside the `01_Projects` folder.

### Step 2 — Plan your coordinates on paper first

Before you touch Blender, work this out with pencil and paper (or a text file).

You're going to build a cube-shaped frame out of eight small cubes, one at each corner. The frame is 4 meters wide, tall, and deep, and it's centered on the world origin `(0, 0, 0)`.

**Why centered matters**: If a cube is 4m wide and centered on 0, its edges reach from `-2` to `+2`. That's just half of 4 on each side.

So the eight corner positions are every combination of $x = \pm 2$, $y = \pm 2$, $z = \pm 2$:

| Corner | X | Y | Z |
| :---: | :---: | :---: | :---: |
| **1** | 2 | 2 | 2 |
| **2** | 2 | 2 | -2 |
| **3** | 2 | -2 | 2 |
| **4** | 2 | -2 | -2 |
| **5** | -2 | 2 | 2 |
| **6** | -2 | 2 | -2 |
| **7** | -2 | -2 | 2 |
| **8** | -2 | -2 | -2 |

Write this table out yourself before moving on. You'll type these numbers in by hand in the next step, so know them cold.

### Step 3 — Place the eight corner cubes

For each of the eight coordinates from your table:

1. Press `Shift+A` > **Mesh** > **Cube**. It'll appear at the 3D cursor (probably `0, 0, 0`).
2. Press `N` to open the sidebar if it's not already open.
3. In the **Location** fields, type in the X, Y, Z values for that corner. **Do not drag the cube into place.** Typing keeps your placement exact; dragging by eye will not.

Now resize each cube to **0.25m per side**. Blender's default cube starts at 2m per side, so you have two ways to shrink it:

- **Option A (recommended for this exercise)**: In the sidebar, find the **Dimensions** fields (below Scale) and type `0.25` into X, Y, and Z. Blender will calculate the scale for you.
- **Option B**: Set **Scale** to `0.125` on all three axes ($0.125 \times 2\text{m} = 0.25\text{m}$). This works the same but requires you to do the math yourself.

Repeat this for all eight cubes. Yes, it's repetitive. That repetition is what builds the habit of typing coordinates instead of eyeballing them.

### Step 4 — Add the center sphere

The center of the frame is the world origin: `(0, 0, 0)`.

1. Press `Shift+A` > **Mesh** > **UV Sphere**.
2. In the sidebar, set **Location** to `(0, 0, 0)`.
3. You want a sphere 0.5m across. In the **Dimensions** fields, type `0.5` for X, Y, and Z.

### Step 5 — Add the connecting cylinder

This is the step that requires actual calculation, so slow down here.

You want a cylinder that runs straight up through the center of the frame, touching the middle of the bottom face and the middle of the top face:

- The bottom face's center is at `(0, 0, -2)`.
- The top face's center is at `(0, 0, 2)`.
- The distance between them is **4 meters**. That's your cylinder's height.
- The midpoint between `-2` and `2` is `0`. Since a cylinder in Blender is centered on its own origin by default, placing its origin at $Z = 0$ means it will automatically stretch from `-2` to `+2`, exactly matching the two face centers.

So:

1. Press `Shift+A` > **Mesh** > **Cylinder**.
2. Set **Location** to `(0, 0, 0)`.
3. In **Dimensions**, set **Z** to `4`.

If your math was right, the cylinder should now touch both the top and bottom of the frame exactly, with no gap and no overlap.

### Step 6 — Check and fix your scale values

This step exists because Option B in Step 3 (and some Dimension edits) can leave an object's underlying Scale value at something other than `1.0, 1.0, 1.0`, even though it looks correct in the viewport. That's a hidden trap: it can cause weird behavior later if you add modifiers or export the file.

For every object you've made:

1. Select it and check the **Scale** row in the sidebar.
2. If any value isn't exactly `1.0`, press `Ctrl+A` and choose **Scale** from the menu. This is called "applying" the scale.
3. Immediately check the **Dimensions** again. They should be unchanged. If the object visibly changed size, something went wrong and you should undo and try again.

### Step 7 — Pivot point experiment

This is the core concept of the exercise. Read it through once before doing it.

**Background**: When you rotate an object in Blender, it doesn't automatically rotate around the object itself. It rotates around whatever point is currently set as the "pivot point." There are a few pivot options, but we're comparing two: **3D Cursor** and **Median Point**.

#### Part A: Rotating around a corner

1. Select one of your bottom corner cubes (any cube with $Z = -2$).
2. Press `Shift+S`, choose **Cursor to Selected**. This moves the 3D cursor to that cube.
3. In the header at the top of the viewport, find the **Transform Pivot Point** dropdown and set it to **3D Cursor**.
4. Select the sphere (not the cube).
5. Press `R`, then `Z`, type `45`, press `Enter`.

- **What to observe**: The sphere doesn't spin in place. It swings through an arc and ends up somewhere else in space entirely.
- **Why**: You told Blender to rotate around the 3D cursor's position, which is at the corner cube, not at the sphere. The sphere got dragged along that rotation like it was tied to the corner with a string.
- **Reset**: Press `Ctrl+Z` to undo the rotation. Confirm the sphere is back at the center before continuing.

#### Part B: Rotating around the object's own center

1. Change the **Transform Pivot Point** dropdown to **Median Point**.
2. With the sphere still selected, press `R`, `Z`, `45`, `Enter` again.

- **What to observe**: This time the sphere stays exactly where it was. Only its orientation changes, which you may not even notice on a sphere since spheres look the same from most angles.
- **Why**: With a single object selected, its "median point" is its own origin. So rotating "around the median point" just means rotating around itself, like a top spinning in place.

**Reflection**: Write one sentence in your own words explaining the difference between what happened in Part A and Part B. This is the actual skill this exercise is testing.

### Step 8 — Capture your proof

Take four screenshots showing your work is accurate:

1. **Front orthographic view** — press `Numpad 1`
2. **Right orthographic view** — press `Numpad 3`
3. **Top orthographic view** — press `Numpad 7`
4. **Perspective view** — any perspective view, with the sidebar (`N`) open and one corner cube selected, so its Location, Scale, and Dimensions values are all visible

**What "correct" looks like**: In all three orthographic views, your cubes should line up into a perfect square outline, evenly spaced, with the sphere and cylinder centered inside. If one cube is off, even slightly, you'll see a visible gap or misalignment. That's intentional. The exercise is designed so mistakes are easy to spot, not hidden.

### Step 9 — Post to your portfolio

Post to your portfolio's **Coursework** page using the standard write-up format, plus:

- Your four screenshots (Front, Right, Top, and Perspective with sidebar open)
- The coordinate table you used for all eight cubes
- Your one-sentence explanation in your own words on the difference between rotating around the 3D cursor and rotating around the median point

{{% /steps %}}

## Submission checklist

- [ ] File saved with correct name (`LASTNAME_NavCourse_v01.blend`) in `01_Projects`
- [ ] Eight cubes at correct coordinates, each 0.25m per side
- [ ] Sphere at center, 0.5m diameter
- [ ] Cylinder spanning the full 4m height, touching top and bottom faces
- [ ] All objects have Scale `1.0, 1.0, 1.0` after applying
- [ ] Pivot point experiment completed, with a one-sentence explanation written
- [ ] Four screenshots captured as described above

## Submit

{{< callout type="info" >}}
**Google Classroom Submission**: Post the link to your published Google Sites portfolio Coursework page in Google Classroom. Keep the `.blend` file saved in your `01_Projects` directory.
{{< /callout >}}

## Rubric

| Criteria | Approaching | Proficient | Advanced |
| :--- | :--- | :--- | :--- |
| **Frame Accuracy (4m Cube)** | Cubes placed by eye or misaligned; incorrect dimensions | All 8 corner cubes placed at exact calculated coordinates (±2m, ±2m, ±2m), 0.25m size | Mathematical symmetry exact; clear precision in coordinate entry |
| **Center Objects** | Sphere or cylinder missing, eyeballed, or wrong dimensions | 0.5m sphere at origin; cylinder connects bottom and top cube faces exactly | Exact Z calculations and scale values verified cleanly |
| **Transform & Scale** | Scale values not applied (non-1.0 scales present) | All objects have scale applied (`Ctrl+A → Scale`) at 1.0 without dimension distortion | Clean transform hierarchy; item properties verified in Item panel |
| **Pivot Comparison** | Difference between 3D cursor and median pivot not documented | Documented rotation results for both 3D Cursor and Median Point with accurate explanation | Clear, insightful explanation in own words of how origin vs cursor influences rotation |
| **Orthographic Proof & Write-up** | Missing orthographic views or incomplete write-up | All 4 views submitted (Front, Right, Top, Perspective with sidebar) plus cube coordinates and reflection | Cleanly framed screenshots showing perfect alignment; well-formatted coursework post |

## Notes

- **Typing beats dragging**: Every professional workflow depends on exact values. If you can only place things by dragging, nothing you build will fit together, and in Unreal nothing will line up.
- **The math is the assignment**: Working out where the corners of a 4m cube sit is the part that transfers. Blender is just where you do the arithmetic.
