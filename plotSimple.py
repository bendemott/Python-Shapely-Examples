#SEE http://matplotlib.sourceforge.net/api/pyplot_api.html


import matplotlib
matplotlib.use('Agg') # Do NOT attempt to open X11 instance
from pylab import *
import matplotlib.pyplot as pyplot
import os

# First argument is the graph of X coords
# Second argument is the plot of Y coords
pyplot.plot([0, 10, 10, 12, 40, 40, 100], [0, 10, 20, 30, 40, 40, 100], 'g--')
# Arguments to control the dimensions (range) of the axis
# ymin, ymax, xmin, xmax
pyplot.axis([0, 100, 0, 100])
pyplot.grid(True)
# Setting the axis labels.
pyplot.xlabel('X Coordinate')
pyplot.ylabel('Y Coordinate')

#Give the plot a title
pyplot.title('Test of Simple Line Plotting')
pyplot.savefig(os.getcwd()+'/plot.png')

#plot arguments:
# (x1, y1, style ...)
# LINE STYLES:
# - (solid line)
# -- (dashed line)
# -. (dashed, dotted line)
# : (dotted line)
#...
#a.plot(x1, y1, 'g^', x2, y2, 'g-')



# other drawing styles -->
# 'r' red line, 'g' green line, 'y' yellow line
# 'ro' red dots as markers, 'r.' smaller red dots, 'r+' red pluses
# 'r--' red dashed line, 'g^' green triangles, 'bs' blue squares
# 'rp' red pentagons, 'r1', 'r2', 'r3', 'r4' well, check out the markers


