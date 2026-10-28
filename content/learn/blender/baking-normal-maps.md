---
id: BLND-206
title: "Baking Normal Maps"
weight: 110
entity: module
subject: blender
tier: 200
status: complete
tools: ["blender"]
prereqs: ["BLND-204", "BLND-205"]
standards: ["AV.17.1", "10.4"]
keywords: ["baking", "high to low poly", "cage", "normal bake", "texture paint", "selected to active", "cycles"]
duration: 15
video: ""
aliases: ["/m/BLND-206"]
---

## What you'll be able to do

- Explain the high-to-low poly baking workflow used in real-time game production
- Configure Blender's **Cycles** render engine for **Selected to Active** tangent normal baking
- Resolve projection clipping and ray artifacts using **Extrusion (Ray Distance)** and custom **Bake Cages**
- Set up target image textures with 32-bit floating point precision in **Non-Color** space
- Save baked textures from RAM to disk to prevent irreversible asset loss
- Use Blender's **Texture Paint** workspace to author hand-painted edge wear, dirt gradients, and surface damage

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### The High-to-Low Poly Workflow

Real-time game engines like Unreal Engine 5 and Unity must render dozens of characters and thousands of environment props at 60+ frames per second. Rendering millions of polygons for every prop would crush GPU performance.

Game studios solve this with the **High-to-Low Poly Baking Pipeline**:
1. **High-Poly Mesh (Sculpt / Subdivision):** Millions of polygons containing intricate details—bevels, panel creases, bolt heads, screw threads, organic muscle, and fabric folds.
2. **Low-Poly Mesh (Game-Ready):** A lightweight, optimized mesh (hundreds to thousands of polygons) with clean UV unwraps designed for real-time performance.
3. **The Bake Process:** The software projects rays inward from the low-poly surface to sample the angular surface normals of the high-poly mesh. It records those angles into a 2D **Tangent Space Normal Map**.

When applied to the low-poly model in game, the normal map deflects incoming light so the flat polygons appear round, beveled, and sculpted, without the performance cost of heavy geometry.

---

### Step-by-Step Cycles Normal Baking Pipeline

Blender requires the **Cycles** engine to bake textures (Eevee cannot perform texture bakes).

#### 1. Mesh Preparation & Alignment

- **Co-Location:** The High-Poly and Low-Poly meshes must occupy the exact same world space coordinates ($X=0, Y=0, Z=0$). Do not position them side-by-side.
- **Apply Transforms:** Select both objects and press **Ctrl + A → Apply All Transforms** so Scale is `(1.0, 1.0, 1.0)` and Rotation is `(0, 0, 0)`.
- **Shade Smooth:** Right-click the Low-Poly object and select **Shade Smooth**. If left flat, Cycles will bake faceted polygon borders directly into your normal map.

#### 2. Create the Target Texture Node

1. Select the **Low-Poly** object and open the **Shader Editor**.
2. If it has no material, create one named `M_[PropName]`.
3. Add a new **Image Texture** node (`Shift + A → Texture → Image Texture`).
4. Click **+ New**:
   - **Name:** `T_[PropName]_Normal_2K`
   - **Width / Height:** `2048` × `2048`
   - **32-bit Float:** Check this box (provides 32-bit floating point precision to eliminate staircase banding across curved surfaces).
   - **Color Space:** Set to **Non-Color**.
5. **The Golden Rule of Baking:** Leave this Image Texture node **selected** (active with a white border) in the Shader Editor. Cycles bakes into whichever Image Texture node is actively selected!

#### 3. Configure the Bake Settings

In the **Properties Panel**, go to **Render Properties** (camera icon):
- **Render Engine:** Switch to **Cycles** (Device: **GPU Compute**).
- Expand the **Bake** panel:
  - **Bake Type:** `Normal`
  - **Normal Space:** `Tangent`
  - Check **Selected to Active**

#### 4. Selection Order: High-to-Low

In the 3D Viewport or Outliner:
1. Select the **High-Poly** object first (dark orange outline).
2. Hold **Shift** and select the **Low-Poly** object second (bright yellow-orange outline — active selection).
3. Confirm in the Outliner that the Low-Poly is the active object.

---

### Controlling the Ray Projection: Extrusion vs. Cage

Cycles projects rays from outside the low-poly surface inward toward the high-poly mesh. Controlling this projection distance prevents baking errors.

```
       Ray Origin (Envelope)
        │
        ▼  [Extrusion / Cage]
   ───────┬───────────────────
          │
          ▼  <-- Ray casts inward
       ╭─────╮  <-- High-Poly detail (sampled)
    ───┴─────┴──  <-- Low-Poly surface (recorded)
```

#### Option A: Extrusion (Ray Distance)
In the Bake panel, set **Extrusion** (e.g., `0.02m` to `0.05m`). 
- If Extrusion is `0.0`, any high-poly geometry sticking slightly outside the low-poly surface is missed, producing flat lavender patches (`#8080FF`).
- If Extrusion is too high, rays shoot too far and accidentally sample unrelated geometry from other parts of the mesh.

#### Option B: Bake Cage (For Complex Meshes)
For overlapping parts (like fingers, mechanical hinges, or tight crevices), uniform extrusion causes rays to cross. A **Bake Cage** provides a custom projection shell:
1. Duplicate the Low-Poly mesh (`Shift + D`) and name it `[PropName]_Cage`.
2. In Edit Mode, select all faces (`A`) and press **Alt + S** (Shrink/Fatten along normals) to inflate the cage until it completely envelops the high-poly mesh.
3. In the Bake panel, check **Cage** and select your cage object.

---

### Executing the Bake and Saving the Image

Click the **Bake** button at the top of the Bake panel. A progress bar will run in the status bar.

> [!CAUTION]
> **Blender Does NOT Auto-Save Baked Textures!**
> The baked normal map exists only in volatile GPU/RAM memory. If you close or crash Blender, your baked image is lost forever.
> 
> Open the **Image Editor**, select your baked texture, and press **Alt + S** (or **Image → Save As**) to save `T_[PropName]_Normal.png` to your project folder immediately!

A successful tangent space normal map will show smooth periwinkle blue fields (`#8080FF`) with red and green gradients defining beveled edges and sculpted details.

---

### The Texture Painting Detail Pass

Once your normal map is baked, switch to the **Texture Paint** workspace to add custom hand-crafted wear, grime, and storytelling details.

#### 1. Texture Paint Setup
1. Switch the 3D Viewport interaction mode to **Texture Paint** (`Ctrl + Tab → Texture Paint`).
2. In the **Active Tool** settings (wrench/screwdriver tab), expand **Texture Slots**:
   - Choose **Mode: Single Image** or **Material**.
   - Select your **Base Color** texture (or add a new layer for dirt/damage).

#### 2. Essential Painting Techniques for Props

| Technique | Brush Blend Mode | Brush Settings | Where to Apply |
|---|---|---|---|
| **Edge Wear / Chipping** | `Mix` (Opaque) | Hard falloff, light metal/primer color | Along high-contact bevels, corners, and raised handles |
| **Cavity Dirt / Grime** | `Multiply` | Soft falloff, low strength ($0.2\text{–}0.3$), dark brown/black | Deep recesses, around bolt heads, inside seams, base contact points |
| **Surface Scratches** | `Mix` or `Screen` | 1–2px brush radius, jitter spacing | Random directional swipes across exposed flat panels |

#### 3. Stencil Painting for Micro-Detail
To paint photorealistic damage without hand-drawing every speck:
1. In Active Tool settings, expand **Texture** and click **+ New**.
2. In the Texture Properties tab (checkered icon at bottom), load a seamless grunge, scratch, or rust texture.
3. In Active Tool settings under **Texture**, set **Mapping** to **Stencil**.
4. A floating preview of your texture appears over your 3D Viewport:
   - **Right-Click Drag:** Move the stencil.
   - **Shift + Right-Click Drag:** Scale the stencil.
   - **Ctrl + Right-Click Drag:** Rotate the stencil.
5. Paint directly over your 3D mesh: your brush will stamp the grunge texture through the stencil onto your model!

> [!IMPORTANT]
> Just like baked maps, hand-painted texture slots reside in temporary RAM. Always run **Image → Save All Images** before saving your `.blend` file.

---

### Essential Baking & Painting Shortcuts

| Shortcut | Context | Action |
|---|---|---|
| `Ctrl + Tab` | 3D Viewport | Mode wheel (switch quickly between Object, Edit, and Texture Paint) |
| `Alt + S` | Edit Mode | Shrink/Fatten mesh along vertex normals (inflate bake cage) |
| `Alt + S` | Image Editor | Save Image As (commit baked normal map to disk) |
| `F` | Texture Paint | Interactively adjust brush radius/size |
| `Shift + F` | Texture Paint | Interactively adjust brush strength/opacity |
| `X` | Texture Paint | Swap foreground and background brush colors |
| `Right-Click Drag` | Texture Paint (Stencil) | Move stencil image overlay |
| `Shift + Right-Click Drag` | Texture Paint (Stencil) | Scale stencil image overlay |

---

## Quick Check

{{< quickcheck question="You perform a high-to-low poly normal bake in Cycles with Selected to Active enabled. The bake finishes, but the resulting normal map is completely solid flat periwinkle purple with none of the high-poly beveled edges or details visible. What was the most likely error?" >}}

- **A.** The high-poly and low-poly meshes were selected in reverse order (Low-Poly selected first, High-Poly active second).
- **B.** The bake type was set to Tangent Normal.
- **C.** The texture image was saved in PNG format instead of JPEG.
- **D.** The Low-Poly mesh has an applied scale of (1.0, 1.0, 1.0).

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>A.</strong> In Cycles Selected to Active baking, rays project from the <em>Active</em> object onto the <em>Selected</em> object. If the selection order is reversed (Low-Poly selected first and High-Poly active second), Cycles attempts to project the flat low-poly surfaces onto the high-poly mesh, resulting in an empty, flat map. The high-poly must be selected first, and the low-poly must be active (bright outline) second.
  </div>
</details>

{{< /quickcheck >}}

---

## Terms

- **Normal Baking** — The computational process of calculating angular surface differences between a high-poly sculpt and an optimized low-poly mesh, saving the data into a 2D tangent normal map.
- **Selected to Active** — A baking mode in Blender Cycles where rays cast from the active low-poly mesh to sample surface data from the selected high-poly mesh.
- **Tangent Space** — A coordinate system aligned to each polygon face's surface normal and UV tangent vectors, allowing normal maps to bend and deform with animated meshes.
- **Extrusion (Max Ray Distance)** — The distance outward from the low-poly surface where projection rays originate before casting inward.
- **Bake Cage** — An inflated duplicate of the low-poly mesh that defines a custom shell envelope for ray projection, eliminating ray crossing in complex crevices.
- **32-Bit Float** — A high-precision image format that prevents quantization staircase banding across smooth normal map gradients.
- **Texture Painting** — The workflow of painting directly onto 2D image textures in 3D viewport space using digital brushes, stencils, and blend modes.
- **Stencil Mapping** — A texture paint projection mode where an overlay image is stamped directly onto the 3D surface through mouse brush strokes.
- **Edge Wear** — Hand-painted or procedural lightening and distressing applied to sharp geometric ridges to simulate paint chipping and friction wear.

---

## Next

- [Texture Painting & Detail Pass](/assignments/texture-detail-pass/) (`texture-detail-pass`)
- [Lighting in Blender](/m/BLND-207/) (`BLND-207`)
