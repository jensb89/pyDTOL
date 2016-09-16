# -*- coding: utf-8 -*-
"""
Created on Fri May 16 14:15:43 2014

@author: Jens Brauer
"""

from DTOL import DTOL
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
from time import time


io = DTOL(name='DT9836(00)')
io.setupGetSingleValue()

data = []

t = time()
for i in range(100):
    data.append(io.getSingleValue()[1])
    sleep(0.001)

elapsed = time() - t

plt.plot(np.linspace(0,elapsed,len(data)),data)
plt.xlabel('Time / s')
plt.ylabel('Voltage / V')
plt.show()


