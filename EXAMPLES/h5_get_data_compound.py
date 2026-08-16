import h5py as h5
import numpy as np
HDF5_FILE = "../DATA/NEONDSTowerTemperatureData.h5"
DATASET = '/Domain_03/OSBS/min_1/boom_1/temperature'

with h5.File(HDF5_FILE) as hdf5_file:  # open file
    # this is a compound_dataset
    ds = hdf5_file[DATASET]

    # first row
    print(f"ds[0]: {ds[0]}")
    print(f"type(ds[0]): {type(ds[0])}")  # numpy array
    

    # first column of first row
    print(f"ds[0][0]: {ds[0][0]}")
    print(f"type(ds[0][0]): {type(ds[0][0])}")
    # second column of first row
    print(f"ds[0][1]: {ds[0][1]}")
    
    # all columns of first row
    
    print(f"list(ds[0]): {list(ds[0])}")
    print(f"type(ds[0]): {type(ds[0])}")
    
    max1 = ds['max'].astype(np.float16)
    print(f"max1: {max1}")
    print(f"type(max1): {type(max1)}")
    
    max2 = ds['max'].astype(int)
    print(f"max2: {max2}")
    print(f"type(max2): {type(max2)}")
    
    # column 'max'
    print(f"ds['max']: {ds['max']}")
    