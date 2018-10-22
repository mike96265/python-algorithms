from functools import lru_cache

'''dynamic programing'''

'''钢条切割'''

length_to_price = {
    0: 0,
    1: 1,
    2: 5,
    3: 8,
    4: 9,
    5: 10,
    6: 17,
    7: 17,
    8: 20,
    9: 24,
    10: 30
}


def iron_split(n: int):
    return iter_all(n, 0)


@lru_cache(maxsize=1000)
def iter_all(length, current):
    if current == 9:
        return length_to_price[10] + iter_all(length - 10, 0)
    else:
        left = 1 + current
        if left >= length:
            return length_to_price[length]
        do_slice = length_to_price[left] + iter_all(length - left, 0)
        current += 1
        undo_slice = iter_all(length, current)
        return max(do_slice, undo_slice)


if __name__ == '__main__':
    print(iron_split(10))
