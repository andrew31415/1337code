"""https://leetcode.com/problems/two-sum/
"""

class Solution:    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        processed = {}

        for index, value in enumerate(nums):
            remainder = target - nums[index]

            if remainder in processed:
                return [index, processed[remainder]]

            processed[value] = index
