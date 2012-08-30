'''
point.length
point.area
distance

@author Ben DeMott
@file shapely_properties.py

Various properties of a shapely object
'''

from shapely.geometry import *
import sys

point1 = Point((10, -10))

point1.x # For a point returns X position
point1.y # For a point returns Y position

point1.coords # Returns coordinates that compose
point1.geom_type # Returns the type of Geometric Shape the object is
point1.area
point1.length
point1.bounds

collection.geom # Returns shapes that composes a collection

shape = LinearRing([(0, 0), (1, 1), (1, 0)])
pointInside = shape.representative_point()
distance = shape.distance(point1)


