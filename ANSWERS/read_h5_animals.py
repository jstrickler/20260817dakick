import h5py

H5_FILE = '../DATA/misc_data.h5'

H5_DATASET = '/Animals/observations'

hfile = h5py.File(H5_FILE)

dset = hfile[H5_DATASET]

for observation1, observation2 in dset:
    print(f"{observation1:3.0f} {observation2:12.5f}")


