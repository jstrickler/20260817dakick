import h5py

H5_FILE = '../DATA/hdf5_test.h5'

with h5py.File(H5_FILE, "r+") as hfile:  # open HDF5 file
    # Do not have to create '/Animals' first
    ds1 = hfile.create_dataset('/Animals/wombat', (15, 2))  # add 15x2 dataset wombat in group Animals
    ds2 = hfile.create_dataset(
        '/Animals/bushbaby', (100, 3), dtype='i8'  # add 100x3 dataset bushbaby in group Animals
    )
