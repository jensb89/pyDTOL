# -*- coding: utf-8 -*-
"""
Created on Fri May 16 14:15:43 2014

@author: Jens Brauer
"""
from __future__ import unicode_literals
from DTOL import DTOL
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
from time import time
import ctypes

#card = bytes(str('DT9836(00)'), 'ascii')
io = DTOL(name='DT9836(00)')
io.setupSetSingleValue()

print('Setting Value:')
err=io.setSingleValue(6.3,channel=1)

print('Waiting 5sek...')
print(err)
sleep(1)

#io.setupGetSingleValue()
#val=io.getSingleValue(channel=0)
#print(val)


#SCANNING
#==================================#
start_time = time()
x=np.linspace(4.95,5.15,1000)
y=np.linspace(6.6,6.8,80)
xv, yv =np.meshgrid(x, y) 
N = len(y)

for i in y:
	io.setSingleValue(i,channel=0)
	for k in x:
		io.setSingleValue(k,channel=1)
		#data = getdatafromcamera()
		#applylockin(data)
		sleep(0.003)
	sleep(0.1)
	print(i)
print("--- %s seconds ---" % (time() - start_time))



#plt.plot(np.linspace(0,elapsed,len(data)),data)
#plt.xlabel('Time / s')
#plt.ylabel('Voltage / V')
#plt.show()

io.closeConnection()


