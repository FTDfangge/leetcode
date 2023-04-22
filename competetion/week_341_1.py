from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_idx, max_count = 0, 0
        for idx, row in enumerate(mat):
            count = row.count(1)
            if count > max_count:
                max_idx = idx
                max_count = count
        return [max_idx, max_count]


print(Solution().rowAndMaximumOnes(mat=[[0, 1], [1, 0]]))
print(Solution().rowAndMaximumOnes(mat=[[0, 0, 0], [0, 1, 1]]))
print(Solution().rowAndMaximumOnes(mat=[[0, 0], [1, 1], [0, 0]]))
