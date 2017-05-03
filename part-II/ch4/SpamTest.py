#!pythn27
# _*_ coding:utf-8 _*_
#垃圾分类
import LoadData
import PrepareData
import NaiveBayesianModel
from numpy import *
def SpamTest():
    docList, classList, _ = LoadData.loadEmailDataSet()
    vocabList = PrepareData.createVocabList(docList)
    trainingSet = range(50)

    testSet = []
    #测试样本10个
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        #随机生成索引
        testSet.append(trainingSet[randIndex])
        #删除已加入样本
        del(trainingSet[randIndex])
    #训练数据准备
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(PrepareData.setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = NaiveBayesianModel.trainNB0(array(trainMat), array(trainClasses))

    errorCount = 0
    for docIndex in testSet:
        wordVector = PrepareData.setOfWords2Vec(vocabList, docList[docIndex])
        if NaiveBayesianModel.classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is :', float(errorCount)/len(testSet)
SpamTest()
SpamTest()
