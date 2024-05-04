"""
169. Majority Element
Boyer-Moore Voting Algorithm, which requires only O(1) space and O(n) time complexity
This algorithm works by initially assuming the first element as the majority candidate. 
It then iterates through the array, incrementing the count if the current element matches the candidate or decrementing 
it otherwise. Whenever the count reaches zero, it resets the candidate to the current element and starts counting again. 
Since the majority element appears more than len(nums)//2 times, 
this algorithm ensures that the candidate returned at the end is indeed the majority element.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate