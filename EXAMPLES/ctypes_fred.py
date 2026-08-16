import sys
import ctypes

# load the C library, according to platform
if sys.platform == 'win32':
    fred = ctypes.cdll.LoadLibrary('../DATA/fred.dll')
elif sys.platform == 'darwin':
    fred = ctypes.cdll.LoadLibrary('../DATA/fred.dylib')
else:
    fred = ctypes.cdll.LoadLibrary('../DATA/fred.so')

print(fred.add(2, 3))  # call a function in the C library
print(fred.add(10000, 9999))  # call a function in the C library

try:
    print(fred.add(1, []))  # call function which raises an exception
except Exception as e:
    print("That didn't work...", e)

fred.hello()  # hello() calls printf() for output

fred.get_skit.restype = ctypes.c_char_p  # default return value type is int;

print(fred.get_skit(1).decode())
print(fred.get_skit(4).decode())
print(fred.get_skit(99).decode())
print()
