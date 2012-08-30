'''
Build a matrix of lines... Paths actually.
'''


import random, os, sys, time, numpy, pprint
from shapely import *
from shapely.geometry import *

def main():
	filename='matrix_plot.png'
	numberOfPoints = 500
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
			lineStrings.append(LineString([(point.x, point.y), (pointObj.x, pointObj.y)]))
			matrixEdges.append([index, distance, pointObj.x, pointObj.y])

		lineMatrices.append(matrixEdges)

		ComplexLine = False
		# assembled the points together into a segment of lines
		for line in lineStrings:
			if not ComplexLine:
				ComplexLine = line
				continue
			ComplexLine = line.intersection(ComplexLine)
	
		ComplexLines.append(ComplexLine)

	# Now you just have to iterate through ComplexLines for each complexLine
	# Each Complex line is composed of a Line
	# Draw EACH LINE


	#pprint.pprint(matrix)
	

	#_-------------------------------------------------------------------------------
	# DRAW A REPRESENTATION OF THE LOGIC ABOVE:
	import matplotlib
	matplotlib.use('Agg') # Do NOT attempt to open X11 instance
	from pylab import *
	from matplotlib.patches import Circle
	import matplotlib.pyplot as pyplot

	mylist = lineMatrices

	matplotlib.rcParams['lines.linewidth'] = 2


	pyplot.axis([0, gridWidth, 0, gridHeight])
	pyplot.grid(True)
	# Setting the axis labels.
	pyplot.xlabel('X Space')
	pyplot.ylabel('Y Space')

	#Give the plot a title
	pyplot.title('Shapely d')
	del idx
	if not isinstance(mylist, list):
		print "The matrix is not a list!"
		print type(mylist).__name__
	
	for idx, connected in enumerate(mylist):
		centerPoint = shapePoints[idx]
		
		for line in connected:
			pprint.pprint(line)
			# index, distance, x, y
			pyplot.plot([centerPoint.x, line[2]], [centerPoint.y, line[3]], 'b-', alpha=0.3, linewidth=.2, markersize=1)
		pyplot.plot(centerPoint.x, centerPoint.y, 'ro', linewidth=2, markersize=2)

	print "Saving Plot Image %s" % filename
	pyplot.savefig(os.getcwd()+'/'+str(filename), dpi=220)
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
