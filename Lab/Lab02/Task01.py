# id - 19101069 , last two digits - 69
 
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
    glBegin(GL_POINTS)
    dy = y1 - y0
    dx = x1 - x0

    d_init = (2 * dy) - dx
    d = d_init

    if x0 == x1:
        while(y0 != y1):
            glVertex2f(x0, y0)
            y0 += 1
        glVertex2f(x0, y0)
    elif y0 == y1:
        while(x0 != x1):
            glVertex2f(x0, y0)
            x0 += 1
        glVertex2f(x0, y0)
    else:
        while(x0 != x1 and y0 != y1):
            glVertex2f(x0, y0)
            if d > 0:
                x0 += 1
                y0 += 1
                d += 2*(dy - dx)
            else:
                x0 += 1
                d *= 2
        glVertex2f(x0, y0)
        
    glEnd()


# def slope(x0,y0,x1,y1):
#     slope_m = (y1-y0)/(x1-x0)
#     print("Slope = " + str(slope_m))
#     if 0 < slope_m < 1:
#         midPointLineAlgo(x0,y0,x1,y1)
#     else:
#         print("Slope not within 0 and 1")


def window():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    main()
    glColor3f(0, 1, 0.5)
    glPointSize(2)

    # 6 --
    midPointLineAlgo(300, 450, 375, 450) # _ 1
    midPointLineAlgo(300, 250, 300, 450) # |
    midPointLineAlgo(300, 250, 375, 250) # _ 3
    midPointLineAlgo(375, 250, 375, 325) # '
    midPointLineAlgo(300, 325, 375, 325) # _ 2 

    # 9 --
    midPointLineAlgo(500, 250, 500, 450) # |
    midPointLineAlgo(425, 450, 500, 450) # _ 1
    midPointLineAlgo(425, 375, 425, 450) # '
    midPointLineAlgo(425, 375, 500, 375) # _ 2
    midPointLineAlgo(425, 250, 500, 250) # _ 3
    
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1400, 900)
glutInitWindowPosition(50, 50)
wind = glutCreateWindow(b"Task - 01")
glutDisplayFunc(window)
glutIdleFunc(window)
glutMainLoop()