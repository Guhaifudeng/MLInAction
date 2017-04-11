#!python27
# -*- coding: utf-8 -*-
'''
Created on Mar 10, 2017
create dataset to test the functions in this book
'''
from numpy import *
import operator

import matplotlib
import matplotlib.pyplot as plt
def createDataSet():
    group = array([[1.1,1.0],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

group, labels = createDataSet()
print group
print group.shape[0]# row
print labels

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(group[:,0], group[:,1])
plt.show()
