#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:06:29 2020

ya_fin.py

[David: Pandas Data Reader - How to get Yahoo Stock Data](youtube.com/watch?v=v66K_y3-ezY)<br>

@author: khafifa
"""

# deployment-flask/ya_fin.py
import pandas as pd
import pandas_datareader as dr
#%%
##%matplotlib inline
import matplotlib as plt
d=dr.data.get_data_yahoo('IBM', start='2020-01-30', end='2020-04-22')
d.head()
#%%
d.info()
d[['Open','Close']].plot(figsize=(15,5))
#%%
d.columns
#Index(['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'],
#%%
d['Volume'].plot()
#%%
