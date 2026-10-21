---
id: DESN-116
title: "Brand Identity and Style Guides"
weight: 165
entity: module
subject: design
tier: 100
status: complete
tools: ["pure-ref"]
prereqs: ["DESN-101", "DESN-102"]
standards: ["GD.17.4", "13.3", "10.3"]
keywords: ["style guide", "art bible", "brand identity", "visual pillars", "shape language", "material consistency", "do's and don'ts"]
duration: 15
video: ""
aliases: ["/m/DESN-116"]
---

## What you'll be able to do

- Explain the purpose of a Studio Art Bible and how it prevents stylistic drift across team members
- Establish 3 actionable **Visual Pillars** that govern all aesthetic decisions on a game project
- Define **Shape Language** rules that subconsciously communicate safety, danger, and faction alignment
- Apply the **60-30-10 palette rule** to control visual hierarchy across 3D props and environments
- Author explicit **Visual Do's & Don'ts** that eliminate guesswork for modelers and texture artists

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### The Problem of "A Pile of Art"

In indie studios and student game teams, a common failure pattern occurs: four talented 3D artists work tirelessly for eight weeks modeling props, characters, and environments. Individually, every single asset looks impressive.

Yet when all the models are imported into Unreal Engine, the game looks like a chaotic mess. One artist modeled stylized, hand-painted anime barrels; another modeled ultra-photorealistic scratched military crates; a third used vibrant neon textures; and the fourth built hyper-detailed sci-fi architecture.

The project does not look like a cohesive game world—it looks like a random asset flip.

The tool that prevents this disaster is the **Studio Art Bible** (also known as the **Art Style Guide**). The Art Bible is the visual constitution of your project. It establishes the non-negotiable artistic laws that ensure every model, texture, and light looks like it was created by the exact same hand.

---

### 1. The Three Visual Pillars

Every great game art style can be distilled into **three core visual pillars**. These are not generic buzzwords like "cool," "dark," or "fun." They are actionable aesthetic principles that guide specific modeling and texturing choices.

Consider how major studios define their visual pillars:

| Game | Visual Pillars | How It Manifests in the 3D Art |
|---|---|---|
| ***Half-Life 2*** | **Grounded, Weathered, Eastern European** | Heavy concrete, utilitarian Soviet architecture, peeling paint, exposed rusted rebar, zero fantasy lasers. |
| ***Overwatch*** | **Heroic, Optimistic, Clean-Chunky** | Vibrant primary colors, exaggerated bevels, soft gradients, stylized anatomy, zero photorealistic grit or gore. |
| ***The Last of Us*** | **Reclaimed, Improvised, Desaturated** | Overgrown organic foliage reclaiming rigid brick and asphalt, duct-taped tools, muted earth tones, soft bounce lighting. |

When an artist on your team finishes a 3D blockout, they must evaluate it against your three pillars:
- *Does this model embody Pillar 1?*
- *Does the texture treatment reflect Pillar 2?*
- *Does the silhouette reinforce Pillar 3?*

If the answer to any pillar is no, the asset goes back for revision.

---

### 2. Shape Language as Narrative Code

Human brains are wired to decode basic geometric shapes instantly. In game art direction, shapes are subconscious emotional signposts:

```
■ RECTANGLES / SQUARES   ▲ TRIANGLES / DIAGONALS   ● CIRCLES / CURVES
  • Solid, heavy, stable   • Aggressive, lethal      • Soft, welcoming, organic
  • Protective bunkers     • Hostile enemy spikes    • Player health pods
  • Defensive barricades   • Razor-wire barriers     • Safe neutral traders
```

When building your Art Bible, you must assign specific shape rules to the competing forces in your world:
- **Friendly / Defensive Factions:** Built on horizontal lines, sturdy rectangles, and rounded bevels.
- **Hostile / Aggressive Factions:** Built on piercing diagonal silhouettes, sharp acute angles, and triangular motifs.
- **Natural / Sacred Elements:** Dominated by smooth ellipses, flowing curves, and concentric rings.

If an artist creates an enemy boss weapon using soft circular shapes and rounded edges, it sends a contradictory signal to the player. The Art Bible enforces shape discipline.

---

### 3. The 60-30-10 Palette Architecture

Visual fatigue occurs when an environment has too many competing bright colors. Professional art directors solve this using the **60-30-10 rule**:

1. **60% Dominant Base (Background & Structural Mass):**
   - Covers large surfaces: concrete walls, terrain, floors, bulkheads, and rock formations.
   - *Rule:* Must be **desaturated and low-to-mid value**. This creates the calm backdrop against which gameplay occurs.
2. **30% Secondary Material (Props, Trim, and Architecture):**
   - Applied to secondary objects: storage containers, doorways, support beams, metal trims, and furniture.
   - *Rule:* Moderate contrast and saturation that harmonizes with the 60% base material.
3. **10% Focal Accent (Interaction, Hazards, and Narrative Signposts):**
   - Reserved strictly for high-priority gameplay cues: objective buttons, climbable traversal ledges, enemy weak points, and emergency lighting.
   - *Rule:* **Maximum saturation and high value contrast**.

```
[==================== 60% ====================][======== 30% ========][== 10% ==]
       Desaturated Environmental Base            Secondary Props & Trim    Focal Pop
```

---

### 4. PBR Material Consistency & Edge Treatment

Nothing breaks immersion faster than inconsistent surface physical properties. Your Art Bible must document:

- **Roughness Hierarchy:** Determine the roughness range for common world materials. For example: *All wet mud sits between 0.15–0.30 roughness; all unpolished stone sits between 0.75–0.90 roughness.*
- **The Edge Wear Rule:** In physically based rendering (PBR), pure CG edges (knife-sharp 90-degree corners) look fake and artificial because real manufactured objects have rounded bevels that catch specular highlights. Your style guide should specify a bevel radius standard (e.g., minimum 2cm bevel on all structural edges).
- **Weathering & Grunge Logic:** Where does dirt accumulate? *Only in concave crevices and along floor contact lines, never as a uniform cloudy noise across the entire asset.*

---

### 5. The Power of "Do's and Don'ts"

The most frequently referenced page in any studio art bible is the **Do's and Don'ts** matrix. Rather than relying on abstract paragraphs, it provides clear, concrete boundaries:

| ✓ DO (MANDATORY IN OUR ART STYLE) | ✗ DON'T (PROHIBITED IN OUR ART STYLE) |
|---|---|
| Ground all machinery with physical power cables, mounting brackets, and heavy floor bolts. | Float technological devices in mid-air without plausible mechanical support. |
| Use high-saturation amber strictly for interactive objective levers and climbable pathing. | Paint non-interactive background crates or decorative walls in saturated amber. |
| Group visual detail into dense clusters surrounded by clean resting spaces (70/30 detail balance). | Cover an entire mesh in uniform noisy panel lines or repeating procedural stamps. |
| Bevel all mechanical hard edges so light catches highlights in the Unreal Engine viewport. | Leave razor-sharp 90-degree polygon edges that break PBR specular reflections. |

---

## Quick Check

{{< quickcheck question="A 3D modeler submits a futuristic shipping container for your team's tactical, grounded vertical slice. The model is covered in bright purple neon lights, razor-sharp 90-degree corners, and has shiny chrome reflective panels everywhere. Which Art Bible rule has been violated most severely?" >}}

- **A.** The model has too few polygons to run in real-time.
- **B.** The asset violates PBR surface rules (ungrounded chrome), shape rules (sharp unbeveled edges), and the 60-30-10 palette hierarchy (loud saturated neon on a background prop).
- **C.** The texture file was exported at 1024x1024 instead of 2048x2048.
- **D.** The asset does not include a skeletal rig for character animation.

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> The asset exhibits stylistic drift across all three major Art Bible pillars: it breaks the 60-30-10 rule by using loud saturated neon on background clutter, ignores PBR edge wear conventions by using ungrounded mirror chrome, and neglects the physical bevel standard. An Art Bible exists specifically to catch and correct these inconsistencies before assets reach the game engine.
  </div>
</details>

{{< /quickcheck >}}

---

## Terms

- **Studio Art Bible** — A comprehensive design document that defines the aesthetic laws, visual pillars, material specifications, and technical standards for a game project.
- **Visual Pillars** — Three core aesthetic principles that guide all visual development and asset critique across a development team.
- **Shape Language** — The deliberate use of geometric silhouettes (squares, triangles, circles) to communicate gameplay function, personality, and faction identity.
- **60-30-10 Rule** — A visual balance guideline allocating 60% of an environment to desaturated base materials, 30% to secondary structures, and 10% to high-contrast focal accents.
- **Visual Do's and Don'ts** — An explicit side-by-side standard showing acceptable versus prohibited artistic executions to prevent stylistic drift.
- **Edge Wear Logic** — The practice of concentrating surface damage and paint chipping along exposed convex edges and contact points rather than applying uniform noise.

---

## Next

- [Color Scripting and Mood](/m/DESN-201/) (`DESN-201`)
- [Art Style Guide Assignment](/assignments/art-style-guide/) (`art-style-guide`)
