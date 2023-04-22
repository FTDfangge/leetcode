# Given an array nums of integers, return the length of the longest arithmetic 
# subsequence in nums. 
# 
#  Note that: 
# 
#  
#  A subsequence is an array that can be derived from another array by deleting 
# some or no elements without changing the order of the remaining elements. 
#  A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (
# for 0 <= i < seq.length - 1). 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,6,9,12]
# Output: 4
# Explanation:  The whole array is an arithmetic sequence with steps of length =
#  3.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [9,4,7,2,10]
# Output: 3
# Explanation:  The longest arithmetic subsequence is [4,7,10].
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [20,1,15,3,10,5,8]
# Output: 4
# Explanation:  The longest arithmetic subsequence is [20,15,10,5].
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 1000 
#  0 <= nums[i] <= 500 
#  
# 
#  Related Topics 数组 哈希表 二分查找 动态规划 👍 275 👎 0
from collections import defaultdict
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        max_diff = max(nums) - min(nums)
        ans = 1
        for diff in range(-max_diff, max_diff + 1):
            dp = dict()
            for i in nums:
                if i - diff in dp:
                    if i not in dp:
                        dp[i] = dp[i - diff] + 1
                    else:
                        dp[i] = max(dp[i], dp[i - diff] + 1)
                    ans = max(ans, dp[i])
                if i not in dp:
                    dp[i] = 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().longestArithSeqLength(nums=[3, 6, 9, 12]))
# print(Solution().longestArithSeqLength(nums=[9, 4, 7, 2, 10]))
print(Solution().longestArithSeqLength(nums=[20, 1, 15, 3, 10, 5, 8]))
