import sys
from functools import cache
from typing import List


class Solution: # 1049 / 1055
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        n = grid.__len__()
        m = grid[0].__len__()

        # read_matrix = [[-1] * m for _ in range(n)]

        @cache
        def dfs(start_x: int, start_y: int) -> int:
            if (start_x, start_y) == (n - 1, m - 1):
                return 0
            if grid[start_x][start_y] == 0:
                return sys.maxsize
            ans = sys.maxsize
            max_step = grid[start_x][start_y]
            # right
            for next_y in range(start_y + 1, min(m, start_y + max_step + 1)):
                if (start_x, next_y) == (n - 1, m - 1):
                    return 1
                if grid[start_x][next_y] == 0:
                    continue
                ans = min(ans, dfs(start_x, next_y) + 1)
            # down
            for next_x in range(start_x + 1, min(n, start_x + max_step + 1)):
                if (next_x, start_y) == (n - 1, m - 1):
                    return 1
                if grid[next_x][start_y] == 0:
                    continue
                ans = min(ans, dfs(next_x, start_y) + 1)
            # read_matrix[start_x][start_y] = ans
            return ans

        result = dfs(0, 0)
        # print(read_matrix)
        if result > m + n:
            return -1
        return result + 1


print(Solution().minimumVisitedCells(grid=[[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]]))
print(Solution().minimumVisitedCells(grid=[[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]]))
print(Solution().minimumVisitedCells(grid=[[2, 1, 0], [1, 0, 0]]))
