from random import randint
import time

class MaxHeap:

    def __init__(self, base: list):
        self._heap = base
        for i in reversed(range(len(self._heap) >> 1)):
            self.max_heapify(i)

    def max_heapify(self, i):
        length = len(self._heap)
        left = i << 1
        right = (i << 1) + 1
        if left < length and self._heap[left] > self._heap[i]:
            largest = left
        else:
            largest = i

        if right < length and self._heap[right] > self._heap[largest]:
            largest = right
        if largest != i:
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            self.max_heapify(largest)

    def pop(self):
        if self._heap:
            result = self._heap.pop(0)
            if self._heap:
                self._heap.insert(0, self._heap.pop())
                self.max_heapify(0)
            return result
        else:
            print('heap empty')

    def __bool__(self):
        return bool(self._heap)


if __name__ == '__main__':
    total = 0
    for i in range(100):
        b = [randint(1, 100000) for _ in range(100000)]
        start = time.time()
        a = MaxHeap(b)
        end = time.time()
        total += (end - start)

    print(f'100 times sort cost {total}')
    print(f'per sort cost {total/100}')

'''
100 times sort cost 9.855445861816406
per sort cost 0.09855445861816406
'''
