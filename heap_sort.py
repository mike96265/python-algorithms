import time
from random import randint


class Solution:

    def heap_sort(self, nums):
        s = MaxHeap(nums)
        return s.sort()


class MaxHeap:

    def __init__(self, heap: list):
        self._heap = heap[:]
        self.length = len(heap)
        for i in reversed(range(len(self._heap) >> 1)):
            self.max_heapify(i)

    def max_heapify(self, i):
        left = (i << 1) + 1
        right = (i << 1) + 2
        if left < self.length and self._heap[left] > self._heap[i]:
            largest = left
        else:
            largest = i

        if right < self.length and self._heap[right] > self._heap[largest]:
            largest = right
        if largest != i:
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            self.max_heapify(largest)

    def sort(self):
        while self.length > 1:
            self._heap[0], self._heap[self.length - 1] = self._heap[self.length - 1], self._heap[0]
            self.length -= 1
            self.max_heapify(0)
        return self._heap


if __name__ == '__main__':
    s = Solution()
    total = 0
    for _ in range(10):
        nums = [randint(1, 100000) for _ in range(100000)]
        start = time.time()
        s.heap_sort(nums)
        end = time.time()
        total += (end - start)
    print(f'10 times sort completed in {total} seconds')
    print(f'per time cost {total/10}')

'''
10 times sort completed in 9.289127349853516 seconds
per time cost 0.9289127349853515
'''
