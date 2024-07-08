def search_in_rotated_array(arr, ele):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == ele:
            return mid
        
        # If the left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= ele < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the right half is sorted
        else:
            if arr[mid] < ele <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1  # Element not found

print(search_in_rotated_array([7, 8, 9, 1, 2, 3, 4, 5, 6], 9))
