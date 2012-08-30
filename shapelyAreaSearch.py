'''
@author Ben DeMott
@file shapely_radius_plot.py

In this example we will perform an area/radius search.

We will create a bunch of points in a 2d coordinate system and then we will
create a circle or a perimeter.  The we will do a search for any points that
are within the circles perimeter!  :) :) :)

'''

import random, os, sys, time, numpy
from shapely import *
from shapely.geometry import Point

filename = 'radius_search.png'
numberOfPoints = 1000
gridWidth = 10000
gridHeight = 10000
shapePoints = []

circleRadius = random.randint(500, 1500)
circleX = random.randint(0, gridWidth)
circleY = random.randint(0, gridHeight)

sCircle = Point(circleX, circleY)
sCircle = sCircle.buffer(circleRadius, 16)

pointList = []
for i in range(numberOfPoints):
	x = random.randint(0, gridWidth)
	y = random.randint(0, gridHeight)
	pointList.append((x, y))
	iPoint = Point(x, y)
	iPoint.idx = i # set our custom attribute. (if this doesnt work I have other ways)
	shapePoints.append(iPoint)

matchingPoints = []
searchBench = time.time()
for idx, point in enumerate(shapePoints):
	if sCircle.contains(point):
		matchingPoints.append(idx)

searchBench = time.time() - searchBench

print "There were %d points within the circle [%d, %d] - r[%d]\n" % (len(matchingPoints), circleX, circleY, circleRadius)
print "Calculation Took %s seconds for %s points" % (searchBench, numberOfPoints)
print "Saving Graph to %s" % (filename)


#_-------------------------------------------------------------------------------
# DRAW A REPRESENTATION OF THE LOGIC ABOVE:
import matplotlib
matplotlib.use('Agg') # Do NOT attempt to open X11 instance
from pylab import *
from matplotlib.patches import Circle
import matplotlib.pyplot as pyplot


matplotlib.rcParams['lines.linewidth'] = 2


pyplot.axis([0, gridWidth, 0, gridHeight])
pyplot.grid(True)
# Setting the axis labels.
pyplot.xlabel('X Space')
pyplot.ylabel('Y Space')

#Give the plot a title
pyplot.title('Radius Search Plot Using Shapely (%d Points)' % (numberOfPoints)) 

# Draw the collision circle/boundary
cir = Circle((circleX, circleY), radius=circleRadius, fc='b')
cir.set_alpha(0.4)
pyplot.gca().add_patch(cir)


for idx, point in enumerate(pointList):
	style = 'go'
	iAlpha = 0.4
	if(idx in matchingPoints):
		style = 'ro'
		iAlpha = 1
	pyplot.plot(point[0], point[1], style, linewidth=1, markersize=3, alpha=iAlpha)


pyplot.savefig(os.getcwd()+'/'+str(filename))






