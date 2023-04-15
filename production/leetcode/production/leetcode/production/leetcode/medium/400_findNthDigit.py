class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        nth_range = 10
        last_nth_range = 10
        bits = 1
        while True:
            if n < nth_range:
                break
            else:
                bits += 1
                last_nth_range = nth_range
                nth_range += 9 * 10 ** (bits - 1) * bits

        target = (n - last_nth_range) // bits + 10 ** (bits - 1)
        mod = (n - last_nth_range) % bits
        print(target, mod)
        return int(str(target)[mod])


print(Solution().findNthDigit(3))
print(Solution().findNthDigit(11))
print(Solution().findNthDigit(27))
print(Solution().findNthDigit(198))
