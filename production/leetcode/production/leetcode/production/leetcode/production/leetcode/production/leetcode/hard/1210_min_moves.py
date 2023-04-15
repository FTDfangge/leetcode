import sys
from typing import List, Optional


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = grid.__len__()
        if grid[-1][-2] == 1 or grid[-1][-1] == 1:
            return -1
        step = {(0, 0, 0): 0}

        # snake is tail position and status, 0 is horizontal, 1 is vertical
        q = [[0, 0, 0]]
        while q:
            x, y, status = q.pop(0)
            current_step = step[(x, y, status)]
            if status == 0:  # horizontal
                # check right
                if y + 2 < n and grid[x][y + 2] == 0 and (x, y + 1, 0) not in step:
                    q.append([x, y + 1, 0])
                    step[(x, y + 1, 0)] = current_step + 1
                # check down and clockwise rotate
                if x + 1 < n and grid[x + 1][y] == 0 and grid[x + 1][y + 1] == 0:
                    # down
                    if (x + 1, y, 0) not in step:
                        q.append([x + 1, y, 0])
                        step[(x + 1, y, 0)] = current_step + 1
                    # rotate clockwise
                    if (x, y, 1) not in step:
                        q.append([x, y, 1])
                        step[(x, y, 1)] = current_step + 1
            else:  # vertical
                # check right and anti-clockwise rotate
                if y + 1 < n and grid[x][y + 1] == 0 and grid[x + 1][y + 1] == 0:
                    # right
                    if (x, y + 1, 1) not in step:
                        q.append([x, y + 1, 1])
                        step[(x, y + 1, 1)] = current_step + 1
                    # rotate anti-clockwise
                    if (x, y, 0) not in step:
                        q.append([x, y, 0])
                        step[(x, y, 0)] = current_step + 1
                # check down
                if x + 2 < n and grid[x + 2][y] == 0 and (x + 1, y, 1) not in step:
                    q.append([x + 1, y, 1])
                    step[(x + 1, y, 1)] = current_step + 1
        try:
            return step[(n - 1, n - 2, 0)]
        except KeyError:
            return -1


print(Solution().minimumMoves(grid=[[0, 0, 0, 0, 0, 1],
                                    [1, 1, 0, 0, 1, 0],
                                    [0, 0, 0, 0, 1, 1],
                                    [0, 0, 1, 0, 1, 0],
                                    [0, 1, 1, 0, 0, 0],
                                    [0, 1, 1, 0, 0, 0]]) == 11)
print(Solution().minimumMoves([[0, 0, 1, 1, 1, 1],
                               [0, 0, 0, 0, 1, 1],
                               [1, 1, 0, 0, 0, 1],
                               [1, 1, 1, 0, 0, 1],
                               [1, 1, 1, 0, 0, 1],
                               [1, 1, 1, 0, 0, 0]]
                              ) == 9)
print(Solution().minimumMoves(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
     [1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]) == -1)

print(Solution().minimumMoves([[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                               [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                               [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                               [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                               [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                               [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]) == 37)
