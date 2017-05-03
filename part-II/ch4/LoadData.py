#!python27
# _*_ coding:utf-8 _*_
from numpy import *
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],#文档词
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #文档类别，abusive or not
    return postingList, classVec
def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*',bigString)
    #只返回词长>2的词的小写形式
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def loadEmailDataSet():
    docList = []
    classList = []
    fullText = []
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)#列表作为元素添加
        fullText.extend(wordList)#扩展
        classList.append(0)
    return docList, classList,fullText
