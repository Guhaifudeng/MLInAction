#!python27
# -*- coding: utf-8 -*-
'''
Created on Jun 14, 2011

@author: Peter
'''
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
#载入数据
train = pd.read_csv('../../input/train.csv').sample(2000)
print('train: ' + str(train.shape))
train.head()
# feature matrix
X = train.ix[:,1:]
# response vector
X = X.values
dataMat = X

#below is a quick hack copied from pca.pca()
meanVals = mean(dataMat, axis=0)
meanRemoved = dataMat - meanVals #remove mean
covMat = cov(meanRemoved, rowvar=0)
eigVals,eigVects = linalg.eig(mat(covMat))
eigValInd = argsort(eigVals)            #sort, sort goes smallest to largest
eigValInd = eigValInd[::-1]#reverse
sortedEigVals = eigVals[eigValInd]
total = sum(sortedEigVals)
varPercentage = sortedEigVals/total*100

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(1, 21), varPercentage[:20], marker='^')
for i in range(20,150):
    print "%.2f" % sum(varPercentage[:i])
plt.xlabel('Principal Component Number')
plt.ylabel('Percentage of Variance')
plt.show()
