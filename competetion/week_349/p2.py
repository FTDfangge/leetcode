class Solution:
    def smallestString(self, s: str) -> str:
        start = 0
        ans = ''
        for idx, i in enumerate(s):
            if i == 'a':
                ans += i
                continue
            start = idx
            break
        else:
            return ans[:-1] + 'z'
        for end in range(start, s.__len__()):
            if s[end] != 'a':
                ans += chr(ord(s[end]) - 1)
                continue
            break
        else:
            return ans
        ans += s[end:]
        return ans


# print(Solution().smallestString(s="cbabc"))
# print(Solution().smallestString("acbbc"))
# print(Solution().smallestString("leetcode"))
print(Solution().smallestString("a"))
print(Solution().smallestString("aa"))
