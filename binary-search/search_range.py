    
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        start, end = -1, -1
        while low <= high:
            middle = (low + high) // 2
            if target <= nums[middle]:
                if nums[middle] == target:
                    start = middle
                    
                high = middle - 1
            else:
                low = middle + 1
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if target >= nums[middle]:
                if nums[middle] == target:
                    end = middle
                low = middle + 1
            else:
                high = middle - 1
        
        return [start, end]

s = Solution()
s.searchRange([5,7,7,8,8,10], 8)
    