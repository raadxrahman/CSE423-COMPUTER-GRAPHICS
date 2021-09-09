from OpenGL.GL import *
from OpenGL.GLUT import *


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def drawTriangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(100, 300)
    glVertex2f(250, 400)
    glVertex2f(400, 300)
    glEnd()

def drawLine(x0, y0, x1, y1):
    glBegin(GL_LINES)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 0, 1)
    glPointSize(5)
    drawTriangle()

    drawLine(160, 300, 160, 100) #house
    # drawLine(340, 300, 340, 100)
    drawLine(340, 100, 340, 380) #extendedLine
    drawLine(160, 100, 340, 100)

    drawLine(340, 380, 310, 380) #chimney
    drawLine(310, 380, 310, 350)

    drawLine(180, 270, 180, 230) #windowBorder
    drawLine(180, 270, 220, 270)
    drawLine(180, 230, 220, 230)
    drawLine(220, 270, 220, 230)

    drawLine(180, 250, 220, 250) #windowGrill
    drawLine(200, 230, 200, 270)

    drawLine(320, 270, 320, 230) #windowBorder
    drawLine(280, 270, 320, 270)
    drawLine(280, 230, 320, 230)
    drawLine(280, 270, 280, 230)

    drawLine(280, 250, 320, 250) #windowGrill
    drawLine(300, 230, 300, 270)


    drawLine(220, 100, 220, 200) #door
    drawLine(280, 100, 280, 200) 
    drawLine(250, 100, 250, 200) #doorMiddle
    drawLine(220, 200, 280, 200)

    glBegin(GL_POINTS) #doorLock
    glVertex2f(260, 150)
    glVertex2f(240, 150)
    glEnd()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 02 - House Building")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()