# -*- coding: utf-8 -*-
"""
Created on Fri May 16 11:05:53 2014

@author: Jens Brauer
"""
import ctypes
from ctypes.util import find_library

dll = ctypes.CDLL(find_library('oldaapi64'))
#print(dll)
dll2 = ctypes.CDLL(find_library('OLMEM64'))
#dll2 = ctypes.CDLL(find_library('OLMEMSUP'))

def errcheck_all(ret, func, args):
    if ret:
        print("Error occured in"+ str(func))
        return
    
    return args

def errcheck_none(ret, func, args):
    if ret:
        print("Error occured in"+ str(func))
        print(ret)
        return

# ----------- Initialize ---------------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_ulong))
paramflags = (1, "name"), (2,'hDev')
olDaInitialize = prototype(("olDaInitialize", dll), paramflags)
olDaInitialize.errcheck = errcheck_all
# -----------END Initialize ---------------------------------

# ----------- olDaGetDASS ---------------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.c_long, ctypes.c_uint, ctypes.POINTER(ctypes.c_ulong))
paramflags = (1, "hDev"), (1,"SubsystemType"), (1,"uiElementNr"), (2,'adhandle')
olDaGetDASS = prototype(("olDaGetDASS",dll), paramflags)
olDaGetDASS.errcheck = errcheck_all
# ----------- olDaGetDASS ---------------------------------

# ----------- olDaSetDataFlow -----------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.c_uint)
paramflags = (1,"adhandle"),(1,"mode") # mode=OL_DF_SINGLEVALUE etc
olDaSetDataFlow = prototype(("olDaSetDataFlow",dll),paramflags)
olDaSetDataFlow.errcheck = errcheck_none
# ----------- olDaSetDataFlow -----------------------------

# ----------- olDaGetDataFlow -----------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.POINTER(ctypes.c_uint))
paramflags = (1,'adhandle'),(2,'flowval')
olDaGetDataFlow = prototype(("olDaGetDataFlow",dll), paramflags)
olDaGetDataFlow.errcheck = errcheck_all
# ----------- olDaGetDataFlow -----------------------------

# ----------- olDaConfig -----------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong)
paramflags = (1,'adhandle'),
olDaConfig = prototype(("olDaConfig",dll),paramflags)
olDaConfig.errcheck = errcheck_none
# ----------- olDaConfig -----------------------------

#------------olDaGetRange -------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
paramflags = (1,"ADDEV"),(2,"rmax"),(2,"rmin")
olDaGetRange = prototype(("olDaGetRange",dll), paramflags)
olDaGetRange.errcheck = errcheck_all
#------------olDaGetRange -------------------------

#------------olDaGetEncoding --------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.POINTER(ctypes.c_uint))
paramflags = (1,"ADDEV"),(2,"res")
olDaGetEncoding = prototype(("olDaGetEncoding",dll), paramflags)
olDaGetEncoding.errcheck = errcheck_all
#------------olDaGetEncoding --------------------------

#------------ olDaGetResolution -----------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.POINTER(ctypes.c_uint))
paramflags = (1,"ADDEV"),(2,"res")
olDaGetResolution = prototype(("olDaGetResolution",dll), paramflags)
olDaGetResolution.errcheck = errcheck_all
#------------ olDaGetResolution -----------------------

#------------ olDaGetSingleValue ----------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.POINTER(ctypes.c_long), ctypes.c_uint, ctypes.c_double)
paramflags = (1,"ADDEV"),(2,'Value'),(1,'Channel'),(1,'Gain')
olDaGetSingleValue = prototype(("olDaGetSingleValue",dll), paramflags)
olDaGetSingleValue.errcheck = errcheck_all
#------------ olDaGetSingleValue ----------------------

#------------ olDaPutSingleValue ----------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.c_long, ctypes.c_uint, ctypes.c_double)
paramflags = (1,"ADDEV"),(1,'Value'),(1,'Channel'),(1,'Gain')
olDaPutSingleValue = prototype(("olDaPutSingleValue",dll), paramflags)
olDaPutSingleValue.errcheck = errcheck_all
#------------ olDaGetSingleValue ----------------------

#------------olDaGetSingleFloat -------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.POINTER(ctypes.c_float), ctypes.c_uint, ctypes.c_double)
paaramflagst = (1,"ADDEV"),(2,'Value'),(1,'Channel'),(1,'Gain')
olDaGetSingleFloat = prototype(("olDaGetSingleFloat",dll), paramflags)
olDaGetSingleFloat.errcheck = errcheck_all
# -> error 26: Request not supported by this subsystem...
#------------olDaGetSingleFloat -------------------------

#------------olDaCodeToVolts --------------------------
#ECODE olDaCodeToVolts(DBL dfMinRangeVolts, DBL dfMaxRangeVolts, DBL dfGain, UINT uiBitsResolution, UINT uiEncoding, LNG lCode, PDBL pdfVoltage)
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_uint, ctypes.c_uint, ctypes.c_long, ctypes.POINTER(ctypes.c_double))
paramflags = (1,"minrange"),(1,"maxrange"),(1,"Gain"),(1,"Resolution"),(1,"Encoding"),(1,"Code"),(2,"Voltage")
olDaCodeToVolts = prototype(("olDaCodeToVolts",dll),paramflags)
olDaCodeToVolts.errcheck = errcheck_all
#------------olDaCodeToVolts --------------------------

#------------olDaVoltsToCode --------------------------
#ECODE olDaVoltsToCode(DBL dfMinRangeVolts, DBL dfMaxRangeVolts, DBL dfGain, UINT uiBitsResolution, UINT uiEncoding, DBL dfVoltage, PLNG plCode)
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_uint, ctypes.c_uint, ctypes.c_double, ctypes.POINTER(ctypes.c_long))
paramflags = (1,"minrange"),(1,"maxrange"),(1,"Gain"),(1,"Resolution"),(1,"Encoding"),(1,"Voltage"),(2,"Code")
olDaVoltsToCode = prototype(("olDaVoltsToCode",dll),paramflags)
olDaVoltsToCode.errcheck = errcheck_all
#------------olDaCodeToVolts --------------------------

HBUF = ctypes.c_void_p #HANDLE
PHBUF = ctypes.POINTER(ctypes.c_void_p)
PUINT = ctypes.POINTER(ctypes.c_int)
DWORD = ctypes.c_ulong
LPHBUF = ctypes.POINTER(HBUF)

#----------- olDaPutBuffer ----------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int,ctypes.c_ulong,HBUF)
paramflags =(1, "hDass"),(1, "hBuf")
olDaPutBuffer = prototype(("olDaPutBuffer", dll), paramflags)
olDaPutBuffer.errcheck = errcheck_none
#----------- olDaPutBuffer ----------------------------

#----------- olDaGetBuffer ----------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int,ctypes.c_ulong, PHBUF)
paramflags =(1, "hDass"),(2, "phBuf")
olDaGetBuffer = prototype(("olDaGetBuffer", dll), paramflags)
olDaGetBuffer.errcheck = errcheck_all
#----------- olDaGetBuffer ----------------------------

#----------- olDmCallocBuffer --------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_uint, ctypes.c_uint, DWORD, ctypes.c_uint, LPHBUF)
paramflags =(1, "uiWinFlags"),(1,"uiExFlags",0),(1, "numSamples"),(1,"uiSampleSize"),(2,"bufferhandle")
olDmCallocBuffer = prototype(("olDmCallocBuffer", dll2), paramflags)
olDmCallocBuffer.errcheck = errcheck_all
#----------- olDmCallocBuffer --------------------------

#----------- olDmgetValidSamples --------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, HBUF, ctypes.POINTER(DWORD))
paramflags =(1, "bufferhandle"),(2,"lpmax")
olDmGetValidSamples = prototype(("olDmGetValidSamples", dll2), paramflags)
olDmGetValidSamples.errcheck = errcheck_all
#----------- olDmgetValidSamples --------------------------

#----------- olDmGetBufferPtr  ----------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, HBUF, ctypes.POINTER(ctypes.c_void_p))
paramflags =(1, "bufferhandle"),(2,"lpBuffer")
olDmGetBufferPtr = prototype(("olDmGetBufferPtr", dll2), paramflags)
olDmGetBufferPtr.errcheck = errcheck_all
#----------- olDmGetBufferPtr  ----------------------------

#----------- olDmGetBufferECode  ----------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, HBUF, ctypes.POINTER(ctypes.c_int))
paramflags =(1, "bufferhandle"),(2,"lpecode")
olDmGetBufferECode = prototype(("olDmGetBufferECode", dll2), paramflags)
olDmGetBufferECode.errcheck = errcheck_all
#----------- olDmGetBufferECode  ----------------------------

#----------- olDmFreeBuffer  --------------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, HBUF)
paramflags =(1, "bufferhandle"),
olDmFreeBuffer = prototype(("olDmFreeBuffer", dll2), paramflags)
olDmFreeBuffer.errcheck = errcheck_none
#----------- olDmGetBufferECode  ----------------------------

#----------- olDmCopyFromBuffer  --------------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, HBUF,ctypes.POINTER(ctypes.c_void_p),ctypes.c_ulong)
paramflags =(1, "bufferhandle"),(2,"lpAppBuffer"),(1,"maxSamples")
olDmCopyFromBuffer = prototype(("olDmCopyFromBuffer", dll2), paramflags)
olDmCopyFromBuffer.errcheck = errcheck_all
#----------- olDmGetBufferECode  ----------------------------

#----------- olDaFlushBuffers   -----------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong)
paramflags =(1, "hDass"),
olDaFlushBuffers = prototype(("olDaFlushBuffers", dll), paramflags)
olDaFlushBuffers.errcheck = errcheck_none
#----------- olDaFlushBuffers   -----------------------------

#ECODE WINAPI olDmCopyFromBuffer(HBUF hBuf, LPVOID lpAppBuffer, ULNG ulMaxSamples);

#ECODE WINAPI olDmCallocBuffer (UINT, UINT, DWORD, UINT, LPHBUF);
#ECODE WINAPI olDmMallocBuffer (UINT, UINT, DWORD, LPHBUF);
#ECODE WINAPI olDmLockBuffer (HBUF);
#ECODE WINAPI olDmUnlockBuffer (HBUF);
#ECODE WINAPI olDmReCallocBuffer (UINT, UINT, DWORD, UINT, LPHBUF);
#ECODE WINAPI olDmReMallocBuffer (UINT, UINT, DWORD, LPHBUF);
#ECODE WINAPI olDmGetDataBits (HBUF, UINT FAR*);
#ECODE WINAPI olDmSetDataWidth (HBUF, UINT);
#ECODE WINAPI olDmGetDataWidth (HBUF, UINT FAR*);
#ECODE WINAPI olDmGetMaxSamples (HBUF, DWORD FAR*);
#ECODE WINAPI olDmSetValidSamples (HBUF, DWORD);
#ECODE WINAPI olDmGetValidSamples (HBUF, DWORD FAR*);
#ECODE WINAPI olDmGetBufferPtr (HBUF, LPVOID FAR*);
#ECODE WINAPI olDmGetBufferECode (HBUF, LPECODE);

#----------- olDaSetChannelListSize. ------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int,ctypes.c_ulong,ctypes.c_uint)
paramflags =(1, "hDass"),(1, "uiSize")
olDaSetChannelListSize = prototype(("olDaSetChannelListSize", dll), paramflags)
olDaSetChannelListSize.errcheck = errcheck_none
#----------- olDaSetChannelListSize. ------------------

#----------- olDaGetChannelListSize. ------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong,PUINT)
paramflags =(1, "hDass"),(2, "puiSize")
olDaGetChannelListSize = prototype(("olDaGetChannelListSize", dll), paramflags)
olDaGetChannelListSize.errcheck = errcheck_all
#----------- olDaGetChannelListSize. ------------------

#----------- olDaSetChannelListEntry ------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong,ctypes.c_uint,ctypes.c_uint)
paramflags =(1, "hDass"),(1, "uiEntry"),(1, "uiChan")
olDaSetChannelListEntry = prototype(("olDaSetChannelListEntry", dll), paramflags)
olDaSetChannelListEntry.errcheck = errcheck_none
#----------- olDaSetChannelListEntry ------------------

#----------- olDaGetChannelListEntry ------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong,ctypes.c_uint,PUINT)
paramflags =(1, "hDass"),(1, "uiEntry"),(2, "puiChan")
olDaGetChannelListEntry = prototype(("olDaGetChannelListEntry", dll), paramflags)
olDaGetChannelListEntry.errcheck = errcheck_all
#----------- olDaGetChannelListEntry ------------------

#----------- olDaSetGainListEntry ---------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong,ctypes.c_uint,ctypes.c_double)
paramflags =(1, "hDass"),(1, "uiEntry"),(1, "dGain")
olDaSetGainListEntry = prototype(("olDaSetGainListEntry", dll), paramflags)
olDaSetGainListEntry.errcheck = errcheck_none
#----------- olDaSetGainListEntry ---------------------

#----------- olDaGetGainListEntry ---------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong,ctypes.c_uint,ctypes.POINTER(ctypes.c_double))
paramflags =(1, "hDass"),(1, "uiEntry"),(2, "pdGain")
olDaGetGainListEntry = prototype(("olDaGetGainListEntry", dll), paramflags)
olDaGetGainListEntry.errcheck = errcheck_all
#----------- olDaGetGainListEntry ---------------------

#----------- olDaSetClockFrequency --------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong,ctypes.c_double)
paramflags =(1, "hDass"),(1, "dfFreq")
olDaSetClockFrequency = prototype(("olDaSetClockFrequency", dll), paramflags)
olDaSetClockFrequency.errcheck = errcheck_none
#----------- olDaSetClockFrequency --------------------

#----------- olDaGetClockFrequency --------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong,ctypes.POINTER(ctypes.c_double))
paramflags =(1, "hDass"),(2, "pdfFreq")
olDaGetClockFrequency = prototype(("olDaGetClockFrequency", dll), paramflags)
olDaGetClockFrequency.errcheck = errcheck_none
#----------- olDaGetClockFrequency --------------------

prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong,ctypes.c_uint)
paramflags =(1, "hDass"),(1, "uiWrapMode")
olDaSetWrapMode = prototype(("olDaSetWrapMode", dll), paramflags)
olDaSetWrapMode.errcheck = errcheck_none

#----------- olDaStart -------------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong)
paramflags =(1, "hDass"),
olDaStart = prototype(("olDaStart", dll), paramflags)
olDaStart.errcheck = errcheck_none
#----------- olDaStart -------------------------------

#----------- olDaStop. -------------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong)
paramflags =(1, "hDass"),
olDaStop = prototype(("olDaStop", dll), paramflags)
olDaStop.errcheck = errcheck_none
#----------- olDaStop. -------------------------------

#----------- olDaReleaseDASS -------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong)
paramflags =(1, "hDass"),
olDaReleaseDASS = prototype(("olDaReleaseDASS", dll), paramflags)
olDaReleaseDASS.errcheck = errcheck_none
#----------- olDaReleaseDASS -------------------------

#----------- olDaTerminate   -------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong)
paramflags =(1, "hDev"),
olDaTerminate  = prototype(("olDaTerminate", dll), paramflags)
olDaTerminate.errcheck = errcheck_none
#----------- olDaTerminate   -------------------------

#----------- olDaGetSSCaps   -------------------------
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong,ctypes.c_int,ctypes.POINTER(ctypes.c_uint))
paramflags =(1, "hDass"),(1, "OlSSc"),(2, "puiCap")
olDaGetSSCaps = prototype(("olDaGetSSCaps", dll), paramflags)
olDaGetSSCaps.errcheck = errcheck_all
#----------- olDaGetSSCaps   -------------------------

#Fehlt:
#olDmCallocBuffer
#olDmGetValidSamples
#olDmGetBufferPtr

# Notify Callback for olDaSetNotificationProcedure 
prototypeNotify = ctypes.WINFUNCTYPE(None, ctypes.c_uint, ctypes.c_ulong, ctypes.c_long)
def NotifyProc(uiMsg, wParam, lParam):
	print(uiMsg)
	print(wParam)
	print(lParam)
notifycallback = prototypeNotify(NotifyProc)

prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, prototypeNotify, ctypes.c_long)
paramflags =(1, "hDass"),(1,'pointer2fcn'),(1,'lparam')
olDaSetNotificationProcedure = prototype(('olDaSetNotificationProcedure',dll), paramflags)
olDaSetNotificationProcedure.errcheck = errcheck_none


# List Boards Callbacl
prototypeListBoards = ctypes.WINFUNCTYPE(None, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long)
def ListBoardsProc(boardname, drivername, lParam):
    print('Name = %s' % boardname)
    print('Drivername = %s' % drivername)
    print(lParam)
listboardscallback = prototypeListBoards(ListBoardsProc)

prototype = ctypes.WINFUNCTYPE(ctypes.c_int, prototypeListBoards, ctypes.c_long)
paramflags =(1,'pointer2fcn'),(1,'lparam')
olDaEnumBoards = prototype(('olDaEnumBoards',dll), paramflags)
olDaEnumBoards.errcheck = errcheck_none


#import matplotlib
#matplotlib.use('TkAgg')
#import matplotlib.pyplot as plt
#import numpy as np
#from time import sleep

#plt.ion() # set plot to animated
#plt.show()

##ydata = [0] * 1000
##ax1=plt.axes()
## make plot
##line, = plt.plot(ydata)
##plt.pause(0.0001)
##sleep(5)


# Notify Callback for olDaSetNotificationProcedure - new as a test for cintinious readout
prototypeNotifytest = ctypes.WINFUNCTYPE(None, ctypes.c_uint, ctypes.c_ulong, ctypes.c_long)
def NotifyProctest(uiMsg, wParam, lParam):
    print(uiMsg)
    if uiMsg == 1127:
        print('Buffer done ...get Data...')
        data = getData(lParam)
        #print(data )
        print(len(data[0]))
        plt.cla()
        plt.plot(data)
        #line.set_xdata(np.arange(len(data[0])))
        #line.set_ydata(data[0])  # update the data
        plt.draw() # update the plot
        plt.pause(0.0001)
        sleep(0.05)
    #print(wParam)
    #print(lParam)
notifycallbacktest = prototypeNotifytest(NotifyProctest)


def getData(sshandle):
    hbuffer = olDaGetBuffer(sshandle) #io create in DTOL_test_cont.py
    print(hbuffer)
    if( hbuffer ):
        data = []
        #/* get max samples in input buffer */
        samples = olDmGetValidSamples( hbuffer )
        print('Numer of samples %d' % samples)

        #/* get pointer to the buffer */
        buftmp = olDmGetBufferPtr( hbuffer)  #type int with adress
        print("Pointer buftemp:")
        print(buftmp)

        P = ctypes.POINTER(ctypes.c_ushort)
        p=ctypes.cast(buftmp,P)

        # Get all samples from buffer
        data.append(p[0:samples-1])

        #/* put buffer back to ready list */
        olDaPutBuffer(sshandle, hbuffer)

        return data