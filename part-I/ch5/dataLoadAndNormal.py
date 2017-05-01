#!python27
# -*- coding: utf-8 -*-
'''
Created on Apr 11, 2017

load data
'''

def loadCostTestDataSet(filename):
    dataMat = []; labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat
def  loadDataSet(filename):
    frData = open(filename);
    dataSet = []; dataLabels = []
    for line in frData.readlines():
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        dataSet.append(lineArr)
        dataLabels.append(float(currLine[21]))
    return dataSet,dataLabels
