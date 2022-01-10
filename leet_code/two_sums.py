import logging
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    https://leetcode.com/problems/two-sum/
    >>> twoSum([2, 7, 11, 15], 9)
    [0, 1]
    >>> twoSum([3, 2, 4], 6)
    [1, 2]
    >>> twoSum([3, 3], 6)
    [0, 1]
    """
    for left_idx, n in enumerate(nums):
        try:
            right_idx = nums.index(target - n, left_idx + 1)
        except ValueError as e:
            logging.debug(e)
            continue
        if right_idx:
            return [left_idx, right_idx]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
