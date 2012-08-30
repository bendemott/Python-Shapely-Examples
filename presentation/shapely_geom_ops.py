'''
@author Ben DeMott
@file shapely_geom_ops.py

Geometric Operations that can be performed against Shapely Objects
'''

from shapely.geometry import *

point = Point(2, 2)
polygon = Polygon([[1, 1], [1, 3], [3, 3], [3, 1]])
polygon2 = Polygon([[2, 2], [2, 4], [4, 4], [4, 2]])

# increase the boundary of a point by 3 units
# Second argument is resolution/accuracy
newPoint = point.buffer(3, 16)

# Compute the distance from the boundary of an object to a point
polygon.distance(point)

# Compute the center of an object
polygon.centroid

# Compute a point inside an object
polygon.representative_point()
# Returns a representation of the boundary of a complex type
# The boundary of a Polgygon is a multi-line, the boundary of a line is a 
# collection of points
polygon.boundary

# Create a shape from the difference between two shapes
polygon.difference(polygon2)
# Combine 2 objects
polygon.intersection(polygon2)
# Return points that are shared
polygon.symmetric_difference()



