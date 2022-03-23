"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)

class Solution:
    def search(self, nums: List[int], target: int, left: int = 0) -> int:
        """
        use binary search to find the the index of target in nums
        """
        if len(nums) == 1:
            logging.debug(f"break 1, {nums=}, {left=}")
            return left if nums[0] == target else -1

        if len(nums) == 2:
            logging.debug("break 2")
            for idx, num in enumerate(nums):
                if num == target:
                    return idx + left
            return -1

        # CHECK MIDDLE
        # if 3 elements
        # check middle element
        middle = len(nums) // 2  # 1
        middle_value = nums[middle]
        if middle_value == target:
            # [1, 2, 3], 2
            logging.debug("Found it in middle")
            return left + middle

        is_head, is_tail = self._determine_if_ending(nums, middle, middle_value)

        if is_head:
            if target <= nums[-1]:
                # assert s.search([3, 1, 2], 2)
                return self._search_right(nums, left, middle, target)
            return self._search_left(nums, left, middle, target)
        # Handle tail
        if is_tail:
            if target >= nums[0]:
                # # assert s.search([2, 3, 1], 1) == 2 # Search right as tail
                return self._search_left(nums, left, middle, target)
            return self._search_right(nums, left, middle, target)

        # head -> right
        if target > middle_value:
            if nums[-1] < middle_value or target > nums[-1]:
                return self._search_right(nums, left, middle, target)
            return self._search_left(nums, left, middle, target)

        # target < middle value
        if target > nums[-1] or nums[-1] > middle_value:
            # 2 3 4 5 1], 2  left
            # 1,2,3,4,5], 2  left
            return self._search_left(nums, left, middle, target)
        return self._search_left(nums, left, middle, target)


    def _search_right(self, nums, left, middle, target):
        return self.search(nums[middle + 1:], target, left + middle + 1)

    def _search_left(self, nums, left, middle, target):
        return self.search(nums[:middle], target, left)

    def _determine_if_ending(self, nums, middle, middle_value):
        is_head = is_tail = False
        left_val, right_val = nums[middle -1], nums[middle + 1]

        # Determine if the middle is the start of the list:
        if left_val < middle_value and middle_value < right_val:
            # 1, 2, 3
            logging.debug(f"{left_val=}, {middle_value=}, {right_val=}: Not an end")
            return False, False
        if left_val > middle_value and middle_value < right_val:
            # 3, 1, 2
            logging.debug(f"{left_val=}, {middle_value=}, {right_val=}: Is head")
            return True, False
        # if left_val < middle_value and middle_value > right_val:
        # 2, 3, 1
        logging.debug(f"{left_val=}, {middle_value=}, {right_val=}: Is Tail")
        return False, True



def main():
    s = Solution()
    # assert s.search([1, 2, 3], 2) == 1 # Found middle
    # assert s.search([2, 3, 1], 1) == 2 # Search right as tail
    # assert s.search([3, 1, 2], 2) == 2 # Search right as head
    # assert s.search([2, 3, 1], 2) == 0 # Search left as tail
    # assert s.search([3, 1, 2], 3) == 0 # Search left as head
    assert s.search([6,7,1,2,3,4,5], 6) == 0 # Search left as head

if __name__ == "__main__":
    main()
