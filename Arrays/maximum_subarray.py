"""
53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize - 1
        sum = 0
        start = 0
        end, ansStart = -1, -1
        for i in range(len(nums)):
            if sum == 0:
                start = i

            sum += nums[i]

            if(sum > maxi):
                maxi = sum
                ansStart = start
                end = i
            
            if sum < 0:
                sum = 0
                
        print(f"The start and end of array is {ansStart, end}")
        return maxi