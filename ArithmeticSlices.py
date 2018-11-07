"""算数序列"""


class ArithmeticSlices:

    def solution(self, A):
        length = len(A)
        if length < 3:
            return 0
        sub_len = 2
        sub = A[1] - A[0]
        slices_sum = 0
        for i in range(2, length):
            temp_sub = A[i] - A[i - 1]
            if temp_sub == sub:
                sub_len += 1
            else:
                sub_len = 2
                sub = temp_sub
            if sub_len >= 3:
                slices_sum += sub_len - 2
        return slices_sum


if __name__ == '__main__':
    s = ArithmeticSlices()
    print(s.solution([1, 2, 3, 4, 3, 6]))
