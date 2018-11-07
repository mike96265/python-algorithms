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


class LongestCommonSequence:

    @lru_cache(maxsize=10000)
    def solution(self, x, y):
        m = len(x)
        n = len(y)
        if 0 in (m, n):
            return ''
        if x[m - 1] == y[n - 1]:
            s = x[m - 1]
            return self.solution(x[:-1], y[:-1]) + s
        else:
            left = self.solution(x[:-1], y)
            right = self.solution(x, y[:-1])
            return left if len(left) > len(right) else right


# class LongestValidParentheses:
#
#     @lru_cache(maxsize=1000)
#     def longestValidParentheses(self, s):
#         length = len(s)
#         if length < 2:
#             if s != '()':
#                 return 0
#             else:
#                 return 2
#         else:
#             spilt_result = []
#             for split_position in range(1, length):
#                 left = self.longestValidParentheses(s[:split_position])
#                 if s[split_position - 1: split_position+1] == '()':
#                     middle = 2
#                     left_start = split_position - 2
#                     right_start = split_position + 1
#                     while True:
#                         try:
#                             if s[left_start] == '(' and s[right_start] == ')' \
#                                   and left_start >= 0 and right_start <= length:
#                                 left_start -= 1
#                                 right_start += 1
#                                 middle += 2
#                             else:
#                                 break
#                         except IndexError:
#                             break
#                 else:
#                     middle = 0
#                     left_start = split_position - 1
#                     right_start = split_position
#                 for i in range(left_start, 0, -2):
#                     if s[i - 1: i + 1] != '()':
#                         break
#                     middle += 2
#                 for i in range(right_start, length, 2):
#                     if s[i: i+2] != '()':
#                         break
#                     middle += 2
#                 right = self.longestValidParentheses(s[split_position:])
#                 spilt_result.append(max(left, middle, right))
#             return max(spilt_result)


'''
public class Solution {

    public int longestValidParentheses(String s) {
        int maxans = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.empty()) {
                    stack.push(i);
                } else {
                    maxans = Math.max(maxans, i - stack.peek());
                }
            }
        }
        return maxans;
    }
}
'''


class LongestValidParentheses:

    def longestValidParentheses(self, s):
        longest = 0
        stack = list()
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    longest = max(longest, i - stack[-1])
                else:
                    stack.append(i)
        return longest


class ClimbingStairs:

    @lru_cache(maxsize=1000)
    def climbStairs(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find_max_subarray(0, len(nums) - 1, nums)

    def find_max_subarray(self, left, right, nums):
        mid = (right + left) // 2
        if left == right:
            return nums[left]
        left_max = self.find_max_subarray(left, mid, nums)
        right_max = self.find_max_subarray(mid + 1, right, nums)
        mid_max = self.find_max_mid_subarray(left, right, mid, nums)
        return max(left_max, right_max, mid_max)

    def find_max_mid_subarray(self, left, right, mid, nums):
        left_max_sum = float('-inf')
        left_sum = 0
        for i in range(mid, left - 1, -1):
            left_sum = nums[i] + left_sum
            if left_sum > left_max_sum:
                left_max_sum = left_sum
        right_max_sum = float('-inf')
        right_sum = 0
        for i in range(mid + 1, right + 1):
            right_sum += nums[i]
            if right_sum > right_max_sum:
                right_max_sum = right_sum
        return left_max_sum + right_max_sum


if __name__ == '__main__':
    '''text justification test'''
    # s = TextJustification()
    # print(s.solution(['a', 'b', 'c', 'd', 'e'], 3))
    # s = LongestCommonSequence()
    # print(s.solution())
    '''longest valid parentheses test'''
    # s = LongestValidParentheses()
    # print(s.longestValidParentheses("()()((()()"))
    '''climbing stairs test'''
    # s = ClimbingStairs()
    # s.climbStairs(3)
    '''max subarray test'''
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
