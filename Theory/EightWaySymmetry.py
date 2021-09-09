# method to find zone
def findZone(sx, sy, ex, ey):
    dx = ex - sx
    dy = ey - sy

    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 'zone 0'
        elif dx < 0 and dy > 0:
            return'zone 3'
        elif dx < 0 and dy < 0:
            return'zone 4'
        elif dx > 0 and dy < 0:
            return'zone 7'
    else:
        if dx >= 0 and dy >= 0:
            return'zone 1'
        elif dx < 0 and dy > 0:
            return'zone 2'
        elif dx < 0 and dy < 0:
            return'zone 5'
        elif dx > 0 and dy < 0:
            return'zone 6'


# method to map any point to zone 0
def convertToZone0(x, y, sourceZone):
    if sourceZone == 'zone 1':
        rx = y
        ry = x
        return (rx, ry)
    elif sourceZone == 'zone 2':
        rx = y
        ry = (-1) * x
        return (rx, ry)
    elif sourceZone == 'zone 3':
        rx = (-1)*x
        ry = y
        return (rx, ry)
    elif sourceZone == 'zone 4':
        rx = (-1)*x
        ry = (-1)*y
        return (rx, ry)
    elif sourceZone == 'zone 5':
        rx = (-1)*y
        ry = (-1)*x
        return (rx, ry)
    elif sourceZone == 'zone 6':
        rx = (-1)*y
        ry = x
        return (rx, ry)
    elif sourceZone == 'zone 7':
        rx = x
        ry = (-1)*y
        return (rx, ry)


# method to map zone 0 point to any other zone
def convertToOriginal(x, y, destinationZone):
    if destinationZone == 'zone 1':
        rx = y
        ry = x
        return (rx, ry)
    elif destinationZone == 'zone 2':
        rx = (-1) * y
        ry = x
        return (rx, ry)
    elif destinationZone == 'zone 3':
        rx = (-1)*x
        ry = y
        return (rx, ry)
    elif destinationZone == 'zone 4':
        rx = (-1)*x
        ry = (-1)*y
        return (rx, ry)
    elif destinationZone == 'zone 5':
        rx = (-1)*y
        ry = (-1)*x
        return (rx, ry)
    elif destinationZone == 'zone 6':
        rx = y
        ry = (-1)*x
        return (rx, ry)
    elif destinationZone == 'zone 7':
        rx = x
        ry = (-1)*y
        return (rx, ry)


# midpoint algo
def midpoint(sx, sy, ex, ey):
    dy = ey-sy
    dx = ex-sx

    d_init = (2*dy) - dx
    d = d_init

    points = []
    while(sx != ex and sy != ey):
        # print('(' + str(sx) + ', ' + str(sy) + ')')
        points.append((sx, sy))
        if d > 0:
            sx += 1
            sy += 1
            d += 2*(dy - dx)
        else:
            sx += 1
            d += 2*dy
    points.append((ex, ey))
    return points


if __name__ == "__main__":
    sx, sy = map(int, input("Starting Point: ").split())
    ex, ey = map(int, input("Ending Point: ").split())

    zone = findZone(sx, sy, ex, ey)

    if zone == 'zone 0':
        points = midpoint(sx, sy, ex, ey)
        for (x, y) in points:
            print((x, y))
    else:
        startingPointsConverted = convertToZone0(sx, sy, zone)
        endingPointConverted = convertToZone0(ex, ey, zone)
        points = midpoint(
            startingPointsConverted[0], startingPointsConverted[1], endingPointConverted[0], endingPointConverted[1])
        for (x, y) in points:
            original = convertToOriginal(x, y, zone)
            print(original)

        # print(zone)
    
    print(findZone(32, 16, 64, 32))