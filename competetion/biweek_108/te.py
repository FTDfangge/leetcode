from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        counting = [[0] * (n - 1) for _ in range(m - 1)]
        ans = [0] * 5
        ans[0] = (m - 1) * (n - 1)
        for x, y in coordinates:
            try:
                counting[x][y] += 1
                ans[counting[x][y]] += 1
                ans[counting[x][y] - 1] -= 1
            except IndexError:
                pass
            if x > 0:
                try:
                    counting[x - 1][y] += 1
                    ans[counting[x - 1][y]] += 1
                    ans[counting[x - 1][y] - 1] -= 1
                except IndexError:
                    pass
            if y > 0:
                try:
                    counting[x][y - 1] += 1
                    ans[counting[x][y - 1]] += 1
                    ans[counting[x][y - 1] - 1] -= 1
                except IndexError:
                    pass
            if x > 0 and y > 0:
                try:
                    counting[x - 1][y - 1] += 1
                    ans[counting[x - 1][y - 1]] += 1
                    ans[counting[x - 1][y - 1] - 1] -= 1
                except IndexError:
                    pass
        return ans

[3, 1, 0, 0, 0]
[0, 2, 2, 0, 0]
[1387, 122, 3, 0, 0]
print(Solution().countBlackBlocks(m=3, n=3, coordinates=[[0, 0]]))
print(Solution().countBlackBlocks(m=3, n=3, coordinates=[[0, 0], [1, 1], [0, 2]]))
print(Solution().countBlackBlocks(22, 73,
                                  [[11, 14], [16, 11], [20, 5], [5, 33], [14, 7], [16, 60], [0, 15], [15, 72], [6, 60],
                                   [9, 16], [14, 51], [1, 52], [18, 24], [17, 30], [3, 4], [19, 13], [9, 10], [11, 40],
                                   [15, 7], [13, 62], [8, 41], [12, 71], [4, 72], [18, 7], [1, 0], [4, 35], [16, 33],
                                   [7, 30], [13, 52], [5, 1], [15, 21], [3, 59], [2, 41], [4, 28]]))
