import sys
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = [[-1] * mat[0].__len__() for _ in range(mat.__len__())]

        # fill 0 first
        q = []
        for i in range(mat.__len__()):
            for j in range(mat[0].__len__()):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    q.append([i, j, 0])

        while q:
            x, y, num = q.pop(0)
            if x > 0 and result[x - 1][y] == -1:
                result[x - 1][y] = num + 1
                q.append([x - 1, y, num + 1])
            if x < mat.__len__() - 1 and result[x + 1][y] == -1:
                result[x + 1][y] = num + 1
                q.append([x + 1, y, num + 1])
            if y > 0 and result[x][y - 1] == -1:
                result[x][y - 1] = num + 1
                q.append([x, y - 1, num + 1])
            if y < mat[0].__len__() - 1 and result[x][y + 1] == -1:
                result[x][y + 1] = num + 1
                q.append([x, y + 1, num + 1])

        return result


# print(Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
# print(Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
print(
    Solution().updateMatrix(mat=[[0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]]))
