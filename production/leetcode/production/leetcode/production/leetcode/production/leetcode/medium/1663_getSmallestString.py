def int2char(num: int) -> str:
    return chr(ord('a') - 1 + num)


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        s = ''
        for i in range(n - 1, -1, -1):
            if k >= 25:
                s = 'z' + s
                k -= 25
            else:
                s = int2char(k + 1) + s
                break
        while s.__len__() < n:
            s = 'a' + s
        return s


print(Solution().getSmallestString(n=3, k=27))
print(Solution().getSmallestString(n=5, k=73))
