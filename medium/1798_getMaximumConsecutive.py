import copy
from functools import cache
from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        max_consecutive = 0
        coins.sort()
        for i in coins:
            if i <= max_consecutive + 1:
                max_consecutive += i
            else:
                return max_consecutive + 1
        return max_consecutive + 1


print(Solution().getMaximumConsecutive(coins=[1, 3]) == 2)
print(Solution().getMaximumConsecutive(coins=[1, 1, 1, 4]) == 8)
print(Solution().getMaximumConsecutive(coins=[1, 4, 10, 3, 1]) == 20)
