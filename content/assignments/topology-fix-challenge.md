---
id: topology-fix-challenge
title: "Topology Fix Challenge"
entity: assignment
tier: 200
status: complete
requires: ["BLND-201"]
standards: ["GD.17.4", "4.3", "AV.17.8"]
evidence_for: "GD.17.4"
portfolio: true
portfolio_section: "GAD1 U1"
est_time: 90
setting: lab
aliases: ["/a/topology-fix-challenge"]
---

## The task

You'll be given a 3D mesh that's deliberately broken: a combination of non-manifold edges, open boundary holes, internal faces, n-gons, a badly placed pole, doubled vertices, and flipped normals. Find every problem, fix it, and prove the mesh is clean.

This is a diagnostic exercise. The value is in finding problems you didn't create, which is a different skill than avoiding them in your own work, and it's the skill that will let you rescue a downloaded or teammate-built asset later this year.

## Before you start

Read [Topology and Edge Flow](/learn/blender/topology-and-edge-flow/) (`BLND-201`).

{{< callout type="info" >}}
**Starter Script Download**: Download the generator script [**`generate_topology_challenge_file.py`**](/downloads/generate_topology_challenge_file.py) to generate your exercise asset inside Blender.
{{< /callout >}}

---

## Steps

{{% steps %}}

### Step 1 — Run the generator script

1. Open Blender: **File > New > General**.
2. Switch to the **Scripting** workspace (tab along top header).
3. In the Text Editor panel, click **Open** and select `generate_topology_challenge_file.py` (or click **New** and paste the code in).
4. Click the **Run Script** button (play icon).
5. Switch to the **Modeling** or **Layout** workspace. You will see a sci-fi pedestal console named `Broken_Console_Prop`.
6. Immediately save your file as `LASTNAME_TopologyChallenge_v01.blend` in your `01_Projects` directory.

> [!CAUTION]
> **Look at it first. Do not fix anything yet.** Before-and-after proof is required for your portfolio write-up.

### Step 2 — Diagnose before touching anything

Take diagnostic screenshots while the mesh is still broken:
1. **Shaded View:** Take a screenshot of the mesh from an angle showing the visible shading pinch or faceted distortion.
2. **Non-Manifold Check:** Tab into Edit Mode (`Tab`), ensure nothing is selected (`Alt + A`), then choose **Select → All by Trait → Non-Manifold**. Take a screenshot showing the highlighted orange edges and open boundaries.
3. **Face Orientation Check:** Open the **Viewport Overlays** dropdown and check **Face Orientation**. Take a screenshot showing any inverted red faces against the blue mesh.

### Step 3 — List what you found

Before fixing anything, write a numbered list in your notes:
- How many separate problem areas did you identify?
- What type is each flaw? (e.g., *Non-manifold edge shared by 3 faces, unsealed boundary hole, loose floating vertex/edge, 6-sided n-gon, 5-edge pole, inverted face normal, coincident doubled vertices*).

You will use this checklist to verify your repairs at the end.

### Step 4 — Fix the non-manifold geometry

Work through the structural flaws first:
1. **Delete Loose:** In Edit Mode, select all (`A`), go to **Mesh → Clean Up → Delete Loose** to purge stray unattached vertices and floating wire edges.
2. **Merge by Distance:** Press **M → By Distance** to weld overlapping vertices sitting at the same coordinates. Notice the status message at the bottom confirming how many duplicate vertices were removed.
3. **Remove Internal Faces:** If an internal face is trapped inside, switch to Face select (`3`), select the internal face, and press **X → Faces**.
4. **Seal Open Holes:** Select the boundary loop around the open side hole (Alt + click the rim edge) and press **F** to fill, or use **Face → Grid Fill** for clean quad subdivisions.

*Check your work:* Re-run **Select → All by Trait → Non-Manifold**. The selection should be significantly reduced or completely clear.

### Step 5 — Fix n-gons and problem poles

1. **Resolve N-Gons:** Find the 6-sided n-gon on the angled console face. Use the **Knife tool (`K`)** or select opposite vertices and press **J** (Join Vertices) to split the n-gon into clean four-sided quads.
2. **Reroute Problem Poles:** Inspect the front bumper where 5 edges converge into a pole. Use loop cuts or edge rotation to redirect the edge flow so the pole does not sit directly on a visible bend or high-specular curve.

### Step 6 — Fix normals

1. Keep the **Face Orientation** overlay active.
2. Select all faces (`A`) and press **Shift + N** (**Mesh → Normals → Recalculate Outside**).
3. Confirm that every exterior surface of the model is solid **blue**. No red or pink faces should be visible anywhere.

### Step 7 — Confirm it's clean

Run your final verification tests:
1. Deselect everything (`Alt + A`).
2. Run **Select → All by Trait → Non-Manifold**.
3. **Blender should select zero edges.** Take a screenshot of your 3D viewport showing that nothing lights up. This is your deliverable proof of a watertight, manifold asset.
4. Temporarily add a **Subdivision Surface modifier** (`Ctrl + 2`). Orbit around and verify that the surface smooths cleanly without ugly pinching, creases, or black shading tears.

### Step 8 — Write it up

Create a post on your Google Sites portfolio **Coursework** page with:
- Your "before" screenshots (showing non-manifold highlights and red flipped normals).
- Your diagnostic checklist of flaws identified.
- Your "after" screenshots (showing all blue face orientation, clean wireframe quad flow, and the empty Select Non-Manifold confirmation).
- A 2–3 sentence reflection: *Which topology flaw was hardest to spot, and what tool revealed it?*

{{% /steps %}}

---

## Submit

{{< callout type="info" >}}
**Google Classroom Submission**: Post the direct link to your published Google Sites portfolio **Coursework** page in Google Classroom. Keep your repaired `.blend` file saved in your `01_Projects` directory.
{{< /callout >}}

---

## Rubric

### Assessment Rubric

| Criteria | Proficient (4-5 pts) | Developing (2-3 pts) | Beginning (0-1 pt) |
|---|---|---|---|
| **Diagnosis & Documentation** | Thorough before-and-after documentation; accurate inventory checklist identifying all planted flaws prior to repair. | Partial documentation; missed 1 or 2 flaws in the diagnostic list or missing initial screenshots. | Incomplete documentation; no before screenshots or diagnostic list. |
| **Non-Manifold Repair** | All non-manifold edges, T-junctions, unsealed boundary holes, doubled vertices, and loose elements completely fixed. Final `Select Non-Manifold` selects 0 edges. | Most non-manifold issues resolved, but 1 boundary hole or doubled vertex remains. | Mesh remains non-manifold with multiple broken edges or holes. |
| **Quad Topology & Edge Flow** | All n-gons resolved into quad-dominant topology; problem poles rerouted away from prominent curvature; mesh subdivides cleanly without pinching. | N-gons converted with haphazard triangles; minor pinching visible under subdivision. | N-gons left unaddressed; severe shading artifacts and pinched geometry under subdivision. |
| **Normal Consistency** | 100% of face normals recalculated outside; verified entirely blue in Face Orientation overlay with zero flipped faces. | Most faces oriented correctly, but an interior or recessed face remains inverted red. | Inverted normals remain unfixed; shading appears reversed or inside-out. |
| **Portfolio Presentation** | Well-organized portfolio post with clear headings, labeled comparison screenshots, and insightful reflection on diagnostic tools. | Portfolio post contains images but lacks descriptive labels or reflection write-up. | Not submitted to Google Sites portfolio. |

---

## Notes

- **Screenshot before you fix anything.** A repaired mesh proves you can fix problems. Before-and-after proves you can find them, which is the actual point of this assignment.
- **This mesh could be someone else's work.** In GAD2 you will receive assets other students built, and in the game industry you will receive assets outsourced or created by teammates. This diagnostic exercise is a rehearsal for real studio pipeline QA, not a punishment for mistakes.
