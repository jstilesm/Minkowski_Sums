import easyplot.easyplot as ep
import math
from poly import poly

## Wrapping Function for A collection of points
ep.init()
ep.switchPen(7)

## Constants
center = (ep.BOUNDS[0]/2, ep.BOUNDS[1]/2)
steps = 1
scale = ep.BOUNDS[1]/10
radius = ep.BOUNDS[1]/ 4


def regularPolygonPoints(x, y, radius, sides, rotation = 0):
    pts = [(x + (math.cos(rotation)) * radius, y + (math.sin(rotation)) * radius)]
    for i in range(sides):
        theta = (((i + 1) * ((2 * math.pi) / sides) + rotation) / (2*math.pi))
        pts.append((x + math.cos(theta * 2 * math.pi) * radius, y + math.sin(theta * 2 * math.pi) * radius))
    temp = [([int(v) for v in p]) for p in list(pts)]
    return list(temp)


def slideShape(pts, sides, drawFunc):
    ptspts = []
    for i in range(len(pts)):
        p0, p1 = pts[i], pts[(i + 1) % sides]
        for j in range(steps):
            t = j/(steps)
            pt = (
                   p0[0]*(1-t) + p1[0]* t,
                   p0[1]*(1-t) + p1[1]* t,
                )
            ptspts += drawFunc(pt[0], pt[1])
    return ptspts

def tri(x, y):
    return regularPolygonPoints(x+center[0], y+center[1], ep.BOUNDS[1]/20, 3)

def squaretri(x, y):
    sqpts = poly(x, y, 4, math.pi/4, scale)
    return slideShape(sqpts, 5, tri)

pts = poly(0, 0, 5, math.pi/5, scale*3)
newPts = slideShape(pts, 5, squaretri)


def normalize(x, y):
    mag = (x ** 2 + y **2) ** 0.5
    return [x/mag, y/mag]

def mag(x, y):
    return (x ** 2 + y **2) ** 0.5

def clamp(n, small, big):
    return max(min(n, big), small)

'''
p0 = normalized(<x >y)
q = normalized(whatever)
prev = <0, 1> if len(hull) == 2 else hull[-2]
find point where q • hull[-1] >

'''

# newPts = [ (1, 1), (1, 1), (1, 1), (5, 4), (0, 4), (8,2), (1, 0), (1, 1), (2, 5), (3, 3), (5, 3), (3, 2), (2, 2), (4, 4), (6, 6), (1, 6), (6, 1), (4, 1), (0, 3), (3, 0), (5, 5), (2, 3) ]


newPts.sort(key = lambda p: p[1])
newPts.sort(key = lambda p: p[0])
leftPoint = newPts[0]

hull = []

while len(hull) == 0 or hull[-1] != leftPoint:
    if len(hull) == 0:
        hull.append(leftPoint)
    bestPoint = None
    bestAngle = -1
    prevPoint = hull[-2] if len(hull) >= 2 else [hull[-1][0], hull[-1][1] +1]
    for p in newPts:
        if (hull[-1][0] == p[0] and hull[-1][1] == p[1]) or (len(hull) > 1 and hull[-2][0] == p[0] and hull[-2][1] == p[1]):
            continue
        vecA = [hull[-1][0]-prevPoint[0], hull[-1][1]-prevPoint[1]] #hull[-1] -> prevPoint
        vecB = [hull[-1][0]-p[0],hull[-1][1]-p[1]] #hull[-1] -> p
        dot = (vecA[0]*vecB[0]+vecA[1]*vecB[1])
        magprod = mag(vecA[0], vecA[1])*mag(vecB[0], vecB[1])
        ans = clamp(dot/magprod, -1, 1)
        angle = math.acos(ans)
        if angle > bestAngle:
            bestAngle = angle
            bestPoint = p
    hull.append(bestPoint)


print(hull)
ep.setSpeed(5)
ep.polyline(hull)

ep.end()