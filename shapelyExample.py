'''
I'm trying to calculate if an objext is within a circle on a 2d coordinate system.
First of all I have no way of currently plotting images of a 2d coordinate system
or interacting with the coordinate system directly - so I'll have to work on a
tool that accomplishes this later.
For right now -> Just trying to calculate intersections of a collection of
objects.
The RTREE index is useful for knowing what objects are within a given area.

'''
from shapely import *
p = Point(0.0, 0.0)
x = p.buffer(1.0)
x.area
#3.1365484905459389
len(x.exterior.coords)
#66
s = x.simplify(0.05, preserve_topology=False)
s.area
#3.0614674589207187
len(s.exterior.coords)
#17

#point = Point(x,y)
'''
Buffering is the act of either exploding, or imploding the area around an object.
Positive buffer numbers explode.
Exploding on a point increases the size of the point equally in all directions-
thus creating a circle.

The default (resolution of 16) buffer of a point is a polygonal patch with 
99.8% of the area of the circular disk it approximates.
'''
point = Point(0,0);
#object.buffer(size, resolution = 16)
circle = point.buffer(1.0)
x.simplify(0.01, preserve_topology=False)


'''
the object.convex_hull is a great way to create objects from arbitrary points or
boundaries.  If you create a connected object you can test when items enter
a specific area or collide/intersect that object - this is perfect for games
'''


# ------------------------------------------------------------------------------

'''
Testing if a point is inside a circle -> 
In this logic below I will create a point, and see if its in a circle.
*I moved this to a different file... 
'''
import random

numberOfPoints = 100
gridWidth = 10,000
gridHeight = 10,000
shapePoints = []

circleRadius = random.randint(50, 500)
circlyX = random.randint(0, gridWidth)
circleY = random.randint(0, gridHeight)

sCircle = 

for i in range(numberOfPoints):
	x = random.randint(0, gridWidth)
	y = random.randint(0, gridHeight)
	shapePoints.append(Point())

for points as point:

if circle.contains(other)
		


'''
BATCH COMPARISON OPERATIONS:


'''
from shapely.geometry import Point
from shapely.prepared import prep
points = [...] # large list of points
circle = Point(0.0, 0.0).buffer(1.0)
prepared_polygon = prep(circle)
hits = filter(prepared_polygon.contains, points)


'''
You can interact with any geometric object and get its coordinates in a simple
fashion using the .xy property:
'''
Point(0, 0).xy
#(array('d', [0.0]), array('d', [0.0]))

# SIMILAR OPERATION WITH NUMPY:
from numpy import array
array(Point(0, 0))
#array([ 0.,  0.])
array(LineString([(0, 0), (1, 1)]))
#array([[ 0.,  0.],
#       [ 1.,  1.]])


