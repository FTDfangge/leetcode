from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        remain = money - prices[0] - prices[1]
        if remain >= 0:
            return remain
        else:
            return money


print(Solution().buyChoco(prices=[1, 2, 2], money=3))
print(Solution().buyChoco(prices=[3, 2, 3], money=3))
