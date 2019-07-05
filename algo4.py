#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 06:38:12 2019

@author: waskithag
"""
import pandas as pd
import numpy as np
#from algo3 import *
import math

def calcMeanStdev(a):
    y = np.mean(a)
    z = np.std(a)
    return y, z

def gaussForm(probvec, feature, stdev, mean, label):
    gauss = np.zeros(6)
    for i in range(len(feature)):
       gauss[i] = (1/(stdev[i] * math.sqrt(2 * 3.14)) * math.exp(-((feature[i] - mean[i])**2) / (2 * (stdev[i])**2)))
#    gauss = np.dot(gauss, probvec)
    prob = gauss.prod() * label  
    return prob

def klasifikasi(tweet, modelYa, modelTidak, probLabel):
    classify = np.zeros(2)
    feature = tweet[1:7]
    classify[0] = gaussForm(pv, feature, modelYa[0], modelYa[1], probLabel[0])
    classify[1] = gaussForm(pv, feature, modelTidak[0], modelTidak[1], probLabel[1])
    if classify[0] > classify[1]:
        return "Kredibel"
    else:
        return "Tidak Kredibel"

def trainModel(data):
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
    
    meanStdevTidak = np.zeros((2, 6))
    meanStdevYa = np.zeros((2, 6))
    
    for i in range(1, 7):
        meanStdevYa[0][i - 1], meanStdevYa[1][i - 1] = calcMeanStdev(dataIya[i])
        meanStdevTidak[0][i - 1], meanStdevTidak[1][i - 1] = calcMeanStdev(dataTidak[i])
    
    return probLabel, meanStdevYa, meanStdevTidak

def precRecall(real, predict, P, N):
    TP, FP, FN, TN = 0, 0, 0, 0
    
    for i in range(len(real)):
        if (real[i] == P):
            if (predict[i] == P):
                TP += 1
            else:
                FN += 1
        elif (real[i] == N):
            if (predict[i] == P):
                FP += 1
            else:
                TN += 1
    
    precision = (TP / (TP + FP)) * 100
    recall = (TP / (TP + FN)) * 100
    acc = ((TP + TN) / len(real)) * 100
    
    return precision, recall, acc
                
def kFold(data, fold):
    newLen = len(data) // fold
    chunk = []
    start = 0
    for i in range(fold):
        chunk.append(data[start : (start + newLen)])
        start += newLen
    
    start = 0
    for i in range(fold):
        print("K-Fold : ", i)
        validate = chunk[i]
        train = data[:start] + data[(start + newLen):]
        probLabel, modelYa, modelTidak = trainModel(train)
        labelVal, labelPredict = [], []
        for j in range(len(validate)):
            labelVal.append(validate[j][7])
            labelPredict.append(klasifikasi(validate[j], modelYa, modelTidak, probLabel))
        prec, rec, acc = precRecall(labelVal, labelPredict, "Kredibel", "Tidak Kredibel")
        print("Precision : ", prec)
        print("Recall : ", rec)
        print("Accuration : ", acc, "\n")
        
        
        
    

matrix = pd.read_excel("matrixpairwise.xlsx", index_col = 0)
pv = pd.read_excel("pve.xlsx")
pv = pv.values.T.tolist()
data = pd.read_excel("coba2.xlsx")
data = data.values.tolist()  


kFold(data, 5)
