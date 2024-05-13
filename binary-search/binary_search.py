def binary_search(arr, element):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == element:
            return middle
        
        if element > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1
            
    return -1
        

# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))

from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        max_dp = float('-inf')

        for i in range(n-1, -1, -1):
            if i + k >= n:
                dp[i] = energy[i]
            else:
                dp[i] = max(energy[i], energy[i] + dp[i + k])
            max_dp = max(max_dp, dp[i])

        return max_dp

s = Solution()
print(s.maximumEnergy([5,2,-10,-5,1], 3))  # Output: 3