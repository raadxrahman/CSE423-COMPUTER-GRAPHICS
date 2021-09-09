# Id - 19101069, odd

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def main():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# def midPointLineAlgo(x0, y0, x1, y1):
#     glBegin(GL_POINTS)
#     dy = y1 - y0
#     dx = x1 - x0

#     d_init = (2 * dy) - dx
#     d = d_init

#     if x0 == x1:
#         while(y0 != y1):
#             glVertex2f(x0, y0)
#             y0 += 1
#         glVertex2f(x0, y0)
#     elif y0 == y1:
#         while(x0 != x1):
#             glVertex2f(x0, y0)
#             x0 += 1
#         glVertex2f(x0, y0)
#     else:
#         while(x0 != x1 and y0 != y1):
#             glVertex2f(x0, y0)
#             if d > 0:
#                 x0 += 1
#                 y0 += 1
#                 d += 2*(dy - dx)
#             else:
#                 x0 += 1
#                 d *= 2
#         glVertex2f(x0, y0)   
#     glEnd()


def midpoint(r, a, b):
    d_init = 1 - r
    d = d_init
    x = 0
    y = r

    points = []
    while(x < y):
        points.append((x, y))
        if d >= 0:
            d += (2*x) - (2*y) + 5
            x = x + 1
            y = y - 1
        else:
            d += (2*x) + 3
            x = x + 1
    return points


def zone0converter(x, y, zoneGiven):
    if zoneGiven == 'zone 1':
        rx = y
        ry = x
        return (rx, ry)
    elif zoneGiven == 'zone 2':
        rx = y
        ry = (-1) * x
        return (rx, ry)
    elif zoneGiven == 'zone 3':
        rx = (-1)*x
        ry = y
        return (rx, ry)
    elif zoneGiven == 'zone 4':
        rx = (-1)*x
        ry = (-1)*y
        return (rx, ry)
    elif zoneGiven == 'zone 5':
        rx = (-1)*y
        ry = (-1)*x
        return (rx, ry)
    elif zoneGiven == 'zone 6':
        rx = (-1)*y
        ry = x
        return (rx, ry)
    elif zoneGiven == 'zone 7':
        rx = x
        ry = (-1)*y
        return (rx, ry)


def originalConverter(x, y, zoneDestination):
    if zoneDestination == 'zone 1':
        rx = y
        ry = x
        return (rx, ry)
    elif zoneDestination == 'zone 2':
        rx = (-1) * y
        ry = x
        return (rx, ry)
    elif zoneDestination == 'zone 3':
        rx = (-1)*x
        ry = y
        return (rx, ry)
    elif zoneDestination == 'zone 4':
        rx = (-1)*x
        ry = (-1)*y
        return (rx, ry)
    elif zoneDestination == 'zone 5':
        rx = (-1)*y
        ry = (-1)*x
        return (rx, ry)
    elif zoneDestination == 'zone 6':
        rx = y
        ry = (-1)*x
        return (rx, ry)
    elif zoneDestination == 'zone 7':
        rx = x
        ry = (-1)*y
        return (rx, ry)


def findZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
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


def drawCircle(r, x, y):
    glBegin(GL_POINTS)
    z1 = midpoint(r, x, y)
    z0 = []
    z2 = []
    z3 = []
    z4 = []
    z5 = []
    z6 = []
    z7 = []

    for (a, b) in z1:
        z0.append(zone0converter(a, b, 'zone 1'))

    for (a, b) in z0:
        z2.append(originalConverter(a, b, 'zone 2'))
        z3.append(originalConverter(a, b, 'zone 3'))
        z4.append(originalConverter(a, b, 'zone 4'))
        z5.append(originalConverter(a, b, 'zone 5'))
        z6.append(originalConverter(a, b, 'zone 6'))
        z7.append(originalConverter(a, b, 'zone 7'))

    for (a, b) in z0:
        glVertex2f(a+x, b+y)

    for (a, b) in z1:
        glVertex2f(a+x, b+y)

    for (a, b) in z2:
        glVertex2f(a+x, b+y)

    for (a, b) in z3:
        glVertex2f(a+x, b+y)

    for (a, b) in z4:
        glVertex2f(a+x, b+y)

    for (a, b) in z5:
        glVertex2f(a+x, b+y)
        
    for (a, b) in z6:
        glVertex2f(a+x, b+y)

    for (a, b) in z7:
        glVertex2f(a+x, b+y)

    glEnd()


def window():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    main()
    glColor3f(0, 1, 0.5)
    glPointSize(3)

    # bunyy
    # head

    glColor3f(255, 255, 255)
    drawCircle(150, 250, 200)       # outer border
    drawCircle(50, 250, 130)        # nose
    drawCircle(70, 150, 330)        # ear - 1
    drawCircle(70, 340, 330)        # ear - 2

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task - 01")
glutDisplayFunc(window)
glutIdleFunc(window)
glutMainLoop()