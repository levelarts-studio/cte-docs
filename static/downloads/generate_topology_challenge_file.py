# ==============================================================================
# CTE Game Art & Design — Topology Fix Challenge Generator
# File: generate_topology_challenge_file.py
#
# Instructions:
# 1. Open Blender (File > New > General).
# 2. Switch to the "Scripting" workspace (tab at top).
# 3. Click "Open" and select this file (or click "New" and paste this code).
# 4. Click the "Run Script" button (play icon) in the Text Editor header.
# 5. Switch to the "Layout" or "Modeling" workspace.
# 6. Immediately save your project as:
#    LASTNAME_TopologyChallenge_v01.blend inside your 01_Projects folder.
#
# The script clears the scene and builds a single prop mesh:
# "Broken_Console_Prop"
#
# This asset looks like a sci-fi terminal console, but it has been planted
# with several deliberate topology flaws:
#   - Flipped Face Normals (shows red in Face Orientation overlay)
#   - Non-Manifold T-Junction / Internal Face (edge shared by 3 faces)
#   - Open Boundary Hole (missing face on side panel)
#   - Stray Loose Vertices & Wire Edges (invisible until cleaned or selected)
#   - Doubled / Coincident Vertices (vertices on top of each other)
#   - An N-Gon (6-sided polygon on the upper console face)
#   - A 5-Edge Pole on a curved surface (causes pinching under subdivision)
#
# Your mission: Diagnose every flaw, document them, fix them, and prove
# the mesh is 100% clean and manifold!
# ==============================================================================

import bpy
import bmesh
from mathutils import Vector

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for block in (bpy.data.meshes, bpy.data.materials, bpy.data.cameras, bpy.data.lights):
        for item in list(block):
            block.remove(item)

def create_broken_prop():
    # Create mesh & object
    mesh = bpy.data.meshes.new("Broken_Console_Prop")
    obj = bpy.data.objects.new("Broken_Console_Prop", mesh)
    bpy.context.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    bm = bmesh.new()

    # --- BASE PEDESTAL (0.8m x 0.8m x 1.2m) ---
    # We construct a console pedestal with angled screen face
    v0  = bm.verts.new((-0.4, -0.4, 0.0))
    v1  = bm.verts.new(( 0.4, -0.4, 0.0))
    v2  = bm.verts.new(( 0.4,  0.4, 0.0))
    v3  = bm.verts.new((-0.4,  0.4, 0.0))

    v4  = bm.verts.new((-0.4, -0.4, 0.7))
    v5  = bm.verts.new(( 0.4, -0.4, 0.7))
    v6  = bm.verts.new(( 0.4,  0.4, 0.7))
    v7  = bm.verts.new((-0.4,  0.4, 0.7))

    # Angled top terminal section
    v8  = bm.verts.new((-0.4, -0.4, 0.9))
    v9  = bm.verts.new(( 0.4, -0.4, 0.9))
    v10 = bm.verts.new(( 0.4,  0.1, 1.2))
    v11 = bm.verts.new((-0.4,  0.1, 1.2))
    v12 = bm.verts.new(( 0.4,  0.4, 1.2))
    v13 = bm.verts.new((-0.4,  0.4, 1.2))

    # Bottom cap
    bm.faces.new([v3, v2, v1, v0])

    # Lower sides
    f_front_low = bm.faces.new([v0, v1, v5, v4])
    f_right_low = bm.faces.new([v1, v2, v6, v5])
    # Note: Left low will have an open hole deliberate flaw
    f_back_low  = bm.faces.new([v2, v3, v7, v6])
    
    # Upper transition
    bm.faces.new([v4, v5, v9, v8])
    bm.faces.new([v7, v6, v12, v13])
    bm.faces.new([v11, v10, v12, v13])  # Top flat cap

    # --- DELIBERATE FLAW 1: OPEN BOUNDARY HOLE ---
    # On left side, we leave a lower face missing (v0, v4, v7, v3 is open!)
    # Students must detect this via Non-Manifold check and close it with 'F' or Grid Fill.

    # --- DELIBERATE FLAW 2: FLIPPED NORMALS ---
    # Right side upper panel is created with inverted winding order
    # (v5, v6, v10, v9 reversed) so its normal points inside!
    # Shows RED in Face Orientation overlay.
    bm.faces.new([v9, v10, v6, v5])  # Inverted normal!

    # Left side upper panel (normal orientation)
    bm.faces.new([v7, v11, v8, v4])

    # --- DELIBERATE FLAW 3: N-GON ON CONSOLE SCREEN ---
    # The slanted console surface is made of an n-gon: 6 vertices!
    # Instead of clean quad quads, a central edge was deleted.
    vn1 = bm.verts.new(( 0.0, -0.4, 0.9))
    vn2 = bm.verts.new(( 0.0,  0.1, 1.2))
    # Face with 6 sides: v8 -> vn1 -> v9 -> v10 -> vn2 -> v11
    bm.faces.new([v8, vn1, v9, v10, vn2, v11])

    # --- DELIBERATE FLAW 4: NON-MANIFOLD T-JUNCTION / INTERNAL FACE ---
    # A hidden face inside the pedestal between v4, v5, v6, v7
    # This creates edges shared by 3 faces!
    bm.faces.new([v4, v5, v6, v7])

    # --- DELIBERATE FLAW 5: 5-EDGE POLE ON FRONT CURVED BUMPER ---
    # Add a curved decorative bumper strip along the front with a 5-edge pole
    # that pinches under subdivision
    bp0 = bm.verts.new((-0.3, -0.45, 0.3))
    bp1 = bm.verts.new(( 0.0, -0.48, 0.3))  # Center protruding pole vert
    bp2 = bm.verts.new(( 0.3, -0.45, 0.3))
    bp_top = bm.verts.new(( 0.0, -0.45, 0.45))
    bp_bot = bm.verts.new(( 0.0, -0.45, 0.15))

    bm.faces.new([bp0, bp1, bp_top])
    bm.faces.new([bp1, bp2, bp_top])
    bm.faces.new([bp0, bp_bot, bp1])
    bm.faces.new([bp1, bp_bot, bp2])
    # bp1 has 4 triangle edges radiating + connections to center = pole pinch

    # --- DELIBERATE FLAW 6: DOUBLED / COINCIDENT VERTICES ---
    # Two vertices sitting at the exact same location at one corner
    # (v0 has a clone sitting right at (-0.4, -0.4, 0.0))
    dup_v = bm.verts.new((-0.4, -0.4, 0.0))
    dup_v_edge = bm.verts.new((-0.4, -0.4, 0.1))
    bm.edges.new([dup_v, dup_v_edge])

    # --- DELIBERATE FLAW 7: STRAY LOOSE VERTICES & FLOATING WIRE EDGE ---
    # Loose floating vertices inside the cabinet
    loose1 = bm.verts.new((0.1, 0.1, 0.3))
    loose2 = bm.verts.new((0.15, 0.1, 0.35))
    loose3 = bm.verts.new((-0.2, 0.0, 0.4))
    bm.edges.new([loose1, loose2])  # Wire edge not attached to any face!

    # Update bmesh to object
    bm.to_mesh(mesh)
    bm.free()

    mesh.update()

    # Apply nice default viewport material
    mat = bpy.data.materials.new("Console_Mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (0.22, 0.25, 0.30, 1.0)
        bsdf.inputs["Roughness"].default_value = 0.4
    mat.diffuse_color = (0.22, 0.25, 0.30, 1.0)
    obj.data.materials.append(mat)

    return obj

def setup_scene(obj):
    # Camera
    cam_data = bpy.data.cameras.new("Inspection_Camera")
    cam_obj = bpy.data.objects.new("Inspection_Camera", cam_data)
    bpy.context.collection.objects.link(cam_obj)
    bpy.context.scene.camera = cam_obj
    cam_obj.location = (2.2, -2.4, 1.8)
    cam_obj.rotation_euler = (1.05, 0.0, 0.78)

    # Key Light
    light_data = bpy.data.lights.new("Key_Light", type='AREA')
    light_data.energy = 80
    light_data.size = 2.0
    light_obj = bpy.data.objects.new("Key_Light", light_data)
    bpy.context.collection.objects.link(light_obj)
    light_obj.location = (2.0, -1.5, 3.0)

    # Fill Light
    fill_data = bpy.data.lights.new("Fill_Light", type='AREA')
    fill_data.energy = 30
    fill_data.size = 3.0
    fill_obj = bpy.data.objects.new("Fill_Light", fill_data)
    bpy.context.collection.objects.link(fill_obj)
    fill_obj.location = (-2.0, -1.5, 1.5)

    # Ground plane
    bpy.ops.mesh.primitive_plane_add(size=8, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.name = "Floor_Pedestal"
    floor_mat = bpy.data.materials.new("Floor_Mat")
    floor_mat.use_nodes = True
    f_bsdf = floor_mat.node_tree.nodes.get("Principled BSDF")
    if f_bsdf:
        f_bsdf.inputs["Base Color"].default_value = (0.08, 0.09, 0.11, 1.0)
    floor_mat.diffuse_color = (0.08, 0.09, 0.11, 1.0)
    floor.data.materials.append(floor_mat)

    # Select prop again
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

def main():
    clear_scene()
    obj = create_broken_prop()
    setup_scene(obj)
    print("=====================================================")
    print("  TOPOLOGY CHALLENGE: Broken_Console_Prop Generated! ")
    print("  Flaws planted:")
    print("   1. Flipped Normal (Right Upper Face)")
    print("   2. Open Boundary Hole (Left Lower Face)")
    print("   3. Internal Face / T-Junction (Inside Pedestal)")
    print("   4. N-Gon (6-sided Face on Slanted Screen)")
    print("   5. 5-Edge Pole (Front Curved Bumper)")
    print("   6. Coincident / Doubled Vertices")
    print("   7. Loose Vertices & Wire Edge")
    print("=====================================================")

if __name__ == "__main__":
    main()
