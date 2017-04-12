#!python27
# -*- coding: utf-8 -*-
'''
Created on Apr 12, 2017

Data Processing
'''

from numpy import *
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect
