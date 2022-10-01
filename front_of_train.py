import numpy as np
import matplotlib.pyplot as plt
import math as m
from vector_drawing import *

# figure, axes = plt.subplots()
# axes.set_aspect(1) #creates a 1:1 ratio

# x1 = 0
# x2 = 220
# y1 = 60
# y2 = 0
#
# plt.axis([x1, x2, y1, y2])
#
# plt.xticks(np.arange(x1, x2, step=10)) and plt.yticks(np.arange(y2, y1, step=10))
# plt.grid(True)
# #—————————————————grid - solid grey
# dx = .5
# dy = -.5
#
# for x in np.arange(x1,x2,dx):
#     for y in np.arange(y2,y1,dy):
#         plt.scatter(x,y,linestyle=':',color='lightgray')
dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
        (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
        (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
    ]

def translate(translation, vectors):
    return [add(translation, v) for v in vectors]

def add(*vectors):
    return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))

def hundred_dinos():
    translations = [(12*x,10*y)
                    for x in range(-5,5)
                    for y in range(-5,5)]
    dinos = [Polygon(*translate(t, dino_vectors),color=blue)
                for t in translations]
    draw(*dinos, grid=None, axes=None, origin=None)

def test():
    print("outsside the draw method")

    draw(
        # Points(*dino_vectors)
        hundred_dinos()
    )

def bottom_of_train():
    level0 = [(74, 47),(74, 48), (83, 48), (83, 47)]
    level1 = [(66, 45), (68, 47), (90, 47), (90, 45)]
    level2 = [(66, 45), (66, 46), (90, 46), (90, 45)]
    level3 = [(66, 45), (90, 45), (90, 42), (67.5, 42)]
    level4 = [(90, 42), (67.5, 42), ()]


    level_test = [(74, 47),(74, 48), (83, 48), (83, 47), (67, 46), (68, 47), (90, 47), (90, 46)]


    draw(
        Polygon(*level0),
        Polygon(*level1),
        Polygon(*level2),
        Polygon(*level3),
        #Polygon(*level_test)
    )



plt.show()

