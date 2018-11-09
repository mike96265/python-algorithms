from functools import lru_cache


class Solution:

    def max_coins(self, nums: list):
        length = len(nums)
        val_index = {nums[i]: i for i in range(length)}



        # @lru_cache(maxsize=20000)
    # def solution(self, nums):
    #     max_coins = 0
    #     length = len(nums)
    #     if length == 0:
    #         return 0
    #     elif length == 1:
    #         return nums[0]
    #     elif length == 2:
    #         return max(nums[0], nums[1]) + nums[0] + nums[1]
    #     else:
    #         for i in range(length):
    #             temp_coins = nums[i]
    #             left = i - 1
    #             right = i + 1
    #             if left >= 0:
    #                 temp_coins *= nums[left]
    #             if right < length:
    #                 temp_coins *= nums[right]
    #             max_coins = max(max_coins, temp_coins + self.solution(nums[0: left + 1] + nums[right: length]))
    #         return max_coins


if __name__ == '__main__':
    s = Solution()
    print(s.max_coins([3, 21, 53, 24, 74, 35, 6, 38, 73, 87, 62, 30, 40, 82, 18, 79, 86, 70, 3, 96]))
