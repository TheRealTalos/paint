from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# TODO: UNDO
# TODO: linesize linetool

width = 500
height = 650

dots = [[]]
delDots = []

lastLine = False

inColor = False
inShade = False

lineSize = 10
circleSize = 50

shdSelX = 0
shdSelY = 625
colSel = 0
lineSel = lineSize * 2
circleSel = circleSize

lineClick = 0

red = 0.0
green = 0.0
blue = 0.0

fullRed = 1.0
fullGreen = 0.0
fullBlue = 0.0

lastRed = 0.0
lastGreen = 0.0
lastBlue = 0.0

TPENCIL = 1
TERASER = 2
TLINE = 3
TCIRCLE = 4
TTRIANGLE = 5
TSQUARE = 6

tool = TPENCIL

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
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, height, 0.0)
    glEnable(GL_BLEND)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_POINT_SMOOTH)

def render():
    global shdSelX
    global shdSelY
    global colSel
    global tool
    global lineSize
    global circleSel
    global circleSize
    global lineClick

    for i in range(1, len(dots)):
        if dots[i] == [] and dots[i-1] == []:
            del dots[i]
    glClear(GL_COLOR_BUFFER_BIT)

    lineSize = int(lineSel/10) + 1
    circleSize = circleSel * 2 + 6
    glPointSize(1)
    glLineWidth(lineSize)

    for i in range(len(dots)):
        if len(dots[i]) > 1:
            glLineWidth(dots[i][0][5])
            glBegin(GL_LINE_STRIP)
            for j in range(len(dots[i])):
                glColor3f(dots[i][0][2], dots[i][0][3], dots[i][0][4])
                glVertex2i(dots[i][j][0], dots[i][j][1])
            glEnd()
        else:
            if dots[i] != []:
                glBegin(GL_POLYGON)
                glColor3f(dots[i][0][2], dots[i][0][3], dots[i][0][4])
                glCircle(dots[i][0][0], dots[i][0][1], int(dots[i][0][5]/2))
                glEnd()

    glColor3f(1.0,1.0,1.0)
    glRecti(0,500,500,650)

    glColor3f(0.0, 0.0, 0.0)
    glCircle(100, 100, 100)

    glPointSize(2.0)
    glLineWidth(2.0)
    #COLOR
    glColor3f(red, green, blue)
    glRecti(150, 600, 200, 650)

    glColor3i(0,0,0)
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
    if tool == 1:
        glColor3f(1.0,0.267,0.875)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2i(161, 579)
        glVertex2i(155, 585)
        glVertex2i(165, 595)
        glVertex2i(171, 589)
        glColor3f(0.937,0.925,0.196)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2i(182, 558)
        glVertex2i(161, 579)
        glVertex2i(171, 589)
        glVertex2i(192, 568)
        glEnd()
        glColor3f(0.93,0.92,0.55)
        glBegin(GL_POLYGON)
        glVertex2i(195, 555)
        glVertex2i(182, 558)
        glVertex2i(192, 568)
        glEnd()
        glColor3i(0,0,0)
        glBegin(GL_POLYGON)
        glVertex2i(195, 555)
        glVertex2i(189, 557)
        glVertex2i(195, 562)
        glEnd()
        glBegin(GL_LINES)

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
    if tool == 2:
        glColor3f(1.0,0.267,0.875)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2i(225, 555)
        glVertex2i(217, 565)
        glVertex2i(238, 576)
        glVertex2i(245, 565)
        glEnd()
        glBegin(GL_LINES)
        glColor3i(0,0,0)

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
    if tool == 3:
        glColor3f(fullRed, fullGreen, fullBlue)
    glVertex2i(290, 560)
    glVertex2i(260, 590)
    glColor3i(0,0,0)

    #CIRCLETOOL
    if tool == 4:
        glColor3f(fullRed, fullGreen, fullBlue)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glCircle(325, 575, 17)
    glEnd()
    glBegin(GL_LINES)
    glColor3i(0,0,0)

    #SHADESQUARE
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(0, 500)
    glColor3i(0,0,0)
    glVertex2i(0, 625)
    glVertex2i(150, 625)
    glColor3f(fullRed, fullGreen, fullBlue)
    glVertex2i(150, 500)

    #SHADECIRCLE
    glEnd()
    if shdSelX < 0:
        shdSelX = 0
    if shdSelY > 625:
        shdSelY = 625
    glBegin(GL_POLYGON)
    glColor3f(red,green,blue)
    glCircle(shdSelX, shdSelY, 10)
    glEnd()
    glColor3i(0,0,0)
    glBegin(GL_LINE_STRIP)
    glCircle(shdSelX, shdSelY, 10)

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
    glColor3f(fullRed, fullGreen, fullBlue)
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

    if tool != 4:
        #LINEWIDTH
        glVertex2i(260, 625)
        glVertex2i(340, 625)
        #LINESEL
        glVertex2i(265+lineSel, 610)
        glVertex2i(265+lineSel, 640)
    else:
        glVertex2i(260, 625)
        glVertex2i(340, 625)
        #LINESEL
        glVertex2i(265+circleSel, 610)
        glVertex2i(265+circleSel, 640)
    glEnd()
    glBegin(GL_POLYGON)
    if tool == 4:
        glCircle(375, 625, int(circleSize/2))
    else:
        glCircle(375, 625, int(lineSize/2))
    glEnd()

    glFlush()

def mouseClicked(button, state, x, y):
    global dots
    global delDots
    global inColor
    global inShade
    global tool
    global shdSelX
    global shdSelY
    global circleSize
    global lineClick

    if state == GLUT_UP:
        if tool != 3:
            dots.append([])
        if y < 500:
            if tool == 1 or tool == 2:
                try:
                    dots[-1].append([dots[-2][len(dots[-2])-1][0],dots[-2][len(dots[-2])-1][1],red,green,blue,lineSize])
                except:
                    a = 5
                dots.append([])
        inShade = False
        inColor = False
    elif y < 500:
        if tool == 1 or tool == 2:
            dots[-1].append([x,y,red,green,blue,lineSize])
            dots.append([])
            dots[-1].append([x,y,red,green,blue,lineSize])
            delDots = []
        elif tool == 3:
            lineClick+=1
            dots[-1].append([x,y,red,green,blue,lineSize])
            dots.append([])
            dots[-1].append([x,y,red,green,blue,lineSize])
            if lineClick == 2:
                dots.append([])
                lineClick = 0
        elif tool == 4:
            dots[-1].append([x,y,red,green,blue,circleSize])
    else:
        if state == GLUT_DOWN:
            if y > 625:
                inShade = True
            else:
                inColor = True
        if x < 150:
            if tool != 2:
                if y >= 625:
                    setPickerColor(x)
                    setPickerShade(shdSelX, shdSelY)
                else:
                    setPickerShade(x,y)
        elif y < 550:
            if x < 200:
                undo()
            elif x < 250:
                redo()
            elif x < 500 and x > 450:
                clear()
        elif y < 600:
            if x < 200:
                tool = 1
            elif x < 250:
                tool = 2
                setLastColor(red, green, blue)
                setColor(1.0, 1.0, 1.0)
            elif x < 300:
                tool = 3
            elif x < 350:
                tool = 4
            if tool != 2:
                if red == 1.0 and green == 1.0 and blue == 1.0:
                    setColor(lastRed, lastGreen, lastBlue)
        elif y < 650:
            setLineSize(x)

    glutPostRedisplay()

def mouseHeld(x, y):
    global inColor
    global inShade
    global shdSelX
    global shdSelY
    global tool
    if y < 500:
        if not inColor and not inShade:
            if tool == 1 or tool == 2:
                dots[-1].append([x,y,red,green,blue,lineSize])
                delDots = []
    elif x < 150:
        if tool != 2:
            if y >= 625 and inShade:
                setPickerColor(x)
                setPickerShade(shdSelX, shdSelY)
            elif inColor:
                setPickerShade(x,y)
    elif y > 600 and y < 650:
        setLineSize(x)

    glutPostRedisplay()

def keyClicked(key, x, y):
    if key.decode('utf8') == 'Z':
        undo()
    if key.decode('utf8') == 'Y':
        redo()

def clear():
    global dots
    global delDots
    dots = [[]]
    delDots = []
    glutPostRedisplay()

def undo():
    global tool
    if len(dots) > 1:
        x = 3
        try:
            print(dots[-2][0][5])
        except:
            doNothing()
        try:
            if dots[-2][0][5] > 7:
                x = 1
        except:
            doNothing()

        for i in range(x):
            delDots.append(dots[-2])
            del dots[-2]
        glutPostRedisplay()

def redo():
    if len(delDots) > 0:
        x = 3 if len(delDots[-2]) > 1 else 2
        for i in range(x):
            dots.insert(-1, delDots[-1])
            del delDots[-1]
        glutPostRedisplay()

def setLineSize(x):
    global lineSel
    global circleSel
    global tool

    if x > 265 and x < 335:
        if tool != 4:
            lineSel = x - 265
        else:
            circleSel = x - 265

def setColor(r, g, b):
    global red
    global green
    global blue
    red = r
    green = g
    blue = b

def setFullColor(r,g,b):
    global fullRed
    global fullGreen
    global fullBlue
    setColor(r,g,b)
    fullRed = r
    fullGreen = g
    fullBlue = b

def setLastColor(r, g, b):
    global lastRed
    global lastGreen
    global lastBlue
    lastRed = r
    lastGreen = g
    lastBlue = b

def setPickerColor(x):
    global colSel
    if x < 0:
        x = 0
    if x <= 15:
        setFullColor(1.0, x/15, 0.0)
    elif x <= 45:
        setFullColor(1.0-(x-15)/30, 1.0, 0.0)
    elif x <= 75:
        setFullColor(0.0, 1.0, (x-45)/30)
    elif x <= 105:
        setFullColor(0.0, 1.0-(x-75)/30, 1.0)
    elif x <= 135:
        setFullColor((x-105)/30, 0.0, 1.0)
    elif x <= 150:
        setFullColor(1.0, 0.0, 1.0-(x-135)/15)
    colSel = x

def setPickerShade(x,y):
    global fullRed
    global fullGreen
    global fullBlue
    global shdSelX
    global shdSelY
    shdSelX = x
    shdSelY = y
    r = blacked(fullRed)
    g = blacked(fullGreen)
    b = blacked(fullBlue)
    setColor(creamed(r,g,b), creamed(g,r,b), creamed(b,r,g))
    #y --> max: aproach 0
    #x --> min: equalize to max value

def glCircle(x, y, r):
    for i in range(r*4):
        glVertex2f(x + r * math.cos((math.pi/2)/r * i), y + r * math.sin((math.pi/2)/r * i))

def blacked(full):
    return (full-1)-(shdSelY-650)/150

def creamed(col1, col2, col3):
    m = max(col1, col2, col3)
    return shdSelX*(col1-m)/150 + m

def doNothing():
    global width

init()
glutMainLoop()
