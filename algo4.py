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
data = pd.read_excel("coba.xlsx")
label = data['label']
data = data.values.tolist()

default = "Tidak ada tweet"

def classifyEngine(data, default):
    if data is None:
        print(default)
    else:
        for i in range(len(data)):
            feature = []
            for j in range(1, 6):
                feature.append(data[i][j])
            feature = np.array(feature)
            pve = pv
            probFi = feature.prod() * pv
            
            