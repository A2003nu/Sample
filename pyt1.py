#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:45:53 2024

@author: anusha
"""

import pandas as pd
df=pd.read_csv('/home/anusha/Desktop/train.csv')
probability_event=df['Survived'].value_counts()/len(df['Survived'])
print(probability_event)