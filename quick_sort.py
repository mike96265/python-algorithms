import time
from random import randint


class Solution:

    def quick_sort(self, A, p, r):
        if p < r:
            i = randint(p, r)
            A[i], A[r] = A[r], A[i]
            q = partition(A, p, r)
            self.quick_sort(A, p, q - 1)
            self.quick_sort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == '__main__':
    total = 0
    s = Solution()
    for i in range(100):
        b = [randint(1, 100000) for _ in range(100000)]
        start = time.time()
        s.quick_sort(b, 0, 100000 - 1)
        end = time.time()
        total += (end - start)

    print(f'100 times sort cost {total}')
    print(f'per sort cost {total/100}')
