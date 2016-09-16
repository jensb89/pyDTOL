
#include "..\..\..\DriverWorks\Include\devintf.h" // DONT USE NEW NUMEGA CODE QUIT YET - USE THE OLD ONES...

class CDtDeviceInterface : public CDeviceInterface
{
   public:
      CDtDeviceInterface( CDeviceInterfaceClass* pClassObject, 
                          DWORD Index,
                          PDWORD Error );

      HKEY OpenDeviceInstanceRegKey( void );
};

DEVINTF_INLINE 
CDtDeviceInterface::CDtDeviceInterface( CDeviceInterfaceClass* pClassObject, 
                                        DWORD Index,
                                        PDWORD Error )
								:  CDeviceInterface( pClassObject,
                                                     Index,
                                                     Error  ) 


{};

										

DEVINTF_INLINE 
HKEY 
CDtDeviceInterface::OpenDeviceInstanceRegKey( void )
{
    HKEY hKey = NULL;

    HMODULE hDll = LoadLibrary( "SetupApi.dll" );
    if( !hDll )
    {
	   return NULL;
    }

    try
    {


        HKEY
        ( WINAPI *pfnSetupDiOpenDeviceInterfaceRegKey ) ( IN HDEVINFO                  DeviceInfoSet,
                                                          IN PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
                                                          IN DWORD                     Reserved,
                                                          IN REGSAM                    samDesired ) = NULL;
        
        
        if( !(*(FARPROC*)&pfnSetupDiOpenDeviceInterfaceRegKey = GetProcAddress(  hDll,                                      // handle to DLL module
                                                                                 "SetupDiOpenDeviceInterfaceRegKey" ) ) )   // function name
        {
           FreeLibrary( hDll );
	       return NULL;
        }
       
        hKey = pfnSetupDiOpenDeviceInterfaceRegKey( m_Class->GetHandle(),
                                                    &m_Data,
                                                    0,
                                                    KEY_READ|KEY_WRITE );
		 if ( (hKey == NULL)||(hKey==(HKEY)0xFFFFFFFF) )
		 { 	// Try opening the hKey read-only
	        hKey = pfnSetupDiOpenDeviceInterfaceRegKey( m_Class->GetHandle(),
	                                                    &m_Data,
	                                                    0,
	                                                    KEY_READ);
		 }
        FreeLibrary( hDll );
        return hKey;
    }
    catch (...)
    {
       FreeLibrary( hDll );
       return NULL;
    }

}




