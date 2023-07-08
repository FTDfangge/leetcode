import sys
from collections import deque
from typing import List


def connect(s1: str, s2: str) -> str:
    if s1[-1] == s2[0]:
        return s1[:-1] + s2
    else:
        return s1 + s2


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        s = words[0]
        n = words.__len__()
        q = set()
        q.add(s)
        for i in range(1, n):
            temp = set()
            for ss in q:
                temp.add(connect(ss, words[i]))
                temp.add(connect(words[i], ss))
            q = temp
        ans = sys.maxsize
        for ii in q:
            ans = min(ans, ii.__len__())
        return ans


# print(Solution().minimizeConcatenatedLength(["aa", "bc", "bb"]))
print(Solution().minimizeConcatenatedLength(["ab", "ca", "a", "caa", "aa"]))
print(Solution().minimizeConcatenatedLength(
    ["c", "gae", "bf", "b", "gfhd", "j", "ge", "haffg", "gd", "ecad", "jbfd", "ehdc", "eigh", "f", "ciah", "ccf", "hc",
     "gdeae", "diib", "h", "ee"]))
