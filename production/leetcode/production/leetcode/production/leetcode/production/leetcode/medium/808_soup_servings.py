# -*- coding: utf-8 -*-
# @Time    : 2022-11-21 12:03 p.m.
# @Author  : qkzhong
# @FileName: 808_soup_servings.py
# @Software: PyCharm


class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 179 * 25:
            return 1.0
        n = (n + 24) // 25
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0.5
        for x in range(1, n + 1):
            dp[0][x] = 1.0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][max(0, j - 1)] + dp[max(0, i - 2)][max(0, j - 2)] +
                            dp[max(0, i - 1)][max(0, j - 3)]) / 4

        return dp[n][n]


print(Solution().soupServings(1))
