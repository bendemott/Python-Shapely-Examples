'''
Because shapely api objects are in fact objects we should be able to set
arbitrary properties on the objects. This is useful if you want the shapely
object to relate back to a OBJECT_ID or an arbitrary index that references
the object the geometric point/object corresponds to.
'''

from shapely import *
from shapely.geometry import Point
myPoint = Point(1.2, 3.0)
myPoint.idx = 'custom_idx'
# Performing operations that creates a new object or modifies the object will
# cause your custom attribute to be lost...
circle = myPoint.buffer(3.0, 16)
circle.idx = myPoint.idx
print circle.idx
