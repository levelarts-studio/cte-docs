---
id: navigating-3d-space
title: "Navigating 3D Space"
entity: assignment
tier: 100
status: draft
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

Complete a precision course in Blender. Place, rotate, and scale objects at exact coordinates using typed values instead of dragging, use both the 3D cursor and median pivots, and prove your accuracy with orthographic screenshots.

This is a drill. Nothing here goes in your portfolio. What you are building is the muscle memory that makes every project after this one faster.

## Before you start

Read [Objects, Transforms, and Pivots](/learn/blender/objects-transforms-and-pivots/) (`BLND-102`).

## Steps

{{% steps %}}

### Step 1 — Set up

New file, delete the default cube, save as `LASTNAME_NavCourse_v01.blend` in `01_Projects`.

### Step 2 — Build the frame

Place eight cubes at the corners of an imaginary 4-meter cube centered on the world origin. Each cube exactly 0.25m on a side.

Work out the coordinates before you place anything. Type them into the sidebar. No dragging.

### Step 3 — Find the center

Add a UV sphere at the exact center of the frame, 0.5m in diameter. Then add a cylinder that runs from the center of the bottom face to the center of the top face, touching both. Calculate its height and Z position rather than eyeballing.

### Step 4 — Fix your scales

Check the sidebar. Any object not at scale 1.0 gets `Ctrl+A → Scale`. Confirm the dimensions did not change.

### Step 5 — Pivot practice

Snap the 3D cursor to one bottom corner (`Shift+S → Cursor to Selected`). Set the pivot to 3D Cursor, select the sphere, rotate 45° on Z. Note where it lands.

Undo. Switch the pivot back to Median Point and repeat the same rotation. Note the difference.

### Step 6 — Prove it

Capture four screenshots:

- Front orthographic (`Numpad 1`)
- Right orthographic (`Numpad 3`)
- Top orthographic (`Numpad 7`)
- Any perspective view with the sidebar open, showing one corner cube's transform values

In the orthographic views your cubes should line up perfectly. Any error will be obvious, which is the point.

### Step 7 — Write it up

Post to your portfolio's **Coursework** page using the standard write-up format, plus:

- Your four screenshots
- The coordinates you used for all eight cubes
- One or two sentences in your own words on the difference between rotating around the 3D cursor and rotating around the median point

{{% /steps %}}

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
| **Orthographic Proof & Write-up** | Missing orthographic views or incomplete write-up | All 4 views submitted (Front, Right, Top, Perspective with sidebar) plus cube coordinates | Cleanly framed screenshots showing perfect alignment; well-formatted coursework post |

## Notes

- **Typing beats dragging**: Every professional workflow depends on exact values. If you can only place things by dragging, nothing you build will fit together, and in Unreal nothing will line up.
- **The math is the assignment**: Working out where the corners of a 4m cube sit is the part that transfers. Blender is just where you do the arithmetic.
