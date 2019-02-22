"""
Implement an algorithm to determine if a string has all unique characters.What if you use additional data structures
"""


class Solution:

    def isUnique(self, s):
        s_map = [0 for _ in range(200)]
        for i in s:
            if s_map[ord(i)] == 1:
                return False
            else:
                s_map[ord(i)] = 1
        return True
