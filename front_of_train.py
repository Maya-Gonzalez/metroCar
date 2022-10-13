'''
    Student Author Name: Stephanie Enriquez Isais
    Group Name: Team Rosa
    Project 1
    Fall 2022
    COMP 313: Computer Graphics
    Professor Schiffer
'''
import numpy as np
import matplotlib.pyplot as plt
import math as m
from vector_drawing import *

def colors(inputColor=0):
    if inputColor == 1:
        return '#594246'
    if inputColor == 2:
        return '#F2DCE0'
    if inputColor == 3:
        return '#F2ACBF'
    if inputColor == 4:
        return '#A67C87'
    if inputColor == 5:
        return '#F2C4D0'
    if inputColor == 6:
        return '#D2EBFF'


def polygons_of_train():
    level0 = [(74, 47), (74, 48), (83, 48), (83, 47)]
    level1 = [(65.5, 45), (67, 47), (90, 47), (90, 45)]
    level2 = [(65.5, 44), (65.5, 45), (90, 45), (90, 44)]
    level3 = [(65, 43), (65, 44), (90, 44), (90, 43)]
    level4 = [(65, 43), (90, 43), (90, 41), (66, 41)]
    level5 = [(66, 41), (90, 41), (90, 40), (66.2, 40)]
    level6 = [(90, 40), (70, 40), (73, 32), (90, 32)]
    level7 = [(73, 32), (90, 32), (90, 31.5), (73, 31.5)]
    level8 = [(73, 31.5), (90, 31.5), (90, 31), (74, 31), (80, 19), (79.5, 19)]

    #windows of train
    window1 = [(90, 31), (74, 31), (80, 19), (90, 19)]
    window2 = [(90, 31), (87, 31), (87, 19), (90, 19)]

    draw(
        Polygon(*level0, color="k", fill=colors(4)),
        Polygon(*level1, color="k", fill=colors(2)),
        Polygon(*level2, color="k", fill=colors(3)),
        Polygon(*level3, color="k", fill=colors(1)),
        Polygon(*level4, color="k", fill=colors(2)),
        Polygon(*level5, color="k", fill=colors(3)),
        Polygon(*level6, color="k", fill=colors(2)),
        Polygon(*level7, color="k", fill=colors(1)),
        Polygon(*level8, color="k", fill=colors(1)),

        Polygon(*window1, color="k", fill="#FFFFFF"),
        Polygon(*window2, color="k", fill="#e3e3e3"),
    )
    # windowshine
    shine_y = [31, 31, 26, 25]
    shine_x = [81, 82, 87, 87]
    shine_y_V2 = [31, 31, 27.6, 27]
    shine_x_V2 = [83, 83.4, 87, 87]
    plt.fill(shine_x, shine_y, colors(6), shine_x_V2, shine_y_V2, colors(6))


def lines_of_train():
    draw(
        Segment((87, 32), (87, 19), "k"),  # middle window line
        Segment((90, 32), (90, 19), "k"),  # outer window line
        Segment((80, 19), (90, 19), "k")  # top perpendicular window line
    )
    plt.plot([77.6, 78.6], [16.8, 16.8], linewidth=1, color="k")


def circles_of_train():
    # Wheels Arcs
    Arc(70.5, 46, 3, 20, (180 - 13), 20).draw_arc()
    Arc(87, 46, 3, 20, (180 - 13), 20).draw_arc()
    #-----------------------------------------------

    # Front of train - Arc Outline
    Arc(179, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arc()
    Arc(180, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arc()

    # Front of train - Filling in arcs
    Arc(179.2, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.3, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.4, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.5, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.6, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.7, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.8, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.9, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()

    #-----------------------------------------------------

    # Top of train - arc
    EllipseArc(1, 21, 76, 92, 22, 20, 8).draw()

    #Top of train - Detail ellises under the top of train
    EllipseArc(1, 26, 76, 92, 25, 20, 8).draw()
    EllipseArc(1, 30, 76, 92, 25.5, 20, 8).draw()
    EllipseArc(1, 30, 76, 92, 12.5, 20, 8).drawUpsideDown()

    # Top of train - Window detail ellipse fill
    EllipseArc(1, 28, 76, 92, 25.2, 20, 8).drawFill()
    EllipseArc(1, 28, 76, 92, 25.3, 20, 8).drawFill()

def connector():
    #Creating background box
    x_vals = [90, 90, 94, 94, 90]
    y_vals = [14.5, 46.5, 46.5, 14.5, 14.5]
    plt.fill(x_vals, y_vals, color = colors(4))
    #Setting the back x value
    x2 = 90
    #Setting the top and botton y values
    y1 = 14
    y2 = 47
    for x in range(5):
        plt.plot((x2 + (x * .8), x2 + (x * .8)), (y1 + .5, y2 - .5), linewidth=.8, color='k')
        Arc.arcSmall(x2 + (x*.8) + .4, y1 + .5, r=.39, ang1=0, ang2=180, dome=True)
        Arc.arcSmall(x2 + (x*.8) + .4, y2 - .5, r=.39, ang1=0, ang2=180, dome=False)  # lower

def details():
    # background color
    Arc(180, 81, 120, (-180 + 20), (-180 + 33), 20).draw_SquareFill()
    EllipseArc(1, 21, 76, 92, 22, 20, 8).drawSquareFill()

    # Text on train
    plt.text(77, 36, "Rosa", size=10, fontweight="bold")
    plt.text(77, 38, "Express", size=7, fontstyle="italic")

    # decorative nails - top train details
    EllipseArc(5, 21, 76, 93, 22, 20, 7.5).drawDots()


    # filling in the wheels
    Arc(70.5, 46, 3, 20, (180 - 13), 20).draw_wheelFill()
    Arc(87, 46, 3, 20, (180 - 13), 20).draw_wheelFill()

def drawFrontTrain():
    details()
    polygons_of_train()
    circles_of_train()
    lines_of_train()
    connector()

class Arc:
    def __init__(self, xc=1., yc=1., r=5, angle1=0., angle2=180., density=100):
        self.r = r
        self.yc = yc
        self.xc = xc
        self.density = density
        # ------------- Establishing what the angle of the begining and end points are
        self.angle1 = angle1
        self.angle2 = angle2

    def draw_arc(self):
        r = self.r
        xc = self.xc
        yc = self.yc
        density = self.density
        # plt.scatter(xc, yc, s=1)

        p1 = self.angle1 * np.pi / 180
        p2 = self.angle2 * np.pi / 180
        # ------------- Establishing the density
        dp = (p2 - p1) / density

        # ------------- Setting the x and y last
        xlast = xc + r * np.cos(p1)
        ylast = yc + r * np.sin(p1)

        # -------------- Creating the loop to plot lines
        for p in np.arange(p1 + dp, p2, dp):
            x = xc + r * np.cos(p)
            y = yc + r * np.sin(p)
            plt.plot([xlast, x], [ylast, y], linewidth=1, color="k")
            xlast = x
            ylast = y

    def draw_arcFill(self):
        r = self.r
        xc = self.xc
        yc = self.yc
        density = self.density
        # plt.scatter(xc, yc, s=1)

        p1 = self.angle1 * np.pi / 180
        p2 = self.angle2 * np.pi / 180
        # ------------- Establishing the density
        dp = (p2 - p1) / density

        # ------------- Setting the x and y last
        xlast = xc + r * np.cos(p1)
        ylast = yc + r * np.sin(p1)

        # -------------- Creating the loop to plot lines
        for p in np.arange(p1 + dp, p2, dp):
            x = xc + r * np.cos(p)
            y = yc + r * np.sin(p)
            plt.plot([xlast, x], [ylast, y], linewidth=1, color=colors(3))
            xlast = x
            ylast = y

    def draw_SquareFill(self):
        r = self.r
        xc = self.xc
        yc = self.yc
        density = self.density
        # plt.scatter(xc, yc, s=1)

        p1 = self.angle1 * np.pi / 180
        p2 = self.angle2 * np.pi / 180
        # ------------- Establishing the density
        dp = (p2 - p1) / density

        # ------------- Setting the x and y last
        xlast = xc + r * np.cos(p1)
        ylast = yc + r * np.sin(p1)

        # -------------- Creating the loop to plot lines
        for p in np.arange(p1 + dp, p2, dp):
            x = xc + r * np.cos(p)
            y = yc + r * np.sin(p)
            # plt.plot([xlast, x], [ylast, y], linewidth=1, color=colors(3))
            # -------------- Calculating the distance between two points to create a square
            dist = np.sqrt((x - xlast) ** 2 + (y - ylast) ** 2)
            x_vertices = [xlast, x, x + dist + 2, xlast + 2, xlast]
            y_vertices = [ylast, y, y + 5, y + 5, ylast]
            plt.fill(x_vertices, y_vertices, linewidth=1, color=colors(2))
            xlast = x
            ylast = y

    def draw_wheelFill(self):
        r = self.r
        xc = self.xc
        yc = self.yc

        # p1 = 0
        # p2 = 2 * np.pi
        p1 = self.angle1 * np.pi / 180
        p2 = self.angle2 * np.pi / 180
        dp = np.pi / 20

        rmax = 3
        dr = .5

        for r in np.arange(dr, rmax, dr):
            for p in np.arange(p1, p2, dp):
                x = xc + r * np.cos(p)
                y = yc + r * np.sin(p)
                plt.scatter(x, y, s=.2, color="k")

    def arcSmall(xc, yc, r, ang1, ang2, dome=False):

        p1 = ang1 * np.pi / 180
        p2 = ang2 * np.pi / 180
        dp = (p2 - p1) / 10  # frequency

        xlast = xc + r * np.cos(p1)
        ylast = yc + r * np.sin(p1)
        for p in np.arange(p1, p2 + dp, dp):
            x = xc + r * np.cos(p)
            y = yc + r * np.sin(p)
            if (dome == True):
                x = xc + r * np.cos(p * -1)
                y = yc + r * np.sin(p * -1)
            plt.plot([xlast, x], [ylast, y], linewidth=.9, color='k')
            plt.fill([xlast, x, xc, xlast], [ylast, y, yc, ylast], linewidth=1, color=colors(4))
            xlast = x
            ylast = y


class EllipseArc:
    def __init__(self, quad=1, start_angle=30, end_angle=60, x_offset=-10., y_offset=-20., a=70., b=50.):
        self.quad = quad  # this determines on which quad of it's midpoint the ellipse is drawn
        self.start_angle = start_angle  # Use this when start angle is not 0, MUST be POS
        self.end_angle = end_angle  # Use this when end angle is not 180, MUST be POS

        self.x_offset = x_offset
        self.y_offset = y_offset

        self.a = a
        self.b = b

    def draw(self):
        a = self.a
        b = self.b

        x_offset = self.x_offset
        y_offset = self.y_offset

        start_angle = self.start_angle
        end_angle = self.end_angle

        p1 = 0. * np.pi / 180.
        p2 = 180. * np.pi / 180.

        dp = (p2 - p1) / 180.

        xplast = a
        yplast = 0

        # TRY THREE
        for p in np.arange(p1, p2 + dp, dp):
            if ((np.tan(p) ** 2.) != 0):
                xp = -(np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5))
                yp = -(np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5))
                if p > np.pi / 2:
                    xp = -xp
                if start_angle * np.pi / 180 < p < end_angle * np.pi / 180:
                    # plt.plot([xplast, xp], [yplast, yp], color='orange')
                    plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=.8,
                             color='k')  # << moved to here
                xplast = xp + x_offset
                yplast = yp + y_offset

    def drawUpsideDown(self):
        a = self.a
        b = self.b

        x_offset = self.x_offset
        y_offset = self.y_offset

        start_angle = self.start_angle
        end_angle = self.end_angle

        p1 = 0. * np.pi / 180.
        p2 = 180. * np.pi / 180.

        dp = (p2 - p1) / 180.

        xplast = a
        yplast = 0

        # TRY THREE
        for p in np.arange(p1, p2 + dp, dp):
            if ((np.tan(p) ** 2.) != 0):
                xp = -(np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5))
                yp = (np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5))
                if p > np.pi / 2:
                    xp = -xp
                if start_angle * np.pi / 180 < p < end_angle * np.pi / 180:
                    # plt.plot([xplast, xp], [yplast, yp], color='orange')
                    plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=.8,
                             color='k')  # << moved to here
                xplast = xp + x_offset
                yplast = yp + y_offset

    def drawDots(self):
        a = self.a
        b = self.b

        x_offset = self.x_offset
        y_offset = self.y_offset

        start_angle = self.start_angle
        end_angle = self.end_angle

        p1 = 0. * np.pi / 180.
        p2 = 180. * np.pi / 180.

        dp = (p2 - p1) / 30.

        xplast = a
        yplast = 0

        # TRY THREE
        for p in np.arange(p1, p2 + dp, dp):
            if ((np.tan(p) ** 2.) != 0):
                xp = -(np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5))
                yp = -(np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5))
                if p > np.pi / 2:
                    xp = -xp
                if start_angle * np.pi / 180 < p < end_angle * np.pi / 180:
                    # plt.plot([xplast, xp], [yplast, yp], color='orange')
                    # plt.scatter()
                    plt.scatter([xplast, xp + x_offset], [yplast, yp + y_offset], s=1, color=colors(4))
                    # plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=.8,
                    # color='k')  # << moved to here
                xplast = xp + x_offset
                yplast = yp + y_offset

    def drawFill(self):
        a = self.a
        b = self.b

        x_offset = self.x_offset
        y_offset = self.y_offset

        start_angle = self.start_angle
        end_angle = self.end_angle

        p1 = 0. * np.pi / 180.
        p2 = 180. * np.pi / 180.

        dp = (p2 - p1) / 60.

        xplast = a
        yplast = 0

        # TRY THREE
        for p in np.arange(p1, p2 + dp, dp):
            if ((np.tan(p) ** 2.) != 0):
                xp = -(np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5))
                yp = -(np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5))
                if p > np.pi / 2:
                    xp = -xp
                if start_angle * np.pi / 180 < p < end_angle * np.pi / 180:
                    # plt.plot([xplast, xp], [yplast, yp], color='orange')
                    # plt.scatter()
                    # plt.scatter([xplast, xp + x_offset], [yplast, yp + y_offset], s=3, color=colors(1))
                    plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=2,
                             color=colors(1))  # << moved to here
                xplast = xp + x_offset
                yplast = yp + y_offset

    def drawSquareFill(self):
        a = self.a
        b = self.b

        x_offset = self.x_offset
        y_offset = self.y_offset

        start_angle = self.start_angle
        end_angle = self.end_angle

        p1 = 0. * np.pi / 180.
        p2 = 180. * np.pi / 180.

        dp = (p2 - p1) / 60.

        xplast = a
        yplast = 0

        # TRY THREE
        for p in np.arange(p1, p2 + dp, dp):
            if ((np.tan(p) ** 2.) != 0):
                xp = -(np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5))
                yp = -(np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5))
                if p > np.pi / 2:
                    xp = -xp
                if start_angle * np.pi / 180 < p < end_angle * np.pi / 180:
                    # plt.plot([xplast, xp], [yplast, yp], color='orange')
                    # plt.scatter()
                    # plt.scatter([xplast, xp + x_offset], [yplast, yp + y_offset], s=3, color=colors(1))
                    #plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=2,
                             #color=colors(1))  # << moved to here
                    # -------------- Calculating the distance between two points to create a square
                    dist = np.sqrt(((xp+x_offset) - xplast) ** 2 + ((yp+y_offset) - yplast) ** 2)
                    x_vertices = [xplast, xp+x_offset, xp+x_offset + dist + 2, xplast + 2, xplast]
                    y_vertices = [yplast, yp+y_offset, yp+y_offset + 5, yp+y_offset + 5, yplast]
                    plt.fill(x_vertices, y_vertices, linewidth=2, color=colors(2))
                xplast = xp + x_offset
                yplast = yp + y_offset


