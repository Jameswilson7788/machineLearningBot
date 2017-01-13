# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 10:10:41 2017

@author: wesst
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[: ,:-1].values
Y = dataset.iloc[: ,3].values