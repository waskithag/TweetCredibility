#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 13:39:33 2019

@author: waskithag
"""

import pandas as pd
import numpy as np

matrix = pd.read_excel("matrixpairwise.xlsx", index_col = 0)
dataa = matrix.values.tolist()
sum = []
geom = []

def featureRank(matrix):
    for i in range(len(matrix)):
        temp = 0
        for j in range(6):
            temp += matrix.iloc[j, i]
        sum.append(temp)
    for i in range(len(matrix)):
        for j in range(6):
            matrix.iloc[j, i] = matrix.iloc[j, i]/sum[i]
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
    return temp2
    
    
x = featureRank(matrix)