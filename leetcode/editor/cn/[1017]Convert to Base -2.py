# Given an integer n, return a binary string representing its representation in 
# base -2. 
# 
#  Note that the returned string should not have leading zeros unless the 
# string is "0". 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: "110"
# Explantion: (-2)² + (-2)¹ = 2
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: "111"
# Explantion: (-2)² + (-2)¹ + (-2)⁰ = 3
#  
# 
#  Example 3: 
# 
#  
# Input: n = 4
# Output: "100"
# Explantion: (-2)² = 4
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 10⁹ 
#  
# 
#  Related Topics 数学 👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        ans = [0] * 50
        base2 = bin(n)[2:][::-1]
        for i in range(base2.__len__()):
            if base2[i] == '1':
                if i % 2 == 0:
                    ans[i] += 1
                else:
                    ans[i + 1] += 1
                    ans[i] += 1
        for i in range(ans.__len__()):
            while ans[i] >= 2:
                if ans[i + 1] > 0:
                    ans[i + 1] -= 1
                    ans[i] -= 2
                    continue

                ans[i + 2] += 1
                ans[i + 1] += 1
                ans[i] -= 2
        ans = map(str, ans[::-1])
        return ''.join(ans).lstrip('0')


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().baseNeg2(100))
# print(Solution().baseNeg2(5))
# print(Solution().baseNeg2(14))
print(Solution().baseNeg2(6))
