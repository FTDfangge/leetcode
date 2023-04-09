# Given an integer array nums, return the number of longest increasing 
# subsequences. 
# 
#  Notice that the sequence has to be strictly increasing. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 
# 3, 5, 7].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there 
# are 5 increasing subsequences of length 1, so output 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2000 
#  -10⁶ <= nums[i] <= 10⁶ 
#  
# 
#  Related Topics 树状数组 线段树 数组 动态规划 👍 722 👎 0
from typing import List


class Solution2:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n, max_len, ans = len(nums), 0, 0
        dp = [1] * n
        cnt = [1] * n
        for i, x in enumerate(nums):
            for j in range(i):
                if x > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]  # 重置计数
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > max_len:
                max_len = dp[i]
                ans = cnt[i]  # 重置计数
            elif dp[i] == max_len:
                ans += cnt[i]
        return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = nums.__len__()
        # dp[i] is end at nums[i], length of LIS
        dp = [1] * n
        count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j] + 1:
                        count[i] += count[j]
                    elif dp[i] < dp[j] + 1:
                        dp[i] = max(dp[i], dp[j] + 1)
                        count[i] = count[j]

        max_len = max(dp)

        ans = 0
        for i in range(n):
            if dp[i] == max_len:
                ans += count[i]
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().findNumberOfLIS(nums=[1, 3, 5, 4, 7]))
# print(Solution().findNumberOfLIS(nums=[2, 2, 2, 2, 2]))
print(Solution().findNumberOfLIS(nums=[1, 2, 4, 3, 5, 4, 7, 2]))
