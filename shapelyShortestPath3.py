'''
This script builds a matrix of vertices, draws paths between them to connect the vertices.
Once the vertices are connected we pick two random vertices and determine the shortest route between
them.

Disclaimer:
-----------
This is kind of a mess, I threw it together rather quickly.
The code is just kind of 'fun' example.
I used this as the basis for a 2 dimensional game I made, written in OpenGL

License:
---------
Copyright (C) 2009 Ben DeMott

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


import random, os, sys, time, numpy, pprint
from shapely import *
from shapely.geometry import *
import dijkstra
from rtree import Rtree

def main():

	# You can edit these vars:
	# -----------------------
	filename='matrix_plot3.png'
	numberOfPoints = 200
	gridWidth = 10000
	gridHeight = 10000
	edgesMinimum = 2
	edgesMaximum = 4 # The maximum number of edges (connecting lines) a vertex can have
	# -----------------------
	edgesMaxDistance = (gridWidth / numberOfPoints) * 2
	
	# instantiate the Rtree class
	RtreeIndex = Rtree()

	# CREATE THE RANDOM POINTS:

	shapelyPointIndex = []  # Stores index = shapely object - We will reference this point from its Index from this point on.
	for idx in range(numberOfPoints): # Each point gets its own index defined by i
		x = random.randint(0, gridWidth)
		y = random.randint(0, gridHeight)
		iPoint = Point(x, y) # Create a new shapely POINT object
		shapelyPointIndex.append(iPoint)
		RtreeIndex.add(idx, (x, y, x, y))  # Add the point to the RTREE Index

	del idx #unset temp variable
	# --------------------------------------------------------------------------

	#MultiPoint([(0, 0), (1, 1)])
	#point.coords
	#point.y   point.x

	lineMatrices = []
	ComplexLines = []
	graphIndex = {} # This is a dictionary we will build into a graph/matrix - Each key will be an integer representing an index
	#                 and each value will be a dictionary of dictionaries representing edges.
	# iterate over all points to calculate each points nearest points
	# build line segments for each point to near points.
	# add all edges to a master complex line to compute intersection.
	for idx, point in enumerate(shapelyPointIndex):


		# Find nearby points quickly
		rtreeMatches = list()
		sRadiusX = gridWidth / 10
		sRadiusY = gridHeight / 10
		tries = 0
		while(len(rtreeMatches) < edgesMinimum+1):  # Add 1 because we can assume it will always find itself
			# Coords is a bounding-box to search within.
			coords = (point.x-sRadiusX, point.y-sRadiusY, point.x+sRadiusX, point.y+sRadiusY)
			print "searching coords"
			print coords
			rtreeMatches = list(RtreeIndex.intersection(coords))
			print "found: ", rtreeMatches, "  ", len(rtreeMatches)
			tries +=1
			sRadiusX *= 1.5
			sRadiusY *= 1.5
			if(tries > 6): #Don't run forever if there is a logic problem.
				break

		del tries, sRadiusX, sRadiusY

		# FIND POSSIBLE EDGES TO ADD BY SEARCHING REGION RECURSIVELY -----------
		# AND CALCULATE DISTANCES TO POSSIBLE POINTS ---------------------------
		# This dictionary will store our distances to each other point from this point.
		edgeDistances={}
		# Calculate distances to matched points
		for pointIdx in rtreeMatches:
			if(pointIdx == idx):
				continue # Don't record a distance to itself
			mPoint = shapelyPointIndex[pointIdx]
			edgeDistances[pointIdx] = round(mPoint.distance(point), 2)  # keep the distance accuracy reasonable

		del mPoint, pointIdx, rtreeMatches

		# create a list that references the distances index for the closest indexes and is sorted by close to far.
		edgeDistancesIdx = sorted(edgeDistances, key=edgeDistances.get)
		#-----------------------------------------------------------------------


		# DECIDE WHICH EDGES TO ADD --------------------------------------------
		# Now add a minimum number of points, and try to keep them within a logic distance
		edgesAdded = 0
		edgesIdx=[]  # this will contain indexes to our added edges
		for pointIdx in edgeDistancesIdx:
			distance = edgeDistances[pointIdx]
			# Stop adding edges if we've meant the minimum number of edges needed and the rest of the edges are too far away, or we have reach the maximum number of allowed edges
			if((edgesAdded >= edgesMinimum and distance > edgesMaxDistance) or edgesAdded >= edgesMaximum):
				break
			
			edgesIdx.append(pointIdx)

		del pointIdx


		#-----------------------------------------------------------------------
		# Initialize the graphIndex as a dict() for the current vertex if it hasn't been.
		if(idx not in graphIndex):
			graphIndex[idx] = {}
		#ADD THE EDGES TO THE GRID STRUCTURE -----------------------------------
		for pointIdx in edgesIdx:
			# Add the edge
			graphIndex[idx][pointIdx] = edgeDistances[pointIdx]
			# Add the reverse edge (so both points share an edge)
			if pointIdx not in graphIndex:
				graphIndex[pointIdx] = {}
			graphIndex[pointIdx][idx] = edgeDistances[pointIdx]

	#-----------------------------------------------------------------------

	# Print out the graph of vertices
	pprint.pprint(graphIndex)

	# Randomely select a Start Vertex, and an End Vertex for Shortest Path 
	# calculation
	startIdx = random.randint(0, len(graphIndex)-1)
	endIdx = startIdx
	# Calculate a random end index - and make sure its not the same as the start 
	while(endIdx == startIdx):
		endIdx = random.randint(0, len(graphIndex)-1)

	# Setup shortest path calculation!
	print "Calculating Shortest Path:\n"

	# (8894.6959143222557, [11, 5, 8L, 7, 9])
	# GraphIndex is a dictionary of dictionaries, startIdx is the INDEX of the startpoint, endIdx is the index of the endpoint vertex.
	shortestPath = dijkstra.shortestpath(graphIndex, startIdx, endIdx)
	shortestPathVertices = shortestPath[1]
	shortestPathDistance = shortestPath[0]

	print "Shortest Path Vertices:"
	print shortestPathVertices, "\n"
	
	del shortestPath


	#_-------------------------------------------------------------------------------
	# DRAW A PLOT FOR THE LINES CALCULATED ABOVE:
	import matplotlib
	matplotlib.use('Agg') # Do NOT attempt to open X11 instance
	from pylab import *
	from matplotlib.patches import Circle
	import matplotlib.pyplot as pyplot
	from matplotlib.text import *

	mylist = lineMatrices

	matplotlib.rcParams['lines.linewidth'] = 2


	pyplot.axis([0, gridWidth, 0, gridHeight])
	pyplot.grid(True)
	# Setting the axis labels.
	pyplot.xlabel('X Space')
	pyplot.ylabel('Y Space')

	figure = pyplot.figure()
	labels = figure.add_subplot(111, projection='rectilinear')


	#Give the plot a title
	pyplot.title('Shapely Shortest Path Simulation')
	del idx
	if not isinstance(mylist, list):
		print "The matrix is not a list!"
		print type(mylist).__name__
	
	for idx, edges in graphIndex.iteritems():
		vertex = shapelyPointIndex[idx]
		
		for edgeIdx, edgeDistance in edges.iteritems():
			# This shouldn't happen, but lets just make sure.
			# DONT PLOT A PATH TO OURSELF
			if(edgeIdx == idx):
				continue
			# Get the edges point-coordinates
			edgePoint = shapelyPointIndex[edgeIdx]

			# Delete the reverse edge so we don't plot the line twice.
			if(edgeIdx in graphIndex):
				del graphIndex[edgeIdx][idx]

			# Print Debuggin Information
			print "PLOTTING EDGE: [%s] to [%s]    X:[%s] Y:[%s]  DIS:[%s] " % (idx, edgeIdx, edgePoint.x, edgePoint.y, edgeDistance)

			# Plot the edge!
			pyplot.plot([vertex.x, edgePoint.x], [vertex.y, edgePoint.y], 'b-', alpha=0.3, linewidth=.2, markersize=1)

			# FIND THE MID-POINT OF THE LINE:
			xMidpoint = (vertex.x + edgePoint.x) / 2
			yMidpoint = (vertex.y + edgePoint.y) / 2

			#print "Plotting Text [%s] [%s]" % (xMidpoint, yMidpoint)
			# Figure out arrows later... arrowprops=dict(facecolor='black', linewidth=2,  alpha=0.4),

			# ANNOTATE THE LENGTH OF THE LINE AT ITS MIDPOINT
			labels.annotate(edgeDistance, xy=(xMidpoint, yMidpoint), xytext=(xMidpoint+80, yMidpoint), alpha=0.4, size='4', color='green')
			# end for ----------------------------------------------------------

		# Plot the VERTEX as a Red Circle
		pyplot.plot(vertex.x, vertex.y, 'ro', linewidth=2, markersize=2)
		# Annotate the VERTEX by its INDEX
		labels.annotate(idx, xy=(vertex.x, vertex.y), xytext=(vertex.x+50, vertex.y), alpha=0.6, size='6', color='red')

	print "Graphing Shortest Path..."
	print "START: %s  END: %s" % (startIdx, endIdx)

	#shortestPathVertices
	for idx, vertexIdx in enumerate(shortestPathVertices):
		
		if(vertexIdx == endIdx):
			break # We are done

		xy1 = shapelyPointIndex[vertexIdx] # this is the start of the line
		vertex2 = shortestPathVertices[idx+1] # The end of the line is the next item in the list shortest path list of indexes
		xy2 = shapelyPointIndex[vertex2] #this is the end of the line

		pyplot.plot([xy1.x, xy2.x], [xy1.y, xy2.y], 'r--', alpha=0.7, linewidth=2, markersize=1)
		print "PLOT -> SHORTEST PATH: [%s] to [%s]" % (vertexIdx, vertex2)

	print "Saving Plot Image %s" % (filename)
	pyplot.savefig(os.getcwd()+'/'+str(filename), dpi=240)
	print "\n\n"



	
	"""
		

	a = LineString([(0, 0), (1, 1), (1,2), (2,2)])
	b = LineString([(0, 0), (1, 1), (2,1), (2,2)])
	x = a.intersection(b) # connext the two line strings

	# Create LineString using:
	LineString(coordinates)
	# Coordinates are sets of [x,y], [x,y]

	# Create a multi-line string using:
	MultiLineString(lines)

	# You can always create a multiline string from lists of lists of (x,y) tuples (hehe)
	 m = MultiLineString([[(0, -2), (0, 2)], [(-2, 0), (2, 0)]])



	from shapely.geometry import MultiLineString
	coords = [((0, 0), (1, 1)), ((-1, 0), (1, 0))]
	lines = MultiLineString(coords)
	lines.area


	object.difference(other)
	   # Returns a representation of the points making up this geometric object that do not make up the other object.

	"""

if __name__ == '__main__':
	sys.exit(main())
