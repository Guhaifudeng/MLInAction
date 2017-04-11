#!python27
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import kNN
#载入数据
train = pd.read_csv('../../input/train.csv').sample(2000)
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
y = train['label']
y = y.values
predictions = []
for test_x in test.values:
    label = kNN.classify0(test_x,X,y,8);
    print label
    predictions.append(label);
#输出数据
result = pd.DataFrame({'ImageId': list(range(1,len(predictions)+1)), 'Label': predictions})
result.to_csv('../../output/dr_result.csv', index=False, header=True)
print "finished!"
