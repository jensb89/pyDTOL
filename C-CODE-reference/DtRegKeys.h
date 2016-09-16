
#ifndef _DTREGKEYS_H_
#define _DTREGKEYS_H_

#ifndef __T
#define __T(x)      L ## x
#endif

#ifndef _T
#define _T(x)       __T(x)
#endif

// Registry Key Names
//
#define REG_BOARD_DATABASE_KEY           _T("BoardDatabase")
#define REG_DTOL_CLASSNAME_KEY           _T("DtOpenLayersDaDevice")

// Registry Value Names
//
#define REG_DT_OPEN_LAYERS_BOARD_NAME_VNAME     _T("DtOpenLayersBoardName")
#define REG_BOARD_MODEL_NAME_VNAME              _T("BoardModelName")
#define REG_DRIVER_NAME_VNAME                   _T("DriverName")
#define REG_SERIAL_NUMBER_VNAME                 _T("SerialNumber")
#define REG_INSTANCE_NUMBER_VNAME               _T("DeviceInstanceNumber")
#define REG_BOARD_TYPE_VNAME                    _T("BoardType")
#define REG_EEPROM_VALIDATION_OVERRIDE_VNAME    _T("EepromValidationOverride")
#define REG_MESSAGE_OVERRUN_OVERRIDE_VNAME      _T("MessageOverrunOverride")
#define REG_STREAM_ENGINE_URB_QUEUE_DEPTH_VNAME _T("DtUrbQueueDepth")
#define REG_PORTD_INTERRUPT_MASK                _T("PortDInterruptMask")
#define REG_CNTR_TMR_INTERRUPT_MASK             _T("CounterTimerInterruptMask")
#define REG_DT322CSLTD_OVERRIDE_VNAME           _T("DT322CSOverride")
#define REG_DT_LINK_NAME_VNAME                  _T("LinkName")
#define REG_DT_PCI_BUS_OVERRIDE_VNAME           _T("PCIBusOverride")
#define REG_INTERRUPT_MASK                      _T("InterruptMask")
#define REG_BOARD_NAME_VNAME                    _T("BoardName")


// Registry Paths
#define REG_CONTROL_PATH                        _T("System\\CurrentControlSet\\Control\\")
#define REG_DEVICEMAP_PATH                      _T("Hardware\\DeviceMap")
#define REG_SOFTWARE_PATH      _T("\\Registry\\Machine\\Software\\Data Translation\\DT-Open Layers Data Acquisition Software")


#endif  /* _DTREGKEYS_H_ */
