import bpy
import numpy as np

class STRAW_PT_panel(bpy.types.Panel):
    bl_label = "Straw Plugin"
    bl_idname = "STRAW_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "straw_material")
        layout.prop(scene, "straw_force")
        layout.prop(scene, "straw_fill_type")
        layout.prop(scene, "gyroid_nozzle_width")
        layout.prop(scene, "gyroid_wall_count")
        layout.prop(scene, "gyroid_density_factor")
        layout.prop(scene, "gyroid_cycles")
        layout.operator("straw.generate")

class STRAW_OT_operator(bpy.types.Operator):
    bl_label = "Generate"
    bl_idname = "straw.generate"

    def execute(self, context):
        scene = context.scene
        generate_shape()
        # ... (previous straw generation logic to create the shape, e.g., a cube)
        if scene.straw_fill_type == 'GYROID':
            generate_gyroid()
            # ... (gyroid generation logic from your provided code to fill the generated shape)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(STRAW_PT_panel)
    bpy.utils.register_class(STRAW_OT_operator)
    bpy.types.Scene.straw_material = bpy.props.EnumProperty(name="Material", items=[("PLA", "PLA", ""), ("PETG", "PETG", ""), ("ABS", "ABS", "")])
    bpy.types.Scene.straw_force = bpy.props.FloatProperty(name="Force (kg)", default=100)
    bpy.types.Scene.straw_fill_type = bpy.props.EnumProperty(name="Fill Type", items=[("SOLID", "Solid", ""), ("GYROID", "Gyroid", "")])
    bpy.types.Scene.gyroid_nozzle_width = bpy.props.FloatProperty(name="Nozzle Width (mm)", default=0.4)
    bpy.types.Scene.gyroid_wall_count = bpy.props.IntProperty(name="Wall Count", default=1, min=1)
    bpy.types.Scene.gyroid_density_factor = bpy.props.FloatProperty(name="Density Factor", default=20)
    bpy.types.Scene.gyroid_cycles = bpy.props.IntProperty(name="Gyroid Cycles", default=6, min=1)

def unregister():
    bpy.utils.unregister_class(STRAW_PT_panel)
    bpy.utils.unregister_class(STRAW_OT_operator)
    del bpy.types.Scene.straw_material
    del bpy.types.Scene.straw_force
    del bpy.types.Scene.straw_fill_type
    del bpy.types.Scene.gyroid_nozzle_width
    del bpy.types.Scene.gyroid_wall_count
    del bpy.types.Scene.gyroid_density_factor
    del bpy.types.Scene.gyroid_cycles

def generate_shape():
    pass

def generate_gyroid():
    pass

if __name__ == "__main__":
    register()
