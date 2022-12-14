from vector_drawing import *
'''
Student Author Name: Maya Gonzalez
Group Name: Rosa
Project 1
Fall 2022
COMP 313: Computer Graphics
Professor Schiffer
'''


x1 = 94
x2 = 174
y1 = 14
y2 = 47

def outerBox():

    x = [x1, x2, x2, x1, x1]
    y = [y1, y1, y2, y2, y1]
    plt.plot(x, y, linewidth=.8, color='k')
# global x Values
xdoor1 = 97
xdoor2 = 115.5
xdoor3 = 153
xdoor4 = 171
xHorizTopDoor = 22
# x vals sections
xSec1Vert1 = 96
xSec5Vert1 = xdoor4 + .75
xSec5Vert2 = xSec5Vert1 + .75

# global y values
yhoriz1 = 40
yhoriz2 = 41
yhoriz3 = 43
yhoriz4 = 44
yhoriz5 = 45
yBottomWindow = 37.5

def plotLines():
    outerBox()
    horiz()
    plotVertLines()
    drawWindows()
    connector()
def horiz():
    
    # section 1 details: all horiz lines above the top door line, line 1 begins at outline
    xHorizTopDoor = 22
    # upper 
    plt.plot((x1,xSec1Vert1),(yhoriz1, yhoriz1), linewidth=.8, color  = 'k')
    plt.plot((x1,xSec1Vert1),(yhoriz2, yhoriz2),linewidth=.8, color  = 'k')
    # lower
    plt.plot((x1,xSec1Vert1),(yhoriz3, yhoriz3), linewidth=.8, color  = 'k')
    plt.plot((x1,xSec1Vert1),(yhoriz4, yhoriz4), linewidth=.8, color  = 'k')
    plt.plot((x1,xdoor1), (95.5,95.5),linewidth=.8, color  = 'k')

    # Section 5 details
    # upper
    plt.plot((xSec5Vert2,x2),(yhoriz2, yhoriz2),linewidth=.8, color  = 'k')
    # lower
    plt.plot((xSec5Vert2,x2),(yhoriz3, yhoriz3), linewidth=.8, color  = 'k')
    plt.plot((xSec5Vert2,x2),(yhoriz4, yhoriz4), linewidth=.8, color  = 'k')

    # lines above windows/doors
    plt.fill((x1,x2,x2,x1,x1),(y1,y1,y1+.5,y1+.5,y1), color = '#F2ACBF')
    # line1
    plt.plot((x1, x2), (y1+.5, y1+.5), linewidth=.8, color='k')
    plt.fill((x1,x2,x2,x1,x1),(y1+.5,y1+.5,15,15,y1+.5), color = '#594246')
    # line2
    plt.plot((x1, x2), (16, 16), linewidth=.8, color='k')
    plt.fill((x1,x2,x2,x1,x1),(15,15,16,16,15), color = '#F2DCE0')
    # line3
    plt.plot((x1, x2), (18, 18), linewidth=.8, color='k')
    plt.fill((x1,x2,x2,x1,x1),(16,16,18,18,16), color = '#F2ACBF')
    # line4
    plt.plot((x1, xSec5Vert2), (22, 22), linewidth=.8, color='k')
    plt.fill((x1,x2,x2,x1,x1),(18,18,22,22,18), color = '#F2DCE0')
    plt.fill((xSec5Vert2,x2,x2,xSec5Vert2,xSec5Vert2),(22,22,yhoriz2,yhoriz2,22), color = '#F2DCE0') # fills left vertical sec 

    # middle of train
    # section below door
    plt.fill((xdoor2,xdoor3,xdoor3,xdoor2,xdoor2),(yBottomWindow,yBottomWindow,yhoriz1,yhoriz1,yBottomWindow), color = '#F2ACBF')

    # bottom of train
    # y section1: directly below doors
    plt.plot((xdoor1, 169), (yhoriz1, yhoriz1), linewidth=.4, color='k')
    plt.fill((xdoor1,xdoor4,xdoor4,xdoor1,xdoor1),(yhoriz1,yhoriz1,yhoriz2,yhoriz2,yhoriz1), color = '#F2ACBF')
    plt.fill((169,xdoor4,xdoor4,169,169),(22,22,yhoriz2,yhoriz2,22), color = '#F2ACBF')
    plt.fill((168,xdoor4,xdoor4,168,168),(22,22,23,23,22), color = '#F2ACBF')
    plt.fill((x1,xSec1Vert1,xSec1Vert1,x1,x1),(yhoriz1,yhoriz1,yhoriz2,yhoriz2,yhoriz1), color = '#F2ACBF')
    # y section2
    plt.plot((xdoor1, xdoor4), (yhoriz2, yhoriz2), linewidth=.8, color='k')
    plt.fill((xdoor1,xdoor4,xdoor4,xdoor1,xdoor1),(yhoriz2,yhoriz2,yhoriz3,yhoriz3,yhoriz2), color = '#F2DCE0')
    plt.fill((x1,xSec1Vert1,xSec1Vert1,x1,x1),(yhoriz2,yhoriz2,yhoriz3,yhoriz3,yhoriz2), color = '#F2DCE0')
        # s section 5
    plt.fill((xSec5Vert2,x2,x2,xSec5Vert2,xSec5Vert2),(yhoriz2,yhoriz2,yhoriz3,yhoriz3,yhoriz2), color = '#F2DCE0')
    # y section3
    plt.plot((xdoor1, xdoor4), (yhoriz3, yhoriz3), linewidth=.8, color='k')
    plt.fill((xdoor1,xdoor4,xdoor4,xdoor1,xdoor1),(yhoriz3,yhoriz3,yhoriz4,yhoriz4,yhoriz3), color = '#594246')
    plt.fill((x1,xSec1Vert1,xSec1Vert1,x1,x1),(yhoriz3,yhoriz3,yhoriz4,yhoriz4,yhoriz3), color = '#594246')
    plt.fill((xSec5Vert2,x2,x2,xSec5Vert2,xSec5Vert2),(yhoriz3,yhoriz3,yhoriz4,yhoriz4,yhoriz3), color = '#594246')
    # y section4
    plt.plot((xdoor1, xdoor4), (yhoriz4, yhoriz4), linewidth=.8, color='k')
    plt.fill((xdoor1,xdoor4,xdoor4,xdoor1,xdoor1),(yhoriz4,yhoriz4,yhoriz5,yhoriz5,yhoriz4), color = '#F2ACBF')
    plt.fill((x1,xSec1Vert1,xSec1Vert1,x1,x1),(yhoriz4,yhoriz4,yhoriz5,yhoriz5,yhoriz4), color = '#F2ACBF')
    plt.fill((xSec5Vert2,x2,x2,xSec5Vert2,xSec5Vert2),(yhoriz4,yhoriz4,yhoriz5,yhoriz5,yhoriz4), color = '#F2ACBF')
    # y section 5
    plt.plot((x1, x2), (yhoriz5, yhoriz5), linewidth=.8, color='k')
    plt.fill((x1,x2,x2,x1,x1),(yhoriz5,yhoriz5,y2,y2,yhoriz3), color = '#F2DCE0')
    plt.plot((x1, x2), (47, 47), linewidth=.8, color='k')

def plotVertLines():
    # section 1: all vert lines before door1
    plt.plot((xSec1Vert1, xSec1Vert1), (xHorizTopDoor, yhoriz5), linewidth=.8, color='k')
    plt.plot((xSec1Vert1 + .5, xSec1Vert1 + .5), (xHorizTopDoor, yhoriz5), linewidth=.8, color='k')
    plt.fill((x1,xSec1Vert1,xSec1Vert1,x1,x1),(22,22,yhoriz1,yhoriz1,22), color = '#F2DCE0') # fills right vertical sec1
    plt.fill((xSec1Vert1,xSec1Vert1+.5,xSec1Vert1+.5,xSec1Vert1,xSec1Vert1),(22,22,yhoriz5,yhoriz5,22), color = '#A67C87') # fills right vertical sec2 
    plt.fill((xSec1Vert1+.5,xSec1Vert1+1,xSec1Vert1+1,xSec1Vert1+.5,xSec1Vert1+.5),(22,22,yhoriz5,yhoriz5,22), color = '#F2C4D0') # fills right vertical sec3 
    # section 2 + door 1 
    plt.plot((xdoor1, xdoor1), (22, y2), linewidth=.8, color='k')
    plt.fill((xSec1Vert1+1,98,98,xSec1Vert1+1,xSec1Vert1+1),(22,22,yhoriz1,yhoriz1,22), color = '#F2ACBF') # fills right vertical sec4
    plt.fill((98,99,99,98,98),(22,22,23,23,22), color = '#F2ACBF') # fills horiz section attached to sec4
    
    plt.fill((114.5, 115.5, 115.5, 114.5, 114.5),(22,22,yhoriz1,yhoriz1,22), color = '#F2ACBF') # fills right vertical sec4
    plt.fill((113.5, 114.5, 114.5,113.5,113.5),(22,22,23,23,22), color = '#F2ACBF') # fills horiz section attached to sec4
    # section 3 + door 2
    plt.plot((xdoor2, xdoor2), (22, y2), linewidth=.8, color='k') # xdoor2 = 115.5
    plt.fill((xdoor2, xdoor2+1, xdoor2+1, xdoor2, xdoor2),(22,22,yhoriz1,yhoriz1,22), color = '#F2ACBF') # fills right vertical sec4
    plt.fill((xdoor2, xdoor2+2, xdoor2+2, xdoor2, xdoor2),(22,22,23,23,22), color = '#F2ACBF') # fills horiz section attached to sec4
    # fill inbetween windows, 133 - 136
    plt.fill((133, 135, 135, 133, 133),(22,22,yhoriz1,yhoriz1,22), color = '#F2ACBF') 
    plt.fill((132, 133, 133, 132, 132),(22,22,23,23,22), color = '#F2ACBF') # fills left horiz section 
    plt.fill((135, 136, 136, 135, 135),(22,22,23,23,22), color = '#F2ACBF') # fills right horiz section 
    # fill to right of window 2
    plt.fill((151, 154, 154, 151, 151),(22,22,yhoriz1,yhoriz1,22), color = '#F2ACBF') 
    plt.fill((150, 155, 155, 150, 150),(22,22,23,23,22), color = '#F2ACBF') # fills entire horiz section 
    # door 3
    plt.plot((153, 153), (22, y2), linewidth=.8, color='k')
    # plt.fill((xdoor3, xdoor4, xdoor4, xdoor3, xdoor3),(22,22,yhoriz1,yhoriz1,22), color = '#F2DCE0')
    # door 4
    plt.plot((xdoor4, xdoor4), (22, y2), linewidth=.8, color='k')
    plt.fill((xdoor4, xSec5Vert1, xSec5Vert1, xdoor4, xdoor4),(22,22,yhoriz5,yhoriz5,22), color = '#594246') # fills vert1 right of door4
    plt.fill((xSec5Vert1, xSec5Vert2, xSec5Vert2, xSec5Vert1, xSec5Vert1),(22,22,yhoriz5,yhoriz5,22), color = '#594246') # fills vert2 right of door4
    # section 5
    plt.plot((xSec5Vert1, xSec5Vert1), (xHorizTopDoor, yhoriz5), linewidth=.8, color='k')
    plt.plot((xSec5Vert2 , xSec5Vert2), (xHorizTopDoor, yhoriz5), linewidth=.8, color='k')
    
def drawWindows():
    # window 1 walls
    plt.plot((98, 98), (23, yhoriz1), linewidth=.8, color='k')
    plt.plot((114.5, 114.5), (23, yhoriz1), linewidth=.8, color='k')
    # window 1, top left corner
    plt.plot((98, 99), (23, 23), linewidth=.8, color='k')
    plt.plot((99, 99), (22, 23), linewidth=.8, color='k')
    # window 1, right corner
    plt.plot((113.5, 114.5), (23, 23), linewidth=.8, color='k')
    plt.plot((113.5, 113.5), (22, 23), linewidth=.8, color='k')
    # window 2 walls
    plt.plot((116.5, 116.5), (23, 36.5), linewidth=.8, color='k')
    plt.plot((133, 133), (23, 36.5), linewidth=.8, color='k')
    # window 2 corners
    arc(117.5, 36.5, r = 1, ang1 = 90, ang2 = 180, dome=False)
    arc(132, 36.5, r = 1, ang1 = 0, ang2 = 90, dome=False)
    #arc(115, 36.5, r = 1, ang1 = 0, ang2 = 270, dome=False)
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
    # window 3 corners
    arc(136, 36.5, r = 1, ang1 = 90, ang2 = 180, dome=False)
    arc(150, 36.5, r = 1, ang1 = 0, ang2 = 90, dome=False)
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
    yVal = yhoriz1
    # window 4 walls
    plt.plot((xMin, xMin ), (23, yhoriz1), linewidth=.8, color='k')
    plt.plot((xMax , xMax ), (23, yhoriz1), linewidth=.8, color='k')

    # window 4, left corner
    plt.plot((xMin, xMin+1), (23, 23), linewidth=.8, color='k')
    plt.plot((xMin+1, xMin+1), (22, 23), linewidth=.8, color='k')
    # window 4, right corner
    plt.plot((xMax-1, xMax), (23, 23), linewidth=.8, color='k')
    plt.plot((xMax-1, xMax-1), (22, 23), linewidth=.8, color='k')
def connector():
    plt.fill((x2,x2+.75,x2+.75, x2, x2), (y1+.5,y1+.5, y2-.5, y2-.5, y1+.5) , color = '#A67C87')
    # line1
    plt.plot((x2+.75,x2+.75), (y1+.5, y2-.5), linewidth = .8, color = 'k' )
    arc(x2+.378, y1+.5, r = .37, ang1 = 180, ang2 = 0, dome=True)
    arc(x2+.378, y2-.5, r = .37, ang1 = 0, ang2 = 180,dome = False) # lower
    plt.fill((x2+.75,x2+1.5,x2+1.5, x2+.75, x2+.75), (y1+.5,y1+.5,y2-.5, y2-.5, y1+.5) , color = '#A67C87') # fill rect
    circle = plt.Circle((x2+.378, y1+.5), .37, color='#A67C87') # fill in arc
    plt.gca().add_patch(circle)
    lowerCircle = plt.Circle((x2+.378, y2-.5), .37, color='#A67C87')
    plt.gca().add_patch(lowerCircle)

    # line2
    plt.plot((x2+1.5,x2+1.5), (y1+.5, y2-.5), linewidth = .8, color = 'k' )
    arc(x2+.75+.378, y1+.5, r = .37, ang1 = 0, ang2 = 180, dome=True)
    arc(x2+.75+.378, y2-.5, r = .37, ang1 = 0, ang2 = 180,dome = False) # lower
    plt.fill((x2+.75+.378,x2+2.25,x2+2.25, x2+.75+.378, x2+.75+.378), (y1+.5,y1+.5,y2-.5, y2-.5, y1+.5) , color = '#A67C87')
    circle = plt.Circle((x2+.75+.378, y1+.5), .37, color='#A67C87')
    plt.gca().add_patch(circle)
    lowerCircle = plt.Circle((x2+.75+.378, y2-.5), .37, color='#A67C87')
    plt.gca().add_patch(lowerCircle)
    # line3
    plt.plot((x2+2.25,x2+2.25), (y1+.5, y2-.5), linewidth = .8, color = 'k' )
    arc(x2+1.5+.378, y1+.5, r = .37, ang1 = 0, ang2 = 180, dome=True)
    arc(x2+1.5+.378, y2-.5, r = .37, ang1 = 0, ang2 = 180, dome = False) # lower
    circle = plt.Circle((x2+1.5+.378, y1+.5), .37, color='#A67C87')
    plt.gca().add_patch(circle)
    lowerCircle = plt.Circle((x2+1.5+.378, y2-.5), .37, color='#A67C87')
    plt.gca().add_patch(lowerCircle)

   
def arc(xc, yc, r, ang1, ang2, dome = False):

    p1=ang1*np.pi/180
    p2=ang2*np.pi/180
    dp=(p2-p1)/10 # frequency

    xlast=xc+r*np.cos(p1)
    ylast=yc+r*np.sin(p1)
    for p in np.arange(p1+dp,p2,dp):
        x=xc+r*np.cos(p) 
        y=yc+r*np.sin(p) 
        if(dome == True):
            x = xc+r*np.cos(p *-1)
            y = yc+r*np.sin(p *-1)
        plt.plot([xlast,x],[ylast,y],linewidth = .9, color='k')
        xlast=x
        ylast=y
    

