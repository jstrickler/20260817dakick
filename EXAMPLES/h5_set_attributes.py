import h5py as h5
import numpy as np

HDF5_FILE = "columns.h5"
HDF5_GROUP = "/2023/April"
HDF5_DATASET = HDF5_GROUP + "/ds01"
COLUMNS = {
    "Delta": "dates",
    "Epsilon": "elderberries",
    "Zeta": "zucchini",
    "Alpha": "apples",
    "Beta": "bananas",
    "Gamma": "grapefruit",
}

with h5.File(HDF5_FILE, "w", track_order=True) as hdf5_file:
    april_2023 = hdf5_file.create_group(HDF5_GROUP)
    numbers_data = np.genfromtxt("../DATA/columns_of_numbers.txt", skip_header=True)
    ds = april_2023.create_dataset("numbers", dtype="i", data=numbers_data)
    del numbers_data
    for column_name, description in COLUMNS.items():
        ds.attrs[column_name] = description
    print(ds)
    print(ds[:])