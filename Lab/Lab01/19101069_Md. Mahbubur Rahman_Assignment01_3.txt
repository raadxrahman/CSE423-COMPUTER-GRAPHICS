from OpenGL.GL import *
from OpenGL.GLUT import *

# Id - 19101069, so I will draw H

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def slope(x0, y0, x1, y1):
    return int((y1-y0)/(x1-x0))


def dda_dashed(x0, y0, x1, y1):
    glBegin(GL_POINTS)
    if x0 != x1:
        m = slope(x0, y0, x1, y1)  
    else:
        m = 2e18  

    if m < 1 and m > -1:  
        while(x0 != x1):
            if x0 % 10 == 0:
                glVertex2f(x0, round(y0))
            x0 = x0 + 1
            y0 = y0 + m
    else:
        while(y0 != y1):
            if y0 % 10 == 0:
                glVertex2f(round(x0), y0)
            y0 = y0 + 1
            x0 = x0 + (1/m)
    glVertex2f(x1, y1)
    glEnd()


def dda(x0, y0, x1, y1):
    glBegin(GL_POINTS)
    if x0 != x1:
        m = slope(x0, y0, x1, y1) 
    else:
        m = 2e18  

    if m < 1 and m > -1:  
        while(x0 != x1):
            glVertex2f(x0, round(y0))
            x0 = x0 + 1
            y0 = y0 + m
    else:
        while(y0 != y1):
            glVertex2f(round(x0), y0)
            y0 = y0 + 1
            x0 = x0 + (1/m)
    glVertex2f(x1, y1)
    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 0, 1)
    glPointSize(5)
    dda(300, 300, 300, 700)
    dda(500, 300, 500, 700)
    dda_dashed(300,400,500,400)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 750)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 03 - Coin Toss using Digital Differential Analyzer (DDA) Line Drawing Algorithm")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()