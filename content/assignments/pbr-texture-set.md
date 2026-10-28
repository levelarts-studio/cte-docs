---
id: pbr-texture-set
title: "PBR Material Set"
entity: assignment
tier: 200
status: complete
requires: ["BLND-205"]
standards: ["AV.17.1", "GD.17.4"]
evidence_for: "AV.17.1"
portfolio: true
portfolio_section: "GAD1 U2"
est_time: 60
setting: lab
aliases: ["/a/pbr-texture-set"]
---

## The task

Author a complete physically based material in Blender's Shader Editor using standard PBR texture maps (Base Color, Roughness, Metallic, and Normal). Apply the material to an unwrapped 3D asset (such as your prop from Unit 1 or a standard test mesh), configure color spaces correctly, and produce two deliverables: a clean screenshot of your shader node graph and a material preview render.

## Before you start

- [UV Unwrapping](/m/BLND-204/) (`BLND-204`)
- [Texturing and PBR Maps](/m/BLND-205/) (`BLND-205`)

## Deliverables

1. **Shader Node Graph Screenshot:** A clean, readable image of your node network showing Texture Coordinate, Mapping, Image Textures, Normal Map node, and the Principled BSDF.
2. **Material Preview Render:** A 1080p render or high-res viewport capture of your textured object under HDRI lighting demonstrating roughness variation, metallic contrast, and surface relief.

## Steps

{{% steps %}}

### Step 1 — Prepare your model and textures

1. Open Blender with your unwrapped 3D prop (or use a test shader ball/prop with clean UVs).
2. Gather a complete PBR texture set (Base Color, Roughness, Metallic, Normal) at 1024x1024 or 2048x2048 resolution (use CC0 assets from ambientCG, Poly Haven, or lab resources).
3. Switch to the **Shading** workspace at the top of the screen.

### Step 2 — Build the shader node network

1. Assign a new material to your object named `M_[AssetName]_PBR`.
2. In the **Shader Editor**, add the following nodes (`Shift + A`):
   - **Input > Texture Coordinate** (use the `UV` output)
   - **Vector > Mapping** (connect `UV` to `Vector`)
   - Four **Texture > Image Texture** nodes (connect Mapping `Vector` to each Image Texture `Vector`)
   - **Vector > Normal Map**
3. Connect the texture outputs to the **Principled BSDF**:
   - Base Color `Color` $\to$ `Base Color`
   - Metallic `Color` $\to$ `Metallic`
   - Roughness `Color` $\to$ `Roughness`
   - Normal `Color` $\to$ Normal Map node `Color` $\to$ Normal Map `Normal` $\to$ `Normal`

*(Tip: You may also use Node Wrangler by selecting Principled BSDF and pressing `Ctrl + Shift + T` to auto-build this setup).*

### Step 3 — Enforce correct color spaces

Verify the **Color Space** dropdown on every Image Texture node:
- **Base Color:** Set to **sRGB**
- **Roughness:** Set to **Non-Color**
- **Metallic:** Set to **Non-Color**
- **Normal Map:** Set to **Non-Color**

### Step 4 — Evaluate in Material Preview mode

1. In the 3D Viewport, press **Z → Material Preview**.
2. Click the shading dropdown arrow (top right) and rotate the HDRI light or switch HDRI environments to inspect specular reflections.
3. If using repeating tiling textures, adjust the `Scale X, Y, Z` values on the **Mapping** node until texel density matches the object's real-world scale.
4. Verify the **Metallic Binary Rule**: ensure pure metal areas read metallic while painted or non-metal parts stay dielectric ($0.0$).

### Step 5 — Capture and submit deliverables

1. In the Shader Editor, press **Home** or organize your nodes neatly so all node titles, sockets, and Color Space settings are clearly visible. Take a clean screenshot.
2. Position your camera to capture your asset showing specular highlight roll-off and normal map relief. Render an image (`F12`) or capture a high-res viewport render (**View > Viewport Render Image**).
3. Save both images to your `01_Projects` directory.

{{% /steps %}}

## Submit

{{< callout type="info" >}}
**Google Sites Portfolio:** Upload both your **Shader Node Graph Screenshot** and your **Material Preview Render** to your Google Sites portfolio under **GAD1 Unit 2**. Include a 2–3 sentence reflection identifying your color space choices and metallic/roughness values. Submit your published portfolio link in Google Classroom.
{{< /callout >}}

## Rubric

| Criteria | Approaching | Proficient | Advanced |
| :--- | :--- | :--- | :--- |
| **Node Graph Architecture** | Missing core nodes or plugged directly into incorrect sockets (e.g., Normal plugged without Normal Map node) | All four PBR maps connected logically to Principled BSDF with Texture Coordinate and Mapping nodes | Clean, organized graph layout with custom node labeling or frame grouping; flawless socket connections |
| **Color Space Execution** | Data maps left on default sRGB, causing washed out roughness or distorted normal shading | Base Color set to sRGB; Roughness, Metallic, and Normal set strictly to Non-Color | Flawless color management with proper normal map strength and verified zero gamma distortion |
| **PBR Surface Fidelity** | Inaccurate metallic/roughness values; uniform plastic look with no variation | Clear distinction between metallic and dielectric surfaces; believable roughness and surface relief | Convincing material response across diverse HDRI lighting angles; well-scaled texel density |
| **Portfolio Presentation** | Low-resolution, blurry, or missing node graph/render | High-resolution node graph and clear material preview render posted to Google Sites with reflection | Professional showcase render with deliberate lighting framing highlights and thoughtful technical reflection |

## Notes

- **The Normal Map Node is Mandatory:** An Image Texture outputs a color; the Normal Map node converts that color into angular surface vectors. Without it, your normal map will not shade correctly.
- **Node Wrangler Shortcut:** Remember `Ctrl + Shift + T` on the Principled BSDF node to automatically wire all matching textures in a single click.
