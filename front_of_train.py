'''
    INSERT HEADER
     front_of_train.details()
    front_of_train.polygons_of_train()
    front_of_train.circles_of_train()
    front_of_train.lines_of_train()
'''
import numpy as np
import matplotlib.pyplot as plt
import math as m
from vector_drawing import *

dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
                (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
                (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
                ]


def translate(translation, vectors):
    return [add(translation, v) for v in vectors]


def add(*vectors):
    return sum([v[0] for v in vectors]), sum([v[1] for v in vectors])


def hundred_dinos():
    translations = [(12 * x, 10 * y)
                    for x in range(-5, 5)
                    for y in range(-5, 5)]
    dinos = [Polygon(*translate(t, dino_vectors), color=blue)
             for t in translations]
    draw(*dinos, grid=None, axes=None, origin=None)


def test():
    print("outsside the draw method")

    draw(
        # Points(*dino_vectors)
        hundred_dinos()
    )


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

    # vertical lines
    column1 = [(90, 47), (90.66, 47), (90.66, 14), (90, 14)]
    column2 = [(90.66, 47), (91.32, 47), (91.32, 14), (90.66, 14)]
    column3 = [(91.32, 47), (91.98, 47), (91.98, 14), (91.32, 14)]
    column4 = [(91.98, 47), (92.64, 47), (92.64, 14), (91.98, 14)]
    column5 = [(92.64, 47), (93.3, 47), (93.3, 14), (92.64, 14)]
    column6 = [(93.3, 47), (93.96, 47), (93.96, 14), (93.3, 14)]

    level_test = [(74, 47), (74, 48), (83, 48), (83, 47), (67, 46), (68, 47), (90, 47), (90, 46)]

    poly_lev_10 = Polygon(*level0)

    draw(
        # Polygon(*level0),
        # plt.gca().add_patch(poly_lev_10),
        Polygon(*level0, color="k", fill=colors(4)),
        Polygon(*level1, color="k", fill=colors(2)),
        Polygon(*level2, color="k", fill=colors(3)),
        Polygon(*level3, color="k", fill=colors(1)),
        Polygon(*level4, color="k", fill=colors(2)),
        Polygon(*level5, color="k", fill=colors(3)),
        Polygon(*level6, color="k", fill=colors(2)),
        Polygon(*level7, color="k", fill=colors(1)),
        Polygon(*level8, color="k", fill=colors(1)),
        Polygon(*column1, color="k", fill=colors(4)),
        Polygon(*column2, color="k", fill="k"),
        Polygon(*column3, color="k", fill=colors(4)),
        Polygon(*column4, color="k", fill=colors(4)),
        Polygon(*column5, color="k", fill=colors(4)),
        Polygon(*column6, color="k", fill=colors(4)),

        # Polygon(*level_test)
    )


def lines_of_train():
    draw(
        Segment((87, 32), (87, 19), "k"),  # middle window line
        Segment((90, 32), (90, 19), "k"),  # outer window line
        Segment((80, 19), (90, 19), "k")  # top perpendicular window line
    )
    plt.plot([77.6, 78.6], [16.8, 16.8], linewidth=1, color="k")


def circles_of_train():
    # wheels
    Arc(70.5, 46, 3, 20, (180 - 13), 20).draw_arc()
    Arc(87, 46, 3, 20, (180 - 13), 20).draw_arc()

    # (self, xc=1., yc=1., r=5, angle1=0, angle2=180, density=100)
    # Arc(180, 80, 120, 290, 303, 20).draw_arc()

    # arcs for front of train -  xc=1., yc=1., r=5, angle1=0., angle2=180., density=100)
    Arc(179, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arc()
    Arc(180, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arc()
    # Filling in arcs
    # Arc(179.15, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.2, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.3, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.4, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.5, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.6, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.7, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.8, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()
    Arc(179.9, 81, 120, (-180 + 20), (-180 + 33), 20).draw_arcFill()

    # EllipseArc().draw()
    # EllipseArc(1, 30, 60, 0, 0, 70., 50.).draw()

    # (1 start_angle=30, end_angle=60, x_offset=-10, y_offset=-20, a=70., b=50.)
    # Top of the train arc
    EllipseArc(1, 21, 76, 92, 22, 20, 8).draw()

    # EllipseArc(2, 30, 60, -130, -190, 70., 50.).draw()

    EllipseArc(1, 26, 76, 92, 25, 20, 8).draw()
    EllipseArc(1, 30, 76, 92, 25.5, 20, 8).draw()
    EllipseArc(1, 30, 76, 92, 12.5, 20, 8).drawUpsideDown()

    #Window ellipse fill
    EllipseArc(1, 28, 76, 92, 25.2, 20, 8).drawFill()
    EllipseArc(1, 28, 76, 92, 25.3, 20, 8).drawFill()
    #EllipseArc(1, 26, 76, 92, 25, 20, 8).drawFill()


def details():
    # Text on train
    plt.text(77, 36, "Rosa", size=10, fontweight="bold")
    plt.text(77, 38, "Express", size=7, fontstyle="italic")

    # Detail lines
    topFront = [(77, 16), (78.5, 16)]

    # draw(
    #     Segment((77.6, 16.8), (78.7, 16.8), "k")
    # )

    #nail top train details
    EllipseArc(5, 21, 76, 93, 22, 20, 7.5).drawDots()

    # windowshine
    shine_y = [31, 31, 26, 25]
    shine_x = [81, 82, 87, 87]
    shine_y_V2 = [31, 31, 27.6, 27]
    shine_x_V2 = [83, 83.4, 87, 87]
    plt.fill(shine_x, shine_y, colors(6), shine_x_V2, shine_y_V2, colors(6))

    # filling in the wheels
    Arc(70.5, 46, 3, 20, (180 - 13), 20).draw_wheelFill()
    Arc(87, 46, 3, 20, (180 - 13), 20).draw_wheelFill()


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
                    #plt.scatter([xplast, xp + x_offset], [yplast, yp + y_offset], s=3, color=colors(1))
                    plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=2, color=colors(1))  # << moved to here
                xplast = xp + x_offset
                yplast = yp + y_offset

        # TRY ONE
        # for p in np.arange(p1, p2 + dp, dp):
        #     if (np.tan(p) ** 2.) != 0:
        #         xp = np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5)  # << removed here
        #         yp = np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5)  # << removed here
        #         if p > np.pi / 2:
        #             xp = -xp
        #     if start_angle * np.pi / 180 < p < end_angle * np.pi / 180:
        #         # Line below print in POS y quadrant
        #         plt.plot([xplast, xp + x_offset], [yplast, yp + y_offset], linewidth=.8, color='r')  # << moved to here
        #         # print('POS:', 'P1:', xplast, yplast, 'P2:', xp, yp, )
        #         # Line below print in NEG y quadrant
        #         # plt.plot([xplast,xp],[-yplast,-yp],color='purple')
        #         # print('NEG:', 'P1:', xplast, -yplast, 'P2:', xp, -yp)
        #         xplast = xp + x_offset  # << moved to here
        #         yplast = yp + y_offset  # << moved to here

        # TRY TWO
        # for p in np.arange(p1, p2 + dp, dp):
        #
        #     if (np.tan(p) ** 2.) != 0:
        #         xp = (np.abs(a * b * (b * b + a * a * (np.tan(p)) ** 2.) ** -.5) + x_offset)
        #         yp = (np.abs(a * b * (a * a + b * b / (np.tan(p) ** 2.)) ** -.5) + y_offset)
        #         if p > np.pi / 2:
        #             xp = -xp
        #         if start_angle * np.pi / 180 < p < end_angle * np.pi / 180:
        #             # Line below print in POS y quadrant
        #             plt.plot([xplast, xp], [yplast, yp], linewidth=.8, color='red')
        #             # print('POS:', 'P1:', xplast, yplast, 'P2:', xp, yp, )
        #             # Line below print in NEG y quadrant
        #             # plt.plot([xplast,xp],[-yplast,-yp],color='purple')
        #             # print('NEG:', 'P1:', xplast, -yplast, 'P2:', xp, -yp)
        #         xplast = xp
        #         yplast = yp