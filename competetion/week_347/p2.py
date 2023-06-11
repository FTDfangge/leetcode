from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        n = grid.__len__()
        m = grid[0].__len__()
        ans = [[0] * m for _ in range(n)]

        def get_ans(r: int, c: int) -> int:
            init_r, init_c = r, c
            tl = set()
            br = set()
            while r > 0 and c > 0:
                r -= 1
                c -= 1
                tl.add(grid[r][c])
            r, c = init_r, init_c
            while r < n - 1 and c < m - 1:
                r += 1
                c += 1
                br.add(grid[r][c])
            return abs(tl.__len__() - br.__len__())

        for i in range(n):
            for j in range(m):
                ans[i][j] = get_ans(i, j)
        return ans
