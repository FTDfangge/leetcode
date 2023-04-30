from collections import defaultdict
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = mat.__len__()
        m = mat[0].__len__()
        num_index_dict = dict()
        for i in range(n):
            for j in range(m):
                num_index_dict[mat[i][j]] = (i, j)
        colored_row = defaultdict(int)
        colored_col = defaultdict(int)
        for idx, i in enumerate(arr):
            x, y = num_index_dict[i]
            colored_row[x] += 1
            if colored_row[x] == m:
                return idx
            colored_col[y] += 1
            if colored_col[y] == n:
                return idx
        return -1


print(Solution().firstCompleteIndex(arr=[1, 3, 4, 2], mat=[[1, 4], [2, 3]]))
print(Solution().firstCompleteIndex(arr=[2, 8, 7, 4, 1, 3, 5, 6, 9], mat=[[3, 2, 5], [1, 4, 6], [8, 7, 9]]))
