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

**Blender Exercise: Generate and Assemble the Tiny House**

You'll run a short Python script inside Blender that builds a full set of house pieces for you, colored, correctly sized, and scattered off to the side like a parts bin. Then you'll assemble them into a house entirely by moving and snapping the pieces into place, and get the door and shutters swinging open the way real hinges do. Everything in this exercise happens inside Blender, there's no outside math to work out first.

Running someone else's setup script instead of building everything by hand is a completely normal part of real 3D and game pipelines, so this exercise has you do it the same way a studio would: read what the script does, run it once, and take it from there.

### What this exercise teaches

By the end, you should understand:

- **Running a script in Blender**: Using the Scripting workspace to load and execute a `.py` file that sets up a scene for you.
- **Snapping objects together**: Using Blender's snap tools to align pieces exactly, instead of eyeballing it.
- **Pivot points**: Why 3D Cursor, Median Point, and Individual Origins each rotate an object differently, and how to pick the one that makes a hinge behave like a real hinge.

## Before you start

Read [Objects, Transforms, and Pivots](/learn/blender/objects-transforms-and-pivots/) (`BLND-102`).

{{< callout type="info" >}}
**Starter Script Download**: Download the generator script [**`generate_house_demo_file.py`**](/downloads/generate_house_demo_file.py) to your computer before beginning Step 1.
{{< /callout >}}

## Steps

{{% steps %}}

### Step 1 — Run the generator script

1. Open Blender: **File > New > General**.
2. Switch to the **Scripting** workspace (tab along the top header).
3. In the Text Editor panel, click **Open** and browse to `generate_house_demo_file.py`. (If Open isn't available for some reason, click **New**, then copy and paste the script's contents in.)
4. Read through the script before running it. You don't need to understand every line, but notice what it's doing: defining each piece's name, size, and color, then placing it at a scattered starting position.
5. Click the **Run Script** button (the play icon) in the Text Editor's header.
6. Switch to the **Layout** workspace. You should see 14 colored objects scattered off to one side. Check the Outliner for their names.
7. Immediately save the file as `LASTNAME_HouseCourse_v01.blend` inside `01_Projects`.

> [!IMPORTANT]
> **Important:** The script clears the entire scene when it runs, including anything you've built. Only run it once, right at the start. If you run it again later by accident, you'll lose your progress.

### Step 2 — Inventory the pieces and turn on snapping

Open the Outliner and find all fourteen objects:

`floor`, `wall_left`, `wall_right`, `wall_back`, `wall_front_L`, `wall_front_R`, `wall_lintel`, `gable_left`, `gable_right`, `roof_slope_front`, `roof_slope_back`, `door`, `shutter_L`, `shutter_R`

Switch your viewport shading to Material Preview (**Z**, then **2**, or click the material preview sphere icon at the top-right of the 3D Viewport) so you can see the colors: brown for the floor, cream for walls and gable ends, terracotta for the roof, dark wood for the door, green for the shutters.

Now turn on snapping:

1. Click the magnet icon near the top center of the viewport (or press **Shift+Tab**) to enable Snapping.
2. Click the small dropdown arrow next to the magnet and set **Snap To: Vertex**.
3. Leave everything else at its default.

With this on, when you grab a piece (**G**) and move your mouse near a corner of another piece, the nearest corner of the piece you're moving will jump to line up with it. This is how you're going to assemble the whole house, corner to corner.

### Step 3 — Understand the floor plan

Before you start dragging pieces around, look at the shapes you have and figure out how they fit together. Here's the general layout, roughly to scale:

```text
                    wall_back
       (shutter_L)     |      (shutter_R)
      +---------------------------------+
      |                                 |
wall_left                          wall_right
      |                                 |
      +----------+           +---------+
      wall_front_L   [door]   wall_front_R
                 (wall_lintel above the door)
```

- The house is roughly 4m long along the wall with the door, and about 3m deep.
- The front wall (the one with the door) is split into three pieces because of the opening: two side segments and a lintel piece that sits above the door.
- Once the four walls and floor are together, the roof sits on top: `gable_left` and `gable_right` fill the triangular gaps above `wall_left` and `wall_right`, and the two sloped roof panels meet along a ridge running the length of the house.
- `shutter_L` and `shutter_R` sit on the outside of `wall_back`, flanking where a window would be, roughly centered.

Use the pieces' own shapes and the gaps between them as your guide, the same way you'd assemble a physical model kit.

### Step 4 — Assemble the floor and walls

1. Move `floor` to the world origin area first—it's your base reference for everything else.
2. Grab each wall (**G**) and drag it toward the floor. As it gets close, snapping should catch the bottom edge of the wall against the top edge of the floor. Watch for the snap indicator (a small orange circle) to know when it's caught.
3. Position each wall along the correct edge of the floor, matching the diagram above. Snap wall corners to floor corners and to each other where walls meet.
4. Place `wall_front_L`, `wall_front_R`, and `wall_lintel` together to form the front wall with its doorway gap. The lintel should snap into the gap above where the door opening will be, level with the tops of the side segments.

Check your work often from Top (**Numpad 7**) and Front (**Numpad 1**) orthographic views. A gap you can see is a snap that didn't catch—go back and try that corner again.

### Step 5 — Assemble the roof

The roof pieces already have their slope baked into their shape, you're not rotating anything here, just snapping them into position on top of the walls.

1. Snap `gable_left` and `gable_right` onto the tops of `wall_left` and `wall_right`. The flat bottom edge of each triangle should catch the top edge of its wall.
2. Snap the two roof slope panels (`roof_slope_front`, `roof_slope_back`) so their lower edges rest on the tops of the front and back walls, and their upper edges meet each other and the peaks of the two gable ends.

Work slowly, check from Front and Side (**Numpad 3**) orthographic views, and confirm there's no gap where the two roof panels meet at the ridge, and no sliver of missing gable showing through underneath the eaves.

### Step 6 — Add the door and shutters

1. Snap `door` into the opening in the front wall, so it sits flush and closed, filling the gap between `wall_front_L`, `wall_front_R`, and `wall_lintel`.
2. Snap `shutter_L` and `shutter_R` onto the outside face of `wall_back`, evenly spaced on either side of the imaginary window's center. Use the Front orthographic view to check they're level and evenly spaced.

Once everything is placed, do a full walkaround in Perspective view. You should have a complete, closed house.

### Step 7 — Open the door

A door hinges on its edge, not its center, so this step is about putting the pivot point exactly on that edge before you rotate. No calculation needed, you'll find the hinge by selecting it directly.

1. Select `door` and press **Tab** to enter Edit Mode.
2. Switch to Vertex select (press **1**), and box-select the two vertices along the door's left edge, the side touching `wall_front_L`.
3. Press **Shift+S** and choose **Cursor to Selected**. This snaps the 3D cursor exactly onto the hinge line, no typing required.
4. Press **Tab** to return to Object Mode.
5. Set the Transform Pivot Point dropdown (top of viewport) to **3D Cursor**.
6. With `door` selected, press **R**, then **Z**, type `90`, and press **Enter**. Watch it swing open around the hinge, like a real door.
7. Try it again with a smaller angle (**R**, **Z**, `30`, **Enter**) to see it open partway.
8. Undo back to a fully open or fully closed position, whichever you'd like for your screenshot.

> [!TIP]
> **Try it wrong, on purpose:** Set the Transform Pivot Point to **Median Point** and rotate the door again. Notice it now spins around its own center instead of swinging on the hinge, clearly not how a real door works. Undo, set the pivot back to **3D Cursor**, and leave the door open for your screenshot.

### Step 8 — Pivot point comparison with the shutters

This step compares three pivot modes side by side, using the same tools as Step 7, so you can see the full picture of why the hinge needed 3D Cursor specifically.

Select both `shutter_L` and `shutter_R` (Shift-click both) for Parts A through C:

#### Part A — 3D Cursor
1. Set the 3D Cursor to the world origin: **Shift+C**.
2. Set Transform Pivot Point to **3D Cursor**.
3. Press **R**, **Z**, `45`, **Enter**.
4. **Observe**: Both shutters swing through a wide arc around the house's center, not around either shutter. Press **Ctrl+Z** to undo.

#### Part B — Median Point
1. Set Transform Pivot Point to **Median Point**.
2. Press **R**, **Z**, `45`, **Enter**.
3. **Observe**: Both shutters rotate around the point exactly between them, swapping toward each other instead of swinging outward. Press **Ctrl+Z** to undo.

#### Part C — Individual Origins (before fixing origins)
1. Set Transform Pivot Point to **Individual Origins**.
2. Press **R**, **Z**, `45`, **Enter**.
3. **Observe**: Each shutter rotates around its own origin, but that's currently its geometric center, so the shutters spin around their middles instead of swinging open. Press **Ctrl+Z** to undo.

#### Part D — Individual Origins, with the origin moved to the hinge
Use the same edit-mode trick from Step 7 to find each hinge, no typing needed:

1. Select only `shutter_L`, press **Tab**, switch to Vertex select (**1**), and select the two vertices on its outer edge (away from the window).
2. Press **Shift+S** > **Cursor to Selected**, then press **Tab** back to Object Mode.
3. With `shutter_L` selected, go to **Object > Set Origin > Origin to 3D Cursor**. Its origin (the orange dot) should jump to its outer edge.
4. Repeat for `shutter_R`: Edit Mode, select its outer edge vertices, **Shift+S > Cursor to Selected**, **Tab** out, **Object > Set Origin > Origin to 3D Cursor**.
5. Select both shutters again, keep **Individual Origins** as the pivot mode.
6. Press **R**, **Z**, `45`, **Enter**.
7. **Observe**: Now each shutter swings open on its own outer edge, like a real shutter.

> [!NOTE]
> **Reflection:** In two or three sentences, describe what was different about Part D compared to Parts A through C. You don't need any numbers, just describe what you saw and why moving the origin mattered.

### Step 9 — Capture your proof

Take six screenshots:

1. **Front orthographic view** (**Numpad 1**), house fully assembled with roof, door and shutters closed
2. **Top orthographic view** (**Numpad 7**)
3. **Side (Right) orthographic view** (**Numpad 3**), showing the roof's ridge and slopes clearly
4. **Perspective view** of the fully assembled house
5. **The door open on its hinge** (from Step 7)
6. **Both shutters open correctly at 45°** (from Step 8, Part D)

**What "correct" looks like:** The assembled house should form a closed structure with a peaked roof, no visible gaps at the wall corners, around the lintel, or at the ridge line.

### Step 10 — Post to your portfolio

Post to your portfolio's **Coursework** page using the standard write-up format, plus:

- Your six screenshots
- Your written reflection on the four pivot/origin setups from Step 8

{{% /steps %}}

## Submission checklist

- [ ] Script run once at the start, file saved as `LASTNAME_HouseCourse_v01.blend` in `01_Projects`
- [ ] Snapping enabled and used to assemble all fourteen pieces
- [ ] House fully assembled with no visible gaps: walls, roof (ridge and gables), door, and shutters
- [ ] Door opens correctly around its hinge using 3D Cursor snapped to the hinge edge
- [ ] Four-part pivot/origin comparison completed on the shutters, with written reflection
- [ ] Six screenshots captured as described above

## Submit

{{< callout type="info" >}}
**Google Classroom Submission**: Post the link to your published Google Sites portfolio Coursework page in Google Classroom. Keep the `.blend` file saved in your `01_Projects` directory.
{{< /callout >}}

## Rubric

| Criteria | Approaching | Proficient | Advanced |
| :--- | :--- | :--- | :--- |
| **Script Setup** | Script not run correctly, pieces missing, or wrong file saved | Script run once, all 14 pieces present and correctly named, file saved correctly | Read through the script and can explain in their own words what it's doing |
| **Assembly Accuracy** | Pieces placed by eye without snapping; visible gaps or misalignment | Snapping used correctly to close all gaps; house forms a complete structure with door opening and full roof | Clean corners and ridge line, gable ends fit their openings exactly, evenly spaced shutters |
| **Door Hinge** | Door rotates from the wrong point, or cursor not placed on the actual hinge edge | Cursor correctly snapped to the hinge edge using Edit Mode selection; door swings correctly around it | Correctly demonstrates the wrong pivot mode too, and can explain why it looked wrong |
| **Pivot & Origin Comparison** | Fewer than four parts completed, or difference not documented | All four setups tested and documented | Reflection clearly distinguishes the role of pivot point vs. object origin |
| **Proof & Write-up** | Missing screenshots or incomplete write-up | All six items submitted, reflection included | Cleanly framed screenshots showing correct alignment; well-formatted coursework post |

## Notes

- **Running scripts is a real skill**: Most production Blender and game pipelines rely on setup scripts, asset importers, and batch tools written by someone else on the team. Knowing how to open the Scripting workspace, read what a script is about to do, and run it safely is a habit worth having early.
- **Snapping beats eyeballing**: Dragging pieces close and letting Blender's snap catch the exact corner is how real modeling gets done fast. You'll notice immediately if a corner isn't caught, which is the whole point.
- **Finding a pivot beats calculating one**: Selecting the actual edge you want to rotate around and snapping the cursor to it is faster and less error-prone than typing in a coordinate, and it's how this is actually done in production work.
