
def reverse_integer(num):
    depth = 0
    temp_num = num
    while temp_num > 0:
        temp_num = temp_num // 10
        depth += 1
    print(depth)
    reversed_num = 0
    while depth > 0:
        x = num % 10
        num = num // 10
        reversed_num += x * 10 ** (depth - 1)
        depth -= 1
    return reversed_num


if __name__ == '__main__':
    print(reverse_integer(2671))
