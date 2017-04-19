#!python27
# -*- coding: utf-8 -*-
'''
Created on April 19, 2017
PCA
Remove the mean
Compute the covariance matrix
Find the eigenvalues and eigenvectors of the covariance matrix
Sort the eigenvalues from largest to smallest
Take the top N eigenvectors
Transform the data into the new space created by the top N eigenvectors
'''
from numpy import *

def pca(dataMat, topNfeat=9999999):
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals #remove mean
    covMat = cov(meanRemoved, rowvar=0)
    eigVals,eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigVals)            #sort, sort goes smallest to largest
    eigValInd = eigValInd[:-(topNfeat+1):-1]  #cut off unwanted dimensions
    redEigVects = eigVects[:,eigValInd]       #reorganize eig vects largest to smallest
    lowDDataMat = meanRemoved * redEigVects#transform data into new dimensions
    return lowDDataMat
