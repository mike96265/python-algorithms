"""
输入一个随机灯矩阵,寻找把灯熄灭的办法

解题思路:
    1.可以利用穷举法,但是对于一个nxm的矩阵,有2^n*m个测试案例,所以时间复杂度很高

    2.考虑到每一个按键按两次的结果相当于异或,相互抵消所以每一个按键只能选择按或者不按两种选择
    试图使所有的为零,那么每一行确定枚举方案之后,因为此时只有之后的行能够影响到前面一行,相当于
    确定了第一行,后面一行的开关方案就只能把之前行全部熄灭当做目标,从而确定了开关方案.此时测试
    案例最少只有2^min(n, m)

"""
from copy import deepcopy
from pprint import pprint
import random


def solution(light_array):
    length = len(light_array)
    width = len(light_array[0])
    solution_first_line = []
    for i in range(0, 2 ** width):
        solution_first_line.append([int(j) for j in bin(i)[2:].zfill(width)])
    solution_container = []
    for i in solution_first_line:
        solution = i
        tmp_array = deepcopy(light_array)
        tmp_solution = []
        for y in range(0, length):
            tmp_solution.append(solution)
            pprint(solution)
            for x in range(0, width):
                effect_points = get_effect_points(x, y, solution[x], length, width)
                solution_process(tmp_array, effect_points)
            solution = [1 if i else 0 for i in tmp_array[y]]
            pprint(tmp_array)
        if not any(tmp_array[-1]):
            solution_container.append(tmp_solution)
    return solution_container


def get_effect_points(x, y, action, length, width):
    if action:
        return [(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if
                0 <= i < width and 0 <= j < length and abs(x - i) + abs(y - j) < 2]
    else:
        return []


def solution_process(light_array, effect_points):
    for x, y in effect_points:
        light_array[y][x] = 0 if light_array[y][x] else 1


def main():
    solution([[random.randint(0, 1) for i in range(6)] for i in range(5)])


if __name__ == '__main__':
    main()

'''
[1, 1, 1, 1, 1, 0]
[[1, 1, 1, 1, 1, 0],
 [1, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 1, 1],
 [1, 1, 1, 0, 1, 0]]
[1, 1, 1, 1, 1, 0]
[[0, 0, 0, 0, 0, 0],
 [1, 1, 1, 1, 0, 0],
 [0, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 1, 1],
 [1, 1, 1, 0, 1, 0]]
[1, 1, 1, 1, 0, 0]
[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 1],
 [0, 1, 1, 1, 1, 1],
 [1, 1, 1, 0, 1, 0]]
[0, 0, 0, 1, 0, 1]
[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 1, 0],
 [1, 1, 1, 1, 1, 1]]
[0, 1, 0, 0, 1, 0]
[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0]]

'''
