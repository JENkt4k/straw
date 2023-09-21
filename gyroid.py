import bpy
import math
import bmesh

# Clear mesh objects in the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Initialize parameters
L = 3.0  # size of the grid, in cm
res = 20  # resolution
thickness = 0.08  # thickness in cm (0.8 mm)

# Create an empty mesh and link it to scene
mesh = bpy.data.meshes.new(name="Gyroid")
obj = bpy.data.objects.new("Gyroid", mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Construct the mesh
mesh = bpy.context.object.data
bm = bmesh.new()

for i in range(res):
    for j in range(res):
        for k in range(res):
            x, y, z = i * (L / res), j * (L / res), k * (L / res)
            
            # Gyroid equation
            gyroid_value = math.sin(2 * math.pi * x / L) * math.cos(2 * math.pi * y / L) + \
                          math.sin(2 * math.pi * y / L) * math.cos(2 * math.pi * z / L) + \
                          math.sin(2 * math.pi * z / L) * math.cos(2 * math.pi * x / L)
            
            # Create vertices where the gyroid equation is close to zero (within the thickness range)
            if abs(gyroid_value) < (thickness / 2):
                bmesh.ops.create_vert(bm, co=(x, y, z))

# Update & Free BMesh
bm.to_mesh(mesh)
bm.free()







#import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

## Parameters
#L = 3.0  # size of the grid, in cm
#res = 50  # resolution
#thickness = 0.08  # thickness in cm (0.8 mm)
#void_max = 3.0  # maximum void size in cm

## Create a grid
#x, y, z = np.linspace(0, L, res), np.linspace(0, L, res), np.linspace(0, L, res)
#x, y, z = np.meshgrid(x, y, z)

## Gyroid equation
#gyroid = np.sin(2*np.pi*x/L) * np.cos(2*np.pi*y/L) + \
#         np.sin(2*np.pi*y/L) * np.cos(2*np.pi*z/L) + \
#         np.sin(2*np.pi*z/L) * np.cos(2*np.pi*x/L)

## Create a mask for the gyroid surface based on the thickness
#mask = np.abs(gyroid) < (thickness / 2)

## Create a mask for the maximum void size
#void_mask = gyroid > void_max

## Combine the masks
#final_mask = np.logical_and(mask, np.logical_not(void_mask))

## Plotting (this is just for visualization)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.voxels(final_mask, edgecolor="k")
#plt.show()
