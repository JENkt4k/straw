#last gen 
import bpy
import numpy as np

# Clear existing mesh and metaball objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.select_by_type(type='META')
bpy.ops.object.delete()

## User-input values
#wall_count = 2  # For example
#nozzle_width = 0.4  # In mm, for example
#bounding_dimension_of_cube = 10.0  # In mm, for example
#min_cell_count = 10  # For example

## Derived parameters
#L = bounding_dimension_of_cube  # Grid size in mm
#cell_size = bounding_dimension_of_cube / min_cell_count  # Cell size in mm
#radius = nozzle_width * wall_count  # Metaball radius in mm
#factor = 6
#res = factor*int(bounding_dimension_of_cube / cell_size)  # Resolution
#thickness = nozzle_width * wall_count  # Thickness in mm

## User-input values
#wall_count = 3  # For example
#nozzle_width = 0.4  # In mm, for example
#bounding_dimension_of_cube = 10.0  # In mm, for example
#min_cell_count = 10  # For example

## Derived parameters
#L = bounding_dimension_of_cube  # Grid size in mm
#cell_size = L / min_cell_count  # Cell size in mm

## Wall thickness and metaball radius should only depend on nozzle_width and wall_count
#radius = nozzle_width * wall_count  # Metaball radius in mm
#thickness = nozzle_width * wall_count  # Thickness in mm

## Resolution should not affect wall thickness
#res = 4*int(L / cell_size)# int(cell_size/thickness) #4*int(L / cell_size)  # Resolution

## User-input values
#wall_count = 2  # For example
#nozzle_width = 0.4  # In mm, for example
#bounding_dimension_of_cube = 10.0  # In mm, for example
#min_cell_count = 5  # For example

## Derived parameters
#L = bounding_dimension_of_cube  # Grid size in mm
#cell_size = L / min_cell_count  # Cell size in mm

## Wall thickness and metaball radius should only depend on nozzle_width and wall_count
#radius = nozzle_width * wall_count  # Metaball radius in mm
#thickness = nozzle_width * wall_count  # Thickness in mm

## Resolution should not affect wall thickness
#res = int(L / cell_size)  # Resolution

## User-input values
#wall_count = 2  # For example
#nozzle_width = 0.4  # In mm, for example
#bounding_dimension_of_cube = 10.0  # In mm, for example
#min_cell_count = 10  # For example
#resolution_factor = 4  # New parameter to increase resolution

## Derived parameters
#L = bounding_dimension_of_cube  # Grid size in mm
#cell_size = L / min_cell_count  # Cell size in mm

## Wall thickness and metaball radius should only depend on nozzle_width and wall_count
#radius = nozzle_width * wall_count  # Metaball radius in mm
#thickness = nozzle_width * wall_count  # Thickness in mm

## Resolution should not affect wall thickness but can be increased to make metaballs merge
#res = resolution_factor * int(L / cell_size)  # Increased Resolution

## Now you can use these derived values in your script to create the metaballs


## User-input values
#wall_count = 2  # For example
#nozzle_width = 0.4  # In mm, for example
#bounding_dimension_of_cube = 10.0  # In mm, for example
#min_cell_count = 5  # For example

## Derived parameters
#L = bounding_dimension_of_cube  # Grid size in mm
#cell_size = L / min_cell_count  # Cell size in mm

## Calculate radius based on the number of metaballs that will span the given space
#radius = L / min_cell_count  # Metaball radius in mm

## Wall thickness should only depend on nozzle_width and wall_count
#thickness = nozzle_width * wall_count  # Thickness in mm

## Resolution should not affect wall thickness
#res = 2*int(L / cell_size)  # Resolution

## Now you can use these derived values in your script to create the metaballs

## User-input values
#wall_count = 2  # For example
#nozzle_width = 0.4  # In mm, for example
#bounding_dimension_of_cube = 10.0  # In mm, for example
#min_cell_count = 10  # For example
#merge_factor = 1.5  # New parameter to increase radius

## Derived parameters
#L = bounding_dimension_of_cube  # Grid size in mm
#cell_size = L / min_cell_count  # Cell size in mm

## Calculate radius based on the number of metaballs that will span the given space
#radius = (L / min_cell_count) * merge_factor  # Adjusted Metaball radius in mm

## Wall thickness should only depend on nozzle_width and wall_count
#thickness = nozzle_width * wall_count  # Thickness in mm

## Resolution should not affect wall thickness
#res = int(L / cell_size)  # Resolution

#print("User-input values:")
#print(f"Wall Count: {wall_count} (Expected: 2)")
#print(f"Nozzle Width: {nozzle_width} mm (Expected: 0.4 mm)")
#print(f"Bounding Dimension of Cube: {bounding_dimension_of_cube} mm (Expected: 10.0 mm)")
#print(f"Minimum Cell Count: {min_cell_count} (Expected: 5)")
#print(f"Merge Factor: {merge_factor} (Expected: 1.2)")

#print("\nDerived parameters:")
#print(f"Grid Size (L): {L} mm (Expected: 10.0 mm)")
#print(f"Cell Size: {cell_size} mm (Expected: {L/min_cell_count} mm)")
#print(f"Metaball Radius: {radius} mm (Expected: {L/min_cell_count * merge_factor} mm)")
#print(f"Wall Thickness: {thickness} mm (Expected: {nozzle_width * wall_count} mm)")
#print(f"Resolution: {res} (Expected: {int(L / cell_size)})")

## User-input values
wall_count = 2
nozzle_width = 0.4
bounding_dimension_of_cube = 10.0
min_cell_count = 10
merge_factor = 4  # Adjust this to control thickness

## Derived parameters
L = bounding_dimension_of_cube
#cell_size = L / min_cell_count

## User-input values
#density_factor = 10  # New parameter to increase density

## Derived parameters
#res = min_cell_count * density_factor  # Increased Resolution

## Calculate distance between metaballs and radius
#distance_between_metaballs = L / res
##radius = (distance_between_metaballs / 2) * merge_factor
## Derived parameters
desired_merged_region = nozzle_width * wall_count
radius = desired_merged_region / 2


## Calculate distance between metaballs and radius
##distance_between_metaballs = L / min_cell_count
##radius = (distance_between_metaballs / 2) * merge_factor

## Wall thickness should only depend on nozzle_width and wall_count
thickness = nozzle_width * wall_count

### Resolution should not affect wall thickness
##res = int(L / cell_size)
## User-input values
#density_factor = 4  # New parameter to increase density

## Derived parameters
##res = min_cell_count * density_factor  # Increased Resolution

# User-input values
#wall_count = 2  # For example
#nozzle_width = 0.4  # In mm, for example
overlap_factor = 1.2  # New parameter to control overlap

# Derived parameters
desired_merged_region = nozzle_width * wall_count

# Calculate cell size and initial radius
cell_size = L / min_cell_count
initial_radius = desired_merged_region / 2

# Calculate initial resolution
res = 10*int(cell_size / initial_radius)

# Adjust radius based on overlap factor and resolution
adjusted_radius = (cell_size / res) * overlap_factor

# Print out all the values for debugging
print("User-input values:")
print(f"Wall Count: {wall_count}")
print(f"Nozzle Width: {nozzle_width} mm")
print(f"Overlap Factor: {overlap_factor}")

print("\nDerived parameters:")
print(f"Desired Merged Region: {desired_merged_region} mm")
print(f"Initial Radius: {initial_radius} mm")
print(f"Cell Size: {cell_size} mm")
print(f"Initial Resolution: {res}")
print(f"Adjusted Radius: {adjusted_radius} mm")

# Now you can use these derived values in your script to create the metaballs



# Print out all the values for debugging
print("User-input values:")
print(f"Wall Count: {wall_count}")
print(f"Nozzle Width: {nozzle_width} mm")
print(f"Bounding Dimension of Cube: {bounding_dimension_of_cube} mm")
print(f"Minimum Cell Count: {min_cell_count}")
print(f"Merge Factor: {merge_factor}")

print("\nDerived parameters:")
print(f"Grid Size (L): {L} mm")
print(f"Cell Size: {cell_size} mm")
#print(f"Distance Between Metaballs: {distance_between_metaballs} mm")
print(f"Metaball Radius: {radius} mm")
print(f"Wall Thickness: {thickness} mm")
print(f"Resolution: {res}")

# Now you can use these derived values in your script to create the metaballs



# Now you can use these derived values in your script to create the metaballs


# Now you can use these derived values in your script to create the metaballs


# Now you can use these derived values in your script to create the metaballs


# Create a new Metaball object
mball = bpy.data.metaballs.new("GyroidMeta")
obj = bpy.data.objects.new("GyroidMeta", mball)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

meshL = 3 #L
meshpointcnt = 64 #res

# Generate grid using NumPy
x, y, z = np.linspace(-meshL, meshL, meshpointcnt), np.linspace(-meshL, meshL, meshpointcnt), np.linspace(-meshL, meshL, meshpointcnt)
x, y, z = np.meshgrid(x, y, z)

# Evaluate gyroid equation
gyroid = np.sin(x) * np.cos(y) + np.sin(y) * np.cos(z) + np.sin(z) * np.cos(x)

# Create mask based on thickness
mask = np.abs(gyroid) < thickness

# Create metaballs based on mask
for i in range(meshpointcnt):
    for j in range(meshpointcnt):
        for k in range(meshpointcnt):
            if mask[i, j, k]:
                element = mball.elements.new(type='BALL')
                element.co = (x[i, j, k], y[i, j, k], z[i, j, k])
                element.radius = radius #0.4  # Adjust the radius as needed

# Update scene
bpy.context.view_layer.update()


## Convert to mesh
#try:
#    bpy.ops.object.convert(target='MESH')
#except Exception as e:
#    print(f"Failed to convert metaball to mesh: {e}")

#end of lastgen

# working

#import bpy
#import numpy as np

## Clear existing mesh and metaball objects
#bpy.ops.object.select_all(action='DESELECT')
#bpy.ops.object.select_by_type(type='MESH')
#bpy.ops.object.select_by_type(type='META')
#bpy.ops.object.delete()

### Initialize parameters
##L = 4.0  # size of the grid
##res = 40  # resolution
##thickness = 0.4  # thickness

## Set the minimum dimension
#min_dim = 0.4  # For example, 0.1 cm or 1 mm
##thickness = #min_dim  # thickness in cm (0.8 mm)

## Derive other parameters
##L = 100 * min_dim  # Grid size
#L = 4.0
#res =  60 #int(L / min_dim)  # Resolution
##radius = res/L  # Metaball radius
#radius = 3*(L / (res))  # Metaball radius
#thickness =0.4 #(L / res)# * 0.5

## Create a new Metaball object
#mball = bpy.data.metaballs.new("GyroidMeta")
#obj = bpy.data.objects.new("GyroidMeta", mball)
#bpy.context.collection.objects.link(obj)
#bpy.context.view_layer.objects.active = obj
#obj.select_set(True)

## Generate grid using NumPy
#x, y, z = np.linspace(-L, L, res), np.linspace(-L, L, res), np.linspace(-L, L, res)
#x, y, z = np.meshgrid(x, y, z)

## Evaluate gyroid equation
#gyroid = np.sin(x) * np.cos(y) + np.sin(y) * np.cos(z) + np.sin(z) * np.cos(x)

## Create mask based on thickness
#mask = np.abs(gyroid) < thickness

## Create metaballs based on mask
#for i in range(res):
#    for j in range(res):
#        for k in range(res):
#            if mask[i, j, k]:
#                element = mball.elements.new(type='BALL')
#                element.co = (x[i, j, k], y[i, j, k], z[i, j, k])
#                element.radius = radius #0.4  # Adjust the radius as needed

## Update scene
#bpy.context.view_layer.update()

## end working

## Convert to mesh
#try:
#    bpy.ops.object.convert(target='MESH')
#except Exception as e:
#    print(f"Failed to convert metaball to mesh: {e}")


#import bpy
#import numpy as np

## Clear mesh and metaball objects in the scene
#bpy.ops.object.select_all(action='DESELECT')
#bpy.ops.object.select_by_type(type='MESH')
#bpy.ops.object.select_by_type(type='META')
#bpy.ops.object.delete()

## Initialize parameters
##L = 3.0  # size of the grid, in cm
##res = 10  # resolution

## Set the minimum dimension
#min_dim = 0.4  # For example, 0.1 cm or 1 mm
#thickness = min_dim  # thickness in cm (0.8 mm)

## Derive other parameters
#L = 100 * min_dim  # Grid size
#res =  int(L / min_dim)  # Resolution
##radius = res/L  # Metaball radius
#radius = 4*(L / (res))  # Metaball radius

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
#                element = mball.elements.new(type='BALL')
#                element.co = (x[i, j, k], y[i, j, k], z[i, j, k])
#                element.radius = radius # 0.4  # You can adjust the radius

## Update the scene
#bpy.context.view_layer.update()

## Convert to mesh
#try:
#    bpy.ops.object.convert(target='MESH')
#except Exception as e:
#    print(f"Failed to convert metaball to mesh: {e}")




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
