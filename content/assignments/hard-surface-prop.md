---
id: hard-surface-prop
title: "Hard Surface Prop 1: Blockout"
entity: assignment
tier: 100
status: complete
requires: ["BLND-104", "BLND-105"]
standards: ["GD.17.4", "AV.17.8", "10.4"]
evidence_for: "GD.17.4"
portfolio: true
portfolio_section: "GAD1 U1"
est_time: 90
setting: lab
aliases: ["/a/hard-surface-prop"]
---

## The task

Build one low-poly hard surface prop using edit mode tools and non-destructive modifiers. Something mechanical or constructed: a weapon, a piece of equipment, a vehicle part, a container, or a device.

This is a blockout. The goal is a clean, correctly proportioned shape with good edge flow, not a finished, textured asset. That comes later.

## Before you start

- [Edit Mode Basics](/m/BLND-104/) (`BLND-104`)
- [Modifiers Introduction](/m/BLND-105/) (`BLND-105`)

---

## Prop Examples & Reference Ideas

If you aren't sure what to build, choose one of these classic hard-surface props. Each one tests a specific combination of edit mode cuts and modifier workflows:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">

<div style="border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.5rem; padding: 1rem; background: rgba(255, 255, 255, 0.02); display: flex; flex-direction: column;">
  <img src="/images/props/walkie-talkie.jpg" alt="Field Walkie-Talkie" style="width: 100%; height: 180px; object-fit: cover; border-radius: 0.375rem; margin-bottom: 0.75rem;" />
  <h3 style="margin: 0.25rem 0 0.5rem; font-size: 1.1rem; color: #818cf8;">1. Tactical Walkie-Talkie</h3>
  <p style="font-size: 0.875rem; opacity: 0.85; margin-bottom: 0.5rem;">A handheld radio with distinct functional elements: beveled main housing, recessed display, inset speaker grill, antenna cylinder, and volume knobs.</p>
  <ul style="font-size: 0.85rem; padding-left: 1.2rem; margin: 0; opacity: 0.9;">
    <li><strong>Base Shape:</strong> Cube scaled on Z</li>
    <li><strong>Edit Mode:</strong> <code>I</code> to inset speaker grill & screen, <code>E</code> to extrude knobs & antenna, <code>Ctrl+R</code> for grip grooves</li>
    <li><strong>Modifiers:</strong> <code>Bevel</code> (casing edges), <code>Mirror</code> (symmetric chassis)</li>
  </ul>
</div>

<div style="border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.5rem; padding: 1rem; background: rgba(255, 255, 255, 0.02); display: flex; flex-direction: column;">
  <img src="/images/props/tactical-case.jpg" alt="Reinforced Equipment Case" style="width: 100%; height: 180px; object-fit: cover; border-radius: 0.375rem; margin-bottom: 0.75rem;" />
  <h3 style="margin: 0.25rem 0 0.5rem; font-size: 1.1rem; color: #818cf8;">2. Reinforced Hard Case</h3>
  <p style="font-size: 0.875rem; opacity: 0.85; margin-bottom: 0.5rem;">A Pelican-style equipment crate. High structural visual interest with molded ridges, latches, corner protectors, and heavy carry handles.</p>
  <ul style="font-size: 0.85rem; padding-left: 1.2rem; margin: 0; opacity: 0.9;">
    <li><strong>Base Shape:</strong> Flattened Cube</li>
    <li><strong>Edit Mode:</strong> <code>Ctrl+R</code> loop cuts across the lid, <code>E</code> to pull out reinforcing ribs, <code>I</code> for recessed latch pockets</li>
    <li><strong>Modifiers:</strong> <code>Mirror</code> (X and Y symmetry), <code>Bevel</code> (rounded bumper edges)</li>
  </ul>
</div>

<div style="border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.5rem; padding: 1rem; background: rgba(255, 255, 255, 0.02); display: flex; flex-direction: column;">
  <img src="/images/props/fire-hydrant.jpg" alt="Municipal Fire Hydrant" style="width: 100%; height: 180px; object-fit: cover; border-radius: 0.375rem; margin-bottom: 0.75rem;" />
  <h3 style="margin: 0.25rem 0 0.5rem; font-size: 1.1rem; color: #818cf8;">3. Municipal Fire Hydrant</h3>
  <p style="font-size: 0.875rem; opacity: 0.85; margin-bottom: 0.5rem;">A classic cylindrical hard-surface test. Features stepped diameter flanges, domed top cap, pentagonal operating nut, and side nozzle ports.</p>
  <ul style="font-size: 0.85rem; padding-left: 1.2rem; margin: 0; opacity: 0.9;">
    <li><strong>Base Shape:</strong> 16-sided Cylinder</li>
    <li><strong>Edit Mode:</strong> <code>E</code> + <code>S</code> to extrude flanges, <code>Ctrl+R</code> for ring control</li>
    <li><strong>Modifiers:</strong> <code>Boolean Difference</code> (side nozzles or bolt holes), <code>Bevel</code> (cast iron rim highlights)</li>
  </ul>
</div>

<div style="border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.5rem; padding: 1rem; background: rgba(255, 255, 255, 0.02); display: flex; flex-direction: column;">
  <img src="/images/props/security-camera.jpg" alt="Security Camera" style="width: 100%; height: 180px; object-fit: cover; border-radius: 0.375rem; margin-bottom: 0.75rem;" />
  <h3 style="margin: 0.25rem 0 0.5rem; font-size: 1.1rem; color: #818cf8;">4. Security Camera / Sensor</h3>
  <p style="font-size: 0.875rem; opacity: 0.85; margin-bottom: 0.5rem;">Combines angular mounting brackets with cylindrical optic housing, sun visor shield, and a multi-axis swivel joint.</p>
  <ul style="font-size: 0.85rem; padding-left: 1.2rem; margin: 0; opacity: 0.9;">
    <li><strong>Base Shape:</strong> Cylinder body + Cube mounting arm</li>
    <li><strong>Edit Mode:</strong> <code>I</code> and <code>E</code> inward for camera lens aperture, <code>Ctrl+R</code> to bevel elbow joints</li>
    <li><strong>Modifiers:</strong> <code>Solidify</code> (sun shield canopy), <code>Bevel</code> (machined chassis edges)</li>
  </ul>
</div>

<div style="border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.5rem; padding: 1rem; background: rgba(255, 255, 255, 0.02); display: flex; flex-direction: column;">
  <img src="/images/props/ammo-box.jpg" alt="Military Ammo Crate" style="width: 100%; height: 180px; object-fit: cover; border-radius: 0.375rem; margin-bottom: 0.75rem;" />
  <h3 style="margin: 0.25rem 0 0.5rem; font-size: 1.1rem; color: #818cf8;">5. Military Ammo Crate</h3>
  <p style="font-size: 0.875rem; opacity: 0.85; margin-bottom: 0.5rem;">Sturdy sheet metal canister with stamped indents, clamping latch, perimeter seal rim, and top folding wire handle.</p>
  <ul style="font-size: 0.85rem; padding-left: 1.2rem; margin: 0; opacity: 0.9;">
    <li><strong>Base Shape:</strong> Rectangular Cube</li>
    <li><strong>Edit Mode:</strong> <code>I</code> and slight negative <code>E</code> for stamped side recesses, loop cuts for rim lip</li>
    <li><strong>Modifiers:</strong> <code>Mirror</code> (symmetrical half), <code>Bevel</code>, <code>Solidify</code> (sheet metal brackets)</li>
  </ul>
</div>

</div>

---

## Steps

{{% steps %}}

### Step 1 — Pick a prop and gather reference

Choose something with clear mechanical shapes: flat panels, cylindrical sections, and a couple of raised or recessed details. You can pick from the examples above or choose your own prop (e.g., a sci-fi power cell, wall electrical box, or sci-fi door lock).

Find **two or three reference photos from different angles** before opening Blender. Save them to your `00_Reference` folder or load them into PureRef.

### Step 2 — Block the base form

Start from a primitive close to the object's overall silhouette (usually a Cube or Cylinder). Get the primary proportions right before adding any cuts or detail. Compare against your reference photos constantly.

Remember to set your primitive's initial vertex or segment count in the **F9** operator panel when you first create it.

### Step 3 — Build out the detail

Switch to **Edit Mode** (`Tab`). Using extrude, inset, and loop cuts, build out the secondary shapes:
- **Inset (`I`)** to create panel borders, recessed screens, and structural rims.
- **Extrude (`E`)** to push out knobs, raised handles, vents, and housings.
- **Loop Cut (`Ctrl + R`)** to add edge loops where shapes need to step or bend.

*Tip:* If the prop is symmetric, delete half the mesh, set the object origin on the centerline seam, and add a **Mirror modifier**.

### Step 4 — Apply your modifiers with intention

Add modifiers non-destructively to shape and polish the mesh:
- Add a **Bevel modifier** to catch light along the hard edges without permanently baking geometry.
- If using **Subdivision Surface**, place supporting loop cuts close to sharp corners to keep key mechanical edges crisp.
- If using a **Boolean** modifier to cut holes or ports, inspect the cut in Edit Mode to ensure geometry remains intact.

**Keep modifiers live and unapplied in your modifier stack.**

### Step 5 — Clean the mesh

Run a cleanup pass on your model:
1. In Edit Mode, select all vertices (`A`) and press **M → By Distance** to weld any duplicate vertices.
2. Turn on **Face Orientation** in the Viewport Overlays dropdown. Ensure the entire exterior of your mesh is blue (pointing outwards). If any faces are red, select all and press **Shift + N** to recalculate normals outside.
3. Check for non-manifold edges, stray floating vertices, or overlapping coplanar faces.

### Step 6 — Check the silhouette

Test your model's readability:
- Switch your viewport shading to flat or matcap silhouette mode (or apply a temporary matte dark material).
- Orbit around and inspect the front, side, top, and 3/4 perspective views.
- Does the prop immediately read as what it's supposed to be without textures or colors? If not, adjust primary proportions before moving on.

### Step 7 — Render and post

1. Set up a simple 3-point lighting rig and a clean backdrop plane in Blender.
2. Frame a camera view that highlights the prop's most interesting angles and surface relief.
3. Render a clean still image (`F12`).
4. Take a viewport screenshot with **Wireframe** or modifier settings visible to show your non-destructive stack.
5. Post your work to your **Google Sites Portfolio** on your **Coursework** page with the standard write-up, your reference images, and a brief reflection.

{{% /steps %}}

---

## Submit

{{< callout type="info" >}}
**Google Classroom Submission**: Post the direct link to your published Google Sites portfolio **Coursework** page in Google Classroom. Keep your `.blend` file (with all modifiers live and unapplied) saved in your project folder (`01_Projects`).
{{< /callout >}}

---

## Rubric

### Assessment Rubric

| Criteria | Proficient (4-5 pts) | Developing (2-3 pts) | Beginning (0-1 pt) |
|---|---|---|---|
| **Edit Mode Construction** | Cleanly utilizes Extrude (`E`), Inset (`I`), and Loop Cuts (`Ctrl+R`) to build accurate secondary forms and mechanical surface details. | Relies on basic transforms with limited inset/extrusion; some awkward geometry or uneven edge flow. | Missing secondary detail; geometry built incorrectly or primitives unedited. |
| **Non-Destructive Modifiers** | Modifiers (Bevel, Mirror, Boolean, Solidify) are configured thoughtfully in the stack and left **live/unapplied**. Origins properly aligned for mirroring. | Modifiers applied prematurely, or stack order causes visible artifacts/shading pinching. | No modifiers used, or destructive tools applied without non-destructive controls. |
| **Mesh Cleanliness & Topology** | No duplicate/overlapping vertices (`Merge by Distance` applied); normals point consistently outward; no non-manifold holes or broken geometry. | A few doubled vertices or minor inverted normals; slight shading artifacts around cuts. | Significant topology errors, doubled vertices, inverted normals, or degenerate faces. |
| **Proportion & Silhouette Readability** | Prop silhouette reads immediately from multiple viewpoints (front, side, 3/4); proportions closely match real-world reference. | Silhouette reads from one primary angle but appears distorted or disproportionate from other views. | Prop silhouette is unrecognizable or proportions clash heavily with real-world reference. |
| **Portfolio & Documentation** | Portfolio post includes final render, viewport wireframe showing modifier stack, reference images, and a written reflection on modifier choices. | Portfolio post contains render and basic write-up, but lacks reference images or modifier stack proof. | Missing portfolio post or incomplete deliverable. |

---

## Notes

- **Keep modifiers unapplied when you submit.** Part of what's being evaluated is whether you used them non-destructively rather than committing early. You will learn when applying is appropriate in a later unit.
- **A messy Boolean is the most common way this assignment goes wrong.** If a Boolean cut looks fine in shaded view but creates jagged triangulation or overlapping edges in Edit Mode, don't ignore it. Clean geometry now saves real pain when this prop gets UV unwrapped in the next unit.
- **Real hard surfaces have rounded edges.** Perfectly sharp 90-degree computer graphics edges look fake because real objects have microscopic bevels that catch highlights. A subtle Bevel modifier makes your blockout look tangible and grounded.
