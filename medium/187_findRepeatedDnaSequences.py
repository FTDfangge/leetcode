from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        n = s.__len__()
        DNA_dict = {s[:10]: 1}
        current = s[:10]

        for i in range(1, n - 9):
            current = current[1:] + s[i + 9]
            try:
                DNA_dict[current] += 1
            except KeyError:
                DNA_dict[current] = 1

        for i in DNA_dict.items():
            if i[1] > 1:
                ans.append(i[0])

        return ans


print(Solution().findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == ["AAAAACCCCC", "CCCCCAAAAA"])
print(Solution().findRepeatedDnaSequences(s="AAAAAAAAAAAAA") == ["AAAAAAAAAA"])
