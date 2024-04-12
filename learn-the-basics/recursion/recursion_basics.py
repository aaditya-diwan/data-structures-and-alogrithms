def print_one_n(num, n):
    if n > num:
        return
    print(str(n) + '\n')
    print_one_n(num, n + 1)


def print_n_one(num):
    if num == 0:
        return
    print(num)
    print_n_one(num - 1)


def sum_of_n(num):
    if num == 0:
        return num
    return num + sum_of_n(num - 1)


def reverse_array(arr, i=0):
    mid = len(arr) // 2
    if i >= mid:
        return arr
    arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    return reverse_array(arr, i + 1)


def fibonacci_number(num):
    if num <= 1:
        return num
    return fibonacci_number(num - 1) + fibonacci_number(num - 2)


if __name__ == '__main__':
    # print_one_n(14, 1)
    # print_n_one(14)
    # print(sum_of_n(10))
    # print(reverse_array([1, 2]))
    print(fibonacci_number(5))
    pass
