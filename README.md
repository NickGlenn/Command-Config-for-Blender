# Command Configuration

This is a simple addon for Blender >=2.80 that allows quick configuration of some additional keyboard shortcuts.

## Installation

Download this repository and open up Blender, then navigate to your user preferences. Select the "Addons" tab and then click "Install Addon from File". When the file selection dialog pops up, select the `.zip` you downloaded.

## Preferences

This add-on manages keymap bindings across multiple view modes instaneously and allows you to customize which custom bindings you want to use. You can access these settings from the preferences menu in Blender.


- **Use W for Smart Select / Transform** remaps the `W` key to a custom toggle between the universal transform gizmo and the standard selection cursor. Additionally, dragging the mouse while holding the `W` key will open a custom pie menu that displays all selection modes and individual transformation gizmos for quick selection.
  - **Default to pie menu** changes the `W` key behavior to immediately open the custom pie menu displaying all selection modes and individual transformation gizmos, rather than toggling between the selection cursor and universal transform gizmo.
- **Use industry standard transform shortcuts** is an alternative mode that remaps keys to match the industry standards of `W`, `E`, and `R`. This option will handle the remapping of that for you across all 3D viewport modes.
  - **Swap E for rotation and R for scale** swaps the `E` and `R` as an alternative to match some other 3D software.
  - **Use S for changing selection mode** changes the `S` key from scale tool (Blender's default) to a selection tool.
  - **Default select tool** allows you to change which selection mode tool will be selected when pressing the `S` key. The available options are the selection cursor, box, circle and lasso tool, provided by Blender, or you can choose to "cycle" the selected tool (just like Blender's default binding for the `W` key).
- **Map alt + arrow Keys to relative selection operations** allows you to quickly select more or less using `Alt + Up` and `Alt + Down` in most modes. Some modes, like the edit mesh mode, allow you to continue a selection pattern using `Alt + Right` or reverse it using `Alt + Left`.
- **Map mesh element menus to CTRL + (1, 2, 3)** binds the Vertex, Edge and Face menus to the `Ctrl + 1`, `Ctrl + 2`, and `Ctrl + 3` keys when in edit mesh mode. This more closely aligns with using the `1`, `2`, and `3` keys for mesh element selection, creating a more natural muscle memory mapping.
- **Use double click to select linked** will select linked objects and elements when double clicking on an object or element. This is useful for quickly selecting islands of objects instead of having to resort to `L` or `Ctrl + L`.
- **Use merge vertex pie menu** replaces the default "Merge Vertices" menu (triggered with `M`) with a pie menu, allowing for muscle memory mappings for faster merge operation selection.