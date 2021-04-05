from bpy.types import Menu
from .icons import get_icon_id


class VIEW3D_MT_commandconfig_selection_mode_pie(Menu):
    bl_label = "Quick Select"

    def draw(self, context):
        pie = self.layout.menu_pie()

        # left
        pie.operator("wm.tool_set_by_id", text="Cursor", icon_value=get_icon_id("select")).name = "builtin.select"

        # right
        pie.operator("wm.tool_set_by_id", text="Transform Gizmo", icon_value=get_icon_id("transform")).name = "builtin.transform"

        # bottom
        pie.operator("wm.tool_set_by_id", text="Move Gizmo", icon_value=get_icon_id("move")).name = "builtin.move"

        # top
        pie.operator("wm.tool_set_by_id", text="Circle", icon_value=get_icon_id("select_circle")).name = "builtin.select_circle"

        # top left
        pie.operator("wm.tool_set_by_id", text="Box", icon_value=get_icon_id("select_box")).name = "builtin.select_box"

        # top right
        pie.operator("wm.tool_set_by_id", text="Lasso", icon_value=get_icon_id("select_lasso")).name = "builtin.select_lasso"

        # bottom left
        pie.operator("wm.tool_set_by_id", text="Rotate Gizmo", icon_value=get_icon_id("rotate")).name = "builtin.rotate"

        # bottom right
        pie.operator("wm.tool_set_by_id", text="Scale Gizmo", icon_value=get_icon_id("scale")).name = "builtin.scale"