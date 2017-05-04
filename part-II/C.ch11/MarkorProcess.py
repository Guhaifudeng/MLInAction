#!python27
# _*_ coding:utf-8 _*_
#
#      晴天 雨天
# 晴天 0.7  0.3
# 雨天 0.8  0.2
#
from numpy import *
import numpy as np
A = mat([[0.7, 0.3],[0.8,0.2]])
A3 = A * A #7.3日转移概率矩阵
print A1
B = np.array([[0.7, 0.3],[0.8,0.2]])
B1 = B * B
print B1
A10 = A #7.10日转移概率矩阵
for i in xrange(8):
    A10 = A10 * A

print A10
