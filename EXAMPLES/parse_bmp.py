from struct import Struct

# short int short short int (native, unsigned)
header = Struct('=2s3I')  # define layout of bitmap header -- could also be '=2sIII'

with open('../DATA/chimp.bmp', 'rb') as chimp_in:
    header_data = chimp_in.read(header.size)  # read first 14 bytes in binary mode

    (signature, file_size, reserved, offset) = header.unpack(header_data)  # unpack the binary header into individual fields

    print("HEADER")
    print(f"{signature = }")
    print(f"{file_size = }")
    print(f"{reserved = }")
    print(f"{offset = }")
    print()
        
    info_header = Struct('=IIIHHIIIIII')  # could be '=3I2H6I'

    info_header_data = chimp_in.read(info_header.size)  # read next 40 bytes

    (info_header_size, width, height, planes, bits_per_pixel, compression, image_size,
     x_pixels_per_m, y_pixels_per_m, colors_used, important_colors) = info_header.unpack(info_header_data)

    print("INFO HEADER")
    print(f"{info_header_size = }")
    print(f"{width = }")
    print(f"{height = }")
    print(f"{planes = }")
    print(f"{bits_per_pixel = }")
    print(f"{compression = }")
    print(f"{image_size = }")
    print(f"{x_pixels_per_m = }")
    print(f"{y_pixels_per_m = }")
    print(f"{colors_used = }")
    print(f"{important_colors = }")
