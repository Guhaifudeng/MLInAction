#!python27
# _*_ coding:utf-8 _*_
import LoadData
import PrepareData
import NaiveBayesianModel
from numpy import *
def testingNB():
    listOPosts,listClasses = LoadData.loadDataSet()
    myVocabList = PrepareData.createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(PrepareData.setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = NaiveBayesianModel.trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(PrepareData.setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',NaiveBayesianModel.classifyNB(thisDoc,p0V,p1V,pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(PrepareData.setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',NaiveBayesianModel.classifyNB(thisDoc,p0V,p1V,pAb)
testingNB()
