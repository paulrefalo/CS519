#! python3
# numpyArrays.py - read large csv into 3D array using numpy
# OSU CS 519
# by Paul ReFalo 30 Nov 2017

import sys
from pprint import pprint
import types, os
import numpy as np
from numpy import genfromtxt


npArray = genfromtxt('array-final.txt', dtype=int, delimiter=',')

arr_3d = npArray.reshape((50, 50, 50)) #.transpose()
pprint(len(arr_3d[1]))
print(arr_3d.shape)
# 1d testing
print(npArray[-1])
print(npArray[-10:])    # [9153 4741 1447 8313 9795    8 9116 6282 3340 2965]

print(sum(npArray[-10:]))   # 55160
print(arr_3d[49][49][-10:])