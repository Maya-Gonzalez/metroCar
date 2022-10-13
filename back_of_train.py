import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from front_of_train import Arc
from vector_drawing import Polygon, draw

# set values for outline of the back rectangle
front_x = 176
back_x = 198
top_y = 14
bottom_y = 47

# color RGB values from our color palette
shade1 = '#594246'
shade2 = '#F2DCE0' #(242/255, 172/255, 191/255)
shade3 = '#F2ACBF' #(242/255, 220/255, 224/255)
shade4 = '#A67C87' #[(166%255), (124%255), (135%255)]
shade5 = '#F2C4D0' #(242/255, 196/255, 208/255)


# call all functions --> whole back section of metro
def back_of_train():
    outline()
    back_wheels()
    back_polygons()
    back_window()
    cable_connector()
    elbow()
    plt.show()


# outermost shape of the back of the train
def outline():
    x = [front_x, back_x, back_x, front_x, front_x]
    y = [top_y, top_y, bottom_y, bottom_y, top_y]
    plt.plot(x, y, linewidth=1, linestyle='-', color="k")


def back_window():
    # y axis values
    left_right_y = [22, 23, 23, 37.5]
    # left side lines
    left_x = [front_x+3, front_x+3, front_x+2, front_x+2]
    plt.plot(left_x, left_right_y, linewidth=1, linestyle='-', color="k")
    # right side lines
    right_x = [back_x-3, back_x-3, back_x-2, back_x-2]
    plt.plot(right_x, left_right_y, linewidth=1, linestyle='-', color="k")
    # bottom horizontal line
    plt.plot((front_x+2.45, back_x-2.45), (37.9, 37.9), linewidth=1, linestyle='-', color="k")
    # connect lines with arc
    connect_window_lines(195.14, 37, 65, 30)  # right
    connect_window_lines(178.865, 36.99, 114.55, 149.5)  # left


def connect_window_lines(xc, yc, p1_angle, p2_angle):
    # draw an arc
    r = 1
    p1 = p1_angle * np.pi / 180
    p2 = p2_angle * np.pi / 180
    dp = (p2 - p1) / 90
    xlast = xc + r * np.cos(p1)
    ylast = yc + r * np.sin(p1)
    for p in np.arange(p1, p2 + dp, dp):
        x = xc + r * np.cos(p)
        y = yc + r * np.sin(p)
        plt.plot([xlast, x], [ylast, y], linewidth=1, color='k')
        xlast = x
        ylast = y


# draw all horizontal lines --> Polygons to fill in
def back_polygons():
    # below the window from bottom to top
    btm_most0 = [(front_x + 7, bottom_y), (back_x - 7, bottom_y), (back_x - 7, bottom_y+1), (front_x + 7, bottom_y+1)]
    btm_most1 = [(front_x, 45), (back_x, 45), (back_x, bottom_y), (front_x, bottom_y)]
    btm_most2 = [(front_x, 44), (back_x, 44), (back_x, 45), (front_x, 45)]
    btm_most3 = [(front_x, 43), (back_x, 43), (back_x, 44), (front_x, 44)]
    btm_most4 = [(front_x, 41), (back_x, 41), (back_x, 43), (front_x, 43)]

    # above the window from top to bottom
    top_most0 = [(front_x, top_y), (back_x, top_y), (back_x, top_y+0.75), (front_x, top_y+0.75)]
    top_most1 = [(front_x, top_y+0.75), (back_x, top_y+0.75), (back_x, top_y + 2), (front_x, top_y + 2)]
    top_most2 = [(front_x, top_y+2), (back_x, top_y+2), (back_x, 17), (front_x, 17)]
    top_most3 = [(front_x, 17), (back_x, 17), (back_x, 19), (front_x, 19)]
    top_most4 = [(front_x, 19), (back_x, 19), (back_x, 22), (front_x, 22)]

    # draw & fill
    draw(Polygon(*btm_most0, color='k', fill=shade4),
         Polygon(*btm_most1, color='k', fill=shade2),
         Polygon(*btm_most2, color='k', fill=shade3),
         Polygon(*btm_most3, color='k', fill=shade1),
         Polygon(*btm_most4, color='k', fill=shade2),
         Polygon(*top_most0, color='k', fill=shade2),
         Polygon(*top_most1, color='k', fill=shade1),
         Polygon(*top_most2, color='k', fill=shade2),
         Polygon(*top_most3, color='k', fill=shade3),
         Polygon(*top_most4, color='k', fill=shade2))


def back_wheels():
    # draw with Arcs
    Arc(front_x + 3.5, 46, 3, 20, (180 - 13), 20).draw_arc()
    Arc(back_x - 3.5, 46, 3, 20, (180 - 13), 20).draw_arc()


def cable_connector():
    # cable connect on top of train
    # outline
    a = [(190, top_y), (195, 12),
         (180, 6), (178.5, 6),
         (178.5, 4.5), (177.5, 4.5), (177.5, 5.5),
         (177, 5.5), (177, 4), (179, 4), (179, 5.5),
         (180.25, 5.5),
         (196.5, 12.15), (192, top_y)]
    b = [(185.25, top_y), (193.2, 11.3), (192.33, 10.96), (183.5, top_y)]
    draw(Polygon(*a, color='k', fill=shade3),
         Polygon(*b, color='k', fill=shade3))
    # draw individual lines.
    plt.plot((191.76, 180), (11.1, 6.44), linewidth=1, linestyle='-', color="k")
    x0 = [180, 178.5, 178, 178]
    y0 = [6.44, 6.44, 6, 4.5]
    plt.plot(x0, y0, linewidth=1, linestyle='-', color="k")
    plt.plot((191.18, 180), (11.25, 6.82), linewidth=1, linestyle='-', color="k")
    x1 = [180, 178.3, 177.5, 177.5]
    y1 = [6.82, 6.82, 6.12, 5.5]
    plt.plot(x1, y1, linewidth=1, linestyle='-', color="k")


def elbow():
    outline = [(back_x, top_y+ 0.15), (back_x, bottom_y - 0.15), (back_x+3, bottom_y - 0.15), (back_x+3, top_y + 0.15)]
    draw(Polygon(*outline, color='k', fill=shade4))
    # thicker line
    plt.plot((back_x, back_x), (top_y + 0.15, bottom_y - 0.15), linewidth=2, linestyle='-', color="k")
    # individual lines
    plt.plot((back_x+0.75, back_x+0.66), (top_y + 0.15, bottom_y - 0.15), linewidth=0.66, linestyle='-', color="k")
    plt.plot((back_x + 1.5, back_x + 1.5), (top_y + 0.15, bottom_y - 0.15), linewidth=0.66, linestyle='-', color="k")
    plt.plot((back_x + 2.25, back_x + 2.25), (top_y + 0.15, bottom_y - 0.15), linewidth=0.66, linestyle='-', color="k")

#def personal_pazzaz():
