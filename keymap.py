import bpy
from .selection_pie import VIEW3D_MT_commandconfig_selection_mode_pie
from .merge_vert_pie import OBJECT_MT_commandconfig_merge_verts
from .toggle_transform_cursor import ToggleTransformCursor

keys = []

view3d_modes = [
    ("object", "Object Mode"),
    ("mesh", "Mesh"),
    ("curve", "Curve"),
    ("surface", "Surface"),
    ("mball", "Metaball"),
    ("lattice", "Lattice"),
    ("gpencil", "Grease Pencil"),
    ("armature", "Armature"),
    ("pose", "Pose"),
]


def register_transform_keys(prefs, keys, km):
    if prefs.use_smart_select_transform:

        if prefs.default_to_pie:

            kmi = km.keymap_items.new("wm.call_menu_pie", "W", "PRESS")
            kmi.properties.name = VIEW3D_MT_commandconfig_selection_mode_pie.__name__
            keys.append((km, kmi))

        else:

            # kmi = km.keymap_items.new("wm.tool_set_by_id", "W", "PRESS")
            # kmi.properties.name = "builtin.transform"
            # keys.append((km, kmi))

            kmi = km.keymap_items.new(ToggleTransformCursor.bl_idname, "W", "PRESS")
            keys.append((km, kmi))

            kmi = km.keymap_items.new("wm.call_menu_pie", "W", "CLICK_DRAG")
            kmi.properties.name = VIEW3D_MT_commandconfig_selection_mode_pie.__name__
            keys.append((km, kmi))

        return

    if not prefs.remap_transform_gizmos:
        return

    if prefs.swap_e_and_r_keys:
        rotate_key = "E"
        scale_key = "R"
    else:
        rotate_key = "R"
        scale_key = "E"

    kmi = km.keymap_items.new("wm.tool_set_by_id", "W", "PRESS")
    kmi.properties.name = "builtin.move"
    keys.append((km, kmi))

    kmi = km.keymap_items.new("wm.tool_set_by_id", scale_key, "PRESS")
    kmi.properties.name = "builtin.scale"
    keys.append((km, kmi))

    kmi = km.keymap_items.new("wm.tool_set_by_id", rotate_key, "PRESS")
    kmi.properties.name = "builtin.rotate"
    keys.append((km, kmi))


def register_selection_keys(prefs, keys, km):
    if prefs.use_smart_select_transform:
        return

    if not prefs.replace_q_key:
        return

    if prefs.remap_selection_mode == "cycle":
        kmi = km.keymap_items.new("wm.tool_set_by_id", "Q", "PRESS")
        kmi.properties.name = "builtin.select"
        kmi.properties.cycle = True
        keys.append((km, kmi))
    else:
        kmi = km.keymap_items.new("wm.tool_set_by_id", "Q", "PRESS", repeat = False)
        kmi.properties.name = "builtin.{}".format(prefs.remap_selection_mode)
        keys.append((km, kmi))

    if prefs.remap_quick_favorites:
        kmi = km.keymap_items.new("wm.tool_set_by_id", "Q", "PRESS", alt=True)
        kmi.properties.name = "SCREEN_MT_user_menu"
        keys.append((km, kmi))


def register_selection_arrows(prefs, keys, km, mode):
    if not prefs.map_selection_arrows:
        return

    if mode not in {"surface", "pose"}:
        kmi = km.keymap_items.new("{}.select_more".format(mode), "UP_ARROW", "PRESS", alt=True)
        keys.append((km, kmi))

        kmi = km.keymap_items.new("{}.select_less".format(mode), "DOWN_ARROW", "PRESS", alt=True)
        keys.append((km, kmi))

    if mode in {"object", "armature", "pose"}:
        kmi = km.keymap_items.new("{}.select_hierarchy".format(mode), "RIGHT_ARROW", "PRESS", alt=True)
        kmi.properties.direction = "CHILD"
        kmi.properties.extend = False
        keys.append((km, kmi))

        kmi = km.keymap_items.new("{}.select_hierarchy".format(mode), "LEFT_ARROW", "PRESS", alt=True)
        kmi.properties.direction = "PARENT"
        kmi.properties.extend = False
        keys.append((km, kmi))

        kmi = km.keymap_items.new("{}.select_hierarchy".format(mode), "RIGHT_ARROW", "PRESS", shift=True, alt=True)
        kmi.properties.direction = "CHILD"
        kmi.properties.extend = True
        keys.append((km, kmi))

        kmi = km.keymap_items.new("{}.select_hierarchy".format(mode), "LEFT_ARROW", "PRESS", shift=True, alt=True)
        kmi.properties.direction = "PARENT"
        kmi.properties.extend = True
        keys.append((km, kmi))

    elif mode == "mesh":
        kmi = km.keymap_items.new("mesh.select_next_item", "RIGHT_ARROW", "PRESS", alt=True)
        keys.append((km, kmi))

        kmi = km.keymap_items.new("mesh.select_prev_item", "LEFT_ARROW", "PRESS", alt=True)
        keys.append((km, kmi))

    elif mode == "curve":
        kmi = km.keymap_items.new("curve.select_next", "RIGHT_ARROW", "PRESS", alt=True)
        keys.append((km, kmi))

        kmi = km.keymap_items.new("curve.select_prev", "LEFT_ARROW", "PRESS", alt=True)
        keys.append((km, kmi))

    elif mode == "surface":
        kmi = km.keymap_items.new("curve.select_more", "UP_ARROW", "PRESS", alt=True)
        keys.append((km, kmi))

        kmi = km.keymap_items.new("curve.select_less", "DOWN_ARROW", "PRESS", alt=True)
        keys.append((km, kmi))

    elif mode == "gpencil":
        kmi = km.keymap_items.new("gpencil.select_last", "RIGHT_ARROW", "PRESS", alt=True)
        keys.append((km, kmi))

        kmi = km.keymap_items.new("gpencil.select_first", "LEFT_ARROW", "PRESS", alt=True)
        keys.append((km, kmi))


def register_mesh_element_keys(prefs, keys, km):
    if prefs.remap_mesh_element_keys:
        kmi = km.keymap_items.new("wm.call_menu", "ONE", "PRESS", ctrl=True)
        kmi.properties.name = "VIEW3D_MT_edit_mesh_vertices"
        keys.append((km, kmi))

        kmi = km.keymap_items.new("wm.call_menu", "TWO", "PRESS", ctrl=True)
        kmi.properties.name = "VIEW3D_MT_edit_mesh_edges"
        keys.append((km, kmi))

        kmi = km.keymap_items.new("wm.call_menu", "THREE", "PRESS", ctrl=True)
        kmi.properties.name = "VIEW3D_MT_edit_mesh_faces"
        keys.append((km, kmi))

    if prefs.merge_verts_pie:
        # merge verts menu
        kmi = km.keymap_items.new("wm.call_menu_pie", "M", "PRESS")
        kmi.properties.name = OBJECT_MT_commandconfig_merge_verts.__name__
        keys.append((km, kmi))



def register_double_click(prefs, keys, km, mode):
    if not prefs.double_click_select_linked:
        return

    if mode in {"object", "mesh", "curve", "surface", "lattice"}:
        op = "{}.select_linked".format(mode)
        kmi = km.keymap_items.new(op, "LEFTMOUSE", "DOUBLE_CLICK")
        keys.append((km, kmi))

        if mode == "object":
            kmi.properties.type = "OBDATA"

        # kmi = km.keymap_items.new(op, "LEFTMOUSE", "DOUBLE_CLICK", shift=True)
        # kmi.properties.extend = True
        # keys.append((km, kmi))


def register(prefs):
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if not kc:
        return

    for vm in view3d_modes:
        km = wm.keyconfigs.addon.keymaps.new(name=vm[1], region_type="WINDOW")
        register_transform_keys(prefs, keys, km)
        register_selection_keys(prefs, keys, km)
        register_selection_arrows(prefs, keys, km, vm[0])
        register_double_click(prefs, keys, km, vm[0])

    km = wm.keyconfigs.addon.keymaps.new(name="Mesh", region_type="WINDOW")
    register_mesh_element_keys(prefs, keys, km)


def unregister():
    for km, kmi in keys:
        km.keymap_items.remove(kmi)
    keys.clear()
