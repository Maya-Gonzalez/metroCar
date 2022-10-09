from vector_drawing import *
import numpy as np

def test():
    print('Mid testing')



# exoskeleton
x1 = 94
x2 = 174
y1 = 13
y2 = 47

def outerBox():

    x = [x1, x2, x2, x1, x1]
    y = [y1, y1, y2, y2, y1]
    plt.plot(x, y, linewidth=.8, color='k')
def plotHorizLines():
    # section 1: all horiz lines above the top door line, line 1 begins at outline
    xHorizTopDoor = 22
    plt.plot(x1,22, linewidth=.8, color  = 'k')
    # line 2
    plt.plot((x1, x2), (16, 16), linewidth=.8, color='k')

    plt.plot((x1, x2), (17, 17), linewidth=.8, color='k')
    plt.plot((x1, x2), (18, 18), linewidth=.8, color='k')
    plt.plot((x1, x2), (22, 22), linewidth=.8, color='k')


    # bottom of train
    # top 3 lines go from door1 - door2
    door1 = 97
    door2 = 171
    plotHorizLines.xHorizTopDoor = 22
    plotHorizLines.horiz1 = 40
    plotHorizLines.horiz2 = 41
    plotHorizLines.horiz3 = 43
    plotHorizLines.horiz4 = 44
    plotHorizLines.horiz5 = 45
    plt.plot((door1, 169), (plotHorizLines.horiz1, plotHorizLines.horiz1), linewidth=.4, color='k')
    plt.plot((door1, door2), (plotHorizLines.horiz2, plotHorizLines.horiz2), linewidth=.8, color='k')
    plt.plot((door1, door2), (plotHorizLines.horiz3, plotHorizLines.horiz3), linewidth=.8, color='k')
    plt.plot((door1, door2), (plotHorizLines.horiz4, plotHorizLines.horiz4), linewidth=.8, color='k')
    plt.plot((door1, door2), (plotHorizLines.horiz5, plotHorizLines.horiz5), linewidth=.8, color='k')
    plt.plot((x1, x2), (47, 47), linewidth=.8, color='k')
    # Filling in objects 
    x = [door1, door2, door2,door1,door1]
    y = [42,42,47,47,42]
    # plt.fill(x,y,color = 'k')

    # continue with mini lines


def plotVertLines():
    # section 1
    plt.plot((95.5, 95.5), (plotHorizLines.xHorizTopDoor, plotHorizLines.horiz5), linewidth=.8, color='k')
    plt.plot((96.5, 96.5), (plotHorizLines.xHorizTopDoor, plotHorizLines.horiz5), linewidth=.8, color='k')
    # door 1
    plt.plot((97, 97), (22, y2), linewidth=.8, color='k')
    # door 2
    plt.plot((115.5, 115.5), (22, y2), linewidth=.8, color='k')
    # door 3
    plt.plot((153, 153), (22, y2), linewidth=.8, color='k')
    # door 4
    plt.plot((171, 171), (22, y2), linewidth=.8, color='k')

    



def drawWindows():
    # window 1 walls
    plt.plot((98, 98), (23, plotHorizLines.horiz1), linewidth=.8, color='k')
    plt.plot((114.5, 114.5), (23, plotHorizLines.horiz1), linewidth=.8, color='k')
    # window 1, left corner
    plt.plot((98, 99), (23, 23), linewidth=.8, color='k')
    plt.plot((99, 99), (22, 23), linewidth=.8, color='k')
    # window 1, right corner
    plt.plot((113.5, 114.5), (23, 23), linewidth=.8, color='k')
    plt.plot((113.5, 113.5), (22, 23), linewidth=.8, color='k')
    # window 2 walls
    plt.plot((116.5, 116.5), (23, 36.5), linewidth=.8, color='k')
    plt.plot((133, 133), (23, 36.5), linewidth=.8, color='k')
    # window 2 bottom wall
    plt.plot((116.5 + 1, 133 - 1), (37.5, 37.5), linewidth=.8, color='k')
    # window 2, left corner
    plt.plot((116.5, 117.5), (23, 23), linewidth=.8, color='k')
    plt.plot((117.5, 117.5), (23, 22), linewidth=.8, color='k')

    # window 2, right corner
    plt.plot((132, 133), (23, 23), linewidth=.8, color='k')
    plt.plot((132, 132), (23, 22), linewidth=.8, color='k')

    # create ellipses for corner windows

    # Window 3
    # x is 135 - 152
    xMin = 135
    xMax = 151
    # window 3 walls
    plt.plot((xMin, xMin), (23, 36.5), linewidth=.8, color='k')
    plt.plot((xMax, xMax), (23, 36.5), linewidth=.8, color='k')
    # window 3 bottom wall
    plt.plot((xMin + 1, xMax - 1), (37.5, 37.5), linewidth=.8, color='k')
    # window 3, left corner
    plt.plot((xMin, xMin + 1 ), (23, 23), linewidth=.8, color='k')
    plt.plot((xMin + 1 , xMin + 1 ), (23, 22), linewidth=.8, color='k')

    # window 3, right corner
    plt.plot((xMax - 1, xMax ), (23, 23), linewidth=.8, color='k')
    plt.plot((xMax - 1, xMax - 1), (23, 22), linewidth=.8, color='k')

    # window 4
    xMin = 154
    xMax = 169
    yVal = plotHorizLines.horiz1
    # window 4 walls
    plt.plot((xMin, xMin ), (23, plotHorizLines.horiz1), linewidth=.8, color='k')
    plt.plot((xMax , xMax ), (23, plotHorizLines.horiz1), linewidth=.8, color='k')

    # window 4, left corner
    plt.plot((xMin, xMin+1), (23, 23), linewidth=.8, color='k')
    plt.plot((xMin+1, xMin+1), (22, 23), linewidth=.8, color='k')
    # window 4, right corner
    plt.plot((xMax-1, xMax), (23, 23), linewidth=.8, color='k')
    plt.plot((xMax-1, xMax-1), (22, 23), linewidth=.8, color='k')




