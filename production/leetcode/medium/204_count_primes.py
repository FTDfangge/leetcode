# -*- coding: utf-8 -*-
# @Time    : 2021-11-089:02 p.m.
# @Author  : raynor
# @FileName: 204_count_primes.py
# @Software: PyCharm

# AC

class Solution:
    def countPrimes(self, n: int) -> int:
        ans = 0
        isPrime = [1] * n
        for i in range(2, n):
            if isPrime[i]:
                ans += 1
                j = i
                while i * j < n:
                    isPrime[i * j] = 0
                    j += 1
        return ans


if __name__ == '__main__':
    print(Solution().countPrimes(10))
