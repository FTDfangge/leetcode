# Given an array of integers nums and an integer k, return the number of 
# contiguous subarrays where the product of all the elements in the subarray is strictly 
# less than k. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly 
# less than k.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3], k = 0
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  1 <= nums[i] <= 1000 
#  0 <= k <= 10⁶ 
#  
# 
#  Related Topics 数组 滑动窗口 👍 671 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        product = nums[0]
        ans = 0
        while left < nums.__len__() and right < nums.__len__():
            if product < k:
                ans += right - left + 1
                print(nums[left:right + 1])
                right += 1
                if right < nums.__len__():
                    product *= nums[right]
            else:
                product //= nums[left]
                left += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
print(Solution().numSubarrayProductLessThanK(nums=[10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], k=19))
print(Solution().numSubarrayProductLessThanK([57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75, 22], k=18))
