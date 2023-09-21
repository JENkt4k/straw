import bpy
import math

class StrawProperties(bpy.types.PropertyGroup):
    material: bpy.props.EnumProperty(
        items=[
            ('PLA', 'PLA', ''),
            ('PET-G', 'PET-G', ''),
            ('ABS', 'ABS', ''),
            ('Hemp PLA', 'Hemp PLA', ''),
            ('Carbon Fiber PLA', 'Carbon Fiber PLA', ''),
            ('Carbon Fiber PET-G', 'Carbon Fiber PET-G', '')
        ],
        name="Material"
    )
    force: bpy.props.FloatProperty(name="Force", default=100.0)
    unit_system: bpy.props.EnumProperty(
        items=[
            ('Metric', 'Metric', ''),
            ('Imperial', 'Imperial', '')
        ],
        name="Unit System",
        default='Metric'
    )

def calculate_side_length(material, force, unit_system):
    tensile_strengths = {
        'PLA': 50,
        'PET-G': 55,
        'ABS': 40,
        'Hemp PLA': 45,
        'Carbon Fiber PLA': 70,
        'Carbon Fiber PET-G': 75
    }
    tensile_strength = tensile_strengths.get(material, 50)
    
    if unit_system == 'Imperial':
        # Convert force from pounds to Newtons (1 lb = 4.44822 N)
        force_newtons = force * 4.44822
    else:
        # Convert force from kg to Newtons
        force_newtons = force * 9.81
    
    min_area = (force_newtons / (tensile_strength * 1e6)) * 2
    side_length = math.sqrt(min_area)
    return side_length


class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.create_straw_cube"
    bl_label = "Create Straw Cube"
    
    def execute(self, context):
        material = context.scene.straw_props.material
        force = context.scene.straw_props.force
        unit_system = context.scene.straw_props.unit_system
        side_length = calculate_side_length(material, force, unit_system)
        
        # Get Blender's unit settings
        unit_settings = bpy.context.scene.unit_settings
        unit_scale = unit_settings.scale_length
        unit_type = unit_settings.length_unit
        
        # Log the calculated side_length
        print("Calculated side_length:", side_length)


        # Adjust the side_length based on the unit settings
        if unit_type == 'MILLIMETERS':
            side_length *= 1/unit_scale
            
        
        # Log the calculated side_length
        print("Calculated side_length:", side_length)


        bpy.ops.mesh.primitive_cube_add(size=side_length, enter_editmode=False, align='WORLD', location=(0, 0, 0))
        return {'FINISHED'}


class StrawPanel(bpy.types.Panel):
    bl_label = "Straw Plugin"
    bl_idname = "OBJECT_PT_straw"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
    def draw(self, context):
        layout = self.layout
        straw_props = context.scene.straw_props
        
        layout.prop(straw_props, "material")
        layout.prop(straw_props, "force")
        layout.prop(straw_props, "unit_system")
        layout.operator("object.create_straw_cube")

def register():
    bpy.utils.register_class(StrawProperties)
    bpy.types.Scene.straw_props = bpy.props.PointerProperty(type=StrawProperties)
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(StrawPanel)

def unregister():
    bpy.utils.unregister_class(StrawPanel)
    bpy.utils.unregister_class(SimpleOperator)
    del bpy.types.Scene.straw_props
    bpy.utils.unregister_class(StrawProperties)

if __name__ == "__main__":
    register()
