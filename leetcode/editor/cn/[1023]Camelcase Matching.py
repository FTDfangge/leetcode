# Given an array of strings queries and a string pattern, return a boolean 
# array answer where answer[i] is true if queries[i] matches pattern, and false 
# otherwise. 
# 
#  A query word queries[i] matches pattern if you can insert lowercase English 
# letters pattern so that it equals the query. You may insert each character at 
# any position and you may not insert any characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer",
# "ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
#  
# 
#  Example 2: 
# 
#  
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer",
# "ForceFeedBack"], pattern = "FoBa"
# Output: [true,false,true,false,false]
# Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
#  
# 
#  Example 3: 
# 
#  
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer",
# "ForceFeedBack"], pattern = "FoBaT"
# Output: [false,true,false,false,false]
# Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" +
#  "T" + "est".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= pattern.length, queries.length <= 100 
#  1 <= queries[i].length <= 100 
#  queries[i] and pattern consist of English letters. 
#  
# 
#  Related Topics 字典树 双指针 字符串 字符串匹配 👍 99 👎 0
from collections import deque
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        pattern_parts = []
        temp = ''
        for letter in pattern:
            if letter.isupper():
                if temp:
                    pattern_parts.append(temp)
                temp = letter
            else:
                temp += letter
        pattern_parts.append(temp)
        match = []

        def check(s: str) -> bool:

            s_parts = []
            _temp = ''
            for i in s:
                if i.isupper():
                    if _temp:
                        s_parts.append(_temp)
                    _temp = i
                else:
                    _temp += i
            s_parts.append(_temp)
            if s[0].islower() and pattern[0].isupper():
                s_parts = s_parts[1:]

            if s_parts.__len__() != pattern_parts.__len__():
                return False

            for i in range(s_parts.__len__()):
                if pattern_parts[i][0] != s_parts[i][0] and pattern_parts[i][0].isupper():
                    return False
                s1 = deque(pattern_parts[i])
                s2 = s_parts[i]
                for j in s2:
                    try:
                        if j == s1[0]:
                            s1.popleft()
                    except IndexError:
                        break
                if s1:
                    return False
            return True

        for q in queries:
            match.append(check(q))
        return match


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
#                             pattern="FoBaT"))
# print(Solution().camelMatch(
#     ["aksvbjLiknuTzqon", "ksvjLimflkpnTzqn", "mmkasvjLiknTxzqn", "ksvjLiurknTzzqbn", "ksvsjLctikgnTzqn",
#      "knzsvzjLiknTszqn"],
#     "ksvjLiknTzqn"))
print(Solution().camelMatch(
    ["uAxaqlzahfialcezsLfj", "cAqlzyahaslccezssLfj", "AqlezahjarflcezshLfj", "AqlzofahaplcejuzsLfj",
     "tAqlzahavslcezsLwzfj", "AqlzahalcerrzsLpfonj", "AqlzahalceaczdsosLfj", "eAqlzbxahalcezelsLfj"],
    "AqlzahalcezsLfj"))
