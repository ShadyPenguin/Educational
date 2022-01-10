"""
example.py

This program is to show a demo of how to doctest python methods.
"""


def add(x: int, y: int) -> int:
    """
    Add two integers and return the sum

    :param x: int
    :param y: int
    :return int:
    >>> add(2, 2)
    4
    >>> add(1, -1)
    0
    """
    return x + y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
