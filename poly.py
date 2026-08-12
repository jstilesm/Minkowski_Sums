import math

def poly(x, y, sides, rotation, radius):
    pts = [(x + (math.cos(rotation)) * radius, y + (math.sin(rotation)) * radius)]
    for i in range(sides):
        theta = (((i + 1) * ((2 * math.pi) / sides) + rotation) / (2*math.pi))
        pts.append((x + math.cos(theta * 2 * math.pi) * radius, y + math.sin(theta * 2 * math.pi) * radius))
    return pts