# Given an array nums of n integers, return an array of all the unique 
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that: 
# 
#  
#  0 <= a, b, c, d < n 
#  a, b, c, and d are distinct. 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 1633 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        num_dict = dict()
        ans = set()
        n = nums.__len__()

        # init num dict
        for xx in range(n):
            try:
                num_dict[nums[xx]].append(xx)
            except KeyError:
                num_dict[nums[xx]] = [xx]

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    s = nums[i] + nums[j] + nums[k]
                    if target - s in num_dict:
                        for t in num_dict[target - s]:
                            if t not in (i, j, k):
                                break
                        else:
                            continue
                        temp = [nums[i], nums[j], nums[k], target - s]
                        temp.sort()
                        ans.add(tuple(temp))
        ans = list(map(list, ans))
        return list(ans)


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
print(Solution().fourSum(nums=[2, -4, -5, -2, -3, -5, 0, 4, -2], target=-14))
