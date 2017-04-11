#!python27
# -*- coding: utf-8 -*-
'''
Created on Mar 11, 2017

Example: using logistic regression to estimate horse fatalities from colic
1. Collect: Data file provided.
2. Prepare: Parse a text file in Python, and fill in missing values.
3. Analyze: Visually inspect the data.
4. Train: Use an optimization algorithm to find the best coefficients.
5. Test: To measure the success, we’ll look at error rate. Depending on the error
rate, we may decide to go back to the training step to try to find better values for
the regression coefficients by adjusting the number of iterations and step size.
6. Use: Building a simple command-line program to collect horse symptoms and output
live/die diagnosis won’t be difficult. I’ll leave that up to you as an exercise.

'''
from numpy import *
import dataLoadAndNormal as dln
import logRegres as lgr
def colicTest():
    trainingSet,trainingLabels = dln.loadDataSet('horseColicTraining.txt') #载入训练数据
    trainWeights = lgr.stocGradAscent1(array(trainingSet), trainingLabels, 1000) #训练得到模型参数：改进的随机梯度上升算法
    testSet,testLabels = dln.loadDataSet('horseColicTest.txt') #载入训练数据
    errorCount = 0; numTestVec = 0.0
    m,n = shape(testSet)
    for i in range(m):
        numTestVec += 1.0
        if int(lgr.classifyVector(array(testSet[i]), trainWeights))!= int(testLabels[i]):
            errorCount += 1
    errorRate = (float(errorCount)/numTestVec)
    print "the error rate of this test is: %f" % errorRate
    return errorRate

def multiTest():
    numTests = 10; errorSum=0.0
    for k in range(numTests):
        errorSum += colicTest()
    print "after %d iterations the average error rate is: %f" % (numTests, errorSum/float(numTests))
    #30%的数据缺失，为什么
    #改进后的随机梯度下降算法：迭代次数450，0.344776
colicTest()

multiTest()
