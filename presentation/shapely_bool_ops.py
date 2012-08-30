
'''
@author Ben DeMott
@file shapely_bool_ops.py

Shapely Boolean Operations are methods associated with a geometric object
that return True/False 
'''

from shapely.geometry import *
import sys

point1 = Point((1, 1))
# See if another point is almost equal to our point...
# The second argument determines variance in the calculation
print "Point 1 is about equal to Point2?:"
print point1.almost_equals(Point(1.01, 1.01), decimal=1)
# True

# See if the exterior of an object is within our object
point2 = point1
point1.buffer(1)
# See if point1 contains point2 ?
print "Point 1 contains Point 2 ?:"
print point1.contains(point2)
# True

sys.exit()

# OTHERS:

# True if the interior or exterior intersects
shape1.intersects(shape2)
# Intersection is equivelant to this statement
intersects = (shape1.contains(shape2) OR shape1.crosses(shape2) OR shape1.equals(shape2) OR shape1.touches(shape2), OR shape1.within(shape2))

# True if ONLY the boundary (exterior) of two objects intersect/touch
shape1.touches(shape2)

# True of one objects components are equal to another
shape1.equals(shape2)

# True If interior of shape1 intersects interior of shape2
shape1.crosses(shape2)

# Interior and exterior boundaries don't intersect/share coordinates
shape1.disjoint(shape2)


