from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n = grid.__len__()
        m = grid[0].__len__()
        ans = [0] * m
        for col in range(m):
            for row in range(n):
                ans[col] = max(ans[col], str(grid[row][col]).__len__())

        return ans
