import bpy
from . import keymap, icons
from .prefs import CommandConfigPreferences, get_prefs
from .selection_pie import VIEW3D_MT_commandconfig_selection_mode_pie

bl_info = {
    "name": "Command Config",
    "author": "Nicholas Glenn",
    "description": "Opinionated keymap configuration tool.",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
    "wiki_url": "https://github.com/NickGlenn/Command-Config-for-Blender",
    "support": "COMMUNITY",
    "warning": "",
    "category": "Generic"
}

classes = (
    VIEW3D_MT_commandconfig_selection_mode_pie,
    CommandConfigPreferences,
)


def register():
    for c in classes:
        bpy.utils.register_class(c)
    icons.register()
    keymap.register(get_prefs())


def unregister():
    keymap.unregister()
    icons.unregister()
    for c in classes[::-1]:
        bpy.utils.unregister_class(c)
