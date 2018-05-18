from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# TODO: ctrl
# TODO: tools
# TODO: save
# TODO: resizable

width = 500
height = 650

dots = [[]]
delDots = []

inTools = False

colSel = 0

red = 0.0
green = 0.0
blue = 0.0
alpha = 1.0

lastRed = 0.0
lastGreen = 0.0
lastBlue = 0.0
lastAlpha = 1.0

def init():
    glutInit()
    glutInitWindowSize(width, height)
    glutInitWindowPosition(700, 25)
    glutCreateWindow("Paint")
    glutDisplayFunc(render)
    glutMouseFunc(mouseClicked)
    glutMotionFunc(mouseHeld)
    glutKeyboardFunc(keyClicked)

    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(2.0)
    glLineWidth(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, height, 0.0)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def render():
    for i in range(1, len(dots)):
        if dots[i] == [] and dots[i-1] == []:
            del dots[i]
    glClear(GL_COLOR_BUFFER_BIT)

    #COLOR
    glColor4f(red, green, blue, alpha)
    glRecti(150, 600, 200, 650)

    glColor4f(0.0, 0.0, 0.0, 1.0)
    glBegin(GL_LINES)

    #LINE
    glVertex2i(0, 500)
    glVertex2i(500, 500)

    #COLUMN SEPARATORS
    for i in range(150, 500, 50):
        glVertex2i(i, 500)
        glVertex2i(i, 600)

    #SECOND ROW LINE
    glVertex2i(150, 550)
    glVertex2i(500, 550)

    #THIRD ROW LINE
    glVertex2i(150, 600)
    glVertex2i(500, 600)

    #UNDO BUTTON
    glVertex2i(160, 525)
    glVertex2i(190, 525)
    glVertex2i(160, 525)
    glVertex2i(175, 540)
    glVertex2i(160, 525)
    glVertex2i(175, 510)

    #REDO BUTTON
    glVertex2i(210, 525)
    glVertex2i(240, 525)
    glVertex2i(240, 525)
    glVertex2i(225, 540)
    glVertex2i(240, 525)
    glVertex2i(225, 510)

    #GARBAGE
    glVertex2i(457, 515)
    glVertex2i(493, 515)
    glVertex2i(460, 545)
    glVertex2i(490, 545)
    glVertex2i(460, 515)
    glVertex2i(460, 545)
    glVertex2i(490, 515)
    glVertex2i(490, 545)
    glVertex2i(470, 520)
    glVertex2i(470, 540)
    glVertex2i(480, 520)
    glVertex2i(480, 540)
    glVertex2i(465, 515)
    glVertex2i(470, 508)
    glVertex2i(485, 515)
    glVertex2i(480, 508)
    glVertex2i(470, 508)
    glVertex2i(480, 508)

    #PENCIL
    glVertex2i(195, 555)
    glVertex2i(182, 558)
    glVertex2i(182, 558)
    glVertex2i(155, 585)
    glVertex2i(155, 585)
    glVertex2i(165, 595)
    glVertex2i(165, 595)
    glVertex2i(192, 568)
    glVertex2i(192, 568)
    glVertex2i(195, 555)
    #tipline
    glVertex2i(182, 558)
    glVertex2i(192, 568)
    #eraserline
    glVertex2i(161, 579)
    glVertex2i(171, 589)

    #ERASER
    glVertex2i(225, 555)
    glVertex2i(245, 565)
    glVertex2i(245, 565)
    glVertex2i(225, 595)
    glVertex2i(225, 595)
    glVertex2i(205, 585)
    glVertex2i(205, 585)
    glVertex2i(225, 555)
    #lineinside
    glVertex2i(217, 565)
    glVertex2i(238, 576)

    #LINETOOL
    glVertex2i(290, 560)
    glVertex2i(260, 590)

    #CIRCLETOOL
    glEnd()
    glBegin(GL_POLYGON)
    for i in range(45):
        glVertex2i(math.cos(i), math.sin(i))
    glEnd()
    glBegin(GL_LINES)

    #TRIANGLETOOL
    glVertex2i(375, 560)
    glVertex2i(390, 590)
    glVertex2i(390, 590)
    glVertex2i(360, 590)
    glVertex2i(360, 590)
    glVertex2i(375, 560)

    #SQUARETOOL
    glVertex2i(410, 560)
    glVertex2i(440, 560)
    glVertex2i(440, 560)
    glVertex2i(440, 590)
    glVertex2i(440, 590)
    glVertex2i(410, 590)
    glVertex2i(410, 590)
    glVertex2i(410, 560)

    #LINEWIDTH
    glVertex2i(260, 625)
    glVertex2i(340, 625)
    glEnd()
    glBegin(GL_POINTS)
    glVertex2i(375, 625)
    glEnd()
    glBegin(GL_LINES)

    #COLSQUARE
    glEnd()
    glBegin(GL_QUADS)
    glColor4f(red, green, blue, 0.0)
    glVertex2i(0, 500)
    glColor3i(0,0,0)
    glVertex2i(0, 625)
    glVertex2i(150, 625)
    glColor4f(red, green, blue, 1.0)
    glVertex2i(150, 500)

    #COLLINE
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,0.0)
    glVertex2i(0, 629)
    glVertex2i(0, 646)
    glColor3f(1.0,1.0,0.0)
    glVertex2i(15, 646)
    glVertex2i(15, 629)
    glColor3f(1.0,1.0,0.0)
    glVertex2i(15, 646)
    glVertex2i(15, 629)
    glColor3f(0.0,1.0,0.0)
    glVertex2i(50, 629)
    glVertex2i(50, 646)
    glColor3f(0.0,1.0,0.0)
    glVertex2i(50, 629)
    glVertex2i(50, 646)
    glColor3f(0.0,1.0,1.0)
    glVertex2i(75, 646)
    glVertex2i(75, 629)
    glColor3f(0.0,1.0,1.0)
    glVertex2i(75, 646)
    glVertex2i(75, 629)
    glColor3f(0.0,0.0,1.0)
    glVertex2i(100, 629)
    glVertex2i(100, 646)
    glColor3f(0.0,0.0,1.0)
    glVertex2i(100, 629)
    glVertex2i(100, 646)
    glColor3f(1.0,0.0,1.0)
    glVertex2i(125, 646)
    glVertex2i(125, 629)
    glColor3f(1.0,0.0,1.0)
    glVertex2i(125, 646)
    glVertex2i(125, 629)
    glColor3f(1.0,0.0,0.0)
    glVertex2i(150, 629)
    glVertex2i(150, 646)
    glEnd()

    #COLLINE SELECTOR
    glBegin(GL_QUADS)
    glColor4f(red, green, blue, 1.0)
    glVertex2i(colSel-5, 625)
    glVertex2i(colSel-5, 650)
    glVertex2i(colSel+5, 650)
    glVertex2i(colSel+5, 625)
    glEnd()
    glBegin(GL_LINES)
    glColor3i(0,0,0)
    glVertex2i(colSel-5, 625)
    glVertex2i(colSel-5, 650)
    glVertex2i(colSel+5, 650)
    glVertex2i(colSel+5, 625)
    glEnd()

    #glColor3f(0.0, 0.0, 0.0)
    for i in range(len(dots)):
        if len(dots[i]) > 1:
            glBegin(GL_LINE_STRIP)
            for j in range(len(dots[i])-1):
                glColor4f(dots[i][j][2], dots[i][j][3], dots[i][j][4], dots[i][j][5])
                glVertex2i(dots[i][j][0], dots[i][j][1])
            glEnd()
        else:
            if dots[i] != []:
                glBegin(GL_POINTS)
                glColor4f(dots[i][0][2], dots[i][0][3], dots[i][0][4], dots[i][0][5])
                glVertex2i(dots[i][0][0], dots[i][0][1])
                glEnd()

    glFlush()

def mouseClicked(button, state, x, y):
    global dots
    global delDots
    global inTools
    global alpha
    if state == GLUT_UP:
        dots.append([])
        inTools = False
    elif y < 500:
        dots[-1].append([x,y,red,green,blue,alpha])
        delDots = []
    else:
        if state == GLUT_DOWN:
            inTools = True
        if x < 150:
            if y >= 625:
                setPickerColor(x)
            else:
                setPickerShade(x,y)
        elif y < 550:
            if x < 200:
                undo()
            elif x < 250:
                redo()
            elif x < 300:
                print('buttonclicked')
            elif x < 350:
                print('buttonclicked')
            elif x < 400:
                print('buttonclicked')
            elif x < 450:
                print('buttonclicked')
            elif x < 500:
                clear()
        elif y < 600:
            if x < 200:
                if red == 1.0 and green == 1.0 and blue == 1.0:
                    setColorA(lastRed, lastGreen, lastBlue, lastAlpha)
            elif x < 250:
                setColorA(1.0, 1.0, 1.0, 1.0)

    glutPostRedisplay()


def mouseHeld(x, y):
    global inTools
    global alpha
    if y < 500:
        if not inTools:
            dots[-1].append([x,y,red,green,blue,alpha])
            delDots = []
    elif inTools:
        if x < 150:
            if y >= 625:
                setPickerColor(x)
            else:
                setPickerShade(x,y)

    glutPostRedisplay()

def keyClicked(key, x, y):
    if key.decode('utf8') == 'Z':
        undo()
    if key.decode('utf8') == 'Y':
        redo()

def clear():
    global dots
    dots = [[]]
    glutPostRedisplay()

def undo():
    if len(dots) > 1:
        delDots.append(dots[-2])
        del dots[-2]
        glutPostRedisplay()

def redo():
    if len(delDots) > 0:
        dots.insert(-1, delDots[-1])
        del delDots[-1]
        glutPostRedisplay()

def setColor(r, g, b):
    global red
    global green
    global blue
    red = r
    green = g
    blue = b

def setColorA(r,g,b,a):
    global alpha
    setColor(r,g,b)
    alpha = a

def setPickerColor(x):
    global colSel
    if x <= 15:
        setColor(1.0, x/15, 0.0)
    elif x <= 45:
        setColor(1.0-(x-15)/30, 1.0, 0.0)
    elif x <= 75:
        setColor(0.0, 1.0, (x-45)/30)
    elif x <= 105:
        setColor(0.0, 1.0-(x-75)/30, 1.0)
    elif x <= 135:
        setColor((x-105)/30, 0.0, 1.0)
    elif x <= 150:
        setColor(1.0, 0.0, 1.0-(x-135)/15)
    colSel = x
def setPickerShade(x, y):
    global alpha
    #setColorA(red*(y-500)/125, green*(y-500)/125, blue*(y-500)/125, x/150)
    alpha = x/150

init()
glutMainLoop()
