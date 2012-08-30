#@file shapely_shapes.py
#@author Ben DeMott

from shapely.geometry.polygon import *

# Create a Point (a vertex)
vertex = Point((0, 0))

# Create a "line string" (x1,y1), (x2, y2)
vector = LineString(((-25.0, -25.0), (25.0, 25.0)))

# Create a more complex line string
path = LineString([(0, 0), (1, 1), (2,1), (-3, 0)])

# Get the length of the Line String
distance = path.distance

# buffer the line string by 1 unit
path.buffer(1)

# Create a Linear Ring (A linestring that connects to itself)
ring = LinearRing([(0, 0), (1, 1), (1, 0)])
ring.area #Outputs 0 - has no area

# get the Bounds of a ring
ring.bounds
(0.0, 0.0, 1.0, 1.0)

# Complex shapes can be created using polygons
#Polygon(exterior[, interiors=None])

# Collection from Intersection
a = LineString([(0, 0), (1, 1), (1,2), (2,2)])
b = LineString([(0, 0), (1, 1), (2,1), (2,2)])
x = a.intersection(b)

# Multi Line Strings are another type of collection
coords = [((0, 0), (1, 1)), ((-1, 0), (1, 0))]
lines = MultiLineString(coords)

# collections support iterable the property geom_type informs you what
# type of object you are dealing with.

# Boolean Methods:
# .crosses
# .touches
# .contains



