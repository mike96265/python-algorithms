class Solution:

    def mOut(self, total, M):
        ind = 0
        for i in range(2, total + 1):
            ind = (ind + M) % i
            # if not ind:
            #     ind = i
        print(ind + 1)


"""
0 1 2 3 4 5 6 7 8 9
0 1 2 3   5 6 7 8
0 1 2 3     6 7 8
0   2 3     6 7 8
0   2 3     6 7
0   2 3     6
    2 3     6
    2       6
    2 
"""

if __name__ == '__main__':
    s = Solution()
    s.mOut(10, 5)
