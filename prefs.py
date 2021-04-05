import bpy
import rna_keymap_ui
from bpy.types import AddonPreferences, Context, UILayout
from bpy.props import BoolProperty, EnumProperty
from .keymap import register, unregister


def update_keys(self, context: Context):
    unregister()
    register(self)


class CommandConfigPreferences(AddonPreferences):
    bl_idname = __package__

    use_smart_select_transform: BoolProperty(
        name="Use W for Smart Select / Transform",
        description="Sets W to toggle between the universal transform gizmo and the default selection tool",
        default=True,
        update=update_keys,
    )

    remap_transform_gizmos: BoolProperty(
        name="Use industry standard transform shortcuts",
        description="Sets W, E, R to Move, Scale and Rotate transformation gizmos respectively",
        default=True,
        update=update_keys,
    )

    swap_e_and_r_keys: BoolProperty(
        name="Swap E for rotation and R for scale",
        description="Switches E and R functions to rotate and scale respectively",
        default=False,
        update=update_keys,
    )

    replace_q_key: BoolProperty(
        name="Use Q for changing selection mode",
        description="Changes the Q key from quick favorites menu to the selection tool",
        default=True,
        update=update_keys,
    )

    remap_quick_favorites: BoolProperty(
        name="Remap Quick Favorites to Alt + Q",
        description="Maps the Quick Favorites menu to Alt + Q",
        default=True,
        update=update_keys,
    )

    remap_selection_mode: EnumProperty(
        name="Default Select Tool",
        description="Determines what tool or behavior the S key should have for changing selection modes",
        items=[
            ("select", "Cursor", ""),
            ("select_box", "Box", ""),
            ("select_circle", "Circle", ""),
            ("select_lasso", "Lasso", ""),
            ("cycle", "Cycle", "Mimics the default behavior of the W key"),
        ],
        default="cycle",
        update=update_keys,
    )

    map_selection_arrows: BoolProperty(
        name="Map alt + arrow Keys to relative selection operations",
        description="Maps select more/less to alt + up and down arrows and select next/prev to alt + left and right arrows",
        default=True,
        update=update_keys,
    )

    remap_mesh_element_keys: BoolProperty(
        name="Map mesh element menus to CTRL + (1, 2, 3)",
        description="Maps CTRL + 1 to vertex menu, CTRL + 2 to edge menu, and CTRL + 3 to face menu while in mesh mode",
        default=True,
        update=update_keys,
    )

    double_click_select_linked: BoolProperty(
        name="Use double click to select linked",
        description="Double clicking on elements will select linked elements",
        default=True,
        update=update_keys,
    )

    merge_verts_pie: BoolProperty(
        name="Use merge vertex pie menu",
        description="Replaces the merge vertex menu with a pie menu for muscle memory selection",
        default=True,
        update=update_keys,
    )

    def draw(self, context: Context):
        layout: UILayout = self.layout

        box = layout.box()

        box.prop(self, "use_smart_select_transform")
        if not self.use_smart_select_transform:
            box.prop(self, "remap_transform_gizmos")
            if self.remap_transform_gizmos:
                box.prop(self, "swap_e_and_r_keys")
            box.prop(self, "replace_q_key")
            if self.replace_q_key:
                box.prop(self, "remap_quick_favorites")
                box.prop(self, "remap_selection_mode")
        box.prop(self, "map_selection_arrows")
        box.prop(self, "remap_mesh_element_keys")
        box.prop(self, "double_click_select_linked")
        box.prop(self, "merge_verts_pie")


def get_prefs():
    return bpy.context.preferences.addons[__package__].preferences
