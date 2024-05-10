"""
560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_cntr = {0: 1}
        cnt = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if (sum - k) in sum_cntr:
                cnt += sum_cntr[sum - k]
            # If sum_cntr has some return it's value incrementing it by 1
            # if not, set's it to zero and increments it by one
            sum_cntr[sum] = sum_cntr.get(sum, 0) + 1
        return cnt

s = Solution()
print(s.subarraySum([1, 2, 3, -3, 1, 1, 1, 4, 2, -3], 3))