class Solution:

    def quick_sort(self, A, p, r):
        if p < r:
            q = partition(A, p, r)
            self.quick_sort(A, p, q - 1)
            self.quick_sort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == '__main__':
    S = Solution()
    a = [1, 8, 7, 6, 5, 3, 3, 6]
    S.quick_sort(a, 0, len(a) - 1)
    print(a)
