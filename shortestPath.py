import sys
infinity = sys.maxint - 1


'''
To generate sample data we will need to first create vertices, then connect the vertices in a logical fashion.
'''

# Each vertex can be described like this:
'''
vertex = {
  'id': vertexName,
  'edges': {vertexName2, distanceTo}
}
'''
 
class Vertex(object):
	"""A vertex in a graph, using adjacency list.

	'edges' is a sequence or collection of tuples (edges), the first element of
	which is a name of a vertex and the second element is the distance to that vertex.

	name = index
	edges = (index, distanceTo)
	

	'name' is a unique identifier for each vertex, like a city name, an integer, a tuple of coordinates..."""

	def __init__(self, vertexIndex):
		self.name = vertexIndex
		self.edges = []

	# 
	def addVertexEdge(self, edgeIndex, distance):
		self.edges.append([edgeIndex, distance])
		
	# you can do this instead of adding vertexes individually.
	def setVertexEdges(self, edges):
		self.edges = edges

#graph is a list of vertex
#source is a vertex that is the START
#dest is a vertex that is the END
class ShortestPath():
	def __init__(self):
		self.graph = []
		self.source = False
		self.dest = False
	
	def addGraphVertex(self, Vertex):
		self.graph.append(Vertex)

	# Set the vertex you would like to Start at - accepts a Vertex() object
	def setStartVertex(self, Vertex):
		self.source = Vertex
	
	# Set the vertex you would like to use as the index - accepts a Vertex() object
	def setDestVertex(self, Vertex):
		self.dest = Vertex
	
	def calculate(self):
		"""Returns the shortest distance from source to dest and a list of traversed vertices, using Dijkstra's algorithm.

		Assumes the graph is connected."""

		# FIX THIS ... replace var names wtih self.x
		graph = self.graph
		source = self.source
		dest = self.dest

		distances = {}
		names = {}
		path = []
		for vertex in graph:
			distances[vertex.name] = infinity # Initialize the distances
			names[vertex.name] = vertex # Map the names to the vertices they represent
		distances[source.name] = 0 # The distance of the source to itself is 0
		dist_to_unknown = distances.copy() # Select the next vertex to explore from this dict
		last = source
		while last.name != dest.name:
			# Select the next vertex to explore, which is not yet fully explored and which 
			# minimizes the already-known distances.
			next = names[ min( [(v, k) for (k, v) in dist_to_unknown.iteritems()] )[1] ]
			for n, d in next.edges: # n is the name of an adjacent vertex, d is the distance to it
				distances[n] = min(distances[n], distances[next.name] + d)
				if n in dist_to_unknown:
					dist_to_unknown[n] = distances[n]
			last = next
			if last.name in dist_to_unknown: # Delete the completely explored vertex
				path.append(last.name)
				del dist_to_unknown[next.name]
		return distances[dest.name], path


