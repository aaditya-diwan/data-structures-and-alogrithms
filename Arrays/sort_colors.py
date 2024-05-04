"""
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

This solution uses three pointers: p0, curr, and p2. 
p0 pointer keeps track of the position where the next 0 should be placed, 
while p2 keeps track of the position where the next 2 should be placed. 
The curr pointer iterates through the array.
We swap elements accordingly while maintaining the invariant that all elements before p0 are 0s, 
all elements after p2 are 2s, and the elements between p0 and p2 are 1s. 
This algorithm has a time complexity of O(n) and a space complexity of O(1)
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        curr = 0

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1