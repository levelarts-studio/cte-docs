import os

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\learn"

char_dir = os.path.join(base_dir, "character")
anim_dir = os.path.join(base_dir, "animation")

os.makedirs(char_dir, exist_ok=True)
os.makedirs(anim_dir, exist_ok=True)

# 1. 3D Character Design _index.md
char_index = """---
title: 3D Character Design
type: docs
description: Character modeling, sculpt blockouts, quad topology, armor modeling, hair cards, and skin texturing.
weight: 35
---

Textbook modules for **3D Character Design** organized from basic proportion blockouts to advanced deformation topology and hair card creation.

## Tier 100 — Character Foundations

{{< cards >}}
  {{< card
    link="/learn/character/character-concept-and-proportions/"
    title="CHAR-101: Character Proportions & Silhouette"
    subtitle="Anatomy ratios, 8-heads rule, landmark points, and silhouette readability."
    tag="STUB"
    tagColor="amber"
  >}}
  {{< card
    link="/learn/character/base-mesh-sculpt-blockout/"
    title="CHAR-102: Sculpt Blockout & Base Meshes"
    subtitle="Dynamic topology, dyna-mesh, torso blockout, and limb assembly in Blender."
    tag="STUB"
    tagColor="amber"
  >}}
{{< /cards >}}

## Tier 200 — Topology & Anatomy

{{< cards >}}
  {{< card
    link="/learn/character/facial-structure-and-anatomy/"
    title="CHAR-201: Facial Structure & Planes"
    subtitle="Zygomatic arch, jawline, eye sockets, and planar head construction."
    tag="STUB"
    tagColor="amber"
  >}}
  {{< card
    link="/learn/character/character-topology-and-deform-flow/"
    title="CHAR-202: Deformable Character Topology"
    subtitle="Shoulder loops, elbow rings, knee bend loops, and quad retopology."
    tag="STUB"
    tagColor="amber"
  >}}
{{< /cards >}}

## Tier 300 — Clothing, Armor & Hair

{{< cards >}}
  {{< card
    link="/learn/character/costume-clothing-and-armor-modeling/"
    title="CHAR-301: Clothing & Armor Modeling"
    subtitle="Cloth simulation, hard-surface armor plates, straps, and seams."
    tag="STUB"
    tagColor="amber"
  >}}
  {{< card
    link="/learn/character/hair-cards-and-grooming/"
    title="CHAR-302: Hair Cards & Alpha Textures"
    subtitle="Hair strand baking, card placement, hair curves, and game-ready hair."
    tag="STUB"
    tagColor="amber"
  >}}
{{< /cards >}}

## Tier 400 — Skin & PBR Texturing

{{< cards >}}
  {{< card
    link="/learn/character/skin-and-character-pbr-texturing/"
    title="CHAR-401: Skin & Character Texturing"
    subtitle="Subsurface scattering, pore detail, color zones, and eye materials."
    tag="STUB"
    tagColor="amber"
  >}}
{{< /cards >}}
"""

with open(os.path.join(char_dir, "_index.md"), "w", encoding="utf-8") as f:
    f.write(char_index)

# 2. Game Animation _index.md
anim_index = """---
title: Game Animation
type: docs
description: 3D keyframe animation, biped rigging, walk cycles, combat actions, and Unreal Anim Blueprints.
weight: 36
---

Textbook modules for **Game Animation** organized from fundamental timing principles to real-time Unreal Anim Blueprints.

## Tier 100 — Animation Foundations

{{< cards >}}
  {{< card
    link="/learn/animation/principles-of-animation-in-3d/"
    title="ANIM-101: 12 Principles in 3D"
    subtitle="Squash and stretch, anticipation, staging, follow through, and slow in/out."
    tag="STUB"
    tagColor="amber"
  >}}
  {{< card
    link="/learn/animation/keyframing-and-graph-editor/"
    title="ANIM-102: Graph Editor & Interpolation"
    subtitle="Bezier handles, constant/linear/bezier interpolation, and graph curves."
    tag="STUB"
    tagColor="amber"
  >}}
{{< /cards >}}

## Tier 200 — Rigging & Locomotion

{{< cards >}}
  {{< card
    link="/learn/animation/biped-rigging-and-weight-painting/"
    title="ANIM-201: Biped Rigging & Weight Painting"
    subtitle="Armature bones, IK/FK constraints, vertex weights, and skinning."
    tag="STUB"
    tagColor="amber"
  >}}
  {{< card
    link="/learn/animation/idle-and-locomotion-cycles/"
    title="ANIM-202: Walk & Run Cycles"
    subtitle="Contact points, passing poses, peak heights, and loopable locomotion."
    tag="STUB"
    tagColor="amber"
  >}}
{{< /cards >}}

## Tier 300 — Action & Combat

{{< cards >}}
  {{< card
    link="/learn/animation/combat-and-action-poses/"
    title="ANIM-301: Action Poses & Impact Keying"
    subtitle="Key poses, line of action, hit pauses, and weight distribution."
    tag="STUB"
    tagColor="amber"
  >}}
{{< /cards >}}

## Tier 400 — Engine Integration

{{< cards >}}
  {{< card
    link="/learn/animation/animation-blueprints-and-blendspaces/"
    title="ANIM-401: Anim Blueprints & Blendspaces"
    subtitle="State machines, 1D/2D blendspaces, locomotion states, and montages."
    tag="STUB"
    tagColor="amber"
  >}}
{{< /cards >}}
"""

with open(os.path.join(anim_dir, "_index.md"), "w", encoding="utf-8") as f:
    f.write(anim_index)

# Create stub module files for character and animation
char_modules = [
    ("character-concept-and-proportions.md", "CHAR-101", "Character Proportions & Silhouette", "3D Character Design", 10),
    ("base-mesh-sculpt-blockout.md", "CHAR-102", "Sculpt Blockout & Base Meshes", "3D Character Design", 20),
    ("facial-structure-and-anatomy.md", "CHAR-201", "Facial Structure & Planes", "3D Character Design", 30),
    ("character-topology-and-deform-flow.md", "CHAR-202", "Deformable Character Topology", "3D Character Design", 40),
    ("costume-clothing-and-armor-modeling.md", "CHAR-301", "Clothing & Armor Modeling", "3D Character Design", 50),
    ("hair-cards-and-grooming.md", "CHAR-302", "Hair Cards & Alpha Textures", "3D Character Design", 60),
    ("skin-and-character-pbr-texturing.md", "CHAR-401", "Skin & Character Texturing", "3D Character Design", 70)
]

anim_modules = [
    ("principles-of-animation-in-3d.md", "ANIM-101", "12 Principles in 3D", "Game Animation", 10),
    ("keyframing-and-graph-editor.md", "ANIM-102", "Graph Editor & Interpolation", "Game Animation", 20),
    ("biped-rigging-and-weight-painting.md", "ANIM-201", "Biped Rigging & Weight Painting", "Game Animation", 30),
    ("idle-and-locomotion-cycles.md", "ANIM-202", "Walk & Run Cycles", "Game Animation", 40),
    ("combat-and-action-poses.md", "ANIM-301", "Action Poses & Impact Keying", "Game Animation", 50),
    ("animation-blueprints-and-blendspaces.md", "ANIM-401", "Anim Blueprints & Blendspaces", "Game Animation", 60)
]

def write_stubs(target_dir, mods):
    for fname, code, title, subj, w in mods:
        stub_text = f"""---
id: "{code}"
title: "{title}"
subject: "{subj}"
entity: "module"
status: "stub"
tier: {100 if "10" in code else 200 if "20" in code else 300 if "30" in code else 400}
estimated_time: "25 mins"
standards: ["AV.17.1"]
weight: {w}
type: docs
description: "{code}: {title} textbook module stub."
summary: "{code}: {title} textbook module stub."
---

{{< callout type="warning" >}}
**Lesson Under Construction**: This module is currently a stub spec. Press **Ctrl + K** to search active tools and topics.
{{< /callout >}}

## What you'll be able to do

- Understand core concepts of **{title}**.
- Demonstrate hands-on workflow steps in production software.
- Produce a portfolio artifact meeting rubrics and CTE standards.

## Try it

{{% steps %}}

### Step 1 — Key Concepts & Tools
Review the core principles and tool shortcuts for this lesson.

### Step 2 — Practice Exercise
Follow along in software to build the exercise file.

### Step 3 — Self Check & Review
Verify your results against the rubric criteria.

{{% /steps %}}
"""
        with open(os.path.join(target_dir, fname), "w", encoding="utf-8") as f:
            f.write(stub_text)

write_stubs(char_dir, char_modules)
write_stubs(anim_dir, anim_modules)

print("Created 3D Character Design and Game Animation libraries with 13 new modules!")