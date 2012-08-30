'''
Copyright (C) 2010 Ben DeMott

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

#SEE http://matplotlib.sourceforge.net/api/pyplot_api.html

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
# Setting the axis labels.
plt.ylabel('some numbers')
plt.show()


import matplotlib.pyplot as plt
#plot red circles on the axis
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# Configuring the Axis:
#[xmin, xmax, ymin, ymax] 
plt.axis([0, 6, 0, 20])


#enable a background grid:
plt.grid(True)

#Give the plot a title
plt.title('Histogram of IQ')


#plot arguments:
# (x1, y1, style ...)
# LINE STYLES:
# - (solid line)
# -- (dashed line)
# -. (dashed, dotted line)
# : (dotted line)
#...
a.plot(x1, y1, 'g^', x2, y2, 'g-')


from pylab import *
import numpy as np
from matplotlib.transforms import Bbox
from matplotlib.path import Path
from matplotlib.patches import Rectangle

# Draw a box
rect = Rectangle((-1, -1), 2, 2, facecolor="#aaaaaa")
gca().add_patch(rect)
pyplot.gca().add_patch(cir)

# other drawing styles -->
# 'r' red line, 'g' green line, 'y' yellow line
# 'ro' red dots as markers, 'r.' smaller red dots, 'r+' red pluses
# 'r--' red dashed line, 'g^' green triangles, 'bs' blue squares
# 'rp' red pentagons, 'r1', 'r2', 'r3', 'r4' well, check out the markers


# save the plot as a PNG image
pylab.savefig('plot.png')


# Making the image into a PIL image for further manipulation!
import StringIO, Image
imgdata = StringIO.StringIO()
fig.savefig(imgdata, format='png')
imgdata.seek(0)  # rewind the data
im = Image.open(imgdata)

