class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        else:
            factor_2 = 2
            factor_3 = 0
            for i in range(4, n):
                if factor_2 > 0:
                    factor_2 -= 1
                    factor_3 += 1
                else:
                    factor_2 += 2
                    factor_3 -= 1
            return (2 ** factor_2 * 3 ** factor_3) % (10 ** 9 + 7)


for i in range(20):
    print(i, Solution().integerBreak(i))
