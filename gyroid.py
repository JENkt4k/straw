import bpy
import numpy as np

# Clear mesh and metaball objects in the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.select_by_type(type='META')
bpy.ops.object.delete()

# Initialize parameters
#L = 3.0  # size of the grid, in cm
#res = 10  # resolution

# Set the minimum dimension
min_dim = 0.4  # For example, 0.1 cm or 1 mm
thickness = min_dim  # thickness in cm (0.8 mm)

# Derive other parameters
L = 10 * min_dim  # Grid size
res = 2* int(L / min_dim)  # Resolution
#radius = res/L  # Metaball radius
radius = 2*(L / (res))  # Metaball radius

# Create a new metaball object
mball = bpy.data.metaballs.new("GyroidMeta")
obj = bpy.data.objects.new("GyroidMeta", mball)
bpy.context.collection.objects.link(obj)

# Create a grid using NumPy
x, y, z = np.linspace(0, L, res), np.linspace(0, L, res), np.linspace(0, L, res)
x, y, z = np.meshgrid(x, y, z)

# Evaluate the gyroid equation using NumPy
gyroid = np.sin(2 * np.pi * x / L) * np.cos(2 * np.pi * y / L) + \
         np.sin(2 * np.pi * y / L) * np.cos(2 * np.pi * z / L) + \
         np.sin(2 * np.pi * z / L) * np.cos(2 * np.pi * x / L)

# Create a mask based on the thickness
mask = np.abs(gyroid) < (thickness / 2)

# Loop through the NumPy array to create metaballs
for i in range(res):
    for j in range(res):
        for k in range(res):
            if mask[i, j, k]:
                element = mball.elements.new(type='BALL')
                element.co = (x[i, j, k], y[i, j, k], z[i, j, k])
                element.radius = radius # 0.4  # You can adjust the radius

# Update the scene
bpy.context.view_layer.update()




#import bpy
#import numpy as np

## Clear mesh and metaball objects in the scene
#bpy.ops.object.select_all(action='DESELECT')
#bpy.ops.object.select_by_type(type='MESH')
#bpy.ops.object.select_by_type(type='META')
#bpy.ops.object.delete()

## Initialize parameters
#L = 3.0  # size of the grid, in cm
#res = 10  # resolution
#thickness = 0.08  # thickness in cm (0.8 mm)

## Create a new metaball object
#mball = bpy.data.metaballs.new("GyroidMeta")
#obj = bpy.data.objects.new("GyroidMeta", mball)
#bpy.context.collection.objects.link(obj)

## Create a grid using NumPy
#x, y, z = np.linspace(0, L, res), np.linspace(0, L, res), np.linspace(0, L, res)
#x, y, z = np.meshgrid(x, y, z)

## Evaluate the gyroid equation using NumPy
#gyroid = np.sin(2 * np.pi * x / L) * np.cos(2 * np.pi * y / L) + \
#         np.sin(2 * np.pi * y / L) * np.cos(2 * np.pi * z / L) + \
#         np.sin(2 * np.pi * z / L) * np.cos(2 * np.pi * x / L)

## Create a mask based on the thickness
#mask = np.abs(gyroid) < (thickness / 2)

## Loop through the NumPy array to create metaballs
#for i in range(res):
#    for j in range(res):
#        for k in range(res):
#            if mask[i, j, k]:
#                element = mball.elements.new()
#                element.co = (x[i, j, k], y[i, j, k], z[i, j, k])
#                element.radius = 0.1  # You can adjust the radius
