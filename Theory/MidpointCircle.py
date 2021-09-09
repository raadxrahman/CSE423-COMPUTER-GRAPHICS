def midpoint(r):
    d_init = 1 - r
    d = d_init
    x = 0
    y = r

    points = []
    while(x <= y):
        points.append((x, y))
        if d >= 0:
            x = x + 1
            y = y - 1
            d += (2*x) - (2*y) + 5
        else:
            x = x + 1
            d += (2*x) + 3
    points.append((x, y))
    return points


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


if __name__ == '__main__':
    r = int(input())
    zone_1_points = midpoint(r)
    zone_0_points = []
    zone_2_points = []
    zone_3_points = []
    zone_4_points = []
    zone_5_points = []
    zone_6_points = []
    zone_7_points = []
    for (x, y) in zone_1_points:
        zone_0_points.append(convertToZone0(x, y, 'zone 1'))

    for (x, y) in zone_0_points:
        zone_2_points.append(convertToOriginal(x, y, 'zone 2'))
        zone_3_points.append(convertToOriginal(x, y, 'zone 3'))
        zone_4_points.append(convertToOriginal(x, y, 'zone 4'))
        zone_5_points.append(convertToOriginal(x, y, 'zone 5'))
        zone_6_points.append(convertToOriginal(x, y, 'zone 6'))
        zone_7_points.append(convertToOriginal(x, y, 'zone 7'))

    print('Zone - 0 :', zone_0_points)
    print('Zone - 1 :', zone_1_points)
    print('Zone - 2 :', zone_2_points)
    print('Zone - 3 :', zone_3_points)
    print('Zone - 4 :', zone_4_points)
    print('Zone - 5 :', zone_5_points)
    print('Zone - 6 :', zone_6_points)
    print('Zone - 7 :', zone_7_points)

    # for (x, y) in zone_0_points:
    #     print((x, y))
    # for (x, y) in zone_1_points:
    #     print((x, y))
    # for (x, y) in zone_2_points:
    #     print((x, y))
    # for (x, y) in zone_3_points:
    #     print((x, y))
    # for (x, y) in zone_4_points:
    #     print((x, y))
    # for (x, y) in zone_5_points:
    #     print((x, y))
    # for (x, y) in zone_6_points:
    #     print((x, y))
    # for (x, y) in zone_7_points:
    #     print((x, y))