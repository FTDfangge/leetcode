import math


def add_a(s: str, a: int) -> str:
    for i in range(1, s.__len__(), 2):
        s = s[:i] + str((int(s[i]) + a) % 10) + s[i + 1:]
    return s


def add_a_even(s: str, a: int) -> str:
    for i in range(0, s.__len__(), 2):
        s = s[:i] + str((int(s[i]) + a) % 10) + s[i + 1:]
    return s


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        b = math.gcd(s.__len__(), b)
        ans = s
        add_times = 10 // math.gcd(10, a)
        # rotate
        for i in range(0, s.__len__(), b):
            temp = s
            for _ in range(add_times):
                temp = add_a(temp, a)
                if b % 2:
                    for _ in range(add_times):
                        temp = add_a_even(temp, a)
                        ans = min(ans, temp)
                else:
                    ans = min(ans, temp)
            s = s[-b:] + s[:-b]
        return ans


print(Solution().findLexSmallestString('5525', 9, 2))
print(Solution().findLexSmallestString("74", 5, 1))
