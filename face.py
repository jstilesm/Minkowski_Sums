import easyplot.easyplot as ep
import math

ep.init()
ep.switchPen(7)

## Lesson, use variables

## Constants
center = (ep.BOUNDS[0]/2, ep.BOUNDS[1]/2)
steps = 4
scale = ep.BOUNDS[1]/10
radius = ep.BOUNDS[1]/ 4

## arc Constants
arcOneX = center[0] - radius*1/2
arcY = center[1] + radius*1/4
arcTwoX = center[0] + radius*1/2
arcRadius = radius/4

ep.circle(center[0], center[1], radius)
## center of eye - 1/2 the arc width

ep.arc(center[0] - radius/2, arcY, arcRadius,  math.pi)
ep.arc(center[0] + radius/2, arcY, arcRadius,  math.pi)

ep.line(arcTwoX - arcRadius, 
        center[1] + radius/16, 
        arcTwoX - arcRadius, 
        arcY)

ep.line(arcTwoX + arcRadius, 
        center[1] + radius/16, 
        arcTwoX + arcRadius, 
        arcY)

ep.line(arcOneX - arcRadius, 
        center[1] + radius/16, 
        arcOneX - arcRadius, 
        arcY)

ep.line(arcOneX + arcRadius, 
        center[1] + radius/16, 
        arcOneX + arcRadius, 
        arcY)

ep.arc(center[0], center[1] - radius/4, -radius/2,  math.pi)
ep.end()
