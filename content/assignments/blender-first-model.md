---
id: blender-first-model
title: "Blender First Model: Hero Prop"
entity: assignment
tier: 100
status: complete
requires: ["BLND-103", "BLND-107"]
standards: ["GD.17.4", "AV.17.8", "10.4"]
evidence_for: "GD.17.4"
portfolio: true
portfolio_section: "GAD1 U1"
est_time: 90
setting: lab
aliases: ["/a/blender-first-model"]
---

## The task

Model one prop from your reference board, all the way through: correct scale, applied transforms, packed resources, and a clean FBX export. This is the first time you'll take a model through the entire pipeline, start to finish, and it sets the pattern every later project follows.

**Deliverable**: `.blend` source file and exported `FBX` model.

## Before you start

Read the prerequisite modules:
- [Primitive Modeling](/m/BLND-103/) (`BLND-103`)
- [Saving, Packing, and Exporting](/m/BLND-107/) (`BLND-107`)

## Steps

{{% steps %}}

### Step 1 — Pick your prop

Use the object from your reference board assignment, or choose something new if your plans changed. Keep it to primitive-friendly shapes: nothing that needs edit mode yet.

### Step 2 — Block out the silhouette

Build the big shapes first. Check proportions against your reference constantly, comparing specific ratios rather than eyeballing the whole thing at once.

### Step 3 — Set a real-world scale

Check your object's dimensions in the sidebar (**N** panel → **Item** tab). Adjust until it matches a believable real-world size for that object.

### Step 4 — Refine

Once the blockout reads correctly and the scale is right, adjust individual primitives until the shape is as close to your reference as you can get using primitives alone.

### Step 5 — Apply your transforms

Select the object. **Ctrl+A → All Transforms**. Confirm in the sidebar that scale reads `1, 1, 1` and rotation reads `0, 0, 0`.

### Step 6 — Pack your resources

**File → External Data → Pack Resources**, even if you haven't added textures yet. This is the habit, not a one-time step.

### Step 7 — Save your source file

Save as `LASTNAME_HeroProp_v01.blend` in your project folder, following the standard naming convention.

### Step 8 — Export

**File → Export → FBX**. Leave Forward/Up at the defaults. Set **Apply Scalings** to **FBX All**. Export into your `04_Exports` folder as `LASTNAME_HeroProp.fbx`.

### Step 9 — Write it up

Publish a standard write-up on your **Coursework** page, plus:
- A render of your final model
- A screenshot of the sidebar showing applied transforms (scale `1, 1, 1` and rotation `0, 0, 0`) right before export
- One sentence on what real-world scale you targeted and why

{{% /steps %}}

## Submit

{{< callout type="info" >}}
**Google Classroom Submission**: Post your portfolio link in Google Classroom. Submit both the `.blend` file and the exported `.fbx`.
{{< /callout >}}

## Rubric

| Criteria | Approaching | Proficient | Advanced |
| :--- | :--- | :--- | :--- |
| **Pipeline & File Hygiene (Transforms & Packing)** | Transforms unapplied (non-1.0 scale or rotated); unpacked external resources | Transforms cleanly applied (Scale 1.0, Rotation 0.0); external resources packed into `.blend` | Flawless asset hygiene; pristine naming convention and structured project directories |
| **Scale & Real-World Dimensions** | Arbitrary or wildly unrealistic scale (e.g., 3m coffee mug) | Scaled to believable real-world dimensions verified in the sidebar Item tab | Precise, real-world metric dimensions directly matched to reference prop specifications |
| **FBX Export Quality** | Export missing, incorrect orientation/scale in engine, or improper settings | Clean FBX export with default axes and Apply Scalings set to FBX All; imports cleanly | Engine-ready FBX with optimal pivot placement, correct scale, and clean mesh grouping |
| **Silhouette & Primitive Blockout** | Unrecognizable silhouette; rushed into micro-detail or inappropriate edit mode cuts | Silhouette reads cleanly from multiple angles using refined primitive assembly | Masterful proportion and silhouette clarity with minimal primitive count |
| **Documentation & Portfolio** | Missing render, sidebar transform screenshot, or scale reflection | Complete Coursework post with final render, sidebar transform screenshot, and scale explanation | Polished portfolio presentation detailing real-world scale rationale and pipeline reflection |

## Notes

- **The FBX is the actual deliverable**: A beautiful model that never gets exported correctly, or exports rotated and tiny, isn't finished. This assignment is graded on the whole pipeline, not just the modeling.
- **This pattern repeats all year**: Block out, scale correctly, apply transforms, pack, export. Every later project assumes you can do this without being walked through it again.
