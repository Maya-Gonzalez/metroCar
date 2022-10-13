import numpy as np
import matplotlib.pyplot as plt
import math as m
# from vector_drawing import *
import front_of_train
import middle_train

figure, axes = plt.subplots()
axes.set_aspect(1)  # creates a 1:1 ratio


def main():
    # ---------------Making the ground
    x = [7, 215]
    y = [49, 49]
    plt.plot(x, y, linewidth=1, color='grey')

    # -------------- Testing
    # front_of_train.test()

    # ---------------- Actual Work
    front_of_train.polygons_of_train()
    front_of_train.lines_of_train()
    front_of_train.circles_of_train()
    middle_train.plotLines()
    # middle_train.horiz()
    # middle_train.drawWindows()
    # middle_train.plotVertLines()
    # #middle_train.arc()
    # middle_train.connector()

    plt.show()


main()
