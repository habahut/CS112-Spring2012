#!/usr/bin/env python

import math

# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

def distance(a, b):
    dA = a[0] - b[0]
    dB = a[1] - b[1]

    dA = dA ** 2
    dB = dB **2

    return math.sqrt(dA + dB)


# ADVANCED
# Normalizing Vectors
#   normalize a vector of length N.  If given all zeros, just spit back the same vector
#   http://www.fundza.com/vectors/normalize/index.html

#   ex:
#     >>> normalize((1,1))
#     [0.70710678118654746, 0.70710678118654746]
#     >>> normalize([0,0,0])
#     [0,0,0]
#     >>> normalize([1,1,1,1])
#     [0.25, 0.25, 0.25, 0.25]

def normalize(vec):
    t = 0
    vec = list(vec)
    for i,v in enumerate(vec):
        t += vec[i]**2

    distance = math.sqrt(t)
    if not (distance == 0):
        for i,v in enumerate(vec):
            vec[i] = vec[i] / distance

    return vec      
    
    distance = math.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)

    vec[0] /= distance
    vec[1] /= distance
    vec[2] /= distance
