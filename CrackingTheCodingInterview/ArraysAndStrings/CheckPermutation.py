"""
Given two strings, write a method to decide if one is a permutation of the other.
"""
class Solution:

    def checkPermutation(self, s1, s2):
        s1_map = [0 for _ in range(200)]
        s2_map = [0 for _ in range(200)]
        for i in s1:
            s1_map[ord(i)] += 1
        for i in s2:
            s2_map[ord(i)] -= 1
        return s1_map == s2_map
