# There is a bag that consists of items, each item has a number 1, 0, or -1 
# written on it. 
# 
#  You are given four non-negative integers numOnes, numZeros, numNegOnes, and 
# k. 
# 
#  The bag initially contains: 
# 
#  
#  numOnes items with 1s written on them. 
#  numZeroes items with 0s written on them. 
#  numNegOnes items with -1s written on them. 
#  
# 
#  We want to pick exactly k items among the available items. Return the 
# maximum possible sum of numbers written on the items. 
# 
#  
#  Example 1: 
# 
#  
# Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
# Output: 2
# Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 
# 0}. We take 2 items with 1 written on them and get a sum in a total of 2.
# It can be proven that 2 is the maximum possible sum.
#  
# 
#  Example 2: 
# 
#  
# Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
# Output: 3
# Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 
# 0}. We take 3 items with 1 written on them, and 1 item with 0 written on it, 
# and get a sum in a total of 3.
# It can be proven that 3 is the maximum possible sum.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= numOnes, numZeros, numNegOnes <= 50 
#  0 <= k <= numOnes + numZeros + numNegOnes 
#  
# 
#  Related Topics 贪心 数学 👍 35 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        total = 0
        if numOnes >= k:
            return k
        else:
            total += numOnes
            k -= numOnes

        if numZeros >= k:
            return total
        else:
            k -= numZeros
        return total - k


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().kItemsWithMaximumSum(6, 6, 6, 13))
