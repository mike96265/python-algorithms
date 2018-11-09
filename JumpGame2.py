class Solution:

    def jump(self, nums):
        step = 0
        start = 0
        end = 1
        length = len(nums)
        while end < length:
            temp_max = max(x + nums[x] for x in range(start, end))
            start = end
            end = temp_max + 1
            step += 1
        return step


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
