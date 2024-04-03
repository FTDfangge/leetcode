import sys
from collections import defaultdict


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        total = dict()
        for i in range(26):
            ch = chr(ord('a') + i)
            total[ch] = 0
        count = 0
        for ll in s:
            if ll != '?':
                total[ll] += 1
            else:
                count += 1
        if count == 0:
            return s
        total_items = sorted(total.items(), key=lambda x: x[1])
        letters = []
        ptr = 0
        for _ in range(count):
            letters.append(total_items[ptr][0])
            total[total_items[ptr][0]] += 1
            total_items = sorted(total.items(), key=lambda x: x[1])
        letters.sort()
        ptr = 0

        ans = []
        for letter in s:
            if letter != '?':
                ans.append(letter)
            else:
                ans.append(letters[ptr])
                ptr += 1

        return ''.join(ans)


print(Solution().minimizeStringValue(s="???"))
print(Solution().minimizeStringValue(s="a?a?"))
print(Solution().minimizeStringValue("abcdefghijklmnopqrstuvwxy??"))
print(Solution().minimizeStringValue("fd????c?mkhfk?to?l??fgzkkup???qtia"))
