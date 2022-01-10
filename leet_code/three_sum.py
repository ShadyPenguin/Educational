"""
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
import collections
import itertools
from typing import Deque, List


def three_sums_using_combinations(nums: List[int]) -> List[list[int]]:
    """
    TODO: TOO SLOW
    https://leetcode.com/problems/3sum/submissions/

    This is a speed of O(n*n)

    [0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 1, 5]
    [0, 2, 3], [0, 2, 4], [0, 2, 5]
    [0, 3, 4], [0, 3, 5]
    [0, 4, 5]

    n = length of nums
    pattern is: [i, i+1, i+2] + ... [i+n-2, i+n-1, i+n]

    >>> three_sums_using_combinations([-1,0,1,2,-1,-4])
    [[-1, -1, 2], [-1, 0, 1]]
    """
    answer = []
    for i, j, k in itertools.combinations(range(len(nums)), 3):
        values = sorted([nums[i], nums[j], nums[k]])
        if values not in answer and sum(values) == 0:
            answer.append(values)
    return list(sorted(answer))


def three_sums_using_recursion(
    nums: Deque[int], possible: Deque[List[int]] = None, answer: Deque[List[int]] = None
) -> Deque[List[int]]:
    """
    TODO: Not working
    """
    # first case setup for recursion
    if possible is None:
        answer = collections.deque()
        possible = collections.deque()
    # base case
    if not nums:
        return answer
    # iterate through all possible lists
    num: int = nums.popleft()
    if possible:
        for _ in range(len(possible)):
            _nums = possible.popleft()
            _nums.append(num)
            if len(_nums) == 3:
                if sum(_nums) == 0:
                    print(f"{_nums=}")
                    answer.append(_nums)
            else:
                possible.append(_nums)

    possible.append([num])

    return three_sums_using_recursion(nums, possible, answer)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
