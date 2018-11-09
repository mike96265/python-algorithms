from functools import lru_cache


class Solution:

    def max_coins(self, nums):
        self.nums = nums
        end = len(nums)
        return self.solution(0, end)

    @lru_cache(maxsize=10000)
    def solution(self, start, end):
        if start == end:
            return 0
        else:
            max_coins = 0
            for i in range(start, end):
                temp_coins = self.nums[i]
                left = i - 1
                right = i + 1
                left_coins = 0
                right_coins = 0
                if left >= start:
                    temp_coins *= self.nums[left]
                    left_coins = self.solution(start, left)
                if right < end:
                    temp_coins *= self.nums[right]
                    right_coins = self.solution(right, end)
                max_coins = max(max_coins, temp_coins + left_coins + right_coins)
            return max_coins


if __name__ == '__main__':
    s = Solution()
    print(s.max_coins([3, 1, 5, 8]))
