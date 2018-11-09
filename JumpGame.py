class Solution:

    def canjump(self, nums):
        length = len(nums)
        max_steps = 0
        for i in range(length):
            print(max_steps)
            if max_steps < i:
                return False
            elif max_steps > (length - 1):
                return True
            else:
                max_steps = max(max_steps, i + nums[i])
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canjump([3, 2, 1, 0, 4]))
