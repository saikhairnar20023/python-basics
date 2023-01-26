# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:15:07 2023

@author: Sai khairnar
"""

from matplotlib import pyplot as plt
import numpy as np
import math

x=np.arange(0,math.pi*2,0.05)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sine')
plt.title('sine wave')
plt.show()

#basic plotting with numpy

from numpy import *
from pylab import *
x= linspace(-3,3,30)
y=sin(x)
plot(x,y)
plt.show()

x=linspace(-3,3,30)
y=sin(x)
plt.plot(x,y,'b.')
show()

#multiple plot command
from pylab import *
x=linspace(-5,5,50)
plot(x,sin(x))
plot(x,cos(x),'r.')
plot(x,-sin(x),'g--')
show()

from matplotlib import pyplot as plt
import numpy as np
import math

x=np.arange(0,math.pi*2,0.05)
y=np.sin(x)
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y)
plt.show()
















