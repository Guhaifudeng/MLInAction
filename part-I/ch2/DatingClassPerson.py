#!python27
# -*- coding: utf-8 -*-
'''
Created on Apr 10, 2017
Example: using kNN on results from a dating site
1. Collect: Text file provided.
2. Prepare: Parse a text file in Python.
3. Analyze: Use Matplotlib to make 2D plots of our data.
4. Train: Doesn’t apply to the kNN algorithm.
5. Test: Write a function to use some portion of the data Hellen gave us as test examples.
The test examples are classified against the non-test examples. If the
predicted class doesn’t match the real class, we’ll count that as an error.
6. Use: Build a simple command-line program Hellen can use to predict whether
she’ll like someone based on a few inputs.
'''
import kNN
import os
from numpy import *
def datingClassTest():
    hoRatio = 0.50      #hold out 10%
    datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')       #load data setfrom file
    normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)# 50% train set,50% test set
    errorCount = 0.0
    errorAns = m
    for k in range(20):
        errorCount = 0
        for i in range(numTestVecs):
            classifierResult = kNN.classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],k+1)
           # print "the classifier came back with: %s, the real answer is: %s" % (classifierResult, datingLabels[i])
            if (classifierResult != datingLabels[i]): errorCount += 1.0
        print "when k is %d the total error rate is: %f" %(k+1,(errorCount/float(numTestVecs)))
        print errorCount
        if errorCount <= errorAns:
            errorAns = errorCount
            ans = k+1
    print "the best k is",ans

def classifyPerson():
    #resultList = ['not at all','in small doses', 'in large doses']
    percentTats = float(raw_input(\
                "percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))#使用sumlime配置的环境python27无法读取输入数据
    iceCream = float(raw_input("liters of ice cream consumed per year?"))#点击*.py运行即可，程序末尾添加待输入
    datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = kNN.classify0((inArr-\
                        minVals)/ranges,normMat,datingLabels,3)
    print "You will probably like this person: ",\
    classifierResult
#测试算法，选择合适的k值
#运行结果显示，k=8，错误率最低
datingClassTest()
#使用算法，
classifyPerson()

os.system("pause")#窗口暂停
