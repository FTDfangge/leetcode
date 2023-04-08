# An integer array is called arithmetic if it consists of at least three 
# elements and if the difference between any two consecutive elements is the same. 
# 
#  
#  For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic 
# sequences. 
#  
# 
#  Given an integer array nums, return the number of arithmetic subarrays of 
# nums. 
# 
#  A subarray is a contiguous subsequence of the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,
# 2,3,4] itself.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5000 
#  -1000 <= nums[i] <= 1000 
#  
# 
#  Related Topics 数组 动态规划 👍 528 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
def from_consecutive_2_ans(consecutive: int) -> int:
    return (consecutive - 1) * consecutive // 2


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if nums.__len__() <= 2:
            return 0

        diffs = []
        ans = 0
        for i in range(1, nums.__len__()):
            diffs.append(nums[i] - nums[i - 1])
        # same_diff_count = []
        pre = diffs[0]
        temp_count = 1
        for d in diffs[1:]:
            if d == pre:
                temp_count += 1
            else:
                if temp_count >= 2:
                    # same_diff_count.append(temp_count)
                    ans += from_consecutive_2_ans(temp_count)
                temp_count = 1
                pre = d
        if temp_count >= 2:
            # same_diff_count.append(temp_count)
            ans += from_consecutive_2_ans(temp_count)
        # print(same_diff_count)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().numberOfArithmeticSlices([1, 2, 3, 4]))
