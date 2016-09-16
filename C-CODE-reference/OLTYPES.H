#if !defined(__OLTYPES__)
#define __OLTYPES__

/*-----------------------------------------------------------------------

  FILE NAME: oltypes.h

ABSTRACT:

   This unit contains declarations for the Open Layers
   Data Acquisition Library.


---------------------------------------------------------------------------*/
#ifdef _WIN32
#define __export
#define __huge
#define _huge
#define huge

#define DllExport __declspec(dllexport)
#define DllImport __declspec(dllimport)

#include <windef.h>

#else 

#undef WINAPI
#define WINAPI    __far __pascal __loadds
#undef CALLBACK
#define CALLBACK  __far __pascal __loadds

#endif // if _WIN32

typedef signed char     CHR;
typedef CHR FAR*        LPCHR;
typedef CHR*            PCHR;
typedef unsigned char   UCHR;
typedef UCHR FAR*       LPUCHR;
typedef UCHR*           PUCHR;
typedef short           SHRT;
typedef SHRT FAR*       LPSHRT;
typedef SHRT*           PSHRT;
typedef unsigned short  USHRT;
typedef USHRT FAR*      LPUSHRT;
typedef USHRT*          PUSHRT;
typedef long            LNG;
typedef LNG FAR*        LPLNG;
typedef LNG*            PLNG;
typedef unsigned long   ULNG;
typedef ULNG FAR*       LPULNG;
typedef ULNG*           PULNG;
typedef float           FLT;
typedef FLT FAR*        LPFLT;
typedef FLT*            PFLT;
typedef double          DBL;
typedef DBL FAR*        LPDBL;
typedef DBL*            PDBL;

#if !defined(UINT)
typedef unsigned int    UINT;
#endif

typedef UINT FAR*       LPUINT;
typedef UINT*           PUINT;
typedef BOOL FAR*       LPBOOL;
typedef BOOL*           PBOOL;


typedef unsigned long    ECODE;      // Error/Warning code definition
typedef ECODE FAR*   LPECODE;   // Far pointer to Error/Warning code definition
typedef ECODE*       PECODE;   // Far pointer to Error/Warning code definition

typedef ECODE  OLSTATUS;

typedef enum
{
    DTUSB_BUS,
    DTPCI_BUS,
    DTPCMCIA_BUS,
    DTISA_BUS
} DTBUS_TYPE;

typedef struct
{
   ULONG Info[32];
}  DRIVER_SPECIFIC_INFO, *PDRIVER_SPECIFIC_INFO;

#endif
