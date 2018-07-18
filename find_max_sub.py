"""
最大子数组问题
"""


def find_max_sub(l: list, left, right) -> tuple:
    if left == right:
        return l[left], left, right
    else:
        average = int((right + left) / 2)
        left_max = find_max_sub(l, left, average)
        right_max = find_max_sub(l, average + 1, right)
        mid_max = find_mid_max(l, left, right, average)
        if left_max > right_max and left_max > mid_max:
            return left_max
        elif right_max > left_max and right_max > mid_max:
            return right_max
        else:
            return mid_max


def find_mid_max(l: list, left: int, right: int, average: int) -> tuple:
    left = find_max_next_mid(range(average, left - 1, -1), l)
    right = find_max_next_mid(range(average + 1, right + 1), l)
    return left[0] + right[0], left[1], right[1]


def find_max_next_mid(iter: iter, l: list) -> tuple:
    total = 0
    index = iter[0]
    max_sum = l[index]
    for i in iter:
        total += l[i]
        if total > max_sum:
            index = i
            max_sum = total
    return max_sum, index


def main():
    data = [-1, -1, -2, 3, 4, -7]
    return find_max_sub(data, 0, len(data) - 1)


if __name__ == '__main__':
    print(main())
