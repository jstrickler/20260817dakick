import h5py as h5
import numpy as np
HDF5_FILE = "../DATA/NEONDSTowerTemperatureData.h5"
DATASET = '/Domain_03/OSBS/min_1/boom_1/temperature'

with h5.File(HDF5_FILE) as hdf5_file:  # open file
    ds = hdf5_file[DATASET]
    for attr_name, attr_value in ds.attrs.items():
        print(f"{attr_name:10s} {attr_value:50.50s}")   
    print()
    print(f"ds.attrs.keys(): {ds.attrs.keys()}")
    print()
    print(f"ds.attrs.values(): {ds.attrs.values()}")
     
