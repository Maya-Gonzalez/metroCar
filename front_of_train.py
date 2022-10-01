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

    level_test = [(74, 47), (74, 48), (83, 48), (83, 47), (67, 46), (68, 47), (90, 47), (90, 46)]

    draw(
        Polygon(*level0),
        Polygon(*level1),
        Polygon(*level2),
        Polygon(*level3),
        Polygon(*level4),
        Polygon(*level5),
        Polygon(*level6),
        Polygon(*level7),
        Polygon(*level8),

        # Polygon(*level_test)
    )


def lines_of_train():
    draw(
        Segment((87, 32), (87, 19), "k"),  # middle window line
        Segment((90, 32), (90, 19), "k"),  # outer window line
        Segment((80, 19), (90, 19), "k")  # top perpendicular window line
    )


def circles_of_train():
    Arc(70.5, 46, 3, 20, (180-13), 20).draw_arc()


class Arc():
    def __init__(self, xc=1, yc=1, r=5, angle1=0, angle2=180, density=100):
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
        plt.scatter(xc, yc, s=1)

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
