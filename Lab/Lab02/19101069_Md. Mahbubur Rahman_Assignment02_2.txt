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

def midPointLineAlgo(x0, y0, x1, y1):
    dy = y1-y0
    dx = x1-x0
    d_init = (2*dy) - dx
    d = d_init
    points = []
    if x0 == x1:
        while(y0 != y1):
            points.append((x0, y0))
            y0 += 1
    elif y0 == y1:
        while(x0 != x1):
            points.append((x0, y0))
            x0 += 1
    else:
        while(x0 != x1 and y0 != y1):
            points.append((x0, y0))
            if d > 0:
                x0 += 1
                y0 += 1
                d += 2*(dy - dx)
            else:
                x0 += 1
                d += 2*dy
    points.append((x1, y1))
    return points

def zone0Converter(x, y, zoneGiven):
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


def lines(x0, y0, x1, y1):
    glBegin(GL_POINTS)
    zone = findZone(x0, y0, x1, y1)
    if zone == 'zone 0':
        points = midPointLineAlgo(x0, y0, x1, y1)
        for point in points:
            glVertex2f(point[0], point[1])
    else:
        spConvert = zone0Converter(x0, y0, zone)
        epConvert = zone0Converter(x1, y1, zone)
        points = midPointLineAlgo(
            spConvert[0], spConvert[1], epConvert[0], epConvert[1])
        for (x, y) in points:
            original = originalConverter(x, y, zone)
            glVertex2f(original[0], original[1])
    glEnd()


def window():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    main()
    glColor3f(0, 1, 0.5)
    glPointSize(2)

    # boat
     
    lines(100, 100, 400, 100) # base - line - 1 (below)
    lines(50, 200, 450, 200) # base - line - 2 (above)
    lines(100, 100, 50, 200) # line 1 + line 2 left
    lines(400, 100, 450, 200) # line 1 + line 2 right
    lines(250, 200, 250, 400) # sail - cone - midline
    lines(250, 400, 350, 200) # sail - cone - right
    lines(250, 300, 150, 200) # sail - cone - left

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task - 02")
glutDisplayFunc(window)
glutIdleFunc(window)
glutMainLoop()