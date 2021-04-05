import bpy
from bpy.types import Menu, Context, UILayout

class OBJECT_MT_commandconfig_merge_verts(Menu):
    """Pie menu for the merge vertices commands."""
    bl_label = "Merge Vertices"

    def draw(self, context: Context):
        pie: UILayout = self.layout.menu_pie()
        pie.operator_context = "EXEC_DEFAULT"

        # left
        pie.separator()

        # right
        pie.separator()

        # bottom
        pie.operator("mesh.remove_doubles", text="Merge By Distance")

        # top
        pie.operator("mesh.merge", text="Center").type = "CENTER"

        # top left
        pie.operator("mesh.merge", text="First").type = "FIRST"

        # top right
        pie.operator("mesh.merge", text="Last").type = "LAST"

        # bottom left
        pie.operator("mesh.merge", text="Cursors").type = "CURSOR"

        # bottom right
        pie.operator("mesh.merge", text="Collapse").type = "COLLAPSE"