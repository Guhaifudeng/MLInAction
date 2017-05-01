#!python27
# -*- coding: utf-8 -*-
'''
Created on Apr 10, 2017
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)

Output:     the most popular class label

@author: Feng Xie
'''
from numpy import *
import operator
from os import listdir
#读取文件数据，保存为matrix(NxM)，labels(Nx1)
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])#从后往前数
        index += 1
    return returnMat,classLabelVector

#归一化数值
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1)) #将变量内容复制成输入矩阵同样大小的矩阵
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide 矩阵除法linalg.solve(matA<matB)
    return normDataSet, ranges, minVals

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] # 数据集元素个数n
    #dataSet.astype('float64')
    diffMat = tile(inX, (dataSetSize,1)) - dataSet #差值矩阵n个xA-xB
    sqDiffMat = diffMat**2 #平方矩阵
    sqDistances = sqDiffMat.sum(axis=1) #距离矩阵Nx1
    distances = sqDistances**0.5

    sortedDistIndicies = distances.argsort() #按照距离值排序得到索引序列
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] #得到排在第i位的目标值
        print type(voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 # k个点中的目标值计数
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

