import time
from random import randint


class LargestRectangleArea:

    def solution(self, nums):
        stack = []
        max_area = 0
        length = len(nums)
        prev_index = 0
        for i in range(length):
            while True:
                if stack:
                    if nums[i] > stack[-1][0]:
                        stack.append((nums[i], prev_index))
                        prev_index = i + 1
                        break
                    elif nums[i] < stack[-1][0]:
                        temp = stack.pop()
                        max_area = max(max_area, temp[0] * (i - temp[1]))
                        prev_index = temp[1]
                        continue
                    else:
                        prev_index = i + 1
                        break
                else:
                    stack.append((nums[i], prev_index))
                    prev_index = i + 1
                    break
        else:
            for i in stack:
                max_area = max(max_area, i[0] * (length - i[1]))
        return max_area


if __name__ == '__main__':
    s = LargestRectangleArea()
    start = time.time()
    print(s.solution([randint(0, 100) for i in range(1000000)]))
    end = time.time()
    print(end - start)
