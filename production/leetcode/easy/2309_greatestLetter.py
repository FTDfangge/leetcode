class Solution:
    def greatestLetter(self, s: str) -> str:
        best = ''
        upper = [0] * 26
        lower = [0] * 26
        for i in s:
            if i.isupper():
                n = ord(i) - ord('A')
                upper[n] = 1
                if lower[n] == 1:
                    if i > best:
                        best = i
            elif i.islower():
                n = ord(i) - ord('a')
                lower[n] = 1
                if upper[n] == 1:
                    if i.upper() > best:
                        best = i.upper()
        return best


print(Solution().greatestLetter(s="lEeTcOdE"))
print(Solution().greatestLetter(s="arRAzFif"))
print(Solution().greatestLetter(s="AbCdEfGhIjK"))
