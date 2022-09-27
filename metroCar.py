#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 19:36:02 2022

@author: mayagonzalez
"""

import numpy as np
import math
import matplotlib.pyplot as plt


# # situate grid
# f = plt.figure()
# ax = f.add_subplot(111)
# # set axes and adjust
# ax.axis([0,400,120,0])
# ax.xaxis.tick_top()
# # draw random line
# plt.plot([100,80],[20,40])
# # create grid
# for x in range(400):
#     for y in range(120):
#         plt.plot(x,y,color ='grey')
                   

# plt.grid(True)
# plt.axis('on')

# __________ Method 1: subplot
# create subplot
fig, ax = plt.subplots()
# set axes aspects 
ax.set_axisbelow(True)
ax.set_aspect('equal')

# create coordinate axes
plt.arrow(0,0, dx = 20, dy = 0, head_length = 4, head_width = 3, color = 'k')
plt.arrow(0,0, dx = 0, dy = 20, head_length = 4, head_width = 3, color = 'k')
x1 = 0
x2 = 380
y1 = 100
y2 = 0

x1 = 0
x2 = 220
y1 = 60
y2 = -10

ax.set_xlim([x1,x2])
ax.set_ylim([y1,y2])

# # adjust trick spacing
# plt.xticks(np.arange(x1,x2,20))
# plt.yticks(np.arange(y1,y2,-20))
# ax.tick_params(axis='both', which='major', labelsize=6)


#—————————————————grid
dx = 10
dy = -10

for x in np.arange(x1,x2,dx):
    for y in np.arange(y1,y2,dy):
        plt.scatter(x,y,s=10,color='lightgray')

# # adjust major/minor ticks
# ax.minorticks_on()
# ax.grid(which = 'major', linestyle = '-', linewidth='.5', color ='gray')
# ax.grid(which = 'minor', linestyle=':', linewidth='.5', color = 'lightgray')


# plt.grid(True)
# plt.axis('on')


# Create skeleton
x = [128, 287,287,128,128]
y = [7,7, 75,75,7]
plt.plot(x,y,linewidth=.5, color = 'k')

# draw road
plt.plot([5,343], [78,78], linewidth=.7, color = 'k')

# __________ end of method 1


# # ___________ Method 2


# dx = 1
# dy = -1
# x1 = 0
# x2 = 380
# y1 = 100
# y2 = 0
# # plt.axis([x1,x2,y1,y2])
# # plt.axis('on')
# # plt.grid(True)

# # create axes


# ax = plt.axes()
# ax.set_aspect('equal')
# plt.title('Sample Axes')


# ax.set_xlim([x1,x2])
# ax.set_ylim([y1,y2])

# # adjust tricks 
# plt.xticks(np.arange(x1,x2,20))
# plt.yticks(np.arange(y1,y2,-20))
# ax.tick_params(axis='both', which='major', labelsize=7)

# #—————————————————grid
# for x in np.arange(x1,x2,dx):
#     for y in np.arange(y1,y2,dy):
#         plt.scatter(x,y,s=1,color='lightgray')

# ax.tick_params(axis="y",direction="in", pad=-22)
# ax.tick_params(axis="x",direction="in", pad=-15)

# plt.show()




