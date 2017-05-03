#!python27
# _*_ coding:utf-8 _*_
from numpy import *

def  trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    #侮辱性文档概率
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    #遍历文档，形成两个向量
    #分子
    p1Num = ones(numWords)
    p0Num = ones(numWords)
    #分母 并不等于1
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    #对贝叶斯公式求log
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect, p1Vect ,pAbusive

#vec2Classify 词集模型
#p0Vect\p1Vect ln(p(w|c))
#pClass1 ln(p(c))
def classifyNB(vec2Classify, p0Vect, p1Vect, pClass1):
    p1 = sum(vec2Classify * p1Vect) + log(pClass1)
    p0 = sum(vec2Classify * p0Vect) + log(pClass1)
    if p1 > p0:
        return 1
    else:
        return 0
