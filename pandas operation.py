# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:49:55 2023

@author: Sai Khairnar
"""

import pandas as pd
import numpy as np
#pandas library use for data manipulations

data = np.array([2,4,5,7])
s = pd.Series(data,index=['a','b','c','d'])
print(s)

#create series from dictionary
import pandas as pd
import numpy as np

data = {'a':0,'b':1,'c':2,'d':3}
s=pd.Series(data)
print(s)

#retrive last 3 elements

s=pd.Series((1,2,3,4,5,6),index=['a','b','c','d','e','f'])
print(s[-3:])

print(s[2:5])
print(s)
print(s['a'])
print(s[['a','b','c','d']])
print(s[0])
