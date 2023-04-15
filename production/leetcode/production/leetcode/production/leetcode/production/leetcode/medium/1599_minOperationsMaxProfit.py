from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = customers.__len__()
        if 4 * boardingCost <= runningCost:
            return -1
        wait = 0
        income = 0
        cost = 0
        max_profit, index = 0, -1
        time = 0
        while wait or time in range(n):
            try:
                wait += customers[time]
            except IndexError:
                pass
            go_up = min(4, wait)
            wait -= go_up
            income += go_up * boardingCost
            cost += runningCost
            profit = income - cost
            time += 1
            if profit > max_profit:
                max_profit = profit
                index = time
        return index


print(Solution().minOperationsMaxProfit(customers=[8, 3], boardingCost=5, runningCost=6))
print(Solution().minOperationsMaxProfit(customers=[10, 9, 6], boardingCost=6, runningCost=4))
print(Solution().minOperationsMaxProfit(customers=[3, 4, 0, 5, 1], boardingCost=1, runningCost=92))
print(Solution().minOperationsMaxProfit([0, 0, 0, 0, 0, 50], 100, 1))
