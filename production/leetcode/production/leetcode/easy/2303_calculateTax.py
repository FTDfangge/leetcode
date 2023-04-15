from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        lower_bound = 0
        for i in brackets:
            if lower_bound < income <= i[0]:
                tax += (income - lower_bound) * i[1] / 100
                break
            elif income > i[0]:
                tax += (i[0] - lower_bound) * i[1] / 100
            lower_bound = i[0]

        return tax


print(Solution().calculateTax(brackets=[[3, 50], [7, 10], [12, 25]], income=10))
print(Solution().calculateTax([[1, 33]], 1))
