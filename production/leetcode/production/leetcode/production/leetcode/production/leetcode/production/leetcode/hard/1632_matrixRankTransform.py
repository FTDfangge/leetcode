import copy
from typing import List


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        num_list = []
        for i in range(matrix.__len__()):
            for j in range(matrix[0].__len__()):
                num_list.append([matrix[i][j], i, j])
        num_list = sorted(num_list, key=lambda x: x[0])
        pre = 1
        for idx, n in enumerate(num_list):
            matrix[n[1]][n[2]] = pre
            if idx > 0 and num_list[idx - 1][0] == n:
                continue
            else:
                pre += 1
        return matrix


print(Solution().matrixRankTransform(matrix=[[1, 2], [3, 4]]))
