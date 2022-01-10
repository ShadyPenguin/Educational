"""
Numpy Example

Usage:
$ python numpy_example.py

Output: This file outputs to STDOUT

Why: This file will help me understand what numpy can do.

Run this file from the command line and scroll throug the console output
to learn a bit about numpy matricies.
---------------------------------------------------------
"""
import numpy as np
import numpy.random as rd
from numpy.core.multiarray import zeros
from numpy.lib.type_check import imag

print(__doc__)

def print_array(a: np.ndarray) -> np.ndarray:
    """Convert a list into an array and print out the characteristics"""
    print(f"{a.ndim}-D array:")
    print(f"{a}")
    print(f"{a.shape=}")
    print(f"{a.dtype=}")
    print(f"{a.itemsize=}")
    print(f"{a.size=}")
    print(f"Bytes of contiguous memory used for array: {a.size * a.itemsize}")
    print("")

def display_dtype_sizing():
    """Explain difference between how the dtype impacts the size of an array

    dtype = data type + number of bits
    Examples:
        int8, int16, int32, in64
        float8, float16, float32, ...
    """
    print_array(np.array([]))
    print_array(np.array([1]))
    print_array(np.array([1.0]))
    print_array(np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))  # => 72 bytes

    print("given the array:")
    two_d = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]], dtype="int8")  # => 72 bytes
    print(two_d)
    print(f"Get a single element:\n\t{two_d[0,1]=}")
    print(f"Get a column by wildcarding the row:\n\t{two_d[:,1]=}")
    print(f"Get a row by wildcarding the column:\n\t{two_d[0,:]=}")
    print()

def initialize_arrays():
    """Initialize the shape"""
    a = rd.rand(2,2,2)
    print(a)
    copy_shape = np.full_like(a, 3)
    print(copy_shape)
    ranom_generated = rd.randint(5, 10, size=(2,2))
    print(ranom_generated)

def find_count_of_chars_in_string(s: str):
    zeros = np.zeros((26, len(s)), dtype="int8")
    ones = np.full_like(zeros, 1, dtype="int8")
    ones
    print(ones)
    print(ones.sum())
    print(ones - zeros)


def create_example_image():
    image = np.ones((5, 5), dtype="int8")
    mid = np.zeros((3, 3))
    mid[1,1]=9
    image[1:-1,1:-1] = mid
    print(image)
    print(image.dtype)


def main():
    create_example_image()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    main()
