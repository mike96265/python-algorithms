from functools import lru_cache


class Solution:

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        nums = tuple(nums)
        return max(self.max_rob(nums, 0, length), self.max_rob(nums, 1, length))

    @lru_cache(maxsize=1000)
    def max_rob(self, nums, start, end):
        if start >= end:
            return 0
        return max(nums[start] + self.max_rob(nums, start + 2, end), nums[start] + self.max_rob(nums, start + 3, end))


if __name__ == '__main__':
    s = Solution()
    print(s.rob([12, 13, 1, 8, 2, 8, 15, 9, 5, 1, 8, 14, 7, 4, 8, 7, 5, 11, 3, 2, 1, 12, 3]))
