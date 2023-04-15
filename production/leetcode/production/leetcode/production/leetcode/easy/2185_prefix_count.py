from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for w in words:
            if w.__len__() >= pref.__len__() and w[:pref.__len__()] == pref:
                count += 1
        return count


print(Solution().prefixCount(words = ["leetcode","win","loops","success"], pref = "code"))
