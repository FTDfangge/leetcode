import sys
from functools import cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        if s in dictionary:
            return 0
        dictionary = set(dictionary)

        @cache
        def dp(i, j):
            if s[i:j + 1] in dictionary:
                return 0
            elif j == i:
                return 1
            else:
                ans = sys.maxsize
                for k in range(i, j):
                    ans = min(ans, dp(i, k) + dp(k + 1, j))
                return ans

        return dp(0, s.__len__() - 1)


print(Solution().minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"]))
print(Solution().minExtraChar(s="sayhelloworld", dictionary=["hello", "world"]))
