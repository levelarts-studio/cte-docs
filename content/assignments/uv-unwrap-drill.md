---
id: uv-unwrap-drill
title: "UV Unwrap & Texel Density Drill"
entity: assignment
tier: 200
status: complete
requires: ["BLND-204"]
standards: ["GD.17.4", "AV.17.8"]
evidence_for: "GD.17.4"
portfolio: true
portfolio_section: "GAD1 U2"
est_time: 90
setting: lab
aliases: ["/a/uv-unwrap-drill"]
---

## The task

Download the production-standard **Low-Poly Male Human** 3D model, import it into Blender, diagnose its form, strategically mark seams on the character geometry, unwrap all body segments into clean 2D UV islands, equalize texel density across the entire mesh, and pack the islands into the 0–1 UV coordinate space with proper margin padding. 

Finally, apply a high-contrast UV checker grid texture to verify zero visible stretching or distortion, and document your results for your portfolio.

This exercise transitions you from simple primitive unwraps to character and organic asset pipelines. Unwrapping a humanoid mesh requires strategic seam placement along natural body contours, balancing island resolution, and preventing pixel bleed.

---

## Before you start

- [Topology and Edge Flow](/m/BLND-201/) (`BLND-201`)
- [UV Unwrapping](/m/BLND-204/) (`BLND-204`)

{{< callout type="info" >}}
**Required Asset Download**:
- **Model:** [**Human (Low Poly Male Human 3D Model)** on Sketchfab](https://sketchfab.com/3d-models/human-03a70758739544b3aa705c13af3872b1)
- **Author:** [aaron.kalvin](https://sketchfab.com/aaron.kalvin)
- **Format:** FBX (or glTF / OBJ)
- **License:** Creative Commons Attribution ([CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)) — *Remember to credit the author in your portfolio documentation.*
{{< /callout >}}

---

## Visual Reference Guide

Keep these three core principles in mind as you work through the drill:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">

<div style="border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.5rem; padding: 1rem; background: rgba(255, 255, 255, 0.02); display: flex; flex-direction: column;">
  <img src="/images/uv/character-seam-placement.jpg" alt="Character Seam Placement Reference" style="width: 100%; height: 170px; object-fit: cover; border-radius: 0.375rem; margin-bottom: 0.75rem;" />
  <h3 style="margin: 0.25rem 0 0.5rem; font-size: 1.05rem; color: #818cf8;">1. Seam Placement Strategy</h3>
  <p style="font-size: 0.85rem; opacity: 0.85; margin-bottom: 0.5rem;">Place cuts along natural occlusions and interior contours (leg inseams, underarms, torso sides, center-back skull) so front-facing camera views remain seamless.</p>
</div>

<div style="border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.5rem; padding: 1rem; background: rgba(255, 255, 255, 0.02); display: flex; flex-direction: column;">
  <img src="/images/uv/uv-distortion-checker.jpg" alt="UV Distortion Checker Comparison" style="width: 100%; height: 170px; object-fit: cover; border-radius: 0.375rem; margin-bottom: 0.75rem;" />
  <h3 style="margin: 0.25rem 0 0.5rem; font-size: 1.05rem; color: #818cf8;">2. Zero Distortion Verification</h3>
  <p style="font-size: 0.85rem; opacity: 0.85; margin-bottom: 0.5rem;">Use a generated UV checker texture. Checkers must be square, upright, and uniform in size across every body part without pinching or diagonal shear.</p>
</div>

<div style="border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.5rem; padding: 1rem; background: rgba(255, 255, 255, 0.02); display: flex; flex-direction: column;">
  <img src="/images/uv/uv-packing-islands.jpg" alt="UV Packing and Margin Padding" style="width: 100%; height: 170px; object-fit: cover; border-radius: 0.375rem; margin-bottom: 0.75rem;" />
  <h3 style="margin: 0.25rem 0 0.5rem; font-size: 1.05rem; color: #818cf8;">3. Island Packing & Margins</h3>
  <p style="font-size: 0.85rem; opacity: 0.85; margin-bottom: 0.5rem;">Fit all islands strictly within the 0–1 UV coordinate bounds. Maintain a 16–32px island margin (padding) to prevent mipmap texture bleeding.</p>
</div>

</div>

---

## Steps

{{% steps %}}

### Step 1 — Download and import the FBX

1. Navigate to the model page on Sketchfab: [**Low Poly Male Human 3D Model**](https://sketchfab.com/3d-models/human-03a70758739544b3aa705c13af3872b1).
2. Click **Download 3D Model**, log in (free account), and choose the **FBX** format (or glTF if FBX is unavailable).
3. Extract the downloaded zip file into your local project directory under `01_Projects/SourceAssets/`.
4. Open Blender: **File > New > General**. Delete the default cube.
5. Go to **File > Import > FBX (.fbx)** and select the downloaded human model.
6. Save your file immediately as `LASTNAME_UV_Unwrap_Drill_v01.blend` in your `01_Projects` directory.

### Step 2 — Reset transforms and prepare the mesh

> [!IMPORTANT]
> **Always apply object scale before unwrapping!** If an object's scale in the Transform panel is anything other than `(1.0, 1.0, 1.0)`, Blender will stretch your UV projection regardless of where you place your seams.

1. In **Object Mode**, select the human mesh.
2. Press **N** to open the Sidebar and check the **Item > Transform** panel.
3. If Scale is not `(1.0, 1.0, 1.0)` or Rotation is non-zero, press **Ctrl + A → Apply All Transforms** (or **Apply Rotation & Scale**).
4. Switch to the **UV Editing** workspace using the top header tabs.
5. In the Properties panel, click the green triangle icon (**Object Data Properties**) and expand the **UV Maps** section.
6. If the downloaded model has a pre-existing broken or messy UV map, click the `-` (minus) button to delete it, then click `+` to create a fresh, clean map named `UVMap_Character`.

### Step 3 — Mark the anatomical seams

Switch to **Edit Mode** (`Tab`) and select Edge Mode (`2`). You will now mark seams on each anatomical section. Use `Alt + Left Click` to select continuous edge loops, and press **Ctrl + E → Mark Seam** (marked edges highlight in orange-red).

Work through the body systematically:

#### A. Head and Neck
- **Collar Seam:** Select the edge loop encircling the base of the neck where it meets the clavicle/trapezius muscles. Mark seam.
- **Skull Seam:** Run a vertical seam starting from the back of the neck collar, traveling up the center-back of the skull to the apex crown.
- *Check:* The face and front crown should be able to peel open forward like a mask without any seams across the forehead, nose, cheeks, or mouth.

#### B. Arms and Hands
- **Shoulder Socket:** Select the loop where the arm joins the shoulder/chest torso. Mark seam.
- **Under-Arm Inseam:** Run a seam starting at the armpit, running along the **underside** of the bicep, through the inner crease of the elbow, down the inner forearm to the wrist crease.
- **Wrist Loop:** Mark a circular loop at the wrist separating the hand from the arm tube.
- **Hand:** Run a perimeter seam along the edge of the palm and between the fingers to split the hand into top (dorsal) and bottom (palmar) islands.

#### C. Torso and Pelvis
- **Lateral Sides:** Run a vertical seam down each side of the ribcage, starting from the armpit down through the flank to the hip.
- **Shoulder Ridge:** Mark a seam across the crest of each shoulder from the neck collar to the arm socket.
- *Check:* The torso should now unfold into two clean halves: a front chest/belly island and a back island.

#### D. Legs and Feet
- **Leg Inseam:** Mark a continuous seam running along the **inside of the leg**, starting from the perineum/crotch, along the inner thigh, behind the knee, down the inner calf to the ankle.
- **Ankle Loop:** Select the circular loop encircling the ankle above the foot. Mark seam.
- **Sole of Foot:** Select the edge loop separating the sole/bottom of the foot from the top/instep.
- *Check:* Each leg unfolds into an unrolled tapered cylinder.

### Step 4 — Unwrap and inspect islands

1. In the 3D Viewport, ensure you are in Edit Mode with all faces selected (**A**).
2. Press **U → Unwrap**.
3. In the 2D **UV Editor** panel (left side), inspect the generated UV islands.
4. You should see distinct, readable islands:
   - Head / Face
   - Front Torso & Back Torso
   - Left Arm & Right Arm
   - Left Leg & Right Leg
   - Left Hand & Right Hand
   - Left Foot & Right Foot (top and soles)
5. In the UV Editor header, click **Overlays** and turn on **Display Stretch**. Verify that all islands display in solid **dark blue** or light cyan. If any island glows orange or red, orbit to that part of the mesh and add a relief cut.

### Step 5 — Equalize texel density

1. In the UV Editor, ensure all UV islands are selected (`A`).
2. Go to **UV → Average Island Scale** (Hotkey: `Ctrl + A` inside the UV Editor window).
3. Observe the islands adjusting in size: Blender automatically rescales every island relative to its actual 3D surface area. The torso will expand to reflect its volume, while smaller parts (hands, feet) will resize proportionally.

### Step 6 — Pack islands in 0–1 space with margin padding

1. With all islands selected in the UV Editor, go to **UV → Pack Islands** (Hotkey: `Ctrl + P`).
2. Open the operator popup at the bottom left (or press **F9**) and configure:
   - **Margin:** `0.015` (approximately a 16–32px gutter at 2K resolution).
   - **Rotate:** Enabled (allows Blender to rotate islands 90° for optimal bounding box packing).
   - **Shape Method:** Exact Shape (or Concave).
3. Verify the layout:
   - All islands must sit entirely inside the dark square canvas ($0.0 \le U, V \le 1.0$).
   - No two islands should touch or overlap.
   - The margin gutters between islands must be uniform.

### Step 7 — Apply the UV checker texture and diagnose

Now, test your unwrap on the 3D surface:

1. In the **Shader Editor** (or Material Properties panel), assign a new material to the character named `M_UVChecker`.
2. Add an **Image Texture** node and connect its `Color` output to the `Base Color` of the Principled BSDF.
3. Click **+ New** on the Image Texture node:
   - **Name:** `T_UV_Checker_2K`
   - **Width:** `2048`
   - **Height:** `2048`
   - **Generated Type:** Change from *Blank* to **UV Grid** (or **Color Grid**).
4. Switch your 3D Viewport to **Material Preview** (`Z → Material Preview`).
5. Orbit around the full character and conduct a visual audit:
   - **Squareness:** Are the checkers perfectly square on the torso, face, arms, and legs?
   - **Consistency:** Are the checker squares approximately the same size on the chest as they are on the thighs and calves?
   - **Seam Invisibility:** From the front view, are the visible seams minimized? Confirm that no seam cuts through the facial features.

### Step 8 — Document and submit

Capture high-resolution screenshots for your portfolio:
1. **Full-Body Checker Render/Capture:** A 3/4 perspective viewport capture showing the entire character textured with the UV checker grid.
2. **UV Editor Layout:** A clear capture of the UV Editor showing all neatly packed, non-overlapping islands within the 0–1 square.
3. **Seam Placement Close-Up:** A wireframe/Edit Mode capture showing your marked orange-red seams along the underarm or inner leg.
4. Post your captures to your Google Sites portfolio with the required reflection and Sketchfab asset attribution.

{{% /steps %}}

---

## Submit

{{< callout type="warning" >}}
**Google Sites Portfolio Deliverable**:
Upload your documentation to your Google Sites portfolio under **Coursework > Unit 2: Materials, UVs & Texturing**:
1. **Title:** Module 2.1 — UV Unwrapping & Texel Density Drill
2. **Three Screenshots:**
   - Full-body 3/4 beauty view with UV Grid applied
   - 2D UV Editor island packing layout (0–1 space)
   - Close-up showing hidden seam placement (in-engine or viewport)
3. **Asset Attribution:** Credit the source model with a live link: *Model: Low Poly Male Human by aaron.kalvin via Sketchfab (CC BY 4.0).*
4. **Written Reflection (3–4 sentences):**
   - *Why is it critical to apply object transforms (`Ctrl + A → Scale`) before unwrapping?*
   - *What tool did you use to normalize texel density across the head, torso, and limbs?*
   - *Why do game artists leave margin padding between UV islands?*
{{< /callout >}}

---

## Rubric

### Assessment Rubric

| Criteria | Proficient (4-5 pts) | Developing (2-3 pts) | Beginning (0-1 pt) |
|---|---|---|---|
| **Strategic Seam Placement** | Seams are placed thoughtfully along natural anatomical lines and occlusions (inner legs, underarms, back of head). No visible seams cut across the face or primary front surfaces. | Seams mostly relieve tension, but 1–2 cuts run across visible front areas or cause minor awkward splits. | Random or missing seams; seams cut directly across focal areas like the face or chest. |
| **Distortion & Checker Grid Uniformity** | UV checker squares are uniformly square across all body parts with no pinching, skewing, or severe stretching. Scale was applied prior to unwrapping. | Minor stretching or diagonal shearing in complex regions (hands, feet, shoulders), but main body is readable. | Heavy distortion, oblong rectangular checkers, severe pinching at poles, or scale unapplied. |
| **Texel Density Optimization** | Texel density is equalized across all islands using `Average Island Scale`. Checkers are proportionally sized from head to toe. | Slight mismatch in island scale between extremities and torso, but overall resolution is acceptable. | Grossly mismatched texel density (e.g., massive blurry checkers on head and tiny sharp checkers on legs). |
| **Island Packing & Margins (0–1 Space)** | All islands are packed tightly inside the 0–1 UV coordinate space with consistent 16–32px margin padding. No overlapping geometry or boundary clipping. | Islands are packed within 0–1 space, but margins are inconsistent (some islands touching) or space is poorly utilized. | Overlapping UV islands, geometry placed outside 0–1 space, or zero margin causing mipmap bleeding. |
| **Documentation & Attribution** | Portfolio post contains all 3 required screenshots, full Creative Commons attribution link for the Sketchfab model, and an insightful technical reflection. | Screenshots included, but missing model attribution link or reflection is superficial. | Missing portfolio post, incomplete screenshots, or unsubmitted assignment. |

---

## Notes & Pro-Tips

- **The #1 Student Mistake is Forgetting Scale:** If you scale an object in Object Mode, Blender stores an internal multiplier ($X=1.0, Y=1.0, Z=2.0$). When you unwrap, Blender calculates 2D coordinates using the unscaled mesh, creating stretched checkers. Always press **Ctrl + A → Apply All Transforms** before unwrapping!
- **Pinning Vertices:** If an island keeps twisting during unwrapping, select two vertices in the UV Editor, press **P** to pin them, and re-unwrap (`U`). Pinned vertices stay locked in place while the rest of the island relaxes around them. Press **Alt + P** to unpin.
- **UV Synchronization:** Toggle the **UV Sync Selection** button (two diagonal arrows in the top-left of the UV Editor). When enabled, selecting a face or edge in the 3D viewport instantly highlights its corresponding UV polygon in the UV Editor, making it effortless to identify which island belongs to which body part.
- **Creative Commons Compliance:** In industry, legal asset tracking is mandatory. Whenever you use a third-party base mesh, you must verify its license terms and maintain an attribution trail in your project files.
