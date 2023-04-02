# Given two strings s and p, return an array of all the start indices of p's 
# anagrams in s. You may return the answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length, p.length <= 3 * 10⁴ 
#  s and p consist of lowercase English letters. 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 1135 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if s.__len__() < p.__len__():
            return []
        ans = []
        p_dict = dict()
        for i in p:
            try:
                p_dict[i] += 1
            except KeyError:
                p_dict[i] = 1
        for i in range(p.__len__()):
            try:
                p_dict[s[i]] -= 1
                if not p_dict[s[i]]:
                    p_dict.pop(s[i])
            except KeyError:
                p_dict[s[i]] = -1
        if not p_dict:
            ans.append(0)
        for starter in range(1, s.__len__() - p.__len__() + 1):
            try:
                p_dict[s[starter - 1]] += 1
                if not p_dict[s[starter - 1]]:
                    p_dict.pop(s[starter - 1])
            except KeyError:
                p_dict[s[starter - 1]] = 1

            try:
                p_dict[s[starter + p.__len__() - 1]] -= 1
                if not p_dict[s[starter + p.__len__() - 1]]:
                    p_dict.pop(s[starter + p.__len__() - 1])
            except KeyError:
                p_dict[s[starter + p.__len__() - 1]] = -1

            if not p_dict:
                ans.append(starter)

        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().findAnagrams(s="abab", p="ab"))
print(Solution().findAnagrams(s="cbaebabacd", p="abc"))
