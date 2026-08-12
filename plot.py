import easyplot.easyplot as ep
import math
from poly import poly


## want function that takes in range of sides of shapes
## from those ranges of sides, interpolates from smallest to largest 

ep.init()
ep.switchPen(7)

## Constants
center = (ep.BOUNDS[0]/2, ep.BOUNDS[1]/2)
steps = 4
scale = ep.BOUNDS[1]/10

def slideShape(pts, sides, drawFunc):
     for i in range(len(pts)):
        p0, p1 = pts[i], pts[(i + 1) % sides]
        for j in range(steps):
            t = j/(steps)
            pt = (
                   p0[0]*(1-t) + p1[0]* t,
                   p0[1]*(1-t) + p1[1]* t,
                )
            drawFunc(pt[0], pt[1])

def tri(x, y):
    ep.regularPolygon(x+center[0], y+center[1], ep.BOUNDS[1]/20, 3)

def squaretri(x, y):
    sqpts = poly(x, y, 4, math.pi/4, scale)
    slideShape(sqpts, 5, tri)

pts = poly(0, 0, 5, math.pi/5, scale*3)
slideShape(pts, 5, squaretri)

ep.end()
