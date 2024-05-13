"""
The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.

The upper bound is the smallest index, ind, where arr[ind] > x.

But if any such index is not found, the upper bound algorithm returns n i.e. size of the given array. The main difference between the lower and upper bound is in the condition. For the lower bound the condition was arr[ind] >= x and here, in the case of the upper bound, it is arr[ind] > x.
"""
def upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] > x:
            high = middle - 1
            ans = middle
        else:
            low = middle + 1
            
        
    return ans

print(upper_bound([1,2,3,4,5,6,7,8,9,10,11,12,22],11))
