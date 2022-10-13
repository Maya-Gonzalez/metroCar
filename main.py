import numpy as np
import matplotlib.pyplot as plt
import math as m

import back_of_train
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
    front_of_train.drawFrontTrain()
    middle_train.plotLines()
    # middle_train.horiz()
    # middle_train.drawWindows()
    # middle_train.plotVertLines()
    # #middle_train.arc()
    # middle_train.connector()
    back_of_train.back_of_train()

    plt.show()


main()
