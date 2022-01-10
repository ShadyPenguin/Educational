"""
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

TODO: Time limit exceeded
"""
import logging
from typing import List

# logging.basicConfig(
#     level=None, format="%(funcName)s: ln %(lineno)s - %(message)s"
# )


class Solution:
    def max_area(self, height: List[int]) -> int:
        """
        Essentially, I need to do two separate tasks:
        1. Compute the area between two heights
        2. Find the largest area
        >>> s = Solution()
        >>> s.max_area([1,8,6,2,5,4,8,3,7])
        49
        >>> s.max_area([1,1])
        1
        """
        _max = 0
        for left in range(len(height) - 1):
            for right in range(left + 1, len(height)):
                vertical = min(height[left], height[right])
                horizontal = right - left
                area = vertical * horizontal
                # a = self.compute_area(*args)
                # logging.debug(f"indicies: ({left}, {right}), values: ({height[left], height[right]})")
                if area > _max:
                    _max = area
        return _max

    def compute_area(self, left: int, right: int, width: int) -> int:
        """
        Compute the area of the provided boundaries.

        Args:
            left (int): height of the left boundary
            right (int): height of the right boundary
            width (int): width of the horizontal boundaries

        >>> s = Solution()
        >>> s.compute_area(2, 5, 2)
        4
        >>> s.compute_area(1, 1, 5)
        5
        """
        # logging.debug(f"{(left, right)}, {min(left, right)}")
        return min(left, right) * width


if __name__ == "__main__":
    import doctest

    doctest.testmod()
