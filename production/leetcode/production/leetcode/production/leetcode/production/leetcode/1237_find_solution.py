from typing import List


class CustomFunction:
    def f(self, x, y) -> int:
        return x + y


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        q = [[1, 1]]
        visited = [[1, 1]]
        ans = []
        while q:
            x, y = q.pop(0)
            result = customfunction.f(x, y)
            if result < z:  # go right and up
                if [x + 1, y] not in visited:
                    visited.append([x + 1, y])
                    q.append([x + 1, y])
                if [x, y + 1] not in visited:
                    visited.append([x, y + 1])
                    q.append([x, y + 1])
            elif result > z:  # go down and left
                if x > 2 and [x - 1, y] not in visited:
                    visited.append([x - 1, y])
                    q.append([x - 1, y])
                if y > 2 and [x, y - 1] not in visited:
                    visited.append([x, y - 1])
                    q.append([x, y - 1])
            else:  # equals
                ans.append([x, y])
                if x > 2 and [x - 1, y + 1] not in visited:
                    visited.append([x - 1, y + 1])
                    q.append([x - 1, y + 1])
                if y > 2 and [x + 1, y - 1] not in visited:
                    visited.append([x + 1, y - 1])
                    q.append([x + 1, y - 1])
        return ans


print(Solution().findSolution(CustomFunction(), 5))
