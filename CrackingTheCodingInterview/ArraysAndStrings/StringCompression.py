"""
Implement a method to perform basic compression using the counts of repeated characters,For example,the string
aaabcccccaaa would become a3b1c5a3.If "compressed" string would net become smaller than the original string,
your method should return the original string.You can assume the string has only uppercase and lowercase letters (a-z)
"""


class Solution:

    def StringCompression(self, s):
        compressed_s = ""
        temp = s[0]
        count = 0
        for i in s:
            if i == temp:
                count += 1
            else:
                compressed_s += '%s%s' % (temp, count)
                temp = i
                count = 1
        else:
            compressed_s += '%s%s' % (temp, count)
        if len(compressed_s) > len(s):
            return s
        else:
            return compressed_s


if __name__ == '__main__':
    s = Solution()
    print(s.StringCompression('aaabcccccaaa'))
