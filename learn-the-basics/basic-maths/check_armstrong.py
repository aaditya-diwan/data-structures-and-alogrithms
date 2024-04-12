def find_depth(num):
    depth = 0
    while num > 0:
        num = num // 10
        depth += 1
    return depth


def check_armstrong(num):
    temp = num
    depth = find_depth(num)
    actual_depth = depth
    sum_of_powers = 0
    while depth >= 0:
        x = num % 10
        num = num // 10
        sum_of_powers += x**actual_depth
        depth -= 1
    if temp == sum_of_powers:
        return True
    return False


if __name__ == '__main__':
    print(check_armstrong(153))
