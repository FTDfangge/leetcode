# There are n piles of coins on a table. Each pile consists of a positive 
# number of coins of assorted denominations. 
# 
#  In one move, you can choose any coin on top of any pile, remove it, and add 
# it to your wallet. 
# 
#  Given a list piles, where piles[i] is a list of integers denoting the 
# composition of the iᵗʰ pile from top to bottom, and a positive integer k, return the 
# maximum total value of coins you can have in your wallet if you choose exactly k 
# coins optimally. 
# 
#  
#  Example 1: 
#  
#  
# Input: piles = [[1,100,3],[7,8,9]], k = 2
# Output: 101
# Explanation:
# The above diagram shows the different ways we can choose k coins.
# The maximum total we can obtain is 101.
#  
# 
#  Example 2: 
# 
#  
# Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
# Output: 706
# Explanation:
# The maximum total can be obtained if we choose all coins from the last pile.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == piles.length 
#  1 <= n <= 1000 
#  1 <= piles[i][j] <= 10⁵ 
#  1 <= k <= sum(piles[i].length) <= 2000 
#  
# 
#  Related Topics 数组 动态规划 前缀和 👍 52 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        piles.sort(key=lambda x: -len(x))

        pre_sum = []
        for p in piles:
            temp = [0]
            for pp in p:
                temp.append(temp[-1] + pp)
            pre_sum.append(temp)

        # dp[i][j], ith pile from start, get j coins totally, the max gain
        dp = [[-1] * (k + 1) for _ in range(piles.__len__())]
        for i in range(piles.__len__()):
            dp[i][0] = 0
        dp[0] = pre_sum[0]

        total_pre = 0
        for i in range(1, piles.__len__()):
            total_pre += piles[i - 1].__len__()
            for j in range(1, k + 1):
                for kk in range(max(0, j - total_pre), j + 1):
                    try:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - kk] + pre_sum[i][kk])
                    except IndexError:
                        continue
        return dp[-1][k]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maxValueOfCoins(piles=[[1, 100, 3], [7, 8, 9]], k=2))
print(Solution().maxValueOfCoins(piles=[[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], k=7))
print(Solution().maxValueOfCoins([[37, 88], [51, 64, 65, 20, 95, 30, 26], [9, 62, 20], [44]], 9))
