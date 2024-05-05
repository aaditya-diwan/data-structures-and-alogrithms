"""
2149. Rearrange Array Elements by Sign
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
"""

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        resultant = [0] * len(nums)

        positive_index, negative_index = 0, 1

        for i in range(len(nums)):
            if nums[i] < 0:
                resultant[negative_index] = nums[i]
                negative_index += 2
            else:
                resultant[positive_index] = nums[i]
                positive_index += 2
        return resultant