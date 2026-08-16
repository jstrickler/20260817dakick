import h5py as h5

INDENT = 3

def _print_tree(node, indent):
    if isinstance(node, h5.Group):
        for name, obj in node.items():
            print(indent * ' ', end='')
            if isinstance(obj, h5.Dataset):
                print("DATASET:", end=' ')
            print(name)
            _print_tree(obj, indent + INDENT)

def h5_print_tree(hdf_file):
    _print_tree(hdf_file, 0)
 
if __name__ == "__main__":
    # H5_FILE = "../DATA/NEONDSTowerTemperatureData.h5"
    H5_FILE = "columns.h5"
    # H5_FILE = "../DATA/NEONDSTowerTemperatureData.h5"

    h = h5.File(H5_FILE)
    h5_print_tree(h)