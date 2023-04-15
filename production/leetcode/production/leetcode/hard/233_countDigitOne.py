class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        bits = str(n).__len__()
        for i in range(1, bits + 1):
            temp_ans = n // (10 ** i)
            remain = n % (10 ** i) - 10 ** (i - 1) + 1
            remain = max(remain, 0)
            remain = min(remain, 10 ** (i - 1))
            ans += temp_ans * 10 ** (i - 1) + remain

        return ans


print(Solution().countDigitOne(12) == 5)
print(Solution().countDigitOne(13) == 6)
print(Solution().countDigitOne(33) == 14)
print(Solution().countDigitOne(333) == 174)
