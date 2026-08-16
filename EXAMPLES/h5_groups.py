import h5py as h5

HDF5_FILE = "../DATA/NEONDSTowerTemperatureData.h5"
DATASET = '/Domain_03/OSBS/min_1/boom_1/temperature'

with h5.File(HDF5_FILE) as hdf5_file:  # open file
    print('/ groups:')
    for group in hdf5_file:  # iterate over the top-level groups
        print(group)
    print()

    d3 = hdf5_file['/Domain_03']
    print(f"d3: {d3}\n")

    print('/Domain_03 groups')
    for group in d3:
        print(group)
    print()
    
