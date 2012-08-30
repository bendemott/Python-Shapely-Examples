'''
RTREE is a spatial index that answers the question ->
What points are within this 2-dimensional box.
RTREE helps us speed up other calculations by only considering legitimate
objects for more complex comparisons.

'''

from rtree import Rtree
# instantiate the Rtree class
idx = Rtree()
# create a selection boundary (2d bounding box)
minx, miny, maxx, maxy = (0.0, 0.0, 1.0, 1.0)
# add an item to the index
idx.add(0, (minx, miny, maxx, maxy))
# Intersect another bounding box with the original bounding box.
list(idx.intersection((1.0, 1.0, 2.0, 2.0)))
#[0L]
# Point out the accuracy of the spatial calculation
list(idx.intersection((1.0000001, 1.0000001, 2.0, 2.0)))
#[]

#add another item to the index. - show EXACT dimensiion matching
index.add(id=id, (left, bottom, right, top))
object = [n for n in index.intersection((left, bottom, right, top))]
#[id]

# Find nearest object / bounding box
idx.add(1, (minx, miny, maxx, maxy))
list(idx.nearest((1.0000001, 1.0000001, 2.0, 2.0), 1))
#[0L, 1L]

