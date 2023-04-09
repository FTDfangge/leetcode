# Given two integers left and right that represent the range [left, right], 
# return the bitwise AND of all numbers in this range, inclusive. 
# 
#  
#  Example 1: 
# 
#  
# Input: left = 5, right = 7
# Output: 4
#  
# 
#  Example 2: 
# 
#  
# Input: left = 0, right = 0
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: left = 1, right = 2147483647
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= left <= right <= 2³¹ - 1 
#  
# 
#  Related Topics 位运算 👍 448 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0:
            return 0

        if bin(right).__len__() > bin(left).__len__():
            return 0
        max_bit = bin(right).__len__() - 3
        return self.rangeBitwiseAnd(left - 2 ** max_bit, right - 2 ** max_bit) + 2 ** max_bit


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().rangeBitwiseAnd(0, 0))
