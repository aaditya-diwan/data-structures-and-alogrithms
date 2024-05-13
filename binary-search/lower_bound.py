"""
The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.


"""
from typing import List


def lower_bound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        middle = (low + high) // 2
        print(middle)
        if arr[middle] >= x:
            high = middle - 1
            ans = middle
        else:
            low = middle + 1
        
    return ans

print(lower_bound([1,2,3,4,5,6,7,8,9,10, 22],11))

        

