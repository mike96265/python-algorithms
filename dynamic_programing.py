from collections import namedtuple
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


# class Solution(object):
#
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """
#         y = len(obstacleGrid)
#         x = len(obstacleGrid[0])
#         start = (0, 0)
#         points = [start]
#         num_map = [[0 for _ in range(x)] for _ in range(y)]
#         num_map[0][0] = 1
#         cache = {}


class TextJustification:
    cache = {}

    def solution(self, words, max_width):
        result = self.solut(words, max_width)
        last = ' '.join(result[-1].split())
        result[-1] = last + (max_width - len(last)) * ' '
        return result

    def solut(self, words, max_width):
        key = tuple(words)
        solu = self.cache.get((key, max_width))
        if solu is not None:
            return solu
        length = len(words)
        if length == 0:
            return []
        total_solutions = []
        for i in range(length, 0, -1):
            current = words[:i]
            remains = words[i:]
            len_cur = len(current)
            len_cur_str = len(''.join(current))
            interval = len_cur - 1
            if max_width < len_cur_str + interval:
                continue
            else:
                spaces = max_width - len_cur_str
                s = ''
                for item in current:
                    s += item
                    spaces_this_time = spaces / interval if interval > 1 else spaces
                    interval -= 1
                    if int(spaces_this_time) != spaces_this_time:
                        spaces_this_time = int(spaces_this_time) + 1
                    else:
                        spaces_this_time = int(spaces_this_time)
                    if spaces:
                        if current[0] != item:
                            s += spaces_this_time * ' '
                            spaces -= spaces_this_time
                        else:
                            s += spaces_this_time * ' '
                            spaces -= spaces_this_time
                total_solutions.append([s] + self.solut(remains, max_width))
        solu = sorted(total_solutions, key=len)[0]
        self.cache[(key, max_width)] = solu
        return solu


if __name__ == '__main__':
    s = TextJustification()
    print(s.solution(['a', 'b', 'c', 'd', 'e'], 3))
