"""
15. 3Sum
1. Sorting the Array: The array is sorted initially, which is necessary for the two-pointer technique to work effectively.
2. Handling Duplicates: The i pointer skips duplicates to prevent checking the same value multiple times. Similarly, after finding a valid triplet, the j and k pointers skip duplicates to avoid adding the same triplet more than once.
3. Two-pointer Technique: After identifying a valid triplet, both j and k are adjusted to move past the current values and continue searching for other potential triplets.
4. Main Loop and Inner Loop: The outer loop iterates over the i pointer, and the inner loop uses j and k pointers to find pairs that sum up with nums[i] to zero. The inner loop condition ensures j is always less than k.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for `i`
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    # Skip duplicates for `j`
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    # Skip duplicates for `k`
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    # Move both pointers after finding a valid triplet
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        
        return result
                



        