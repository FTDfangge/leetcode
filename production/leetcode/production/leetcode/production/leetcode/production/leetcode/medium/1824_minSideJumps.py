import sys
from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = obstacles.__len__()
        dp = [[-2] * 4 for _ in range(n)]
        dp[0] = [-1, 1, 0, 1]
        for i in range(1, n):
            for j in range(1, 4):
                if obstacles[i] == j:
                    continue
                dp[i][j] = sys.maxsize
                if dp[i - 1][j] != -1:
                    if dp[i - 1][j] >= 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j])
                for k in range(1, 4):
                    if k != j:
                        if dp[i - 1][k] >= 0 and obstacles[i] != k:
                            dp[i][j] = min(dp[i][j], dp[i - 1][k] + 1)
        ans = sys.maxsize
        for i in range(1, 4):
            if dp[-1][i] >= 0:
                ans = min(ans, dp[-1][i])
        return ans


print(Solution().minSideJumps(obstacles=[0, 1, 2, 3, 0]))
print(Solution().minSideJumps(obstacles=[0, 1, 1, 3, 3, 0]))
