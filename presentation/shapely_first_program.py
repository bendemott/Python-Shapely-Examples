# OUR FIRST SHAPELY PROGRAM
# @file shapely_first_program.py
# @author Ben DeMott

from shapely.geometry import Point
# Create a xy point (all coordinates are given as tuples)
patch = Point(0.0, 0.0).buffer(10.0)
# Find the area of our point after giving it a radius of 10
print patch.area
#313.65484905459385 - measurement is given in arbitrary units

