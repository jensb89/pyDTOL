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
data = io.setupAiLiveview()
dataneu = []
print len(data)

for datai in data:
    for val in datai:
        dataneu.append(io.CodeToVolts(val))

plt.plot(np.linspace(0,10,len(dataneu)),dataneu)
plt.xlabel('Time / s')
plt.ylabel('Voltage / V')
plt.show()


