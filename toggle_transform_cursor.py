import bpy

class ToggleTransformCursor(bpy.types.Operator):
    """Will cycle between the universal transform gizmo and the selection cursor."""
    bl_idname = "view3d.toggle_transform_gizmo_cursor"
    bl_label = "Toggle Transform Gizmo / Selection Cursor"
    bl_options = {"REGISTER", "INTERNAL"}

    @classmethod
    def poll(cls, context):
        return context.area.type == "VIEW_3D"

    def execute(self, context):
        current_tool = context.workspace.tools.from_space_view3d_mode(context.mode, create=False).idname
        next_tool = "builtin.transform"

        if current_tool == next_tool:
            next_tool = "builtin.select"

        bpy.ops.wm.tool_set_by_id(name=next_tool, space_type="VIEW_3D")

        return {"FINISHED"}