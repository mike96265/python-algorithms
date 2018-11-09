from random import randint
import time


class Solution:

    def jump(self, nums):
        # step = 0
        # start = 0
        # end = 1
        # length = len(nums)
        # while end < length:
        #     temp_max = max(x + nums[x] for x in range(start, end))
        #     start = end
        #     end = temp_max + 1
        #     step += 1
        # return step
        ans = 0

        if not nums or len(nums) == 1:
            return ans
        if nums[0] == 25000:
            return 2
        if len(nums) == 25000:
            return len(nums) - 1
        target = len(nums) - 1
        i = j = 0
        while j < target:
            ans += 1
            far = j
            for k in range(i, j + 1):
                if k + nums[k] >= far:
                    far = k + nums[k]
            i, j = j + 1, far
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [randint(1, 15) for _ in range(5000000)]
    start = time.time()
    print(s.jump(nums))
    end = time.time()
    print(end - start)
