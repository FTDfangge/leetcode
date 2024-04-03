# Given a string s and an integer k, return the number of substrings in s of 
# length k with no repeated characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "havefunonleetcode", k = 5
# Output: 6
# Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno',
# 'etcod','tcode'.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "home", k = 5
# Output: 0
# Explanation: Notice k can be larger than the length of s. In this case, it is 
# not possible to find any substring.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of lowercase English letters. 
#  1 <= k <= 10⁴ 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 57 👎 0
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > s.__len__():
            return 0
        letter_dict = defaultdict(int)
        front = 0
        back = 0
        distinct_dict = set()
        ans = 0
        while back < k:
            letter_dict[s[back]] += 1
            if letter_dict[s[back]] >= 2:
                distinct_dict.add(s[back])
            back += 1

        if not distinct_dict:
            ans += 1
        while back < s.__len__():
            letter_dict[s[back]] += 1
            if letter_dict[s[back]] >= 2:
                distinct_dict.add(s[back])
            letter_dict[s[front]] -= 1
            if letter_dict[s[front]] == 1:
                distinct_dict.remove(s[front])
            if not distinct_dict:
                ans += 1
            front += 1
            back += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().numKLenSubstrNoRepeats(s="havefunonleetcode", k=5))
# print(Solution().numKLenSubstrNoRepeats(s="home", k=5))
print(Solution().numKLenSubstrNoRepeats(
    "gdggdbjchgadcfddfahbdebjbagaicgeahehjhdfghadbcbbfhgefcihbcbjjibjdhfhbdijehhiabad",
    5))
