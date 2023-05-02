# Given three integers x, y, and bound, return a list of all the powerful 
# integers that have a value less than or equal to bound. 
# 
#  An integer is powerful if it can be represented as xⁱ + yʲ for some integers 
# i >= 0 and j >= 0. 
# 
#  You may return the answer in any order. In your answer, each value should 
# occur at most once. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation:
# 2 = 2⁰ + 3⁰
# 3 = 2¹ + 3⁰
# 4 = 2⁰ + 3¹
# 5 = 2¹ + 3¹
# 7 = 2² + 3¹
# 9 = 2³ + 3⁰
# 10 = 2⁰ + 3²
#  
# 
#  Example 2: 
# 
#  
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= x, y <= 100 
#  0 <= bound <= 10⁶ 
#  
# 
#  Related Topics 哈希表 数学 👍 87 👎 0
import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound <= 1:
            return []
        if x == 1 and y == 1:
            return [2]
        elif x == 1 or y == 1:
            x = max(x, y)
            ans = set()
            i_bound = int(math.log(bound, x)) + 1
            for i in range(i_bound):
                if x ** i + 1 > bound:
                    break
                ans.add(x ** i + 1)
            return list(ans)
        else:
            ans = set()
            i_bound = int(math.log(bound, x)) + 1
            j_bound = int(math.log(bound, y)) + 1
            for i in range(i_bound):
                for j in range(j_bound):
                    if x ** i + y ** j > bound:
                        break
                    ans.add(x ** i + y ** j)
            return list(ans)


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().powerfulIntegers(81, 21, 900000))
# print(Solution().powerfulIntegers(2, 1, 10))
print(Solution().powerfulIntegers(2, 3, 0))
