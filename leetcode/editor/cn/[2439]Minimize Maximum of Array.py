# You are given a 0-indexed array nums comprising of n non-negative integers. 
# 
#  In one operation, you must: 
# 
#  
#  Choose an integer i such that 1 <= i < n and nums[i] > 0. 
#  Decrease nums[i] by 1. 
#  Increase nums[i - 1] by 1. 
#  
# 
#  Return the minimum possible value of the maximum integer of nums after 
# performing any number of operations. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,7,1,6]
# Output: 5
# Explanation:
# One set of optimal operations is as follows:
# 1. Choose i = 1, and nums becomes [4,6,1,6].
# 2. Choose i = 3, and nums becomes [4,6,2,5].
# 3. Choose i = 1, and nums becomes [5,5,2,5].
# The maximum integer of nums is 5. It can be shown that the maximum number 
# cannot be less than 5.
# Therefore, we return 5.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [10,1]
# Output: 10
# Explanation:
# It is optimal to leave nums as is, and since 10 is the maximum value, we 
# return 10.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  2 <= n <= 10⁵ 
#  0 <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics 贪心 数组 二分查找 动态规划 前缀和 👍 36 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pre_sum = [0]
        for i in nums:
            pre_sum.append(pre_sum[-1] + i)
        pre_sum = pre_sum[1:]
        dp = [0] * nums.__len__()
        dp[0] = nums[0]
        for i in range(1, nums.__len__()):
            temp = pre_sum[i] // (i + 1)
            temp += 1 if pre_sum[i] % (i + 1) else 0
            dp[i] = max(dp[i - 1], temp)
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().minimizeArrayValue([3, 7, 1, 6]))
print(Solution().minimizeArrayValue(nums=[10, 1]))
