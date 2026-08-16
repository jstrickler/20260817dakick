import pandas as pd

HDF5_FILE = "../DATA/NEONDSTowerTemperatureData.h5"
DATASET = '/Domain_03/OSBS/min_1/boom_1/temperature'

df = pd.read_hdf(HDF5_FILE, key=DATASET)
df.index = pd.to_datetime(df.date)
df.drop(['date'], axis=1, inplace=True)
print(df.head())
