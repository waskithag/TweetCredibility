#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 06:38:12 2019

@author: waskithag
"""
import pandas as pd
import numpy as np
from algo3 import *

matrix = pd.read_excel("matrixpairwise.xlsx", index_col = 0)
pv = pd.read_excel("pve.xlsx")
pv = pv.values.T.tolist()
data = pd.read_excel("coba2.xlsx")
label = data['label'].tolist()
data = data.values.tolist()
probLabel = np.zeros(2)

for i in range(len(label)):
    if (label[i] == 'Kredibel'):
        probLabel[0] += 1
    else:
        probLabel[1] += 1
        
probLabel = probLabel / np.sum(probLabel)

default = "Tidak ada tweet"
                
def classify(tweet):
    classify = np.zeros(2)
    feature = tweet[1:7]
    probFeat = feature.prod() * pve
    classify[0] = probFeat * probLabel[0]
    classify[1] = probFeat * probLabel[1]
    if classify[0] > classify[1]:
        return "Kredibel"
    else:
        return "Tidak Kredibel"