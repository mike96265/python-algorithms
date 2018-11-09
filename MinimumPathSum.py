from collections import namedtuple
from random import randint


class MinimumPathSum:

    def minimum_path_sum(self, grid):
        x = len(grid[0])
        y = len(grid)
        new_point = namedtuple('point', ('x', 'y'))
        end = new_point(x - 1, y - 1)
        prev_points = [end]
        points_cache = [[None for _ in range(x)] for _ in range(y)]
        while prev_points:
            point = prev_points.pop(0)
            if points_cache[point.y][point.x] is not None:
                continue
            if point.y - 1 >= 0:
                prev_points.append(new_point(point.x, point.y - 1))
            if point.x - 1 >= 0:
                prev_points.append(new_point(point.x - 1, point.y))
            if point == end:
                points_cache[point.y][point.x] = grid[point.y][point.x]
            else:
                if point.x + 1 < x:
                    left_sum = points_cache[point.y][point.x + 1] + grid[point.y][point.x]
                else:
                    left_sum = float('inf')
                if point.y + 1 < y:
                    right_sum = points_cache[point.y + 1][point.x] + grid[point.y][point.x]
                else:
                    right_sum = float('inf')
                points_cache[point.y][point.x] = min(left_sum, right_sum)
        return points_cache[0][0]

        # x = len(grid[0])
        # y = len(grid)
        # new_point = namedtuple('point', ('x', 'y'))
        # start = new_point(0, 0)
        # end = new_point(x - 1, y - 1)
        # prev_points = [end]
        # points_cache = {}
        # while prev_points:
        #     point = prev_points.pop(0)
        #     if point in points_cache:
        #         continue
        #     if point.y - 1 >= 0:
        #         prev_points.append(new_point(point.x, point.y - 1))
        #     if point.x - 1 >= 0:
        #         prev_points.append(new_point(point.x - 1, point.y))
        #     if point == end:
        #         points_cache[end] = grid[end[1]][end[0]]
        #     else:
        #         if point.x + 1 < x:
        #             left_sum = points_cache[(point.x + 1, point.y)] + grid[point.y][point.x]
        #         else:
        #             left_sum = float('inf')
        #         if point.y + 1 < y:
        #             right_sum = points_cache[(point.x, point.y + 1)] + grid[point.y][point.x]
        #         else:
        #             right_sum = float('inf')
        #         points_cache[point] = min(left_sum, right_sum)
        # return points_cache.get(start)


if __name__ == '__main__':
    s = MinimumPathSum()
    print(s.minimum_path_sum([
        [randint(1, 100) for _ in range(100)]
        for _ in range(100)
    ]))
