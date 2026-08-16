import h5py as h5
HDF5_FILE = "../DATA/NEONDSTowerTemperatureData.h5"
DATASET = '/Domain_03/OSBS/min_1/boom_1/temperature'

with h5.File(HDF5_FILE) as hdf5_file:  # open file
    print(f"HDF5 File object: {hdf5_file}")
    ds = hdf5_file[DATASET]  # dataset is 1-dimensional -- each row is compound type
    print()
    print(f"dataset: {ds[:]}")
    print()
    print(f"len(dataset): {len(ds)}")
    print(f"dataset.shape: {ds.shape}")
    print(f"dataset.ndim: {ds.ndim}")
    print(f"dataset[0]: {ds[0]}")
