---
id: PROD-108
title: "Asset Management and Naming"
weight: 100
entity: module
subject: production
tier: 100
status: complete
tools: ["Unreal Engine", "Blender", "Spreadsheets"]
prereqs: []
standards: ["4.5", "16.6", "GD.18.1"]
keywords: ["asset management", "naming conventions", "master asset manifest", "LOD poly budgets", "folder structure", "Unreal Engine 5", "Nanite", "collision", "channel packing", "ORM"]
duration: 15
video: ""
aliases: ["/m/PROD-108"]
---

## What you'll be able to do

- Explain why standardized asset taxonomy is the operational backbone of real-time game development
- Construct canonical Unreal Engine asset identifiers using standard prefixes (`SM_`, `SK_`, `M_`, `MI_`, `T_`, `BP_`, `WBP_`, `A_`, `UCX_`) and texture suffixes (`_BC`, `_N`, `_ORM`, `_E`)
- Architect a clean, scalable Content Browser directory tree inside `/Game/` and enforce the developer sandbox quarantine
- Differentiate traditional LOD reduction chains from modern UE5 Nanite virtualized geometry, identifying when Nanite applies and when traditional LODs remain mandatory
- Author custom convex collision hulls (`UCX_`) and explain why complex-as-simple collision degrades physics frame rates
- Explain texture channel packing (ORM) and calculate memory bandwidth savings over loose grayscale maps
- Build and maintain a studio Master Asset Manifest to track poly budgets, priority, ownership, and pipeline milestones from blockout to final sign-off

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### The high cost of naming chaos

In game development, naming conventions and folder structures are not decorative bureaucracy; they are technical load-bearing infrastructure. A file named `crate_final_v2_edit.fbx` or textures named `New_Texture(1).png` break automated engine re-import scripts, generate duplicate asset redirectors, trigger cross-platform Git merge conflicts, and turn asset auditing into an expensive scavenger hunt.

When multiple artists, designers, and programmers collaborate on an Unreal Engine project, the engine's Content Browser must function like an indexed database. If a tech artist searches for an asset, they must be able to filter by type, zone, and variant in seconds. If an asset is named inconsistently, automated cooking, shader bundling, and packaging pipelines will inevitably fail.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   CANONICAL ASSET NAMING SYNTAX                        │
├────────────────────────────────────────────────────────────────────────┤
│   [Prefix] _ [Category] _ [AssetName] _ [Variant] _ [Suffix]           │
│                                                                        │
│   Examples:                                                            │
│   • SM_Prop_Generator_01          (Static Mesh: Generator Prop #1)     │
│   • T_Prop_Generator_01_BC        (Texture: Base Color Map)            │
│   • T_Prop_Generator_01_ORM       (Texture: Packed Occlusion/Rough/Met)│
│   • MI_Prop_Generator_01          (Material Instance)                  │
│   • UCX_SM_Prop_Generator_01      (Convex Collision Hull in DCC)       │
│   • A_SFX_Generator_Hum_Loop      (Audio Wave: Spatialized SFX)        │
└────────────────────────────────────────────────────────────────────────┘
```

---

### Unreal Engine standard prefixes & suffixes

Industry studios (including Epic Games' internal production teams) adhere to a standardized prefix and suffix taxonomy. Every asset type in the engine has an assigned prefix that instantly communicates its class and technical constraints:

| Prefix | Asset Class | Description & Production Example |
|---|---|---|
| `SM_` | **Static Mesh** | Non-deforming environment models, props, and modular pieces (`SM_Wall_400x300_01`). |
| `SK_` | **Skeletal Mesh** | Meshes with bones, joints, and vertex weights: characters, creatures, rigged weapons (`SK_Hero_Pilot`). |
| `M_` | **Master Material** | Base shader network containing logic, parameter nodes, and functions (`M_Prop_Master_PBR`). |
| `MI_` | **Material Instance** | Parameterized shader variation referencing unique textures; applied directly to meshes (`MI_Wall_Concrete_01`). |
| `T_` | **Texture Map** | 2D bitmap texture paired with a semantic channel suffix (`T_Wall_Concrete_01_BC`). |
| `BP_` | **Blueprint Actor** | Interactive gameplay class with components and script logic (`BP_Door_Airlock`). |
| `WBP_` | **Widget Blueprint** | UMG user interface canvas for HUDs, menus, and reticles (`WBP_HUD_Status`). |
| `NS_` / `NE_` | **Niagara System / Emitter** | Real-time particle simulations for smoke, fire, sparks, and atmospheric fog (`NS_SteamVent_01`). |
| `A_` / `SFX_` | **Audio Wave / Cue** | Spatialized sound effect, Foley asset, or ambient loop (`A_SFX_Door_Pneumatic`). |
| `UCX_` | **Convex Collision** | Custom convex physics collision mesh authored in Blender/Maya and exported inside the FBX (`UCX_SM_Wall_400x300_01`). |

#### Texture suffixes and channel packing

Textures require specific semantic suffixes so the engine and material graph immediately identify their color space and channel data:

| Suffix | Texture Role | Color Space | Pipeline Standard |
|---|---|---|---|
| `_BC` / `_D` | **Base Color / Diffuse** | **sRGB (Enabled)** | Pure surface albedo only. Absolutely zero pre-baked directional lighting or ambient shadowing. |
| `_N` | **Normal Map** | **Linear (sRGB Off)** | Tangent space normal map. Unreal Engine expects DirectX orientation (+X Right, -Y Down / Green inverted, +Z Up). |
| `_ORM` | **Packed AO / Rough / Metal** | **Linear (sRGB Off)** | Single composite texture packing three grayscale maps: **Red = Ambient Occlusion**, **Green = Roughness**, **Blue = Metallic**. |
| `_E` | **Emissive** | **sRGB (Enabled)** | Self-illumination mask multiplied by an HDR scalar for bloom and glow. |
| `_Mask` | **Utility / Opacity Mask** | **Linear (sRGB Off)** | Grayscale mask used for opacity clipping, decal blending, or team color shifts. |

#### Three golden rules of asset naming

1. **Zero Spaces and Special Characters**: Use `PascalCase` with underscores as delimiters (`SM_Prop_ControlTerminal_01`). Never use spaces, hyphens, or symbols (`#`, `@`, `!`, `?`, `%`, `&`). Spaces break console commands and script automations.
2. **Never Version in Asset Names**: Never name an asset `SM_Crate_final_v2_edit.fbx`. Version control systems (Git or Perforce) track historical versions. Suffix numbers (`_01`, `_02`) are reserved exclusively for genuine visual or gameplay variants.
3. **Consistent Casing for Cross-Platform Integrity**: Windows is case-insensitive, but Linux build servers, Mac workstations, and console platforms are strictly case-sensitive. If an asset is saved as `SM_Door_01` and referenced as `sm_door_01`, packaged release builds will crash.

---

### The magic of packed textures (ORM)

In older pipelines, artists exported separate grayscale image files for Ambient Occlusion, Roughness, and Metallic. In a modern PBR engine like Unreal Engine 5, doing so wastes massive amounts of GPU memory and bandwidth:

- Three separate grayscale textures require **three individual texture samplers** and **three memory fetches** on the GPU every time a pixel is drawn.
- By channel-packing Ambient Occlusion into the **Red** channel, Roughness into the **Green** channel, and Metallic into the **Blue** channel, all three PBR properties are stored in a single 8-bit RGB texture (`_ORM`).
- A single `_ORM` texture requires only **one texture sampler** in the material shader, reducing texture memory footprint by 66% and preserving GPU texture sampler slots (which are capped per material).

{{< callout type="warning" >}}
**Crucial Texture Import Rule**: When importing an `_ORM` texture into Unreal Engine, you **must uncheck sRGB** in the texture properties. Because Ambient Occlusion, Roughness, and Metallic represent mathematical linear data rather than human-perceived color, gamma curve correction will corrupt roughness highlights and metallic reflections.
{{< /callout >}}

---

### Content Browser architecture & developer quarantine

To prevent circular dependencies and broken asset links, studios maintain a rigid folder hierarchy inside Unreal Engine's `/Game/` root directory:

```
Content (/Game/)
├── Art/
│   ├── Characters/        (Hero, NPC, and enemy meshes, rigs, and anims)
│   ├── Environment/       (Modular kits, terrain, and architecture by biome)
│   ├── Props/             (Dressing props categorized by theme: Tech, Furniture, Containers)
│   ├── Materials/         (Master shaders M_, functions MF_, shared parameters)
│   └── VFX/               (Niagara systems, emitters, and sprite materials)
├── Audio/
│   ├── SFX/               (Spatialized sound effects and Foley)
│   ├── Music/             (Soundtracks and interactive stingers)
│   └── VO/                (Dialogue and voice-over tracks)
├── Blueprints/
│   ├── Core/              (GameMode, GameState, PlayerController)
│   ├── Actors/            (Interactive doors, levers, hazard volumes)
│   └── Characters/        (Player character Blueprint and animation Blueprints)
├── UI/                    (Widget Blueprints WBP_, icons, fonts, reticles)
├── Maps/                  (Persistent level Slice_P, lighting sublevels, test gyms)
└── Developers/            (Personal artist and designer sandboxes)
```

#### The developer sandbox quarantine

The `/Game/Developers/` folder exists so individual artists can prototype without fear of breaking the build. However, studios enforce a strict **Sandbox Quarantine**:

- Assets located inside `/Game/Developers/[StudentName]/` must **never** be placed inside a production map or referenced by a production Blueprint.
- When an asset is finished and approved, the artist moves it to its permanent location (e.g., `/Game/Art/Props/Tech/`).
- **Fix Up Redirectors**: When assets are moved in Unreal Engine, the engine leaves behind hidden pointer files called *Redirectors*. Before committing to Git, artists must right-click their folder in the Content Browser and select **Fix Up Redirectors in Folder**. Failing to do this causes missing asset errors when teammates pull the repo.

---

### LOD poly budgets and the Nanite reality

Real-time rendering requires balancing visual fidelity against frame time budgets. While modern PCs and current-generation consoles are powerful, geometry budgets prevent vertex shading bottlenecks and memory overruns.

#### Traditional LOD reduction chains

Before virtualized geometry, games relied exclusively on Level of Detail (LOD) chains. As an object moves further from the camera, the engine switches to simpler polygon meshes:

- **LOD0 (100% Detail)**: Full detail mesh seen close-up.
- **LOD1 (50% Tris)**: First reduction step (screen size ~0.5).
- **LOD2 (25% Tris)**: Distant view reduction (screen size ~0.25).
- **LOD3 (10–12% Tris)**: Far background silhouette or cross-billboard (screen size ~0.1).

#### The Nanite revolution in Unreal Engine 5

Unreal Engine 5 introduced **Nanite**, a virtualized micropolygon geometry system. Nanite analyzes static meshes, divides them into clusters of 128 triangles, and dynamically streams and renders only the triangles needed for the current screen pixels. Nanite eliminates manual LOD generation for supported meshes and prevents visible LOD pop-in.

However, junior artists often mistakenly assume that *"Nanite means poly counts don't matter anymore."* This is false.

| Asset Type | Nanite Enabled? | Technical Reason |
|---|---|---|
| **Rigid Static Props** (Crates, consoles, machinery) | **YES** | Nanite excels at rigid static geometry with opaque or masked materials. |
| **Modular Architecture** (Walls, floors, beams) | **YES** | Allows seamless high-density architectural detail without LOD pops. |
| **Hero Characters / Skeletal Meshes** | **NO** | Deforming skeletal meshes with skin weights cannot use standard Nanite. They **require traditional LOD0–LOD3 chains**. |
| **Translucent Assets** (Glass, water, energy shields) | **NO** | Translucency shaders do not support Nanite clustering. |
| **Foliage with WPO Wind Animation** | **Conditional** | High-density vertex wind deformation on thin alpha leaves can cause severe performance hits; requires careful testing. |

#### Studio polygon budget baseline (Vertical Slice 60 FPS)

For your team's 5-minute slice running at a stable 60 FPS in Unreal Engine 5:

- **Hero Character (Skeletal Mesh)**: 25,000 – 45,000 triangles (with 3 manual LOD reduction levels).
- **Hero Prop / Vehicle (Nanite or LOD0)**: 15,000 – 30,000 triangles.
- **Medium Environment Prop** (Terminal, generator, server rack): 3,000 – 8,000 triangles.
- **Small Dressing Prop** (Tool, bottle, debris, circuit board): 300 – 1,500 triangles.
- **Modular Architectural Kit Piece** (Wall panel, door frame): 200 – 1,200 triangles.

---

### Collision geography: simple primitives vs. complex traps

Every physical asset in a game engine requires collision data so players, projectiles, and physics props interact with it correctly. Unreal Engine categorizes collision into two systems:

1. **Simple Collision**: Lightweight geometric primitives (boxes, capsules, spheres) or custom convex hulls (`UCX_`). The physics engine evaluates simple collision with minimal CPU mathematical overhead.
2. **Complex Collision**: The physics engine evaluates raycasts and collisions against the **actual render mesh triangles**.

{{< callout type="danger" >}}
**The "Complex as Simple" Performance Trap**: Setting a prop's collision setting to *"Use Complex Collision as Simple"* forces the physics engine to calculate contact points against thousands of triangles. If multiple props or ragdolls collide simultaneously, the CPU physics thread will stall, causing severe frame rate stuttering. **Complex collision is strictly forbidden for interactive and physics-simulated props.**
{{< /callout >}}

#### Creating custom convex hulls in Blender (`UCX_`)

For irregular props where a simple box or cylinder is insufficient, model a custom convex collision hull in Blender before exporting:

- Model a low-poly cage enclosing the prop.
- The hull must be **convex**: it cannot have inward indentations, cavities, or holes. If a prop has an open doorway or hollow interior, build **multiple separate convex hulls** (e.g., `UCX_DoorFrame_01_01`, `UCX_DoorFrame_01_02`).
- Name the collision mesh with the exact prefix `UCX_` followed by the base mesh name:
  `UCX_SM_Prop_Crate_SciFi_01`
- When imported into Unreal Engine with *One Convex Hull Per UCX* checked, Unreal converts these objects into fast, hardware-accelerated PhysX/Chaos hulls.

---

### Pivot points, orientation, and metric units

In Unreal Engine:
- **1 Unreal Unit (UU) = 1 centimeter (cm)**.
- Standard player height: `180 cm`.
- Standard doorway width: `100 cm` (interior) to `140 cm` (exterior industrial); height `220 cm` to `240 cm`.

#### Pivot placement rules

- **Floor-Standing Props**: Origin pivot MUST be placed at the absolute base of the mesh (`Z = 0`) and centered on `X = 0, Y = 0`. This ensures that when an artist drags the asset into the level or snaps it to a surface, the asset sits flush on the floor without sinking into the terrain or hovering.
- **Wall Props**: Origin pivot centered on the rear contact surface (`Y = 0` or `X = 0`).
- **Doors and Hinges**: Origin pivot placed along the hinge axis line so rotation Blueprints open the door naturally.
- **Blender Export Requirement**: Always apply all transformations in Blender (`Ctrl + A > All Transforms`) prior to FBX export. A mesh exported with non-uniform scale (e.g., `Scale X: 1.0, Y: 2.5, Z: 0.8`) will cause stretched textures, distorted collision, and physics anomalies in Unreal Engine.

---

### The Master Asset Manifest (MAM)

The **Master Asset Manifest** is the central spreadsheet or database tracking every single asset required to build the vertical slice. It bridges the gap between Concept, 3D Art, Tech Art, Level Design, and Audio.

Every row represents a discrete deliverable. By tracking asset IDs, priorities, poly budgets, and pipeline stages, the production lead can immediately detect bottlenecks and schedule risks:

- **Priority Categorization**:
  - **P0 (Blocker / Critical Path)**: Core gameplay assets without which the vertical slice cannot function (player character, critical path modular kit, interactive objective terminal). P0 assets are protected and built first.
  - **P1 (Essential)**: Major dressing, key audio effects, and secondary props that fulfill the art style guide.
  - **P2 (Polish / Dressing)**: Environmental clutter, extra decals, secondary Foley, and ambient particles. If production falls behind schedule, P2 assets are cut immediately.
- **Lifecycle Status Tracking**:
  - `Concept / Ref` → `Blockout (Scale tested in engine)` → `High Poly` → `Low Poly / UV` → `Texturing (PBR bake)` → `In-Engine (Collision & Material Instance verified)` → `Approved`.

---

## Quick Check

{{< quickcheck question="A 3D artist finishes a high-tech terminal prop. They name the FBX file 'Console_v2_final.fbx', export three separate 2048x2048 grayscale textures for AO, Roughness, and Metallic, place the pivot point at the center of the screen, and set collision in Unreal to 'Use Complex Collision as Simple'. How many industry standard pipeline rules were violated?" >}}

- **A.** 1 rule
- **B.** 2 rules
- **C.** 3 rules
- **D.** 4 rules

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>D. 4 rules were violated:</strong><br>
    1. <strong>Naming Convention Violation:</strong> Filename lacks standard prefix (<code>SM_</code>) and uses illegal versioning (<code>_v2_final</code>) instead of canonical PascalCase.<br>
    2. <strong>Texture Memory Waste:</strong> AO, Roughness, and Metallic should be packed into a single <code>_ORM</code> texture to save GPU sampler slots and reduce memory overhead by 66%.<br>
    3. <strong>Incorrect Pivot Placement:</strong> A floor console's pivot must be at the base (<code>Z=0</code>), not centered on the screen, causing placement and grid snapping headaches in Unreal.<br>
    4. <strong>Physics Performance Hazard:</strong> Setting collision to "Complex as Simple" forces per-triangle physics computation, which introduces severe CPU hitching. It should use a simple convex hull (<code>UCX_</code>) or box primitive.
  </div>
</details>

{{< /quickcheck >}}

{{< quickcheck question="Why must the sRGB checkbox be unchecked in Unreal Engine when importing a packed ORM texture map?" >}}

- **A.** It makes the texture file size smaller on disk
- **B.** Ambient Occlusion, Roughness, and Metallic represent mathematical linear data; applying an sRGB gamma curve distorts surface reflectivity and lighting response
- **C.** sRGB is only supported for textures smaller than 1024x1024
- **D.** Leaving sRGB enabled causes Unreal Engine to automatically convert the mesh to Nanite

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> Base color maps use sRGB because human eyes perceive color non-linearly. However, packed maps like ORM contain pure numerical data (0.0 to 1.0) defining physical roughness and metallic properties. Gamma-correcting them skews the values, making materials look overly glossy, unnaturally dark, or washed out.
  </div>
</details>

{{< /quickcheck >}}

---

## Terms

- **Master Asset Manifest (MAM)** — A centralized production registry itemizing every asset in a project, detailing technical budgets, priority, ownership, dependencies, and lifecycle status.
- **Static Mesh (`SM_`)** — A 3D geometry asset that does not deform via skin weights or skeletal joints, commonly used for environmental architecture, foliage, and props.
- **Skeletal Mesh (`SK_`)** — A 3D mesh bound to a bone hierarchy (skeleton) using vertex skin weights, allowing dynamic deformation for characters and animated mechanisms.
- **Master Material (`M_`)** — A foundational shader network authored in the material editor that defines shader logic, lighting equations, and exposed parameters.
- **Material Instance (`MI_`)** — A lightweight derivative of a master material that allows rapid parameter changes (color, roughness scalar, texture swap) without triggering shader recompilation.
- **Channel Packing (ORM)** — Combining three discrete grayscale texture maps into the individual Red, Green, and Blue channels of a single image file (Red = Occlusion, Green = Roughness, Blue = Metallic).
- **Nanite** — Unreal Engine 5's virtualized micropolygon geometry streaming architecture that renders pixel-scale detail on rigid meshes without manual LOD creation or pop-in.
- **Level of Detail (LOD)** — Successively simplified versions of a 3D mesh swapped into rendering based on the object's screen size to conserve GPU processing power.
- **Simple Collision (`UCX_`)** — Hardware-accelerated convex hull or primitive volume (box, sphere, capsule) used by the physics engine for rapid player and projectile collision resolution.
- **Fix Up Redirectors** — An essential maintenance operation in Unreal Engine that cleans up lingering pointer files left behind when assets are renamed or moved between folders.

---

## Next

Apply these studio standards to your vertical slice project in the **[Asset List & Pipeline Doc](/assignments/asset-list-pipeline/)** assignment. You will download the studio template, audit your greybox slice, establish poly budgets, and build your team's master asset registry.
