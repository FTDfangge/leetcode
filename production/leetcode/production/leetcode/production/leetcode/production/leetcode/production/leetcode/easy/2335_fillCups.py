from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        ans = 0
        if amount[2] >= (amount[0] + amount[1]):
            return amount[2]
        else:
            while amount[1]:
                amount[1] -= 1
                amount[2] -= 1
                ans += 1
                amount.sort()
            ans += amount[2]
        return ans


print(Solution().fillCups(amount=[1, 4, 2]))
print(Solution().fillCups(amount=[5, 4, 4]))
print(Solution().fillCups(amount=[5, 0, 0]))
