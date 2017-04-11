#!python27
# -*- coding: utf-8 -*-
'''
Created on Mar 11, 2017

Plotting the J line with the change of theta[1]

'''
from numpy import *
import matplotlib.pyplot as plt
import dataLoadAndNormal as dln
import logRegres as lgr

# the batch gradient descent algrithm
def plotJwiththeta2(x,y):
    m,n = shape(x)     #m: number of training example; n: number of features
    x = c_[ones(m),x]     #add x0
    x = mat(x)      # to matrix
    y = mat(y)
    maxcycle = 90000
    theta = zeros((n+1,1))  #initial theta
    theta[1] = -50
    J = []
    theta1 = zeros((maxcycle,1))
    for i in range(maxcycle):
        h = lgr.sigmoid(x*theta)
        theta[1] = theta[1] + 0.003
        theta1[i] = theta[1];#直接用append会出错，没有中间变量地址
        cost = lgr.costfunction(y,h)
        J.append(cost)
    #    print theta[1]


    fig = plt.figure()
    plt.plot(theta1, J)
    plt.xlabel('theta1');
    plt.ylabel('J');
    plt.show()
    return
dataMat,labelMat=dln.loadCostTestDataSet('testSet.txt')
plotJwiththeta2(dataMat, labelMat)
