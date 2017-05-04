#!python27
# _*_ coding:utf-8 _*_
# 观测集合:(潮湿、湿润、干燥、干旱)
# 状态集合:(晴天、阴天、雨天)
# 初始化概率向量:(0.63、0.17、0.20)
###状态转移概率矩阵
#      晴天 阴天  雨天
# 晴天 0.5  0.375 0.125
# 阴天 0.25 0.125 0.625
# 雨天 0.25 0.375 0.375
###观测概率分布
#      干旱 干燥 湿润 潮湿
# 晴天 0.60 0.20 0.15 0.05
# 阴天 0.25 0.25 0.25 0.25
# 雨天 0.05 0.10 0.35 0.50
from numpy import *
import numpy as np
#初始概率
startP = mat([0.63, 0.17, 0.20])

stateP = mat([[0.5 , 0.375, 0.125],
              [0.25, 0.125, 0.625],
              [0.25, 0.375, 0.375]])
emitP = mat([[0.60, 0.20, 0.15, 0.05],
             [0.25, 0.25, 0.25, 0.25],
             [0.05, 0.10, 0.35, 0.50]])
#干旱
state1Emit = multiply(startP,emitP[:,0].T)
print state1Emit
print 'argmax1:', state1Emit.argmax()
#干燥
state2Emit =  state1Emit * stateP
state2Emit = multiply(state2Emit, emitP[:,1].T)
print state2Emit
print 'argmax2:',state2Emit.argmax()
#潮湿
state3Emit = state2Emit * stateP
state3Emit = multiply(state3Emit, emitP[:,3].T)
print state3Emit
print 'argmax3:',state3Emit.argmax()
