with open("../DATA/mystery", "rb") as mystery_in:
    all_bytes = mystery_in.read()
    picture_bytes = all_bytes[1::3]  # get every third byte
    print((picture_bytes.decode()))  # decode from bytes to printable string
