#!python27
# -*- coding: utf-8 -*-
'''
Created on Apr 14, 2017
测试
'''
import TrainAdaBoost as adb
import ClassifyFunction as clf
import LoadData as ld
from numpy import *
datArr , labelArr = ld.loadDataSet('horseColicTraining2.txt')
classifierArray,aggClassEst = adb.adaBoostTrainDS(datArr, labelArr, 10)


#l = [(u'{"Task":"true","People":"John"}',)]
#for item in l:
# eval   d = eval(item[0])
#    print d["Task"]
testArr,testLabelArr = ld.loadDataSet('horseColicTest2.txt')
prediction10 = clf.adaClassify(testArr, classifierArray)
#报错 TypeError: list indices must be integers, not str
#原因 classfireArray 被赋值为 classifierArray,aggClassEst

errArr = mat(ones((67, 1)))
print errArr[prediction10 != mat(testLabelArr).T].sum()
