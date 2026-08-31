import os

out_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\standards"

anchor_md = """---
title: AME Anchor Standards (1.0 - 12.0)
type: docs
description: California AME Anchor Standards covering essential 21st century skills, literacy, and career readiness.
weight: 2
---

The twelve **Anchor Standards (1.0–12.0)** build on the California Standards for Career Ready Practice and are common across all CTE industry sectors.

{{< callout type="info" >}}
Anchor Standards emphasize essential 21st century workplace skills, communication, problem solving, ethics, and professional literacy embedded across every level of instruction.
{{< /callout >}}

## Anchor Standards Overview

| Standard Code | Standard Title | Focus Area |
|---|---|---|
| **1.0** | Academics | Integration of academic knowledge and technical skills |
| **2.0** | Communications | Professional writing, speaking, and digital literacy |
| **3.0** | Career Planning & Management | O*NET research, portfolio development, and career paths |
| **4.0** | Technology | Industry-standard software and technical workflows |
| **5.0** | Problem Solving & Critical Thinking | Creative evaluation and technical debugging |
| **6.0** | Health & Safety | Studio ergonomics, digital wellness, and equipment safety |
| **7.0** | Responsibility & Leadership | Project management, teamwork, and accountability |
| **8.0** | Ethics & Legal | Copyright, fair use, open licensing, and AI ethics |
| **9.0** | Technical Literacy | Industry terminology and technical specifications |
| **10.0** | Demonstration & Application | Capstones, pitch decks, and portfolio showcases |
| **11.0** | Professionalism | Studio culture, critiques, and client communication |
| **12.0** | Interdisciplinary Integration | Cross-curricular arts, science, and technical synthesis |
"""

inter_md = """---
title: AME Interdisciplinary Standards (13.0 - 16.0)
type: docs
description: Cross-curricular interdisciplinary standards for Arts, Media, and Entertainment.
weight: 3
---

The **Interdisciplinary Standards (13.0–16.0)** establish cross-curricular connections combining creative visual craft, storytelling math/science concepts, and technical design logic.

## Interdisciplinary Standards Matrix

| Code | Title | Core Competency |
|---|---|---|
| **13.0** | Visual & Digital Storytelling | Narrative premises, composition, framing, and pacing |
| **14.0** | Creative Process & Critique | Iteration, feedback integration, and peer critique |
| **15.0** | Asset Pipelines & Optimization | Mesh topology, texture density, lighting, and rendering |
| **16.0** | Systems & Interactive Logic | Gameplay logic, Blueprints, state management, and UI |
"""

anim_md = """---
title: Animation, VFX & Games Pathway
type: docs
description: Pathway standards for 3D modeling, animation, visual effects, and game development.
weight: 4
---

The **Animation, Visual Effects, and Games Pathway** prepares students for technical and creative roles in 3D production, game art, engine logic, and environment design.

## Core Competency Areas

- **3D Modeling & Topology**: Polygon modeling, hard-surface subdivision, quad topology, and retopology.
- **UVs & PBR Texturing**: Seam layout, texel density, albedo, roughness, metallic, and normal map baking.
- **Lighting & Rendering**: Physical cameras, environment lighting, global illumination (Lumen), and renders.
- **Game Engine Integration**: Static meshes, collision setup, Blueprint visual scripting, and level assembly.
"""

design_md = """---
title: Design & Visual Arts Pathway
type: docs
description: Pathway standards for visual design, digital craft, composition, and color theory.
weight: 5
---

The **Design & Visual Arts Pathway** develops core foundational craft in traditional and digital design principles.

## Core Competency Areas

- **Elements & Principles**: Line, shape, form, value, color, balance, contrast, emphasis, and movement.
- **Composition & Layout**: Rule of thirds, focal points, silhouette clarity, and grid typography.
- **Brand & Portfolio**: Personal branding, Google Sites portfolio organization, and presentation decks.
"""

files = {
    "anchor-standards.md": anchor_md,
    "interdisciplinary-standards.md": inter_md,
    "animation-vfx-games.md": anim_md,
    "design-visual-arts.md": design_md
}

for name, content in files.items():
    with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Created {len(files)} structured standards section pages in content/standards/")