#!python27
#_*_ coding:utf-8 _*_
'''
SVD application
'''
from numpy import *
from numpy import linalg as la
import LoadData
#欧氏距离
def ecludSim(inA,inB):
    return 1.0/(1.0 + la.norm(inA - inB))
#皮尔逊相关系数
def pearsSim(inA,inB):
    if len(inA) < 3 : return 1.0
    return 0.5+0.5*corrcoef(inA, inB, rowvar = 0)[0][1]
#余弦相似度
def cosSim(inA,inB):
    num = float(inA.T*inB)
    denom = la.norm(inA)*la.norm(inB)
    return 0.5+0.5*(num/denom)
###基于物品相似度的推荐引擎
#给定相似度计算方法的情况下，用户对物品的估计评分
def standEst(dataMat, user, simMeas, item):
    """
    """
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0: continue
        #寻找两个用户都评级的物品集合
        overLap = nonzero(logical_and(dataMat[:,item].A>0, \
                                      dataMat[:,j].A>0))[0]
        if len(overLap) == 0: similarity = 0
        else: similarity = simMeas(dataMat[overLap,item], \
                                   dataMat[overLap,j])
        print 'the %d and %d similarity is: %f' % (item, j, similarity)
        #物品相似度 物品相似度*物品评分/物品总的相似度 加权平均
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal
#
def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=standEst):
    unratedItems = nonzero(dataMat[user,:].A==0)[1]#find unrated items
    if len(unratedItems) == 0: return 'you rated everything'
    itemScores = []
    for item in unratedItems:
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        itemScores.append((item, estimatedScore))
    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[:N]

#基于SVD的评分估计
def svdEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    U,Sigma,VT = la.svd(dataMat)
    print Sigma.shape

    Sig4 = mat(eye(4)*Sigma[:4]) #arrange Sig4 into a diagonal matrix
    print Sig4.shape
    print eye(4)
    print Sigma[:4].shape
    #矩阵*向量，先扩展向量为矩阵，后元素相乘法
    print eye(4)*Sigma[:4]
    xformedItems = dataMat.T * U[:,:4] * Sig4.I  #create transformed items
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0 or j==item: continue
        #采用U
        similarity = simMeas(xformedItems[item,:].T,\
                             xformedItems[j,:].T)
        #print 'the %d and %d similarity is: %f'%(item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal




def imgCompress(numSV=3, thresh=0.8):
    myMat = LoadData.loadData('0_5.txt')
    print "****original matrix******"
    printMat(myMat, thresh)
    U,Sigma,VT = la.svd(myMat)
    SigRecon = mat(zeros((numSV, numSV)))
    for k in range(numSV):#construct diagonal matrix from vector
        SigRecon[k,k] = Sigma[k]
    reconMat = U[:,:numSV]*SigRecon*VT[:numSV,:]
    print "****reconstructed matrix using %d singular values******" % numSV
    printMat(reconMat, thresh)
def printMat(inMat, thresh=0.8):
    for i in range(32):
        for k in range(32):
            if float(inMat[i,k]) > thresh:
                print 1,
            else: print 0,
        print ''

myMat = mat(LoadData.loadExData())
#print myMat
print recommend(myMat,2)[:2]

myMat = mat(LoadData.loadExData2())
#print myMat
print recommend(myMat,2)[:4]

myMat = mat(LoadData.loadExData2())
print recommend(myMat,2,estMethod = svdEst)[:4]
#imgCompress()
