#This is a spatial hash. 
#A simple way of putting it is: "we store these points in a grid, 
# and you can retrieve an entire grid cell with its points."
 
 
import random
import time
import math
 
 
def from_points(cell_size, points):
    """
    Build a HashMap from a list of points.
    """
    hashmap = HashMap(cell_size)
    #setdefault = hashmap.grid.setdefault
    #key = hashmap.key
    for point in points:
        #setdefault(key(point),[]).append(point)
        dict_setdefault(hashmap.grid, hashmap.key(point),[]).append(point)
    return hashmap
 
 
 
# this is because dict.setdefault does not work.
def dict_setdefault(D, k, d):
    #D.setdefault(k[,d]) -&gt; D.get(k,d), also set D[k]=d if k not in D
    r = D.get(k,d)
    if k not in D:
        D[k] = d
    return r
 
 
 
class HashMap(object):
    """
    Hashmap is a a spatial index which can be used for a broad-phase
    collision detection strategy.
    """
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.grid = {}
 
 
    def key(self, point):
        cell_size = self.cell_size
        return (
            int((math.floor(point[0]/cell_size))*cell_size),
            int((math.floor(point[1]/cell_size))*cell_size),
            int((math.floor(point[2]/cell_size))*cell_size)
        )
 
    def insert(self, point):
        """
        Insert point into the hashmap.
        """
        #self.grid.setdefault(self.key(point), []).append(point)
        dict_setdefault( self.grid, self.key(point), []).append(point)
   
    def query(self, point):
        """
        Return all objects in the cell specified by point.
        """
        #return self.grid.setdefault(self.key(point), [])
        return dict_setdefault( self.grid, self.key(point), [])
 
 
 
 
if __name__ == '__main__':
 
 
    #NUM_POINTS = 100000
    #NUM_POINTS = 6000
    NUM_POINTS = 1000000
    #new_point = lambda: (
    #    #random.uniform(-100,100),random.uniform(-100,100),random.uniform(-100,100)
    #    (random.random() * 200) - 100, (random.random() * 200) - 100, (random.random() * 200) - 100
    #)
 
    #points = [new_point() for i in xrange(NUM_POINTS)]
    points = []
    for i in range(NUM_POINTS):
        points.append( ((random.random() * 200) - 100,
                        (random.random() * 200) - 100,
                        (random.random() * 200) - 100 ) )
 
 
    T = time.time()
    hashmap = from_points(10, points)
    print 1.0 / (time.time() - T), '%d point builds per second.' % NUM_POINTS
 
    T = time.time()
 
    # if this is using ints, then the thing fails to compile with shedskin.
    #hashmap.query((0,0,0))
    hashmap.query((0.0,0.0,0.0))
    print 1.0 / (time.time() - T), '%d point queries per second.' % NUM_POINTS
 
    #hashmap.insert([22,33,33])
    hashmap.insert((22.0,33.0,33.0))



