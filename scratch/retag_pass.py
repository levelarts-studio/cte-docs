import os, re

content_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"
changes = []

def replace_tag(filepath, old_tag, new_tag):
    """Replace a single tag in the standards array of a markdown file."""
    fpath = os.path.join(content_dir, filepath)
    if not os.path.exists(fpath):
        print(f"  SKIP (not found): {filepath}")
        return False
    
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Match the standards line and replace the specific tag
    # Handle both quoted and unquoted forms
    orig = text
    text = text.replace(f'"{old_tag}"', f'"{new_tag}"')
    
    if text != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(text)
        changes.append((filepath, old_tag, new_tag))
        print(f"  RETAG: {filepath}: {old_tag} -> {new_tag}")
        return True
    else:
        print(f"  SKIP (tag not found in expected form): {filepath}")
        return False

print("=" * 60)
print("PARTIAL RETAG PASS: 6 worst REVIEW codes")
print("=" * 60)

# ================================================================
# AV.17.8: "3D Animation Fundamentals" - was assumed to be "3D Asset Modeling"
# Blender MODELING modules should NOT be tagged with an animation standard.
# Keep AV.17.8 only on files genuinely about animation.
# ================================================================
print("\n--- AV.17.8 (3D Animation Fundamentals) ---")
print("Modules about 3D modeling -> GD.17.4 (Art & Design Fundamentals)")
print("Modules genuinely about animation -> KEEP AV.17.8")

# Files that are about MODELING, not animation -> retag to GD.17.4
modeling_files = [
    "assignments/blender-first-model.md",
    "assignments/form-studies.md",
    "assignments/hard-surface-prop.md",
    "assignments/prop-modeling-set.md",
    "learn/blender/edit-mode-basics.md",
    "learn/blender/hard-surface-modeling.md",
    "learn/blender/modifiers-introduction.md",
    "learn/blender/modular-kit-building.md",
    "learn/blender/objects-transforms-and-pivots.md",
    "learn/blender/primitive-modeling.md",
    "learn/blender/retopology.md",
    "learn/blender/sculpting-introduction.md",
    "learn/blender/topology-and-edge-flow.md",
]
for f in modeling_files:
    replace_tag(f, "AV.17.8", "GD.17.4")

# Blender interface/navigation -> GD.17.4 (general art tool fundamentals)
replace_tag("learn/blender/interface-and-navigation.md", "AV.17.8", "GD.17.4")

# Texturing/shading pipeline -> 10.3 (Visualization Techniques) or keep domain-specific
# UV unwrapping, baking normals, viewport shading = technical art, not animation
replace_tag("learn/blender/baking-normal-maps.md", "AV.17.8", "GD.17.4")
replace_tag("learn/blender/uv-unwrapping.md", "AV.17.8", "GD.17.4")
replace_tag("learn/blender/viewport-shading-and-preview.md", "AV.17.8", "GD.17.4")

# Export/import pipeline -> 4.5 (Document & Asset Management)
replace_tag("learn/blender/game-ready-export.md", "AV.17.8", "4.5")
replace_tag("assignments/import-your-asset.md", "AV.17.8", "4.5")
replace_tag("learn/unreal/importing-assets.md", "AV.17.8", "4.5")

# Poly budget/LODs -> GD.18.8 (Game Performance & Evaluation)
replace_tag("learn/blender/poly-budget-and-lods.md", "AV.17.8", "GD.18.8")

# KEEP AV.17.8 on genuinely animation-related files:
print("  KEEP: learn/blender/keyframe-animation-basics.md (genuinely animation)")
print("  KEEP: learn/blender/rigging-basics.md (genuinely animation)")

# ================================================================
# AV.17.1: "Art & Design Fundamentals" - was assumed to be "PBR Materials & Texturing"
# Animation modules can legitimately keep AV.17.1 (Art & Design Fundamentals).
# PBR-specific files should get a more specific texturing standard.
# Character design files -> GD.17.5 (Character Design) or AV.17.4 (Character Design & Posing)
# ================================================================
print("\n--- AV.17.1 (Art & Design Fundamentals) ---")
print("Animation modules -> KEEP AV.17.1 (Art & Design Fundamentals fits)")
print("Character design -> AV.17.4 (Character Design & Posing)")
print("PBR texturing -> 10.3 (Visualization Techniques)")

# Animation modules - AV.17.1 ("Art & Design Fundamentals") is actually a reasonable fit
# for animation foundations. KEEP these.
anim_keep = [
    "learn/animation/animation-blueprints-and-blendspaces.md",
    "learn/animation/biped-rigging-and-weight-painting.md",
    "learn/animation/combat-and-action-poses.md",
    "learn/animation/idle-and-locomotion-cycles.md",
    "learn/animation/keyframing-and-graph-editor.md",
    "learn/animation/principles-of-animation-in-3d.md",
]
for f in anim_keep:
    print(f"  KEEP: {f} (AV.17.1 Art & Design Fundamentals fits animation)")

# Character design modules -> AV.17.4 (Character Design & Posing)
char_files = [
    "learn/character/base-mesh-sculpt-blockout.md",
    "learn/character/character-concept-and-proportions.md",
    "learn/character/character-topology-and-deform-flow.md",
    "learn/character/costume-clothing-and-armor-modeling.md",
    "learn/character/facial-structure-and-anatomy.md",
    "learn/character/hair-cards-and-grooming.md",
]
for f in char_files:
    replace_tag(f, "AV.17.1", "AV.17.4")

# PBR texturing modules -> 10.3 (Visualization Techniques) 
replace_tag("learn/character/skin-and-character-pbr-texturing.md", "AV.17.1", "10.3")
replace_tag("learn/blender/texturing-and-pbr-maps.md", "AV.17.1", "10.3")
replace_tag("learn/blender/baking-normal-maps.md", "AV.17.1", "10.3")
replace_tag("assignments/pbr-texture-set.md", "AV.17.1", "10.3")

# UV unwrapping -> GD.17.4 (Art & Design Fundamentals in game context)
replace_tag("assignments/uv-unwrap-drill.md", "AV.17.1", "GD.17.4")
replace_tag("learn/blender/uv-unwrapping.md", "AV.17.1", "GD.17.4")

# Unreal materials -> 10.3 (Visualization Techniques)
replace_tag("learn/unreal/materials-basics.md", "AV.17.1", "10.3")

# ================================================================
# GD.17.1: "Game Design Fundamentals" - was assumed to be "Game Engine Navigation & Setup"
# Engine setup/navigation is NOT game design fundamentals.
# Engine-specific modules -> GD.20.3 (Game Development) or 4.3 (Industry-Standard Technology)
# ================================================================
print("\n--- GD.17.1 (Game Design Fundamentals) ---")
print("Engine navigation/setup -> 4.3 (Industry-Standard Technology)")
print("Engine orientation assignments -> 4.3")

# Engine navigation and setup files -> 4.3 (Industry-Standard Technology)
engine_files = [
    "assignments/engine-orientation.md",
    "learn/unreal/interface-and-navigation.md",
    "learn/unreal/project-setup-and-folder-structure.md",
    "learn/unreal/placing-and-transforming-actors.md",
]
for f in engine_files:
    replace_tag(f, "GD.17.1", "4.3")

# Import/export pipeline -> 4.5 (Document & Asset Management)
replace_tag("assignments/import-your-asset.md", "GD.17.1", "4.5")
replace_tag("learn/unreal/importing-assets.md", "GD.17.1", "4.5")
replace_tag("learn/blender/game-ready-export.md", "GD.17.1", "4.5")

# Unreal materials -> 10.3 (Visualization Techniques)
replace_tag("learn/unreal/materials-basics.md", "GD.17.1", "10.3")

# ================================================================
# GD.17.7: "Gameplay Systems & Balancing" - was "Interactive Gameplay Mechanics"
# The meaning is close but shifted. Review each file.
# Core loop, MDA, game feel = game design theory -> KEEP GD.17.7
# Collision/triggers, input/movement = engine implementation -> GD.20.3 (Game Development)
# ================================================================
print("\n--- GD.17.7 (Gameplay Systems & Balancing) ---")

# Game design theory modules - GD.17.7 is a reasonable fit. KEEP.
gd_keep = [
    "assignments/core-loop-prototype.md",
    "assignments/feedback-systems-pass.md",
    "learn/gamedesign/game-feel-and-feedback.md",
    "learn/gamedesign/mechanics-dynamics-aesthetics.md",
    "learn/gamedesign/the-core-loop.md",
]
for f in gd_keep:
    print(f"  KEEP: {f} (GD.17.7 Gameplay Systems & Balancing fits)")

# Engine implementation -> GD.20.3 (Game Development)
replace_tag("learn/unreal/collision-and-triggers.md", "GD.17.7", "GD.20.3")
replace_tag("learn/unreal/input-and-character-movement.md", "GD.17.7", "GD.20.3")

# ================================================================
# 3.7: "Professional Organizations & Unions" - was "Career Planning & Resumes"
# Career planning / resume modules -> 3.8 (Resumes & Portfolios)
# Networking -> 3.3 (Networking)
# Career exploration -> 3.1 (Career Pathways)
# ================================================================
print("\n--- 3.7 (Professional Organizations & Unions) ---")

# Resume and portfolio files -> 3.8 (Resumes & Portfolios)
replace_tag("learn/career/resumes.md", "3.7", "3.8")
replace_tag("learn/career/artist-statement-and-bio.md", "3.7", "3.8")
replace_tag("assignments/careers-portfolio-page.md", "3.7", "3.8")

# Career exploration -> 3.1 (Career Pathways)
replace_tag("learn/career/interests-skills-and-aptitude.md", "3.7", "3.1")
replace_tag("assignments/career-plan-draft.md", "3.7", "3.1")

# Networking -> 3.3 (Networking)
replace_tag("learn/career/networking-and-professional-presence.md", "3.7", "3.3")

# ================================================================
# 15.4: "Storytelling Across Mediums" - was "Camera Angles & Framing"
# Camera/framing modules -> 15.6 (Cinematic Techniques)
# Storyboarding -> AV.17.5 (Storyboarding) or keep 15.4 if cross-medium
# ================================================================
print("\n--- 15.4 (Storytelling Across Mediums) ---")

# Camera angles and framing -> 15.6 (Cinematic Techniques)
replace_tag("learn/media/camera-angles-and-movement.md", "15.4", "15.6")
replace_tag("learn/media/shot-types-and-framing.md", "15.4", "15.6")
replace_tag("learn/blender/cameras-and-rendering.md", "15.4", "15.6")

# Storyboarding -> AV.17.5 (Storyboarding)
replace_tag("learn/design/storyboarding-basics.md", "15.4", "AV.17.5")
replace_tag("assignments/storyboard-sequence.md", "15.4", "AV.17.5")

# ================================================================
# SUMMARY
# ================================================================
print("\n" + "=" * 60)
print(f"TOTAL RETAGS: {len(changes)}")
print("=" * 60)
for filepath, old, new in changes:
    print(f"  {filepath}: {old} -> {new}")
