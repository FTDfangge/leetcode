class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_dict = dict()
        start = 0
        end = -1
        max_len = 0
        while end < s.__len__():
            if char_dict.__len__() <= k:
                max_len = max(max_len, end - start + 1)
                end += 1
                try:
                    char_dict[s[end]] += 1
                except KeyError:
                    char_dict[s[end]] = 1
                except IndexError:
                    break
            else:
                char_dict[s[start]] -= 1
                if char_dict[s[start]] == 0:
                    char_dict.pop(s[start])
                start += 1
        return max_len


print(Solution().lengthOfLongestSubstringKDistinct('eceba', 2))
print(Solution().lengthOfLongestSubstringKDistinct(s="aa", k=1))
