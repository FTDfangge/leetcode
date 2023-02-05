class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = dict()
        for i in s:
            if i not in char_dict:
                char_dict[i] = 1
            else:
                char_dict[i] += 1
        odd_count = 0
        for i in char_dict.items():
            if i[1] % 2 == 1:
                odd_count += 1
        if odd_count >= 1:
            return s.__len__() - odd_count + 1
        else:
            return s.__len__()


print(Solution().longestPalindrome(s="abccccdd"))
print(Solution().longestPalindrome(s="aaaaaccc"))
