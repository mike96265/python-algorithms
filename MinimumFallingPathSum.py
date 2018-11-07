from functools import lru_cache


class MinimumFallingPathSum:

    def solution(self, A):
        length = len(A)
        self.A = A
        min_sum = float('inf')
        for i in range(length):
            min_sum = min(min_sum, self.find_min_falling_path(0, i, length))
        return min_sum

    @lru_cache(maxsize=1000)
    def find_min_falling_path(self, row, column, length):
        if row == length - 1:
            return self.A[row][column]
        else:
            next_points = [column]
            if column > 0:
                next_points.append(column - 1)
            if column < length - 1:
                next_points.append(column + 1)
            temp_min = float('inf')
            for i in next_points:
                temp_min = min(temp_min, self.A[row][column] + self.find_min_falling_path(row + 1, i, length))
            return temp_min


if __name__ == '__main__':
    s = MinimumFallingPathSum()
    print(s.solution([[51,24],[-50,82]]))
