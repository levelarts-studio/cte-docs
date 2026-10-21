---
id: BLND-204
title: "UV Unwrapping"
weight: 90
entity: module
subject: blender
tier: 200
status: complete
tools: ["blender"]
prereqs: ["BLND-104", "BLND-201"]
standards: ["GD.17.4", "AV.17.8"]
keywords: ["seams", "unwrap", "uv map", "texel density", "uv packing", "islands", "checker grid", "distortion"]
duration: 15
video: ""
aliases: ["/m/BLND-204"]
---

## What you'll be able to do

- Explain how 2D UV coordinates ($U, V$) map flat textures onto 3D polygon meshes ($X, Y, Z$)
- Strategically place seams to unroll complex forms while hiding cuts from camera view
- Diagnose stretching, shearing, and compression using UV checker grids and stretch heatmaps
- Equalize and balance texel density across multiple mesh islands using **Average Island Scale**
- Pack UV islands within 0–1 coordinate space with correct margin padding to prevent mipmap texture bleed

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### The 3D to 2D Translation Problem

Every texture in computer graphics—whether a hand-painted sprite, a scanned photo, or a PBR normal map—is a flat, two-dimensional image defined by horizontal and vertical pixels. But a 3D model exists in three-dimensional space with $X, Y,$ and $Z$ coordinates.

How does a 3D engine know which pixel of a flat image belongs on the tip of a character's nose or the strap of a backpack?

The answer is **UV coordinates**. Just as $X, Y,$ and $Z$ represent positions in 3D world space, **$U$** (horizontal) and **$V$** (vertical) represent positions on a 2D texture canvas, normalized from **0.0 to 1.0**.

![UV Mapping: 3D Model to 2D Texture Space](/images/uv/uv-mapping-concept.png)
<p style="font-size: 0.85rem; opacity: 0.8; margin-top: -0.5rem; margin-bottom: 1.5rem;"><em>The relationship between 3D spatial coordinates (X, Y, Z), 2D UV coordinates (U, V), and the final 2D texture map.</em></p>

UV unwrapping is the process of cutting open a 3D mesh and flattening its surface onto that 2D grid. The closest real-world analogy is tailoring: clothing patterns start as flat sheets of fabric cut into specific shapes and stitched together along seams into a wearable 3D jacket or pair of pants. In 3D software, you do the exact reverse: you cut along seams and unfold the 3D surface into flat 2D pattern pieces called **UV islands**.

Without clean UV coordinates, you cannot apply detailed materials, bake normal maps, paint textures, or export game-ready assets to Unreal Engine or Unity.

---

### Seam Strategy: Where to Cut and Where to Hide

If you try to flatten a hollow sphere or a hollow cylinder without cutting it, the surface will crumple, tear, or stretch violently. A **seam** is a marked edge along which Blender cuts the mesh apart so it can lie flat without distortion.

Placing seams is both a technical requirement and an artistic craft. Every seam creates a potential visual discontinuity in your texture, so your goal is twofold:

1. **Relieve geometric tension:** Add enough cuts so that curved 3D geometry can flatten out with minimal stretching.
2. **Hide the cut lines:** Place seams where players and cameras are least likely to see them.

#### Anatomical Seam Placement Guide

| Body Region | Seam Placement | Why It's Placed Here |
|---|---|---|
| **Head & Neck** | Collar loop around base of neck; vertical cut up the **center-back of the skull** to the crown. | Keeps the face 100% seamless; hides the back cut line under hair geometry or behind the character. |
| **Arms & Hands** | Armpit/shoulder socket loop; continuous inseam along the **underside** of the arm to the inner wrist. | Hides the seam when the character's arms rest in a natural idle or combat pose at their sides. |
| **Torso & Pelvis** | Vertical seams down the **lateral sides** of the ribcage (armpit to hip); shoulder top ridges. | Splits the torso cleanly into front and back halves, occluding side cuts under resting arms. |
| **Legs & Feet** | Continuous **inseam** along the inside of each leg (crotch to inner ankle); perimeter cut around foot sole. | The inner leg seam is naturally occluded between the legs; foot sole cut stays hidden on the ground. |

#### Blender Seam Controls

In Edit Mode (`Tab`), switch to Edge select (`2`):
- Select edges or edge loops (`Alt + Left Click`).
- Press **Ctrl + E → Mark Seam** to turn the selected edges into orange-red seam lines.
- To remove an accidental seam, select the edges and press **Ctrl + E → Clear Seam**.
- Once all seams are marked, select all faces (`A`) and press **U → Unwrap**.

---

### Diagnosing Distortion: UV Checker Grids & Stretch Heatmaps

How do you know if an unwrap is successful? You cannot reliably judge distortion on a solid gray mesh. You must inspect it with a **UV Checker Texture**.

A checker grid maps an alternating black-and-white grid across your model. When an unwrap is correct:
- Every checker square is **perfectly square** (equal width and height).
- The grid lines remain **straight and parallel**, with no diagonal shear or waviness.
- The squares maintain a **consistent, uniform scale** across the entire mesh.

![Character Model with Uniform UV Checker Grid in Blender](/images/uv/human-checker-preview.png)
<p style="font-size: 0.85rem; opacity: 0.8; margin-top: -0.5rem; margin-bottom: 1.5rem;"><em>A clean humanoid unwrap evaluated with a procedural UV checker texture in Blender. Squares remain uniform in scale from head to toe with straight, undistorted flow along natural contours.</em></p>

#### Common UV Flaws and Symptoms

| Symptom on Checker Grid | Underlying Cause | How to Fix |
|---|---|---|
| **Oblong / Rectangular Checkers** | Object scale was not applied before unwrapping ($X, Y, Z$ scale $\neq 1.0$). | Return to Object Mode, press **Ctrl + A → Apply All Transforms (Scale)**, then re-unwrap (`U → Unwrap`). |
| **Diagonal Shearing / Diamond Checkers** | Cylindrical surface was not given a longitudinal relief seam. | Add a longitudinal seam along the inner edge of the cylinder/limb. |
| **Severe Pinching at Corners / Poles** | Insufficient relief cuts; geometry is being pulled inward like a drawstring pouch. | Extend the seam further into the concave fold or apex vertex. |
| **Checkers Much Bigger in One Area than Another** | Non-uniform texel density between separate UV islands. | Select all islands in UV Editor and run **UV → Average Island Scale** (`Ctrl + A`). |

#### Using Blender's Built-in Stretch Overlay

In the **UV Editor** header, click the **Overlays** dropdown (overlapping circles icon) and enable **Display Stretch**:
- **Dark Blue:** Zero distortion ($1:1$ area/angle mapping between 3D face and 2D UV island).
- **Green / Cyan:** Acceptable minor relaxation.
- **Yellow / Orange / Red:** Heavy geometric stretching or compression. If you see red or orange patches, your unwrap is fighting the topology—add a seam to relieve the tension.

---

### Texel Density: Keeping Pixel Resolution Consistent

**Texel density** is the amount of texture resolution allocated per unit of 3D geometric surface area, commonly measured in **pixels per meter (px/m)** or **pixels per centimeter (px/cm)**.

Imagine placing a 2048x2048 brick texture on a wall. If one brick island takes up half the UV canvas and another takes up 5%, the first brick will look crisp and razor-sharp while the second will look pixelated and muddy. In a real-time game, mismatched texel density immediately ruins visual immersion.

```
Texel Density = Texture Resolution (pixels) / Real-World Dimension (meters)
```

For standard third-person and first-person game assets, studios enforce standardized texel density budgets (e.g., $10.24\text{ px/cm}$ for hero characters and weapons, $5.12\text{ px/cm}$ for environment props, $2.56\text{ px/cm}$ for large architectural walls).

#### Equalizing Texel Density in Blender

Blender provides an automated tool to match island scale across your entire mesh:
1. In the **UV Editor**, select all UV islands (`A`).
2. Go to **UV → Average Island Scale** (Hotkey: `Ctrl + A` inside the UV Editor window).

Blender instantly recalculates the area of every 3D polygon and rescales its corresponding 2D UV island so that all islands share identical pixel density. Check your 3D viewport: your checkerboard squares will instantly match in size from head to toe.

> [!NOTE]
> **Intentional Texel Density Scaling:** In character art, artists sometimes intentionally scale up high-priority focal islands (like the **face** and **eyes**) by $1.25\times$ to $1.5\times$ after averaging, while scaling down occluded, unseen areas (like the soles of the shoes or the inside of the mouth) to $0.75\times$. This budget reallocation directs maximum texture resolution where the player's eyes focus most.

---

### UV Island Packing & Margin Padding (0–1 Space)

Once your islands are unwrapped, relaxed, and scaled, they must be neatly arranged inside the **0.0 to 1.0 UV coordinate square**. This step is called **UV Packing**.

A game engine evaluates texture maps within this single $[0, 1] \times [0, 1]$ bounding box. Any geometry placed outside this square will repeat or clamp, depending on material settings.

#### The 3 Golden Rules of UV Packing

1. **Maximize UV Space Utilization:** Fill as much of the 0–1 canvas as possible (aim for $70\%\text{–}85\%$ surface coverage on game assets). Empty space on your UV sheet represents wasted GPU memory.
2. **Prevent Overlaps:** Unless you are deliberately stacking symmetrical halves to save texture space, no two UV faces may ever occupy the same UV space. Overlapping islands will cause one part of your model to display the paint strokes or baked normals of another.
3. **Always Include Margin Padding:** UV islands must **never touch each other** and must **never touch the outer boundary** of the UV square.

#### Why Island Margins Matter: Mipmapping & Pixel Bleed

As your camera moves away from a 3D object in a game engine, the GPU automatically downsamples the texture into smaller versions called **mipmaps** ($2048 \to 1024 \to 512 \to 256 \to 128 \to 64$).

At lower mipmap levels, individual pixels blur and blend together. If two UV islands are separated by only 1 or 2 pixels, their colors will bleed across each other at medium-to-long distances, producing bright outlines or black seam artifacts in your scene.

| Texture Map Resolution | Recommended Margin Padding | Blender Pack Margin Setting |
|---|---|---|
| **1024 × 1024** | 8 – 16 pixels | `~0.010` |
| **2048 × 2048** | 16 – 32 pixels | `~0.015` |
| **4096 × 4096** | 32 – 64 pixels | `~0.020` |

To pack islands with safe padding:
- In the UV Editor, select all islands (`A`).
- Run **UV → Pack Islands** (Hotkey: `Ctrl + P`).
- In the operator panel (bottom-left or `F9`), set **Margin** to approximately `0.015` for a 2048x2048 texture.
- Enable **Rotate** so Blender can orient islands at optimal angles to pack tightly.

---

### Essential UV Shortcuts

| Shortcut | Context | Action |
|---|---|---|
| `Tab` | 3D Viewport | Toggle between Object Mode and Edit Mode |
| `2` | 3D Viewport (Edit Mode) | Edge Select Mode |
| `Alt + Left Click` | 3D Viewport (Edit Mode) | Select complete edge loop |
| `Ctrl + E → Mark Seam` | 3D Viewport (Edit Mode) | Mark selected edges as UV seams (orange-red) |
| `Ctrl + E → Clear Seam` | 3D Viewport (Edit Mode) | Remove seams from selected edges |
| `U → Unwrap` | 3D Viewport (Edit Mode) | Unwrap selected mesh based on active seams |
| `Ctrl + A` (Object Mode) | 3D Viewport | **Apply Scale** (essential before unwrapping!) |
| `Ctrl + A` (UV Editor) | UV Editor | **Average Island Scale** (equalizes texel density) |
| `Ctrl + P` | UV Editor | **Pack Islands** (fits islands into 0–1 space with margin) |
| `L` | UV Editor | Select entire connected UV Island under cursor |
| `Ctrl + V` | UV Editor | **Minimize Stretch** (interactive relaxation mode) |

---

## Quick Check

{{< quickcheck question="You unwrap a character model and apply a 2048x2048 UV checker texture. In the 3D viewport, the checker squares on the character's torso are crisp, small, and sharp, but the checker squares on the head are massive, blurry, and stretched out. What is the cause of this issue, and what is the standard fix?" >}}

- **A.** The head mesh has inverted face normals; press `Shift + N` to recalculate outside.
- **B.** The UV islands have mismatched texel density; select all UV islands in the UV Editor and run `UV → Average Island Scale` (`Ctrl + A`).
- **C.** The texture file resolution is too low; increase the texture map to 8192x8192.
- **D.** The head island is overlapping the torso island; move the head outside the 0–1 UV coordinate space.

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> When checker squares vary dramatically in size across different parts of the same mesh, the UV islands have disparate texel densities (the torso island was scaled significantly larger in UV space than the head island relative to their actual 3D geometry). Running <strong>Average Island Scale</strong> (<code>Ctrl + A</code> in the UV Editor) rescales all islands proportionally to their 3D surface area, ensuring uniform resolution.
  </div>
</details>

{{< /quickcheck >}}

---

## Terms

- **UV Map** — A 2D planar projection that maps pixel coordinates ($U, V$) from a 2D image texture to vertex coordinates ($X, Y, Z$) on a 3D polygon mesh.
- **UV Island** — A discrete, continuous grouping of connected polygon faces that has been cut and flattened out into 2D UV space.
- **Seam** — A designated edge line on a 3D mesh along which the software cuts geometry to unfold it into planar UV islands.
- **Texel Density** — The ratio of texture pixels to physical 3D world geometry (e.g., px/cm or px/m), determining consistent visual resolution.
- **UV Distortion** — Shearing, stretching, or pinching that occurs when a 3D curved polygon is forcibly flattened onto a 2D plane without adequate relief seams.
- **Island Margin / Padding** — The protective pixel spacing maintained between adjacent UV islands and the outer UV canvas boundary to prevent mipmap texture bleeding.
- **Mipmapping** — A GPU optimization technique that precalculates sequences of progressively downsampled versions of a texture to accelerate rendering and eliminate distant aliasing.
- **0–1 Coordinate Space** — The normalized square canvas bounding the primary UV coordinate system from $(0.0, 0.0)$ to $(1.0, 1.0)$.
- **Average Island Scale** — An automated operator in Blender that equalizes the relative scale of all UV islands to reflect their proportional 3D surface area.

---

## Next

- [UV Unwrap & Texel Density Drill](/assignments/uv-unwrap-drill/) (`uv-unwrap-drill`)
- [Texturing and PBR Maps](/m/BLND-205/) (`BLND-205`)
