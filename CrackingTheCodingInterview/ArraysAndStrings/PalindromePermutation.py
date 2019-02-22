"""
Given a string,write a function to check if it is a permutation of a palindrome.A palindrome is
a word or phrase that is the same forwards and backwards.A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

EXAMPLE:
    Input: Tact Coa
    Output: true (permutations: "taco cat", "atco cta", etc.)
"""


class Solution:

    def PalindromePermutation(self, s: str):
        s = s.replace(' ', '').lower()
        s_map = [0 for _ in range(200)]
        for i in s:
            s_map[ord(i)] += 1
        odd_flag = 0
        for i in s_map:
            if i & 1 == 1:
                if odd_flag == 1:
                    return False
                else:
                    odd_flag += 1
        return True
