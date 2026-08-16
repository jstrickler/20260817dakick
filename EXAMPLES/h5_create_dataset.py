import h5py as h5
import numpy as np

HDF5_FILE = "monthly_data.h5"
HDF5_GROUP = "/2023/April"
HDF5_DATASET = HDF5_GROUP + "/ds01"

with h5.File(HDF5_FILE, "w") as hdf5_file:
    april_2023 = hdf5_file.create_group(HDF5_GROUP)
    numbers_data = np.genfromtxt("../DATA/columns_of_numbers.txt", skip_header=True)
    ds = april_2023.create_dataset("numbers", dtype="i", data=numbers_data)
    del numbers_data
    print(ds)
    print(ds[:])