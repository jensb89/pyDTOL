# pyDTOL - Using "Data Translation" AD/DA Acquistion Devices with python

The repo contains some code to use the Data Translation AD/DA devices via python. It is mainly using python ctypes to call the C functions from the DT Open Layer SDK. 

## Installation

DT Open Layers SDK has to be installed on the PC. When you have installed the driver for your AD/DA device, you probably have this installed already. 

When using python 32bit, change the library in "DTOL_prototypes.py" to the 32bit version:
```python
    dll = ctypes.CDLL(find_library('oldaapi32'))
    dll2 = ctypes.CDLL(find_library('OLMEM32'))
```

## Usage
`analog_input_get_single_vals.py` and `analog_output_set_single_vals.py` are two examples of how to use the code. The main class is defined in `DTOL.py`, the ctypes protoype function are outsoruced in the `DTOL_prototypes.py` and `DTOL_defs.py` files.

`DTOL_test_cont.py` is a first test for continious analog input and therefore a "live view" of the input channel(s). It is not fully working right now, still in progress.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


## License
MIT License
