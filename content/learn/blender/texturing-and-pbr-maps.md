---
id: BLND-205
title: "Texturing and PBR Maps"
weight: 100
entity: module
subject: blender
tier: 200
status: complete
tools: ["blender"]
prereqs: ["BLND-204"]
standards: ["AV.17.1", "GD.17.4"]
keywords: ["albedo", "roughness", "metallic", "normal map", "pbr", "principled bsdf", "shader editor"]
duration: 15
video: ""
aliases: ["/m/BLND-205"]
---

## What you'll be able to do

- Explain the principles of Physically Based Rendering (PBR) and the Metallic/Roughness workflow
- Distinguish the roles of Base Color, Roughness, Metallic, Normal, and Ambient Occlusion maps
- Apply the **Metallic Binary Rule** to accurately represent conductors versus dielectrics
- Build and connect shader networks in Blender's **Shader Editor** using the **Principled BSDF**
- Assign correct color spaces (**sRGB** vs. **Non-Color**) to avoid gamma distortion in mathematical data maps
- Use Blender's **Node Wrangler** addon (`Ctrl + Shift + T`) to rapidly hook up complete PBR texture sets

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### The PBR Paradigm: Physics Over Guesswork

In older 3D graphics pipelines, artists hand-painted specular highlights and shadows directly into textures, resulting in assets that only looked convincing under one specific light setup. If a prop moved from bright daylight into a dark dungeon, it looked fake.

**Physically Based Rendering (PBR)** changed game art by simulating the real physics of light interaction with matter:
1. **Conservation of Energy:** An object cannot reflect more light than it receives. As a surface becomes rougher, reflected light scatters in all directions and spreads out, losing intensity. As a surface becomes smoother, reflections concentrate into a tight, bright highlight.
2. **Standardized Material Properties:** Instead of arbitrary numbers, surfaces are defined by measurable physical characteristics: color, micro-roughness, electrical conductivity (metalness), and micro-surface angles (normals).

Because PBR materials obey physical laws, an asset textured in Blender looks consistent when rendered in Cycles, Eevee, Unreal Engine 5, or Unity under any lighting condition.

---

### The Four Core PBR Maps

A complete PBR material is driven by image texture maps feeding into the inputs of Blender's **Principled BSDF** shader:

| Texture Map | What It Controls | Grayscale / Color | Sockets in Principled BSDF | Color Space Setting |
|---|---|---|---|---|
| **Base Color (Albedo)** | Surface color and diffuse reflectivity | Full RGB Color | `Base Color` | **sRGB** |
| **Roughness** | Micro-surface smoothness vs. microscopic irregularities | Grayscale ($0.0 \to 1.0$) | `Roughness` | **Non-Color** |
| **Metallic** | Conductor (metal) vs. Insulator (dielectric) | Grayscale ($0.0$ or $1.0$) | `Metallic` | **Non-Color** |
| **Normal** | High-frequency surface relief without geometry | RGB Vector ($X, Y, Z$) | `Normal` (via Normal Map node) | **Non-Color** |
| **Ambient Occlusion (AO)** | Soft shadows in crevices and corners | Grayscale ($0.0 \to 1.0$) | Multiplied over Base Color | **Non-Color** |

---

### 1. Base Color (Albedo): Pure Reflectance

The **Base Color** map defines what color light bounces back from the surface. 

> [!IMPORTANT]
> **No Painted Shadows:** In PBR, the Base Color must be "delit." Never bake directional shadows, flashlight spots, or highlights into this texture. The 3D engine's light sources handle all dynamic illumination.

- **For Non-Metals (Dielectrics):** Wood, stone, plastic, fabric, skin, brick. The Base Color represents diffuse reflected light (e.g., green for grass, terracotta for clay). Non-metal base colors generally stay within a brightness range of $30\text{–}240$ sRGB (pure black `#000000` and pure white `#FFFFFF` do not exist in nature).
- **For Metals (Conductors):** Raw steel, brass, copper, gold, aluminum. Metals have no diffuse reflection; all incoming light is reflected specularly. For metals, the Base Color defines the *color of the reflection* (e.g., bright yellow-orange for copper, warm yellow for gold, pale silver-gray for iron).

---

### 2. Roughness: The Specular Spread

The **Roughness** map is a grayscale texture that governs how sharp or blurry reflections appear across the surface:
- **Black ($0.0$):** Optically polished and mirror-smooth (chrome, polished glass, wet ice, glossy lacquer). Reflections are razor-sharp.
- **White ($1.0$):** Micro-rough and diffuse (chalk, unfinished concrete, rough clay, unglazed ceramic). Reflections are completely scattered and matte.
- **Mid-Grays ($0.2 \to 0.7$):** Most manufactured real-world surfaces (brushed plastic, painted metal, weathered wood, worn leather).

Surface believability lives in the roughness map. Fingerprints, subtle scratches, scuffs, and water drips are primarily roughness variations rather than color changes.

---

### 3. The Metallic Binary Rule

The **Metallic** map dictates whether a surface is an electrical conductor (metal) or an insulator (dielectric):

> [!WARNING]
> **The Metallic Binary Rule:** In the real world, an atom is either metallic or it isn't. Therefore, the metallic map must almost always be strictly **binary**:
> - **$0.0$ (Black):** Non-metal (plastic, paint, rubber, wood, rock, flesh, leather).
> - **$1.0$ (White):** Raw bare metal (iron, chrome, copper, brass, gold).
> 
> Setting a metallic value to $0.5$ (mid-gray) is physically impossible and results in a murky, synthetic look. The **only** exceptions for grayscale values are transitional pixels: a thin dust layer settling on steel, or the feathered boundary edge between chipped paint ($0.0$) and bare iron ($1.0$). If a metal part is painted red, the paint is a non-metal ($0.0$)!

---

### 4. Normal Maps: Faking Micro-Geometry

A **Normal Map** simulates fine geometric details—rivets, recessed panel seams, bevels, skin pores, and scratches—without adding a single polygon to the model.

Unlike grayscale bump maps that only describe height, a normal map stores a 3D direction vector in its RGB color channels:
- **Red Channel ($X$):** Surface slope left and right.
- **Green Channel ($Y$):** Surface slope up and down.
- **Blue Channel ($Z$):** Perpendicular surface height pointing directly outward along the surface normal (hence why tangent space normal maps look mostly light purple/blue `#8080FF`).

---

### The #1 Beginner Mistake: Color Space

When you add an Image Texture node in Blender, the default **Color Space** setting is **sRGB**. 

- **sRGB** applies gamma correction ($\approx 2.2$) designed for images human eyes look at directly (like Base Color or photos).
- **Non-Color** treats image pixels as raw mathematical data ($0.0 \to 1.0$), with no gamma curve applied.

> [!CAUTION]
> If you leave a Roughness or Normal map set to **sRGB**, Blender applies a non-linear gamma curve that ruins the math. Your roughness values will become artificially bright and washed out, and normal maps will project warped, jagged shading artifacts.
> - **Base Color:** `sRGB`
> - **Roughness:** `Non-Color`
> - **Metallic:** `Non-Color`
> - **Normal Map:** `Non-Color`
> - **Ambient Occlusion:** `Non-Color`

---

### Constructing the Node Graph in Blender

Switch to the **Shading** workspace. In the **Shader Editor**:

```
[Texture Coordinate] (UV)
        │
        ▼
   [Mapping] (Vector) 
        │
        ├──► [Image Texture: Base Color] (sRGB) ───────► Base Color [Principled BSDF]
        ├──► [Image Texture: Metallic]   (Non-Color) ──► Metallic   [Principled BSDF]
        ├──► [Image Texture: Roughness]  (Non-Color) ──► Roughness  [Principled BSDF]
        └──► [Image Texture: Normal]     (Non-Color) ──► [Normal Map] ──► Normal [Principled BSDF]
```

1. **Mapping Nodes:** Add **Input > Texture Coordinate** and **Vector > Mapping**. Connect the `UV` output of Texture Coordinate to the `Vector` input of Mapping. This allows you to scale, offset, or rotate all texture channels simultaneously.
2. **Image Texture Nodes:** Connect the `Vector` output of the Mapping node to the `Vector` input of each Image Texture node.
3. **Connecting Sockets:**
   - Base Color `Color` $\to$ Principled BSDF `Base Color`.
   - Metallic `Color` $\to$ Principled BSDF `Metallic`.
   - Roughness `Color` $\to$ Principled BSDF `Roughness`.
4. **The Normal Map Node:** 
   - Never plug an Image Texture node directly into the Principled BSDF `Normal` socket (yellow color socket into purple vector socket).
   - Add **Vector > Normal Map**.
   - Connect Image Texture `Color` $\to$ Normal Map `Color`.
   - Connect Normal Map `Normal` $\to$ Principled BSDF `Normal`.
   - Keep the dropdown set to **Tangent Space**.

---

### Studio Workflow: Node Wrangler (`Ctrl + Shift + T`)

Blender includes a built-in add-on called **Node Wrangler** that automates texture wiring in seconds:

1. Go to **Edit > Preferences > Add-ons**, search for `Node Wrangler`, and enable it.
2. In the Shader Editor, click on the **Principled BSDF** node to highlight it.
3. Press **Ctrl + Shift + T** (Principled Texture Setup).
4. In the file browser, navigate to your texture folder, select all map files at once (`_BaseColor`, `_Roughness`, `_Metallic`, `_Normal`), and click **Principled Texture Setup**.
5. Blender automatically:
   - Spawns Texture Coordinate and Mapping nodes.
   - Adds all Image Texture nodes and wires them to the correct BSDF inputs.
   - Automatically sets Roughness, Metallic, and Normal to **Non-Color**.
   - Inserts a Tangent Space **Normal Map** node with proper connections.

---

### Evaluating Materials in the Viewport

To inspect how your material responds to real light:
1. In the 3D Viewport, press **Z → Material Preview** (or click the Material Preview shading sphere in the top-right corner).
2. Blender lights your model using an HDRI environment.
3. Click the small **downward arrow** next to the shading spheres in the 3D Viewport header:
   - Cycle through different HDRI environments (e.g., *Studio*, *Forest*, *Courtyard*, *Sunset*) to check how reflections look under different colors and contrast levels.
   - Adjust **Rotation** (or hold **Alt** and drag with your middle mouse button) to spin the environment light around your asset and watch the specular highlights dance across roughness transitions.

---

### Essential Shader Shortcuts

| Shortcut | Context | Action |
|---|---|---|
| `Shift + A` | Shader Editor | Add new shader, texture, or vector node |
| `Ctrl + Shift + T` | Shader Editor (Principled BSDF selected) | Auto-build PBR texture network with Node Wrangler |
| `Ctrl + T` | Shader Editor (Image Texture selected) | Auto-add Texture Coordinate & Mapping nodes |
| `Ctrl + Shift + Left Click` | Shader Editor (any node) | Viewer node preview (solo inspect a single texture channel) |
| `X` or `Delete` | Shader Editor | Delete selected node |
| `F` | Shader Editor | Connect selected outputs and inputs together |
| `H` | Shader Editor | Collapse/hide unused node sockets for clean layout |
| `Z → Material Preview` | 3D Viewport | View real-time PBR shading under HDRI lighting |

---

## Quick Check

{{< quickcheck question="You import a PBR texture set and connect all nodes to the Principled BSDF. However, in Material Preview mode, the model looks greasy, dull, and washed out, and the normal map produces strange dark faceted artifacts across the surface. What is the most likely error?" >}}

- **A.** The UV coordinates were not unwrapped before applying the material.
- **B.** The Roughness and Normal map Image Texture nodes are incorrectly set to the sRGB color space instead of Non-Color.
- **C.** The Metallic value is set to 1.0 on a metal object.
- **D.** The render engine is set to Eevee instead of Cycles.

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> When mathematical data textures like Roughness, Metallic, or Normal maps are loaded with the default <strong>sRGB</strong> color space, Blender applies a gamma 2.2 curve that warps the numerical values. Roughness becomes overly bright (greasy/washed out) and tangent normal vectors are distorted, causing severe shading anomalies. Switching these data textures to <strong>Non-Color</strong> fixes the issue immediately.
  </div>
</details>

{{< /quickcheck >}}

---

## Terms

- **PBR (Physically Based Rendering)** — A rendering paradigm that calculates surface shading by obeying real-world optical physics, including conservation of energy.
- **Base Color (Albedo)** — The flat, unshaded color reflectance of a material, free of any directional lighting, baked shadows, or specular highlights.
- **Roughness** — A grayscale texture ($0.0 \to 1.0$) controlling microscopic surface irregularity; determines whether reflections are mirror-sharp or blurry and matte.
- **Metallic** — A binary material channel indicating whether a surface is a dielectric insulator ($0.0$) or an electrical conductor / raw metal ($1.0$).
- **Normal Map** — An RGB image storing 3D tangent vectors ($X, Y, Z$) that simulate surface angle relief and micro-geometry without extra polygons.
- **Non-Color Space** — A raw linear data mode in Blender that reads pixel values directly as mathematical coordinates without applying gamma correction.
- **Principled BSDF** — Blender's unified uber-shader combining dielectric and conductive material algorithms into a single physically based node.
- **Node Wrangler** — A built-in Blender add-on that provides hotkeys and automated workflows for shader graph construction.
- **Dielectric** — A non-conductive material (wood, stone, plastic, skin) with low surface reflectivity ($\approx 4\%$) and colored diffuse bounce.
- **Conductor** — A conductive metallic material (iron, copper, gold) with high specular reflectivity and zero diffuse reflectance.

---

## Next

- [PBR Material Set](/assignments/pbr-texture-set/) (`pbr-texture-set`)
- [Baking Normal Maps](/m/BLND-206/) (`BLND-206`)
