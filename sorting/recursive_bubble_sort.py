def bubble_sort_recursive(arr, n):
    if n <= 1:
        return
    # Base case: if array size is 1, it's already sorted
    if n == 1:
        return

    # One pass of bubble sort, moving the largest element to the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursively sort the first n-1 elements
    bubble_sort_recursive(arr, n - 1)


if __name__ == '__main__':
    # Example usage:
    arr = []
    n = len(arr)
    bubble_sort_recursive(arr, n)

    print("Sorted array:", arr)