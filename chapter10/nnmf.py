# encoding: utf8

import numpy as np
from numpy import *  # NOQA


def difcost(a, b):
    dif = 0
    for i in range(np.shape(a)[0]):
        for j in range(np.shape(a)[1]):
            # Euclidean Distance
            dif += pow(a[i, j]-b[i, j], 2)
    return dif


def factorize(v, pc=10, iter=50):
    ic = np.shape(v)[0]
    fc = np.shape(v)[1]

    # Initialize the weight and feature matrices with random values
    w = np.matrix([[np.random.random() for j in range(pc)] for i in range(ic)])
    h = np.matrix([[np.random.random() for i in range(fc)] for i in range(pc)])

    # Perform operation a maximum of iter times
    for i in range(iter):
        wh = w*h

        # Calculate the current difference
        cost = difcost(v, wh)

        if i % 10 == 0:
            print cost

        # Terminate if the matrix has been fully factorized
        if cost == 0:
            break

        # Update feature matrix
        hn = (np.transpose(w)*v)
        hd = (np.transpose(w)*w*h)

        h = np.matrix(np.array(h)*np.array(hn)/np.array(hd))

        # Update weights matrix
        wn = (v*np.transpose(h))
        wd = (w*h*np.transpose(h))

        w = np.matrix(np.array(w)*np.array(wn)/np.array(wd))

    return w, h
