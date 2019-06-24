#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:14:28 2019

@author: waskithag
"""

import pandas as pd
import numpy as np

matrix = pd.read_excel("matrixpairwise.xlsx", index_col = 0)
#matrix = matrix.values.tolist()
sum = []
geom = []
normMatrix = []

def featureRank(matrix):
    for i in range(len(matrix)):
        temp = 0
        for j in range(6):
            temp += matrix.iloc[j, i]
        sum.append(temp)
    for i in range(len(matrix)):
        for j in range(6):
            matrix.iloc[j, i] = matrix.iloc[j, i]/sum[i]
    normMatrix = matrix.values.tolist()
    geomtemp = matrix.values.T.tolist()
    geomtemp1 = []
    geomtemp2 = []
    for i in range(6):
        temp1 = np.array(geomtemp[i])
        a = temp1.prod()
        geomtemp1.append(a**(1/len(temp1)))
        geomtemp2.append(a)
    temp2 = []
    for i in range(6):
        a = (geomtemp1[i]/np.array(geomtemp2).sum())**(1/6)
        temp2.append(a)
    return temp2, normMatrix
    
x, normMatrix = featureRank(matrix)

pv = pd.read_excel("pve.xlsx")
pv = pv.values.T.tolist()

eigen = []

def calcEigenMax(normMatrix):
    for i in range(len(normMatrix)):
        temp = 0
        for j in range(6):
            temp += normMatrix[i][j]
        temp = temp/len(normMatrix)
        eigen.append(temp)
    temp = 0
    for i in range(len(normMatrix)):
        temp += sum[i] * eigen[i]
    return temp
        
eigenMax = calcEigenMax(normMatrix)
            
matrix = matrix.values.tolist()

def checkConsistency(matrix):
    RI = 1.24
    v = np.dot(matrix, pv)
    m = len(v)
    lambdaMax = eigenMax
    CI = (lambdaMax - m) / (m - 1)
    CR = CI / RI
    if (CR > 0.1):
        return False
    else:
        return True
    
tes = checkConsistency(matrix)



    
    