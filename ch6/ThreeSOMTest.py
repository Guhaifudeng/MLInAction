#!python27
# -*- coding: utf-8 -*-
'''
Created on Apr 12, 2017

test all SMO algorithm
'''
from numpy import *
import OptStructSimpleSOM as ssmo
import OptStructSOM as fsmo
import OptStructKSOM as fksmo
import LoadData as ld
dataArr, labelArr = ld.loadDataSet('testSetRBF.txt')
print "test Simple SMO:"
ssmo.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
print "test Full Platt SMO:"
fsmo.smoP(dataArr, labelArr, 0.6, 0.001, 40)
print "test Full Platt SMO using Kernel:"
fksmo.smoPK(dataArr, labelArr, 0.6, 0.001, 40)
