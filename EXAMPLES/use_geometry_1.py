import sys
from alpha.mathlib import geometry  #  find and run geometry.py

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# module search path:
# 1. current folder
# 2. folders in PYTHONPATH environment variable
# 3. predefined folders in Python installation folder 

for path in sys.path:
    print(path)

# Python editable install