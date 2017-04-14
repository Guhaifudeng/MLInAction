#!python27
# -*- coding: utf-8 -*-
'''
强分类器
'''
import TrainAdaBoost as adb
from numpy import *


def adaClassify(datToClass,classifierArr):
    #print classifierArr
    dataMatrix = mat(datToClass)#do stuff similar to last aggClassEst in adaBoostTrainDS
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m,1)))
    for i in range(len(classifierArr)):
        classEst = adb.stumpClassify(dataMatrix,classifierArr[i]['dim'], classifierArr[i]['thresh'],\
                                 classifierArr[i]['ineq'])#call stump classify
        aggClassEst += classifierArr[i]['alpha']*classEst
        print aggClassEst
    return sign(aggClassEst)
