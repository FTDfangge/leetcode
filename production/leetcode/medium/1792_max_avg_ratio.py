from heapq import *
from typing import List


class Entry:
    __slots__ = 'p', 't'

    def __init__(self, p: int, t: int):
        self.p = p
        self.t = t

    def __lt__(self, b: 'Entry') -> bool:
        return (self.t - self.p) * b.t * (b.t + 1) > (b.t - b.p) * self.t * (self.t + 1)


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [Entry(*c) for c in classes]
        heapify(h)
        for _ in range(extraStudents):
            heapreplace(h, Entry(h[0].p + 1, h[0].t + 1))
        return sum(e.p / e.t for e in h) / len(h)


print(Solution().maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2))
print(Solution().maxAverageRatio(classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4))
