# Run this in Blender's Scripting tab (Scripting workspace > new text file > paste > Run Script).
# It clears the current scene and builds a colored "parts bin" of correctly-sized
# and correctly-shaped pieces, scattered off to the side, correctly named, ready
# for students to place by typing Location values.
#
# New in this version:
#   - Every piece gets a colored material (switch viewport shading to Material
#     Preview, Z then 2, or the sphere icon top-right, to see the colors)
#   - The flat roof is replaced with two sloped roof panels (a real gable roof)
#   - Two triangular gable-end pieces close off the roof openings above the
#     left and right walls
#
# House geometry: footprint 4m x 3m, wall height 2.4m (eave height), wall
# thickness 0.2m, 1m-wide door opening centered on the front wall, roof ridge
# 1.0m above the eave line, running along X.

import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)


def get_or_create_material(name, rgba):
    mat = bpy.data.materials.get(name)
    if mat is None:
        mat = bpy.data.materials.new(name)
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs["Base Color"].default_value = rgba
        mat.diffuse_color = rgba  # shows up in Solid shading too
    return mat


def assign_color(obj, rgba, mat_name):
    mat = get_or_create_material(mat_name, rgba)
    obj.data.materials.append(mat)


# Category color palette (R, G, B, A)
COLORS = {
    "floor":   (0.55, 0.35, 0.20, 1.0),  # warm brown
    "wall":    (0.85, 0.75, 0.55, 1.0),  # cream/tan
    "roof":    (0.70, 0.25, 0.20, 1.0),  # terracotta
    "door":    (0.35, 0.20, 0.10, 1.0),  # dark wood
    "shutter": (0.15, 0.40, 0.20, 1.0),  # forest green
}

# ---------------------------------------------------------------------------
# Piece builders
# ---------------------------------------------------------------------------

def add_box_piece(name, dims, loc, color_key):
    """A plain axis-aligned box, for walls, floor, door, shutters."""
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.active_object
    obj.name = name
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    assign_color(obj, COLORS[color_key], f"{color_key}_mat")
    return obj


def add_triangular_prism(name, loc, y_z_profile, thickness, color_key):
    """
    A triangular prism extruded along local X by `thickness`, for the gable
    ends. y_z_profile is a list of (y, z) points relative to `loc`, e.g. the
    two base corners and the peak.
    """
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.location = loc

    bm = bmesh.new()
    half_t = thickness / 2
    front_verts = [bm.verts.new((-half_t, y, z)) for (y, z) in y_z_profile]
    back_verts = [bm.verts.new((half_t, y, z)) for (y, z) in y_z_profile]
    bm.faces.new(front_verts)
    bm.faces.new(list(reversed(back_verts)))
    n = len(y_z_profile)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new([front_verts[i], front_verts[j], back_verts[j], back_verts[i]])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(mesh)
    bm.free()

    assign_color(obj, COLORS[color_key], f"{color_key}_mat")
    return obj


def add_sloped_slab(name, x_width, slope_run, slope_rise, thickness, loc, mirror_y, color_key):
    """
    A rectangular slab tilted around the X axis to form one side of a gable
    roof. The tilt is baked into the mesh itself, so the object's rotation
    stays (0, 0, 0) and the only unknown for students is still Location.

    slope_run / slope_rise describe the pitch (how far it climbs in Z over
    how far it runs in Y). mirror_y=True flips the tilt direction for the
    side that slopes down toward +Y instead of -Y.
    """
    length = math.hypot(slope_run, slope_rise)
    angle = math.atan2(slope_rise, slope_run)
    if mirror_y:
        angle = -angle

    hw, hl, ht = x_width / 2, length / 2, thickness / 2
    local_verts = [
        Vector((-hw, -hl, -ht)), Vector((hw, -hl, -ht)),
        Vector((hw, hl, -ht)), Vector((-hw, hl, -ht)),
        Vector((-hw, -hl, ht)), Vector((hw, -hl, ht)),
        Vector((hw, hl, ht)), Vector((-hw, hl, ht)),
    ]
    rot = Matrix.Rotation(angle, 4, 'X')
    world_verts = [rot @ v for v in local_verts]

    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.location = loc

    bm = bmesh.new()
    bmverts = [bm.verts.new(v) for v in world_verts]
    faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
    for f in faces:
        bm.faces.new([bmverts[i] for i in f])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(mesh)
    bm.free()

    assign_color(obj, COLORS[color_key], f"{color_key}_mat")
    return obj

# ---------------------------------------------------------------------------
# Build the parts bin
# ---------------------------------------------------------------------------

clear_scene()

# Roof pitch: rises 1.0m over a 1.5m horizontal run (half the 3m depth),
# from eave height 2.4m up to ridge height 3.4m.
EAVE_RUN, EAVE_RISE = 1.5, 1.0

box_pieces = [
    ("floor",        (4.0, 3.0, 0.1),  (-8, -8, 0.05), "floor"),
    ("wall_left",    (0.2, 3.0, 2.4),  (-8, -4, 1.2),  "wall"),
    ("wall_right",   (0.2, 3.0, 2.4),  (-8,  0, 1.2),  "wall"),
    ("wall_back",    (4.0, 0.2, 2.4),  (-8,  4, 1.2),  "wall"),
    ("wall_front_L", (1.5, 0.2, 2.4),  (-8,  8, 1.2),  "wall"),
    ("wall_front_R", (1.5, 0.2, 2.4),  (-8, 12, 1.2),  "wall"),
    ("wall_lintel",  (1.0, 0.2, 0.4),  (-4, -8, 0.2),  "wall"),
    ("door",         (1.0, 0.05, 2.0), (-4,  0, 1.0),  "door"),
    ("shutter_L",    (0.4, 0.05, 1.0), (-4,  4, 0.5),  "shutter"),
    ("shutter_R",    (0.4, 0.05, 1.0), (-4,  8, 0.5),  "shutter"),
]
for name, dims, loc, color_key in box_pieces:
    add_box_piece(name, dims, loc, color_key)

# Gable ends: triangular prisms, base 3m wide (matching wall_left/wall_right
# depth), rising 1.0m to the ridge peak, 0.2m thick (matching wall thickness).
gable_profile = [(-1.5, 0.0), (1.5, 0.0), (0.0, EAVE_RISE)]
add_triangular_prism("gable_left",  (-4, -4, 2.0), gable_profile, 0.2, "wall")
add_triangular_prism("gable_right", (-4,  0, 2.0), gable_profile, 0.2, "wall")

# Roof slopes: two panels, 4.4m wide (0.2m overhang past each side wall),
# 0.1m thick, tilted to the roof pitch. mirror_y flips the tilt direction.
add_sloped_slab("roof_slope_front", 4.4, EAVE_RUN, EAVE_RISE, 0.1, (-4, 4, 2.0), mirror_y=False, color_key="roof")
add_sloped_slab("roof_slope_back",  4.4, EAVE_RUN, EAVE_RISE, 0.1, (-4, 8, 2.0), mirror_y=True,  color_key="roof")

bpy.ops.object.select_all(action='DESELECT')

print("Created 14 pieces. Switch to Material Preview shading (Z, then 2) to see "
      "the colors, then save this file as your starter/demo file.")
