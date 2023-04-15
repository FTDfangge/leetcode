class Solution:
    def toHex(self, num: int) -> str:
        h_str = '0123456789abcdef'
        if num < 0:
            num = pow(2, 32) + num
        if num == 0:
            return '0'
        else:
            ans = ''
            while num:
                ans = h_str[num % 16] + ans
                num //= 16
            return ans

print(Solution().toHex(26))
print(Solution().toHex(-1))