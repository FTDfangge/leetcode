# Given a string s consisting of words and spaces, return the length of the 
# last word in the string. 
# 
#  A word is a maximal substring consisting of non-space characters only. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of only English letters and spaces ' '. 
#  There will be at least one word in s. 
#  
# 
#  Related Topics 字符串 👍 605 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(" ")
        ptr = -1
        try:
            while s[ptr] != ' ':
                ptr -= 1
        except IndexError:
            pass
        return -ptr - 1


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().lengthOfLastWord("a"))
