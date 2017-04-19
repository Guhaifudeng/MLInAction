#!python27
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import kNN
import PCA
from numpy import *
#载入数据
train = pd.read_csv('../../input/train.csv').sample(4000)
print('train: ' + str(train.shape))
test = pd.read_csv('../../input/test.csv')
print('test: ' + str(test.shape))
train.head()
#train: (2000, 785)
#test: (28000, 784)

# feature matrix
X = train.ix[:,1:]
# response vector
X = X.values
print type(X)
lowX = numpy.array(PCA.pca(X, 160))
y = train['label']
y = y.values
predictions = []
print shape(lowX)
lowtest= numpy.array(PCA.pca(test.values, 160))
for test_x in lowtest:
    label = kNN.classify0(test_x,lowX,y,10);
    #print label
    predictions.append(label);
#输出数据
result = pd.DataFrame({'ImageId': list(range(1,len(predictions)+1)), 'Label': predictions})
result.to_csv('../../output/dr_result.csv', index=False, header=True)
print "finished!"
