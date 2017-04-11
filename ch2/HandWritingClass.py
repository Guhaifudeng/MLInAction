#!python27
# -*- coding: utf-8 -*-
'''
Created on Mar 10, 2017
Example: using kNN on a handwriting recognition system
1. Collect: Text file provided.
2. Prepare: Write a function to convert from the image format to the list format
used in our classifier, classify0().
3. Analyze: We’ll look at the prepared data in the Python shell to make sure it’s
correct.
4. Train: Doesn’t apply to the kNN algorithm.
5. Test: Write a function to use some portion of the data as test examples. The
test examples are classified against the non-test examples. If the predicted
class doesn’t match the real class, you’ll count that as an error.
6. Use: Not performed in this example. You could build a complete program to extract
digits from an image, such a system used to sort the mail in the United States.
'''
import kNN
import os
import operator
from numpy import *
from os import listdir
def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        linestr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(linestr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')           #load the training set 需将digit.zip 解压缩
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)

    testFileList = listdir('testDigits')        #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = kNN.classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))
#测试程序
handwritingClassTest()
