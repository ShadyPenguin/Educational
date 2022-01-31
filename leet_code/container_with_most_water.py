"""
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
import logging
from typing import List

# logging.basicConfig(level=logging.DEBUG)

class Solution:
    def maxArea_v1(self, height: List[int]) -> int:
        """
        This algorithm is too slow with O(n)
        """
        largest = 0
        # O(n**2)
        for li, left in enumerate(height[:-1]):
            for ri, right in enumerate(height[0:]):
                vertical = min(left, right)
                width = ri - li
                area = width * vertical
                if largest < area:
                    logging.debug(f"Updating: {largest=} with: {area=} ({width=} x {vertical=})")
                    largest = area

        return largest


    def maxArea(self, height: List[int]) -> int:
        """
        Runtime O(n)
        1340 ms	27.3 MB
        """
        largest = 0

        left, right = 0, len(height) - 1
        while left < right:
            lv, rv = height[left], height[right]
            vertical = min(lv, rv)
            area = vertical * (right - left)
            largest = max(largest, area)
            if lv < rv:
                left += 1
            else:
                right -= 1
        return largest




def main():
    s = Solution()
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert s.maxArea([1,1]) == 1

if __name__ == "__main__":
    main()
