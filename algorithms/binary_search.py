import bisect
from typing import List, Optional


def binary_search_recursive(
    a: List[int], x: int, left: int = 0, right: int = None
) -> Optional[int]:
    """
    implementing a binary search algorithm
    >>> binary_search_recursive([1,2,3,4,5], 10) is None
    True
    >>> binary_search_recursive([1,2,3,4,5], 2)
    1
    >>> binary_search_recursive([1,2,3,4,5], 5)
    4
    """
    if right is None:
        right = len(a) - 1

    if left > right:
        return None

    mid = (left + right) // 2
    if a[mid] == x:  # found it
        return mid
    if x < a[mid]:  # go left
        return binary_search_recursive(a, x, left, mid - 1)
    # go right
    return binary_search_recursive(a, x, mid + 1, right)


def using_bisect(a: List[int], x: int) -> Optional[int]:
    """Use the provided bisect module to get the index of the value in a sorted array

    >>> using_bisect([1,2,3,4,5], 10)
    >>> using_bisect([1,2,3,4,5], 2)
    1
    >>> using_bisect([1,2,3,4,5], 5)
    4
    """
    maybe_index = bisect.bisect(a, x) - 1
    if a[maybe_index] == x:
        return maybe_index
    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
