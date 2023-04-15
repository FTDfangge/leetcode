class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        n = abs(num)
        s = ''
        while n:
            s = str(n % 7) + s
            n //= 7
        if num < 0:
            return '-' + s
        else:
            return s


print(Solution().convertToBase7(100))
