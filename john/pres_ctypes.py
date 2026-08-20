import sys
import ctypes

# load the library, according to platform
try:
    if sys.platform == 'win32':
        pres_lib = r'DATA\presidents.dll'
    elif sys.platform == 'darwin':
        pres_lib = '../DATA/presidents.dylib'
    else:
        pres_lib = '../DATA/presidents.so'
    presidents = ctypes.cdll.LoadLibrary(pres_lib)
except Exception as err:
    print("Unable to load presidents module", err)
    exit(1)

presidents.get_name.restype = ctypes.c_char_p

for i in range(1, 45):
    print(presidents.get_name(i).decode())
