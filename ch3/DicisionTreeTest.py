#!python27
# -*- coding: utf-8 -*-
'''
Example: using decision trees to predict contact lens type
1. Collect: Text file provided.
2. Prepare: Parse tab-delimited lines.
3. Analyze: Quickly review data visually to make sure it was parsed properly. The final
tree will be plotted with createPlot().
4. Train: Use createTree() from section 3.1.
5. Test: Write a function to descend the tree for a given instance.
6. Use: Persist the tree data structure so it can be recalled without building the
tree; then use it in any application.
'''
from numpy import *
import LoadData as ld
import DicisionTree as dts
import TreePlotter as tplt
dataSet,labels = ld.createDataSet('lenses.txt')
#testLabels = zeros(len(labels),1)#也不能采用
#testLabels =  labels# 不能采用
lensesTree = dts.createTree(dataSet,labels)
print lensesTree
tplt.createPlot(lensesTree)
print labels
#利用训练数据做测试数据
dataSet,testLabels = ld.createDataSet('lenses.txt')
errorCount = 0
numTestVec = 0
for testVec in dataSet:
    numTestVec += 1.0
    classLabel = dts.classify(lensesTree,testLabels,testVec)
    if classLabel != testVec[-1]:
        errorCount += 1;
errorRate = (float(errorCount)/numTestVec)
print "the error rate of this test is: %f" % errorRate

