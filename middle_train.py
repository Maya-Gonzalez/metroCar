from vector_drawing import *import numpy as npdef test():    print('Mid testing')# exoskeletonx1 = 94x2 = 174y1 = 13y2 = 47def outerBox():    x = [x1, x2, x2, x1, x1]    y = [y1, y1, y2, y2, y1]    plt.plot(x, y, linewidth=.5, color='k')def plotHorizLines():    plt.plot((x1, x2), (16, 16), linewidth=.5, color='k')    plt.plot((x1, x2), (17, 17), linewidth=.5, color='k')    plt.plot((x1, x2), (18, 18), linewidth=.5, color='k')    plt.plot((x1, x2), (22, 22), linewidth=.5, color='k')    169    # bottom of train    # top 3 lines go from door1 - door2    door1 = 97    door2 = 171    plt.plot((door1, 169), (41, 41), linewidth=.4, color='k')    plt.plot((door1, door2), (42, 42), linewidth=.5, color='k')    plt.plot((door1, door2), (43, 43), linewidth=.4, color='k')    plt.plot((door1, door2), (44, 44), linewidth=.4, color='k')    plt.plot((door1, door2), (45, 45), linewidth=.4, color='k')    plt.plot((x1, x2), (47, 47), linewidth=.5, color='k')    # continue with mini linesdef drawWindows():    # window 1 walls    plt.plot((98, 98), (23, 41), linewidth=.5, color='k')    plt.plot((114.5, 114.5), (23, 41), linewidth=.5, color='k')    # window 1, left corner    plt.plot((98, 99), (23, 23), linewidth=.5, color='k')    plt.plot((99, 99), (22, 23), linewidth=.5, color='k')    # window 1, right corner    plt.plot((113.5, 114.5), (23, 23), linewidth=.5, color='k')    plt.plot((113.5, 113.5), (22, 23), linewidth=.5, color='k')    # window 2 walls    plt.plot((116.5, 116.5), (23, 36.5), linewidth=.5, color='k')    plt.plot((133, 133), (23, 36.5), linewidth=.5, color='k')    # window 2 bottom wall    plt.plot((116.5 + 1, 133 - 1), (37.5, 37.5), linewidth=.5, color='k')    # window 2, left corner    plt.plot((116.5, 117.5), (23, 23), linewidth=.5, color='k')    plt.plot((117.5, 117.5), (23, 22), linewidth=.5, color='k')    # window 2, right corner    plt.plot((132, 133), (23, 23), linewidth=.5, color='k')    plt.plot((132, 132), (23, 22), linewidth=.5, color='k')def plotDoors():    plt.plot((97, 97), (22, y2), linewidth=.5, color='k')    plt.plot((115.5, 115.5), (22, y2), linewidth=.5, color='k')    plt.plot((153, 153), (22, y2), linewidth=.5, color='k')    plt.plot((171, 171), (22, y2), linewidth=.5, color='k')