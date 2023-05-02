# Given a string s, determine if it is valid. 
# 
#  A string s is valid if, starting with an empty string t = "", you can 
# transform t into s after performing the following operation any number of times: 
# 
#  
#  Insert string "abc" into any position in t. More formally, t becomes tleft + 
# "abc" + tright, where t == tleft + tright. Note that tleft and tright may be 
# empty. 
#  
# 
#  Return true if s is a valid string, otherwise, return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aabcbc"
# Output: true
# Explanation:
# "" -> "abc" -> "aabcbc"
# Thus, "aabcbc" is valid. 
# 
#  Example 2: 
# 
#  
# Input: s = "abcabcababcc"
# Output: true
# Explanation:
# "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
# Thus, "abcabcababcc" is valid.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "abccba"
# Output: false
# Explanation: It is impossible to get "abccba" using the operation.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2 * 10⁴ 
#  s consists of letters 'a', 'b', and 'c' 
#  
# 
#  Related Topics 栈 字符串 👍 79 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = ['abc']
        for i in s:
            if i == 'a':
                if 'a' not in my_stack[-1]:
                    my_stack[-1] += 'a'
                else:
                    my_stack.append('a')
            elif i == 'b':
                if my_stack[-1] != 'a':
                    return False
                if 'b' not in my_stack[-1]:
                    my_stack[-1] += 'b'
                else:
                    my_stack.append('b')
            elif i == 'c':
                if my_stack[-1].__len__() == 2:
                    my_stack.pop()
                else:
                    return False
        return my_stack.__len__() == 1


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().isValid(s="aabcbc"))
print(Solution().isValid(s="abcabcababcc"))
print(Solution().isValid(s="abccba"))
print(Solution().isValid(s="bac"))
print(Solution().isValid(s="aaabc"))
