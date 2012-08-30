'''
Build a matrix of lines... Paths actually.
'''


import random, os, sys, time, numpy, pprint
from shapely import *
from shapely.geometry import *
import shortestPath

def main():
	filename='matrix_plot.png'
	numberOfPoints = 10
	gridWidth = 10000
	gridHeight = 10000

	pointList = []
	shapePoints = []
	for i in range(numberOfPoints):
		x = random.randint(0, gridWidth)
		y = random.randint(0, gridHeight)
		pointList.append((x, y))
		iPoint = Point(x, y)
		iPoint.idx = i # set our custom attribute. (if this doesnt work I have other ways)
		shapePoints.append(iPoint) 

	#MultiPoint([(0, 0), (1, 1)])

	#point.coords
	#point.y   point.x

	lineMatrices = []
	ComplexLines = []
	# iterate over all points to calculate each points nearest points
	# build line segments for each point to near points.
	for idx, point in enumerate(shapePoints):
		idx = point.idx
		distances={}
		# iterate a second time over the list to calculate distances to all other points
		for idx2, point2 in enumerate(shapePoints):
			distances[idx2] = point2.distance(point)

		connections = random.randint(1, 3)
		# create a list that references the distances index for the closest indexes
		sortedIdx = sorted(distances, key=distances.get)
		#print sortedIdx
		lineStrings = []
		matrixEdges=[]
		iteration = 0
		skipCount = 4 - connections # skip more when theres less connections
		skipDepth = random.randint(connections+2, connections+5)  # base the random depth on how many connections there are
		for index in sortedIdx:
			iteration += 1
			if iteration > connections:
				print 'Breaking - idx:%s - con:%s' % (iteration, connections)
				break
			if skipCount > 0:
				skipCount -= 1
				slicePos = skipDepth+iteration
				subiter = 0
				for subIdx in sortedIdx:
					subiter += 1
					if subiter == slicePos:
						distance = distances[subIdx]
						index = subIdx
						break
				print "Skip Distance: %s" % distance
			else:
				distance = distances[index]
			if(distance == 0):
				iteration -= 1
				continue
			pointObj = shapePoints[index]
			print 'distance: %s' % distance
			#Add to the lineStrings list a LineString -> this is for collision detection and shapely arithmetic
			lineStrings.append(LineString([(point.x, point.y), (pointObj.x, pointObj.y)]))
			#Add to the matrix edges other points (this is for shortest path first calculation)
			matrixEdges.append([index, distance, pointObj.x, pointObj.y])
		# Take all of the connections and add them to the list of lineMatrices -> note that the ordinal position will be correct by the nature of how this code iterates
		# ordinal position inside lineMatrices will match pointList, and shapePoints
		lineMatrices.append(matrixEdges)
		#-----------------------------------------------------------------------

	# Setup shortest path calculation!
	print "Calculating Shortest Path:\n"
	dijkstraPath = shortestPath.ShortestPath()

	# Randomely select the start and end vertexes based on a random index.
	startIdx = random.randint(0, numberOfPoints)
	endIdx = random.randint(0, numberOfPoints)

	print "START: %s  END: %s" % (startIdx, endIdx)

	if(len(lineMatrices) != numberOfPoints):
		print "Hmm... lineMatrices != numberOfPoints ???"
	
	for idx, edges in enumerate(lineMatrices):
		print "on %s\r" % (idx)
		iVertexEdges = tuple()
		iVertex = shortestPath.Vertex(idx)
		#add the edges to the vertex object
		for edge in edges:
			iVertex.addVertexEdge(edge[0], edge[1])
		dijkstraPath.addGraphVertex(iVertex)

		# Set this as the starting vertex
		if(idx == startIdx):
			print "START: ", iVertex
			dijkstraPath.setStartVertex(iVertex)

		# Set thsi as the end vertex (destination
		if(idx == endIdx):
			print "END: ", iVertex
			dijkstraPath.setDestVertex(iVertex)

	# Perform the calculation!
	print 'Performing ShortestPath Calculations'
	# ShortestPathVertices are the names of the vertices (which is the index)
	distance, shortestPathVertices = dijkstraPath.calculate()

	print 'Shortest Path Vertices:'
	print shortestPathVertices

	'''
	NOT DONE WITH THIS YET.. 
	ComplexLine = False
	# assembled the points together into a segment of lines
	for line in lineStrings:
		if not ComplexLine:
			ComplexLine = line
			continue
		ComplexLine = line.intersection(ComplexLine)

	ComplexLines.append(ComplexLine)
	'''

	# Now you just have to iterate through ComplexLines for each complexLine
	# Each Complex line is composed of a Line
	# Draw EACH LsetINE


	#pprint.pprint(matrix)
	

	#_-------------------------------------------------------------------------------
	# DRAW A REPRESENTATION OF THE LOGIC ABOVE:
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
	
	for idx, connected in enumerate(mylist):
		centerPoint = shapePoints[idx]
		
		for line in connected:
			print "PLOTTING EDGE: [%s] to [%s] " % (idx, line[0]),
			pprint.pprint(line)
			# index, distance, x, y
			# line = [index, distance, x, y]

			# Plot the edge!
			pyplot.plot([centerPoint.x, line[2]], [centerPoint.y, line[3]], 'b-', alpha=0.3, linewidth=.2, markersize=1)

			# FIND THE MID-POINT OF THE LINE:
			xMidpoint = (centerPoint.x + line[2]) / 2
			yMidpoint = (centerPoint.y + line[3]) / 2
			dText = line[2]

			#print "Plotting Text [%s] [%s]" % (xMidpoint, yMidpoint)
			# Figure out arrows later... arrowprops=dict(facecolor='black', linewidth=2,  alpha=0.4),
			labels.annotate(dText, xy=(xMidpoint, yMidpoint), xytext=(xMidpoint+80, yMidpoint),   alpha=0.4, size='4', color='green')
			# end for ----------------------------------------------------------

		# Plot the XY point
		pyplot.plot(centerPoint.x, centerPoint.y, 'ro', linewidth=2, markersize=2)
		labels.annotate(idx, xy=(centerPoint.x, centerPoint.y), xytext=(centerPoint.x+50, centerPoint.y),   alpha=0.6, size='6', color='red')

	print "Graphing Shortest Path..."
	print "START: %s  END: %s" % (startIdx, endIdx)

	#shortestPathVertices
	lastVertex = False
	for vertexIdx in shortestPathVertices:
		print "Plotting Path: ", vertexIdx
		if(not lastVertex):
			lastVertex = startIdx #This variable is referenced a ways above... 

		xy1 = shapePoints[lastVertex] # this is the start of the line
		xy2 = shapePoints[vertexIdx] #this is the end of the line

		pyplot.plot([xy1.x, xy2.x], [xy1.y, xy2.y], 'r--', alpha=0.3, linewidth=.4, markersize=1)
		lastVertex = vertexIdx

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
