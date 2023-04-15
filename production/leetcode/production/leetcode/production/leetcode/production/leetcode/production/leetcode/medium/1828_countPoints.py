import math
from typing import List


def cal_distance(point1: List[int], point2: List[int]) -> float:
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            count = 0
            for p in points:
                if cal_distance(p, [q[0], q[1]]) <= q[2]:
                    count += 1
            ans.append(count)
        return ans


print(Solution().countPoints(points=[[1, 3], [3, 3], [5, 3], [2, 2]], queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]]))
print(Solution().countPoints(points=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
                             queries=[[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]))
