#
import h5py
import matplotlib.pyplot as plt  # import matplotlib for plotting

DATA_FILE = '../DATA/TSX_SM_053_0008_20111223-20121026_0308_00063.h5'

DATASET_NAME = '/GEOCODE/unwrapped_interferogram'
# note: dataset is 2-dimensional

hfile = h5py.File(DATA_FILE, mode="r")  # open HDF5 file

dset = hfile[DATASET_NAME]  # get dataset
print(f"dset: {dset}")
print(f"dset: {dset}\n")

print(dset[475:480, 195:205])  # print slice of dataset

for row in range(475, 486, 5):
    columns = slice(195, 300)
    plt.plot(dset[row, columns], '-', linewidth=2)  # iterate over rows and plot slice of columns for each row

plt.show()  # NOTE: this is an interferogram, and is really an image -- here we're just plotting it to illustrate using data from a dataset
