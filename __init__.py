bl_info = {
    "name": "Straw Plugin",
    "author": "James Nelson",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tool Shelf",
    "description": "Creates straw structures based on material and force",
    "warning": "",
    "wiki_url": "",
    "category": "3D View",
}

from . import your_main_module  # replace 'your_main_module' with the name of your main Python file

def register():
    your_main_module.register()  # replace 'your_main_module' with the name of your main Python file

def unregister():
    your_main_module.unregister()  # replace 'your_main_module' with the name of your main Python file
