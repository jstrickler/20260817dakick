import numpy as np
import h5py as h5


fremont_data = np.genfromtxt(
    '../DATA/FremontBridge.csv', skip_header=1, usecols=(1,2), delimiter=',',
    filling_values=(0,))

print(f"fremont_data: {fremont_data}")


with h5.File('bicycles.h5', "w") as h5_file:
    grp = h5_file.create_group('bicycledata')
    ds = grp.create_dataset('fremont', data=fremont_data)
    
        
    

