"""
Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.
"""

def search_insert(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        middle = (low + high) // 2
        
        if arr[middle] >= x:
            ans = middle
            high = middle - 1
        
        else:
            low = middle + 1
    return ans

print(search_insert([1, 5, 9, 11, 43, 56, 61], 34))
        