---
id: texture-detail-pass
title: "Texture Painting & Detail Pass"
entity: assignment
tier: 200
status: complete
requires: ["BLND-206"]
standards: ["AV.17.1", "10.4"]
evidence_for: "10.4"
portfolio: true
portfolio_section: "GAD1 U2"
est_time: 90
setting: lab
aliases: ["/a/texture-detail-pass"]
---

## The task

Bake a tangent-space normal map from a high-poly detail mesh onto your optimized low-poly game asset using Blender's Cycles engine, then use Texture Paint tools to hand-craft a detail pass featuring edge wear, dirt gradients, and surface damage.

## Before you start

- [Texturing and PBR Maps](/m/BLND-205/) (`BLND-205`)
- [Baking Normal Maps](/m/BLND-206/) (`BLND-206`)

## Deliverables

1. **Baked Normal Map Image:** A clean 2048x2048 PNG export of your tangent space normal map showing smooth bevels and high-poly details with no projection clipping or missing rays.
2. **Detail Pass Beauty Render:** A 1080p render or high-resolution viewport capture of your textured low-poly model under studio or three-point lighting showcasing the combined effect of the baked normal map and hand-painted wear.

## Steps

{{% steps %}}

### Step 1 — Prepare and align your meshes

1. Open your project containing both the high-poly detailed mesh and the low-poly unwrapped mesh.
2. Verify both meshes share the exact same origin $(0, 0, 0)$.
3. Select both meshes and press **Ctrl + A → Apply All Transforms** (Scale must be `(1.0, 1.0, 1.0)`).
4. Right-click the low-poly mesh and select **Shade Smooth**.

### Step 2 — Create the bake target node

1. Select the low-poly mesh and open the **Shader Editor**.
2. Add an **Image Texture** node (`Shift + A → Texture → Image Texture`).
3. Click **+ New**:
   - **Name:** `T_[Prop]_Normal_2K`
   - **Width / Height:** `2048` × `2048`
   - **32-bit Float:** Checked
   - **Color Space:** Set to **Non-Color**
4. Keep this Image Texture node selected (white outline).

### Step 3 — Configure Cycles bake settings

1. In the **Render Properties** tab:
   - Set **Render Engine** to **Cycles** (Device: **GPU Compute**).
   - Expand the **Bake** panel.
   - Set **Bake Type** to **Normal** (Space: **Tangent**).
   - Check **Selected to Active**.
   - Set **Extrusion** to `0.02m` (or use a custom cage object if your mesh has overlapping tight geometry).
2. In the 3D Viewport or Outliner, select the **High-Poly mesh first**, then hold **Shift** and select the **Low-Poly mesh second** (Low-Poly must have the bright orange active highlight).

### Step 4 — Bake and save the normal map

1. Click **Bake** in the Bake panel. Wait for the progress bar to finish.
2. Switch to the **Image Editor** panel and select `T_[Prop]_Normal_2K`.
3. Press **Alt + S** (or **Image → Save As**) and save the file to your project directory as `T_[PropName]_Normal.png`.
4. In the Shader Editor, connect your saved normal map through a **Normal Map** node into the Principled BSDF `Normal` input to verify the smooth beveled look in Material Preview mode (`Z`).

### Step 5 — Paint the hand-crafted detail pass

1. Switch to the **Texture Paint** workspace (or press `Ctrl + Tab → Texture Paint`).
2. In the Active Tool settings (wrench/screwdriver icon), set your paint target to your **Base Color** or add a new dedicated paint layer.
3. Paint the following environmental wear passes:
   - **Edge Wear:** Use an opaque brush (`Mix` mode) with a light metal/primer color along exposed bevels, corners, and contact points.
   - **Cavity Grime:** Switch brush blend mode to **Multiply** with low strength ($0.2\text{–}0.3$) and paint dark dirt into recessed crevices, bolt recesses, and ground contact points.
   - **Scratches & Distress:** Use a small 1–2px brush or a stencil mask to stamp subtle surface scratches across broad panels.

### Step 6 — Save all images and render

1. In the Image Editor header, click **Image → Save All Images** so painted pixels are committed to disk.
2. Switch to the 3D Viewport in **Material Preview** or **Rendered** mode.
3. Frame your camera to highlight normal map edge bevels and painted damage under contrast lighting.
4. Render (`F12`) or capture a high-res viewport image (**View > Viewport Render Image**).

{{% /steps %}}

## Submit

{{< callout type="info" >}}
**Google Sites Portfolio:** Post your **Baked Normal Map PNG** and your **Detail Pass Beauty Render** to your Google Sites portfolio under **GAD1 Unit 2**. Include a short 2-sentence technical reflection explaining your extrusion/cage setting and how you approached the edge wear pass. Submit your published portfolio link in Google Classroom.
{{< /callout >}}

## Rubric

| Criteria | Approaching | Proficient | Advanced |
| :--- | :--- | :--- | :--- |
| **Normal Bake Quality** | Heavy projection errors, inverted green channel, ray clipping (lavender patches), or flat result | Clean tangent-space normal bake accurately transferring high-poly bevels and details without noticeable clipping | Flawless projection with zero ray artifacting; crisp 32-bit floating point depth gradient and smooth curvature |
| **Edge Wear & Damage Pass** | Unrealistic brush strokes, sloppy airbrushing, or paint applied randomly across flat areas | Believable edge wear concentrated on high-friction bevels and subtle dirt in ambient crevices | Convincing storytelling distress with varied stroke weight, multi-layered wear (primer/bare metal), and natural grime gradients |
| **Technical File Management** | Normal or paint maps lost due to failure to save from RAM; unapplied transforms | All textures saved to disk in correct color spaces; transforms applied; smooth shading verified | Production-ready naming conventions (`T_[Prop]_Normal`, `T_[Prop]_BaseColor`), clean UV usage, and optimized memory |
| **Portfolio Presentation** | Missing normal map file or low-resolution dark render | Both the normal map PNG and final beauty render displayed clearly on Google Sites with technical reflection | Portfolio-grade showcase with deliberate lighting framing specular edge highlights, side-by-side low/high comparison, and thorough reflection |

## Notes

- **Always Save from RAM:** Blender does not write baked or painted images to your hard drive automatically. Always press **Alt + S** on baked images and run **Image → Save All Images** before closing.
- **Selection Order Mnemonic:** "From High to Low, Selected to Active." Select the high-poly source first, select the low-poly target second.
