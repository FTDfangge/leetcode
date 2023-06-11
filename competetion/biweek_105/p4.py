import math
from functools import cache
from typing import List


class Dsu:
    def __init__(self, size: int):
        self.pa = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x) -> int:
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.pa[y] = x
        self.size[x] += self.size[y]

    def beautify(self):
        for i in range(self.pa.__len__()):
            self.find(i)

    def check_connected(self, x, y) -> bool:
        return self.pa[x] == self.pa[y]

    def check_all_connected(self) -> bool:
        return set(self.pa).__len__() == 1


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        @cache
        def gcd(i, j)->bool:
            return math.gcd(nums[i], nums[j]) > 1
        n = nums.__len__()
        dsu = Dsu(n)
        for i in range(n - 1):
            for j in range(i, n):
                if dsu.check_connected(i, j):
                    continue
                if math.gcd(nums[i], nums[j]) > 1:
                    dsu.union(i, j)
            if dsu.check_all_connected():
                return True
        dsu.beautify()
        return dsu.check_all_connected()


print(Solution().canTraverseAllPairs([2, 3, 6]))
