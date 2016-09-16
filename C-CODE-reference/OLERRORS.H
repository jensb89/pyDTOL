#ifndef _OLERRORS_              
#define _OLERRORS_        // Include error codes if not already included

/*-----------------------------------------------------------------------

FILE NAME: olerrors.h

ABSTRACT:

   This unit contains Error code declarations for the 
   Open Layers Data Acquisition and Memory Manager


---------------------------------------------------------------------------*/


#ifndef OLIWBASE
	#define OLIWBASE                    ((ECODE)0)
#endif

#define OLNOERROR                   OLIWBASE     // No Error
#define OLSUCCESS                   OLIWBASE     // No Error
#define OLBADCAP                    OLIWBASE+1   // Invalid capability specified
#define OLBADELEMENT                OLIWBASE+2   // Invalid element specified
#define OLBADSUBSYSTEM              OLIWBASE+3   // Invalid subsystem specified
#define OLNOTENOUGHDMACHANS         OLIWBASE+4   // Not Enough DMA Channels
#define OLBADLISTSIZE               OLIWBASE+5   // Invalid List Size
#define OLBADLISTENTRY              OLIWBASE+6   // Invalid List Entry
#define OLBADCHANNEL                OLIWBASE+7   // Invalid Channel
#define OLBADCHANNELTYPE            OLIWBASE+8   // Invalid Channel Type
#define OLBADENCODING               OLIWBASE+9   // Invalid Encoding
#define OLBADTRIGGER                OLIWBASE+10  // Invalid Trigger
#define OLBADRESOLUTION             OLIWBASE+11  // Invalid Resolution
#define OLBADCLOCKSOURCE            OLIWBASE+12  // Invalid Clock source
#define OLBADFREQUENCY              OLIWBASE+13  // Invalid Frequency  
#define OLBADPULSETYPE              OLIWBASE+14  // Invalid Pulse Type
#define OLBADPULSEWIDTH             OLIWBASE+15  // Invalid Pulse Width
#define OLBADCOUNTERMODE            OLIWBASE+16  // Invalid Counter Mode
#define OLBADCASCADEMODE            OLIWBASE+17  // Invalid Cascade Mode
#define OLBADDATAFLOW               OLIWBASE+18  // Invalid Data Flow
#define OLBADWINDOWHANDLE           OLIWBASE+19  // Invalid Window Handle
#define OLSUBSYSINUSE               OLIWBASE+20  // Subsystem in use
#define OLSUBSYSNOTINUSE            OLIWBASE+21  // Subsystem not in use
#define OLALREADYRUNNING            OLIWBASE+22  // Subsystem already running
#define OLNOCHANNELLIST             OLIWBASE+23  // No channel list
#define OLNOGAINLIST                OLIWBASE+24  // No gain list
#define OLNOFILTERLIST              OLIWBASE+25  // No filter list
#define OLNOTCONFIGURED             OLIWBASE+26  // Subsystem Not configured
#define OLDATAFLOWMISMATCH          OLIWBASE+27  // Data flow mismatch
#define OLNOTRUNNING                OLIWBASE+28  // Subsystem not running
#define OLBADRANGE                  OLIWBASE+29  // Invalid Range
#define OLBADSSCAP                  OLIWBASE+30  // Invalid Subsystem Capability
#define OLBADDEVCAP                 OLIWBASE+31  // Invalid Device Capability
#define OLBADRANGEINDEX             OLIWBASE+32  // Invalid Range Index
#define OLBADFILTERINDEX            OLIWBASE+33  // Invalid Filter Index
#define OLBADGAININDEX              OLIWBASE+34  // Invalid Gain Index
#define OLBADWRAPMODE               OLIWBASE+35  // Invalid Wrap Mode
#define OLNOTSUPPORTED              OLIWBASE+36  // Not Supported
#define OLBADDIVIDER                OLIWBASE+37  // Invalid Divider Value
#define OLBADGATE                   OLIWBASE+38  // Invalid Gate

#define OLBADDEVHANDLE              OLIWBASE+39  // Invalid Device Handle
#define OLBADSSHANDLE               OLIWBASE+40  // Invalid Subsystem Handle
#define OLCANNOTALLOCDASS           OLIWBASE+41  // Cannot allocate DASS
#define OLCANNOTDEALLOCDASS         OLIWBASE+42  // Cannot Deallocate DASS
#define OLBUFFERSLEFT               OLIWBASE+43  // Transfer list not empty

#define OLBOARDRUNNING              OLIWBASE+44  // Another Subsystem on board is already running 
#define OLINVALIDCHANNELLIST        OLIWBASE+45  // Channel list has been filled incorrectly
#define OLINVALIDCLKTRIGCOMBO       OLIWBASE+46  // Selected clock & trigger source may not be used together
#define OLCANNOTALLOCLUSERDATA      OLIWBASE+47  // Driver could not allocate needed memory 

#define OLCANTSVTRIGSCAN            OLIWBASE+48  // Triggered Scan not available in single value mode 
#define OLCANTSVEXTCLOCK            OLIWBASE+49  // External Clock is not available in single value mode
#define OLBADRESOLUTIONINDEX        OLIWBASE+50  // Bad Resolution Selected

#define OLADTRIGERR                 OLIWBASE+60  // A/D Trigger Error
#define OLADOVRRN                   OLIWBASE+61  // A/D Overrun Error
#define OLDATRIGERR                 OLIWBASE+62  // D/A Trigger Error
#define OLDAUNDRRN                  OLIWBASE+63  // D/A Underrun Error
   
#define OLNOREADYBUFFERS            OLIWBASE+64  // No Ready Buffers

#define OLBADCPU                    OLIWBASE+65  // Library Requires i386 or i486
#define OLBADWINMODE                OLIWBASE+66  // Library Requires Windows 3.x Enhanced mode
#define OLCANNOTOPENDRIVER          OLIWBASE+67  // Driver cannot be initialized
#define OLBADENUMCAP                OLIWBASE+68  // Cannot enumerate this capability
#define OLBADDASSPROC               OLIWBASE+69  // Dass Proc CallBack NUL
#define OLBADENUMPROC               OLIWBASE+70  // Enum Proc CallBack NULL
#define OLNOWINDOWHANDLE            OLIWBASE+71  // No Window Handle
#define OLCANTCASCADE               OLIWBASE+72  // Subsystem cannot be cascaded  

#define OLINVALIDCONFIGURATION      OLIWBASE+73  // Invalid configuration in SYSTEM.INI
#define OLCANNOTALLOCJUMPERS        OLIWBASE+74  // Cannot allocate memory for jumpers
#define OLCANNOTALLOCCHANNELLIST    OLIWBASE+75  // Cannot allocate channel list
#define OLCANNOTALLOCGAINLIST       OLIWBASE+76  // Cannot allocate gain list
#define OLCANNOTALLOCFILTERLIST     OLIWBASE+77  // Cannot allocate filter list
#define OLNOBOARDSINSTALLED         OLIWBASE+78  // No DT-Open Layers boards installed
#define OLINVALIDDMASCANCOMBO       OLIWBASE+79  // Invalid DMA / Scan combination
#define OLINVALIDPULSETYPE          OLIWBASE+80  // Invalid pulse type
#define OLINVALIDGAINLIST           OLIWBASE+81  // Invalid gain list
#define OLWRONGCOUNTERMODE          OLIWBASE+82  // Wrong counter mode
#define OLLPSTRNULL                 OLIWBASE+83  // LPSTR passed as a parameter was NULL
#define OLINVALIDPIODFCOMBO         OLIWBASE+84  // Invalid Polled I/O combination
#define OLINVALIDSCANTRIGCOMBO      OLIWBASE+85  // Invalid Scan / Trigger combo
#define OLBADGAIN                   OLIWBASE+86  // Invalid Gain
#define OLNOMEASURENOTIFY           OLIWBASE+87  // No window handle specified for frequency measurement
#define OLBADCOUNTDURATION          OLIWBASE+88  // Invalid count duration for frequency measurement
#define OLBADQUEUE                  OLIWBASE+89  // Invalid queue type specified
#define OLBADRETRIGGERRATE          OLIWBASE+90  // Invalid Retrigger Rate for channel list size
#define OLCOMMANDTIMEOUT            OLIWBASE+91  // No Command Response from Hardware
#define OLCOMMANDOVERRUN            OLIWBASE+92  // Hardware Command Sequence Error
#define OLDATAOVERRUN               OLIWBASE+93  // Hardware Data Sequence Error

#define OLCANNOTALLOCTIMERDATA      OLIWBASE+94  // Cannot allocate timer data for driver 
#define OLBADHTIMER                 OLIWBASE+95  // Invalid Timer handle
#define OLBADTIMERMODE              OLIWBASE+96  // Invalid Timer mode
#define OLBADTIMERFREQUENCY         OLIWBASE+97  // Invalid Timer frequency
#define OLBADTIMERPROC              OLIWBASE+98  // Invalid Timer callback procedure
#define OLBADDMABUFFERSIZE          OLIWBASE+99  // Invalid Timer DMA buffer size

#define OLBADDIGITALIOLISTVALUE     OLIWBASE+100 // Illegal synchronous digital I/O value requested.
#define OLCANNOTALLOCSSLIST         OLIWBASE+101 // Cannot allocate simultaneous start list
#define OLBADSSLISTHANDLE           OLIWBASE+102 // Illegal simultaneous start list handle specified.
#define OLBADSSHANDLEONLIST         OLIWBASE+103 // Invalid subsystem handle on simultaneous start list.
#define OLNOSSHANDLEONLIST          OLIWBASE+104 // No subsystem handles on simultaneous start list.
#define OLNOCHANNELINHIBITLIST      OLIWBASE+105 // The subsystem has no channel inhibit list.
#define OLNODIGITALIOLIST           OLIWBASE+106 // The subsystem has no digital I/O list.
#define OLNOTPRESTARTED             OLIWBASE+107 // The subsystem has not been prestarted.
#define OLBADNOTIFYPROC             OLIWBASE+108 // Invalid notification procedure
#define OLBADTRANSFERCOUNT          OLIWBASE+109 // Invalid DT-Connect transfer count
#define OLBADTRANSFERSIZE           OLIWBASE+110 // Invalid DT-Connect transfer size
#define OLCANNOTALLOCINHIBITLIST    OLIWBASE+111 // Cannot allocate channel inhibit list
#define OLCANNOTALLOCDIGITALIOLIST  OLIWBASE+112 // Cannot allocate digital I/O list
#define OLINVALIDINHIBITLIST        OLIWBASE+113 // Channel inhibit list has been filled incorrectly
#define OLSSHANDLEALREADYONLIST     OLIWBASE+114 // Dass handle is already on simultaneous start list 
#define OLCANNOTALLOCRANGELIST      OLIWBASE+115 // Cannot allocate range list
#define OLNORANGELIST               OLIWBASE+116 // No range list
#define OLNOBUFFERINPROCESS         OLIWBASE+117 // No buffers in process
#define OLREQUIREDSUBSYSINUSE       OLIWBASE+118 // Additional required sub system in use
#define OLWRAPMODEMISMATCH          OLIWBASE+119 // Wrap mode mismatch
#define OLVXDNOTINSTALLED           OLIWBASE+120 // VDTDAD virtual device driver not loaded
#define OLBADRETRIGGERMODE          OLIWBASE+121 // Invalid Retrigger Mode
#define OLBADCOUNT                  OLIWBASE+122 // Invalid count.  Count exceeds maximum # of scans of the CGL. 
#define OLBADRETRIGGER              OLIWBASE+123 // Invalid Retrigger
#define OLBADPRETRIGGER             OLIWBASE+124 // Invalid Pretrigger

#define OLGENERALFAILURE            OLIWBASE+125 // General Failure
#define OLREQUESTPENDING            OLIWBASE+126 // Defer Completion of Open Layers call
#define OLUNSUPPORTEDSYSTEM         OLIWBASE+127 // Operating System not supported
#define OLBADEDGE					OLIWBASE+128 // Invalid counter edge specified
#define OLHALFCTR					OLIWBASE+129 // Only half of 32 bit count value read via CGL
#define OLBADINDEX					OLIWBASE+130 // Invalid Index
#define OLINVALIDX4INDEXCOMBO		OLIWBASE+131 // Invalid combination of Index and X4Scaling
#define OLBADCOUPLINGTYPE			OLIWBASE+132 // Invalid coupling type 
#define OLBADEXCITATIONCURRENTSRC			OLIWBASE+133 // Invalid current source 
#define OLBADVALUE					OLIWBASE+134 // Invalid value set
#define OLINVALIDWHENADRUNNING		OLIWBASE+135 // Operation is prohibited while A/D is running
#define OLBADTHERMOCOUPLETYPE		OLIWBASE+136 // Invalid thermocouple type was specified	
#define OLNOMEMORY					OLIWBASE+137 // Internal memory allocation failed
#define OLBADRETURNPOINTER			OLIWBASE+138 // The return value pointer is not valid
#define OLBADRTDTYPE				OLIWBASE+139 // Invalid RTD type was specified
#define OLBADSYNCMODE				OLIWBASE+140 // Invalid synchronization mode specified
#define OLBADTEMPFILTERTYPE			OLIWBASE+141 // Invalid temperature filter type was specified



#ifndef OLBMBASE
	#define OLBMBASE                    ((ECODE)200)
#endif

#define OLCANNOTALLOCBCB            OLBMBASE+0   // Cannot allocate a buffer control block for the requested data buffer.
#define OLCANNOTALLOCBUFFER         OLBMBASE+1   // Cannot allocate the requested data buffer.
#define OLBADBUFFERHANDLE           OLBMBASE+2   // Invalid buffer handle (HBUF) passed to a library from an application.
#define OLBUFFERLOCKFAILED          OLBMBASE+3   // The data buffer cannot be put to a section because it cannot be properly locked.
#define OLBUFFERLOCKED              OLBMBASE+4   // Buffer Locked
#define OLBUFFERONLIST              OLBMBASE+5   // Buffer on List
#define OLCANNOTREALLOCBCB          OLBMBASE+6   // Reallocation of a buffer control block was unsuccessful.
#define OLCANNOTREALLOCBUFFER       OLBMBASE+7   // Reallocation of the data buffer was unsuccessful.
#define OLBADSAMPLESIZE             OLBMBASE+8   // Bad Sample Size
#define OLCANNOTALLOCLIST           OLBMBASE+9   // Cannot Allocate List
#define OLBADLISTHANDLE             OLBMBASE+10  // Bad List Handle
#define OLLISTNOTEMPTY              OLBMBASE+11  // List Not Empty
#define OLBUFFERNOTLOCKED           OLBMBASE+12  // Bufffer Not Locked
#define OLBADDMACHANNEL             OLBMBASE+13  // Invalid DMA Channel specified
#define OLDMACHANNELINUSE           OLBMBASE+14  // Specified DMA Channel in use
#define OLBADIRQ                    OLBMBASE+15  // Invalid IRQ specified
#define OLIRQINUSE                  OLBMBASE+16  // Specififed IRQ in use
#define OLNOSAMPLES                 OLBMBASE+17  // Buffer has no valid samples
#define OLTOOMANYSAMPLES            OLBMBASE+18  // Valid Samples cannot be larger than buffer
#define OLBUFFERTOOSMALL            OLBMBASE+19  // Specified buffer too small for requested copy operation
#define OLODDSIZEDBUFFER		    OLBMBASE+20  // Num buffer points must be multiple 2 for this operation
#endif



