import sys
from collections import deque
from functools import cache
from typing import List


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        start_x, start_y = start
        target_x, target_y = target

        special_roads = dict()
        for x1, y1, x2, y2, cost in specialRoads:
            if cost < abs(x2 - x1) + abs(y2 - y1):
                try:
                    special_roads[(x1, y1)].append((x2, y2, cost))
                except KeyError:
                    special_roads[(x1, y1)] = [(x2, y2, cost)]
        visited = dict()
        q = deque()
        q.append(start + [0])
        visited[(start_x, start_y)] = 0
        ans = abs(target_x - start_x) + abs(target_y - start_y)
        while q:
            x, y, spent = q.popleft()
            # up
            if ((x, y + 1) not in visited or visited[(x, y + 1)] > spent + 1) and y + 1 <= target_y:
                if (x, y + 1) == (target_x, target_y):
                    ans = min(ans, spent + 1)
                visited[(x, y + 1)] = spent + 1
                q.append([x, y + 1, spent + 1])
            # down
            if ((x, y - 1) not in visited or visited[(x, y - 1)] > spent + 1) and y - 1 >= start_y:
                if (x, y - 1) == (target_x, target_y):
                    ans = min(ans, spent + 1)
                visited[(x, y - 1)] = spent + 1
                q.append([x, y - 1, spent + 1])
            # left
            if ((x - 1, y) not in visited or visited[(x - 1, y)] > spent + 1) and x - 1 >= start_x:
                if (x - 1, y) == (target_x, target_y):
                    ans = min(ans, spent + 1)
                visited[(x - 1, y)] = spent + 1
                q.append([x - 1, y, spent + 1])
            # right
            if ((x + 1, y) not in visited or visited[(x + 1, y)] > spent + 1) and x + 1 <= target_x:
                if (x + 1, y) == (target_x, target_y):
                    ans = min(ans, spent + 1)
                visited[(x + 1, y)] = spent + 1
                q.append([x + 1, y, spent + 1])
            # special
            if (x, y) in special_roads:
                for tx, ty, cost in special_roads[(x, y)]:
                    if (tx, ty) not in visited or visited[(tx, ty)] > spent + cost:
                        if (tx, ty) == (target_x, target_y):
                            ans = min(ans, spent + cost)
                        visited[(tx, ty)] = spent + cost
                        q.append([tx, ty, spent + cost])
        return ans


print(Solution().minimumCost(start=[1, 1], target=[4, 5], specialRoads=[[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]]))
print(Solution().minimumCost(start=[3, 2], target=[5, 7],
                             specialRoads=[[3, 2, 3, 4, 4], [3, 3, 5, 5, 5], [3, 4, 5, 6, 6]]))
print(Solution().minimumCost([1, 1], [10, 4], [[4, 2, 1, 1, 3], [1, 2, 7, 4, 4], [10, 3, 6, 1, 2], [6, 1, 1, 2, 3]]))
print(Solution().minimumCost([1, 1], [10, 9], [[5, 2, 3, 6, 3], [5, 6, 9, 5, 3], [5, 9, 1, 2, 5], [8, 6, 9, 8, 1]]))
print(Solution().minimumCost([1, 1], [4, 8], [[2, 5, 1, 8, 1], [2, 5, 3, 2, 2], [2, 3, 2, 3, 5], [1, 6, 2, 7, 2]]))
print(Solution().minimumCost([1, 1],
                             [10, 8],
                             [[6, 4, 9, 7, 1], [5, 2, 2, 1, 3], [3, 2, 5, 5, 2]]))
