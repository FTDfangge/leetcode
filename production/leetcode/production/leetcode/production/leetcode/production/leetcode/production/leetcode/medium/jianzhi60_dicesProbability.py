from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [[0.0] * (n * 6) for _ in range(n)]
        for i in range(6):
            dp[0][i] = 1 / 6
        for i in range(1, n):
            for j in range(i, (i + 1) * 6):
                for k in range(1, 7):
                    if j - k < 0:
                        break
                    dp[i][j] += dp[i - 1][j - k] / 6
        return dp[-1][n - 1:]


print(Solution().dicesProbability(1))
print(Solution().dicesProbability(2))
