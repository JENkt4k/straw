import bpy
import numpy as np

# Clear existing mesh and metaball objects in the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.select_by_type(type='META')
bpy.ops.object.delete()

# User-defined parameters
cube_volume = 5000  # cm^3
nozzle_width = 0.4  # mm
wall_count = 1
material_strength = 50  # MPa or any unit (used for future calculations)
density_factor = 20  # Factor to increase density of metaballs

# Calculate mesh parameters
gyroid_cycles = 6  # Number of gyroid cycles
meshpointcnt = int(density_factor * gyroid_cycles)  # Resolution

# Derived parameters
L = cube_volume ** (1/3)  # Cube side length in cm
scaling_factor = L / (2 * gyroid_cycles)  # Scale the gyroid to fit within the cube
desired_thickness = nozzle_width * wall_count  # in mm
radius = desired_thickness / 2  # in mm


# Generate grid using NumPy
x, y, z = np.linspace(-gyroid_cycles, gyroid_cycles, meshpointcnt), np.linspace(-gyroid_cycles, gyroid_cycles, meshpointcnt), np.linspace(-gyroid_cycles, gyroid_cycles, meshpointcnt)
x, y, z = np.meshgrid(x, y, z)

# Evaluate gyroid equation
gyroid = np.sin(x) * np.cos(y) + np.sin(y) * np.cos(z) + np.sin(z) * np.cos(x)

# Create mask based on thickness
mask = np.abs(gyroid) < desired_thickness

# Create a new metaball object
mball = bpy.data.metaballs.new("GyroidMeta")
obj = bpy.data.objects.new("GyroidMeta", mball)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Create metaballs based on mask
for i in range(meshpointcnt):
    for j in range(meshpointcnt):
        for k in range(meshpointcnt):
            if mask[i, j, k]:
                element = mball.elements.new(type='BALL')
                element.co = (scaling_factor * x[i, j, k], scaling_factor * y[i, j, k], scaling_factor * z[i, j, k])
                element.radius = radius * scaling_factor  # Adjust the radius as needed

# Update scene
bpy.context.view_layer.update()

## Convert to mesh
try:
    bpy.ops.object.convert(target='MESH')
except Exception as e:
    print(f"Failed to convert metaball to mesh: {e}")