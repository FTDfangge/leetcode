from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotted = []
        num_of_not_rotted = 0
        for i in range(grid.__len__()):
            for j in range(grid[0].__len__()):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 1:
                    num_of_not_rotted += 1
                else:
                    rotted.append([i, j, 0])
        max_rot_number = 0
        while num_of_not_rotted:
            if not rotted:
                return -1
            x, y, rot_number = rotted.pop(0)
            if x > 0 and grid[x - 1][y] == 1:
                num_of_not_rotted -= 1
                rotted.append([x - 1, y, rot_number + 1])
                max_rot_number = max(max_rot_number, rot_number + 1)
                grid[x - 1][y] = 2
            if x < grid.__len__() - 1 and grid[x + 1][y] == 1:
                num_of_not_rotted -= 1
                rotted.append([x + 1, y, rot_number + 1])
                max_rot_number = max(max_rot_number, rot_number + 1)
                grid[x + 1][y] = 2
            if y > 0 and grid[x][y - 1] == 1:
                num_of_not_rotted -= 1
                rotted.append([x, y - 1, rot_number + 1])
                max_rot_number = max(max_rot_number, rot_number + 1)
                grid[x][y - 1] = 2
            if y < grid[0].__len__() - 1 and grid[x][y + 1] == 1:
                num_of_not_rotted -= 1
                rotted.append([x, y + 1, rot_number + 1])
                max_rot_number = max(max_rot_number, rot_number + 1)
                grid[x][y + 1] = 2
        return max_rot_number


# print(Solution().orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(Solution().orangesRotting(
[[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]]
))
