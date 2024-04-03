import sys
from collections import deque


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        if s[0] == '0':
            return -1
        beauty = []
        beauty_len = []
        for i in range(7):
            beauty.append(bin(5 ** i)[2:])
            beauty_len.append(bin(5 ** i).__len__() - 2)
        q = deque()
        q.append([[], s])
        ans = sys.maxsize
        while q:
            l, ss = q.popleft()
            n = ss.__len__()
            for i in range(1, n + 1):
                if ss[:i] in beauty:
                    if i == n:
                        ans = min(ans, l.__len__() + 1)
                    elif ss[i] != '0':
                        q.append([l + [ss[:i]], ss[i:]])
        return ans if ans != sys.maxsize else -1


print(Solution().minimumBeautifulSubstrings("1011"))
print(Solution().minimumBeautifulSubstrings("10110"))
print(Solution().minimumBeautifulSubstrings("111"))
print(Solution().minimumBeautifulSubstrings("0"))
