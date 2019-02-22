class Solution:

    def OneWay(self, a, b):
        if abs(len(a) - len(b)) > 1:
            return False
        else:
            for i in range(len(a)):
                if a[i] != b[i]:
                    a = a[i:]
                    b = b[i:]
                    if len(a) == len(b):
                        return a[i + 1] == b[i + 1]
                    elif len(a) > len(b):
                        return a[i - 1] == b
                    else:
                        return a == b[i + 1]
            return True


if __name__ == '__main__':
    s = Solution()
    print(s.OneWay('plat', 'pls'))
