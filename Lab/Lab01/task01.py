from OpenGL.GL import *
from OpenGL.GLUT import *
import random

def drawPoints():
    glBegin(GL_POINTS)
    for i in range(0, 50):
        glVertex2f(xlist[i], ylist[i])
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 0, 1)
    glPointSize(15)
    # call the draw methods here
    drawPoints()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
xlist = []
ylist = []
for i in range(0, 50):
    xlist.append(random.randint(0, 500))
    ylist.append(random.randint(0, 500))

wind = glutCreateWindow(b"Task 01 - Drawing Pixels")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()