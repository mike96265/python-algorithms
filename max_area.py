class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                max_area = max((right - left) * height[left], max_area)
                left += 1
            else:
                max_area = max((right - left) * height[right], max_area)
                right -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
