# Given an integer array nums that may contain duplicates, return all possible 
# subsets (the power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in 
# any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
#  Example 2: 
#  Input: nums = [0]
# Output: [[],[0]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
# 
#  Related Topics 位运算 数组 回溯 👍 1066 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = set()
        for i in range(pow(2, nums.__len__())):
            bin_str = bin(i)[2:].zfill(nums.__len__())
            s = []
            for index, fill in enumerate(bin_str):
                if fill == '1':
                    s.append(nums[index])
            s.sort()
            out.add(tuple(s))

        return list(map(list, out))


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().subsetsWithDup(nums=[1, 2, 2]))
print(Solution().subsetsWithDup(nums=[1, 2, 3]))
