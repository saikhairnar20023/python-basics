# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:26:11 2023

@author: Sai Khairnar
"""

import numpy as np
a= np.array([1,2,3,4,5,6,7],dtype=(complex))
print(a)

#shape attributes
a=np.array([[1,2,3],[4,5,6]])
print(a.shape)
print(a)

#reshape atributes i.e 3 rows, 2 columns
a=np.array([[1,2,3],[4,5,6]])
print(a.reshape(3,2))
print(a)


