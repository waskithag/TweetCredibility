#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 06:38:12 2019

@author: waskithag
"""
import pandas as pd
import numpy as np
from algo3 import *
from math import *

matrix = pd.read_excel("matrixpairwise.xlsx", index_col = 0)
pv = pd.read_excel("pve.xlsx")
pv = pv.values.T.tolist()
data = pd.read_excel("coba2.xlsx")
data = data.values.tolist()
probLabel = np.zeros(2)
dataTidak = []
dataIya = []

for i in range(len(data)):
    if (data[i][7] == 'Kredibel'):
        probLabel[0] += 1
        dataIya.append(data[i])
    else:
        probLabel[1] += 1
        dataTidak.append(data[i])


dataIya = list(map(list, zip(*dataIya)))
dataTidak = list(map(list, zip(*dataTidak)))
        
probLabel = probLabel / np.sum(probLabel)

def calcMeanStdev(a):
    y = np.mean(a)
    z = np.std(a)
    return y, z

meanStdevTidak = np.zeros((2, 6))
meanStdevYa = np.zeros((2, 6))

for i in range(1, 7):
    meanStdevYa[0][i - 1], meanStdevYa[1][i - 1] = calcMeanStdev(dataIya[i])
    meanStdevTidak[0][i - 1], meanStdevTidak[1][i - 1] = calcMeanStdev(dataTidak[i])
    
def gaussForm(probvec, feature, stdev, mean, label):
    gauss = np.zeros(6)
    for i in range(len(feature)):
       gauss[i] += (1/stdev[i] * sqrt(2 * 3.14)) * exp(-0.5 * pow((feature[i] - mean[i]),2)/(pow(stdev[i], 2)))
#    feature = np.dot(feature, probvec)
    prob = gauss.prod() * label  
    return prob

def klasifikasi(tweet):
    classify = np.zeros(2)
    feature = tweet[1:7]
    classify[0] = gaussForm(pv, feature, meanStdevYa[0], meanStdevYa[1], probLabel[0])
    classify[1] = gaussForm(pv, feature, meanStdevTidak[0], meanStdevTidak[1], probLabel[1])
    print(classify[0])
    print(classify[1])
    if classify[0] > classify[1]:
        return "Kredibel"
    else:
        return "Tidak Kredibel"
    

for i in range(10):
    print('iterasi : ', i) 
    print(klasifikasi(data[i]))

