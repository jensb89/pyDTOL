# -*- coding: utf-8 -*-
"""
Created on Fri May 16 10:20:40 2014

@author: Jens Brauer
"""

import ctypes
#import numpy
#from string import atoi
from time import sleep
from DTOL_defs import *
from DTOL_prototypes import *


class DTOL:
    """ Data Translation DtOLWrapper Class """
    def __init__(self, name=b'DT9836(00)'):
        self.name = name
        self.data = []
        self.sshandle = []
        self.hdev = []
        self.range = (-10,10)
        self.rmin = ctypes.c_double(-10)
        self.rmax = ctypes.c_double(10)
        self.gain = ctypes.c_double(1)
        self.res = ctypes.c_uint(16)
        self.enc = ctypes.c_uint(OL_ENC_BINARY)
        self.val = 0
        
    def Initialize(self, name):
        #print('Available Boards:')
        #olDaEnumBoards(listboardscallback, 0)
        #print('-----')
        print('Initializing: ' + name)
        hdev = olDaInitialize(name)
        #hdev = args
        self.hdev = hdev
        return hdev
    
    def GetSubsystem(self, subsystem_code, elemNum):
        sshandle = olDaGetDASS(self.hdev, subsystem_code, elemNum)
        #print(args)
        #sshandle = args[3]
        self.sshandle = sshandle
        return sshandle
    
    def SetDataFlow(self, flowvar):
        #print(type(self.sshandle))
        olDaSetDataFlow(self.sshandle, flowvar)
        
    def GetDataFlow(self):
        flow = olDaGetDataFlow(self.sshandle)
        return flow

    def setClockFrequency(self, freq):
        olDaSetClockFrequency(self.sshandle,freq)

    def getClockFrequency(self):
        freq = olDaGetClockFrequency(self.sshandle)
        return freq
    
    def olDaConfig(self):
        olDaConfig(self.sshandle)
    
    def getRange(self):
        args=olDaGetRange(self.sshandle)
        #print(args)
        rmax = args[0]
        rmin = args[1]
        self.rmax = rmax
        self.rmin = rmin
        return rmax, rmin
    
    def getEncoding(self):
        enc=olDaGetEncoding(self.sshandle)
        self.enc = enc
        return enc
    
    def getResolution(self):
        res = olDaGetResolution(self.sshandle)
        self.res = res
        return res
    
    def getSingleValue(self,channel=0, gain=ctypes.c_double(1)):
        val = olDaGetSingleValue(self.sshandle, ctypes.c_uint(channel), gain)
        #val = args[1]
        val_voltage = self.CodeToVolts(val)
        #self.val = val_voltage
        return val, val_voltage

    def setSingleValue(self,value,channel=0, gain=ctypes.c_double(1)):
        value_code = self.VoltsToCode(value)
        olDaPutSingleValue(self.sshandle, value_code, ctypes.c_uint(channel), gain)
        #val = args[1]
        #val_voltage = self.CodeToVolts(val)
        #self.val = val_voltage
        #return val

    def setWrapMode(self, mode):
        olDaSetWrapMode(self.sshandle, mode)

    def setChannelListSize(self, size):
        olDaSetChannelListSize(self.sshandle, size)

    def setChannelListEntry(self, entry, channel):
        olDaSetChannelListEntry(self.sshandle, entry, channel)

    def setGainListEntry(self, entry, gain):
        olDaSetGainListEntry(self,sshandle, entry, gain)
    
    def CodeToVolts(self, val, rmin=None,rmax=None, gain=None, res=None, enc=None):
        if rmin is None:
            rmin = self.rmin
        if rmax is None:
            rmax = self.rmax
        if gain is None:
            gain = self.gain
        if res is None:
            res = self.res
        if enc is None:
            enc = self.enc
        val = olDaCodeToVolts(rmin, rmax, gain, res, enc, val)
        return val #voltage number

    def VoltsToCode(self, val, rmin=None,rmax=None, gain=None, res=None, enc=None):
        if rmin is None:
            rmin = self.rmin
        if rmax is None:
            rmax = self.rmax
        if gain is None:
            gain = self.gain
        if res is None:
            res = self.res
        if enc is None:
            enc = self.enc
        val = olDaVoltsToCode(rmin, rmax, gain, res, enc, val)
        return val #Code number

    def start(self):
        olDaStart(self.sshandle)
        print('Starting...')

    def stop(self):
        olDaStop(self.sshandle) 
    
    def setupGetSingleValue(self):
        self.Initialize(self.name)
        self.GetSubsystem(OLSS_AD, ctypes.c_ulong(0))
        self.SetDataFlow(OL_DF_SINGLEVALUE)
        self.olDaConfig()
        self.getRange()
        self.getEncoding()
        self.getResolution()

    def setupSetSingleValue(self):
        self.Initialize(self.name)
        self.GetSubsystem(OLSS_DA, ctypes.c_ulong(0))
        self.SetDataFlow(OL_DF_SINGLEVALUE)
        self.olDaConfig()
        self.getRange()
        self.getEncoding()
        self.getResolution()

    def closeConnection(self):
        olDaReleaseDASS(self.sshandle)
        olDaTerminate(self.hdev)

    def setupAiLiveview(self):
        NUM_BUFFERS = 10
        channel = 0
        print('Available Boards:')
        olDaEnumBoards(listboardscallback, 0)
        print('-----')
        self.Initialize(self.name)
        self.GetSubsystem(OLSS_AD, ctypes.c_ulong(0))
        self.SetDataFlow(OL_DF_CONTINUOUS)
        #dma  = min (1, dma)            #/* try for one dma channel   */ 
        #freq = min (1000.0, freq)      #/* try for 1000hz throughput */
        dma = 1
        freq = 1000
        #self.setDMAUsage(1)
        olDaSetNotificationProcedure(self.sshandle, notifycallback, self.sshandle) #notifycallback für plotting tests (siehe in DTOL_prototypes)
        #self.olDaSetNotificationProcedure(self.sshandle,lpfnNotifyProc,lparam) #???, The procedure address lpfnNotifyProc can be set to null to disable notification. 
        self.setWrapMode(OL_WRP_NONE) #In continuous acquisition (including post-trigger, pre-trigger, and about-trigger), you can specify the wrap mode as none (allocated buffers are filled – or emptied for DACs – and operation stops), single (continuously reuses one buffer), or multiple (continuously uses multiple buffers).
        self.setClockFrequency(freq)
        self.setChannelListSize(1)
        self.setChannelListEntry(0,channel)
        #self.setGainListEntry(0,gain)
        self.olDaConfig()
        size = freq/1    #/* 1 second buffer */
        res = self.getResolution()
        self.getEncoding()
        self.getRange()
        if res > 16:
            samplesize = 4 #e.g. 24 bits = 4 btyes
        else:
            samplesize = 2 #e.g. 16 or 12 bits = 2 bytes
            
        for i in range(NUM_BUFFERS):
            hBuffer = olDmCallocBuffer(0,0,size,samplesize);
            olDaPutBuffer(self.sshandle, hBuffer);
        
        self.start()
        sleep(30)
        data = []
        ret = olDaGetSSCaps(self.sshandle,OLSSC_SUP_CONTINUOUS)
        print('OLSSC_SUP_CONTINUOUS')
        print(ret)
        for i in range(NUM_BUFFERS):
            print('i= ' + str(i))
            hbuffer = olDaGetBuffer(self.sshandle)
            #hbuffer = 0
            print(hbuffer)
            if( hbuffer ):
                data_tmp = []
                print(hbuffer)
                #/* get max samples in input buffer */
                samples = olDmGetValidSamples( hbuffer )
                print(samples)

                #/* get pointer to the buffer */
                if (res > 16): #type=PDWORD (ulong)
                    print(res)
                    buftmp = olDmGetBufferPtr( hbuffer)
                    print(buftmp)
                    sleep(0.01)
                    #/* get last sample in buffer */
                    value = buftmp[samples-1]
                    print('Last Val:')
                    print(value)
                    print(buftmp)
                else: #type=PWORD (ushort=Ganze 16-Bit-Zahl ohne Vorzeichen)
                    print(res)
                    buftmp = olDmGetBufferPtr( hbuffer)  #type int with adress
                    print(buftmp)
                    sleep(0.01)
                    print(type(buftmp))
                    #test = olDmCopyFromBuffer(hbuffer,samples)
                    #print(test)
                    #test = ctypes.c_double(42)
                    #testptr = ctypes.pointer(test)
                    #print(testptr)
                    #print(testptr[0])
                    P = ctypes.POINTER(ctypes.c_ushort)
                    #p = P.from_address(buftmp)
                    p=ctypes.cast(buftmp,P)
                    print(ctypes.addressof(p))
                    print(p)
                    print(p[0])
                    val = self.CodeToVolts(p[0])
                    print(val)
                    print(self.rmin)
                    print(self.enc)
                    print(OL_ENC_BINARY)
                    print((self.rmax-self.rmin)/2**res*p[0]+self.rmin)
                    print(p[1])
                    val = self.CodeToVolts(p[1])
                    print(val)
                    print(p.contents)

                    #/* get last sample in buffer */
                    #value = p[samples-1]
                    #print(value)
                    print(p[samples-1])
                    data.append(p[0:samples-1])
                    #data.append(data_tmp)
                    #print(data)
                #/* put buffer back to ready list */
                olDaPutBuffer(self.sshandle, hbuffer)

        # Delete Buffers
        #sleep(5)
        print('Freeing of buffers...')
        olDaFlushBuffers(self.sshandle)
        for i in range(NUM_BUFFERS):
            hbuffer = olDaGetBuffer(self.sshandle)
            print(hbuffer)
            if not(hbuffer == None):
                print('Free Buffer')
                olDmFreeBuffer(hbuffer)
    
        # Close Connection
        olDaReleaseDASS(self.sshandle)
        olDaTerminate(self.hdev)
        return data

if __name__ == "__main__":
    print("Usage: io=DTOL('DT9836(01)')")
    print("io.setupSingleValue()")
    print("io.getSingleValue()")
    io = DTOL()
    io.setupGetSingleValue()
    print(io.getSingleValue())
        
    
