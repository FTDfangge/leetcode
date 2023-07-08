from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = words.__len__()
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] == words[j][::-1]:
                    count += 1
        return count


print(Solution().maximumNumberOfStringPairs(words=["cd", "ac", "dc", "ca", "zz"]))
print(Solution().maximumNumberOfStringPairs(words=["ab", "ba", "cc"]))
