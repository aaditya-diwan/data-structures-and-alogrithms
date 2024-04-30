def calculate_frequency(arr, num):
    freq = dict()
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return freq[num]


def calculate_highest_lowest_freq(arr):
    max_freq = -1
    min_freq = 1000

    frequencies = dict()
    for i in arr:
        if i not in frequencies:
            frequencies[i] = 1
        else:
            frequencies[i] += 1
    for k, v in frequencies.items():
        if v > max_freq:
            max_freq = v
        if v < min_freq:
            min_freq = v

    return [min_freq, max_freq]


if __name__ == '__main__':
    # print(calculate_frequency([1, 1, 1, 2, 3, 3, 2, 2, 6, 6, 5, 4], 3))
    print(calculate_highest_lowest_freq([1, 1, 1, 1, 2, 3, 3, 2, 2, 6, 6, 5, 4]))
