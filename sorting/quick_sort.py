def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left_of_pivot = [num for num in arr[1:] if num <= pivot]
    right_of_pivot = [num for num in arr[1:] if num > pivot]

    return quick_sort(left_of_pivot) + [pivot] + quick_sort(right_of_pivot)


if __name__ == '__main__':
    arr = [6, 4, 2, 1, 7, 11, 1]
    print(quick_sort(arr))