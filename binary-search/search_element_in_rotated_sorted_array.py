def search_in_rotated_array(arr, ele):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == ele:
            return True
        
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

    return False  # Element not found

print(search_in_rotated_array([1,0,1,1,1], 0))