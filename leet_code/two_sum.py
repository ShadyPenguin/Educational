"""
https://leetcode.com/problems/two-sum/

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Parameters:
            nums: numbers containing exactly one combination to equal target
            target: the value two nums should sum to

        Notes:
        - one solution
        - can't repeat number

        Return:
            indicies of two elements in nums that reduce to target

        Speed: O(n)
        Size: dictionary space
        Runtime: 104 ms
        """
        desired = {}
        for idx, num in enumerate(nums):
            if num in desired:
                return [desired[num], idx]

            desire = target - num
            desired[desire] = idx

def main():
    s = Solution()
    print(s.twoSum([2,7,11,15], target = 9))

if __name__ == "__main__":
    main()
