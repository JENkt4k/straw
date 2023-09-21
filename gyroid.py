# working

import bpy
import numpy as np

# Clear existing mesh and metaball objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.select_by_type(type='META')
bpy.ops.object.delete()

# Initialize parameters
L = 4.0  # size of the grid
res = 40  # resolution
thickness = 0.4  # thickness

# Create a new Metaball object
mball = bpy.data.metaballs.new("GyroidMeta")
obj = bpy.data.objects.new("GyroidMeta", mball)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Generate grid using NumPy
x, y, z = np.linspace(-L, L, res), np.linspace(-L, L, res), np.linspace(-L, L, res)
x, y, z = np.meshgrid(x, y, z)

# Evaluate gyroid equation
gyroid = np.sin(x) * np.cos(y) + np.sin(y) * np.cos(z) + np.sin(z) * np.cos(x)

# Create mask based on thickness
mask = np.abs(gyroid) < thickness

# Create metaballs based on mask
for i in range(res):
    for j in range(res):
        for k in range(res):
            if mask[i, j, k]:
                element = mball.elements.new(type='BALL')
                element.co = (x[i, j, k], y[i, j, k], z[i, j, k])
                element.radius = 0.4  # Adjust the radius as needed

# Update scene
bpy.context.view_layer.update()

# end working

## Convert to mesh
#try:
#    bpy.ops.object.convert(target='MESH')
#except Exception as e:
#    print(f"Failed to convert metaball to mesh: {e}")

