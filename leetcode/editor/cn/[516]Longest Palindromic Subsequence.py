# Given a string s, find the longest palindromic subsequence's length in s. 
# 
#  A subsequence is a sequence that can be derived from another sequence by 
# deleting some or no elements without changing the order of the remaining elements. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consists only of lowercase English letters. 
#  
# 
#  Related Topics 字符串 动态规划 👍 1004 👎 0
from functools import cache


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        print_matrix = [[0] * s.__len__() for _ in range(s.__len__())]

        # dp(i,j) is from s[i] to s[j], the max length of palindrome
        @cache
        def dp(i: int, j: int) -> int:
            if not 0 <= i <= j < s.__len__():
                print_matrix[i][j] = 0
                return 0
            if i == j:
                print_matrix[i][j] = 1
                return 1
            if s[i] == s[j]:
                print_matrix[i][j] = 2 + dp(i + 1, j - 1)
                return 2 + dp(i + 1, j - 1)
            else:
                print_matrix[i][j] = max(dp(i + 1, j), dp(i, j - 1))
                return max(dp(i + 1, j), dp(i, j - 1))

        return dp(0, s.__len__() - 1)


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().longestPalindromeSubseq('bbbab'))
