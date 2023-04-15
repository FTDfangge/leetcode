class Solution:
    def countHomogenous(self, s: str) -> int:
        result = -1
        pre = '-'
        continue_count = 1
        for i in s:
            if i == pre:
                continue_count += 1
            else:
                result += (1 + continue_count) * continue_count // 2
                continue_count = 1
                pre = i
        result += (1 + continue_count) * continue_count // 2
        return result % (pow(10, 9) + 7)


print(Solution().countHomogenous(s="abbcccaa"))
print(Solution().countHomogenous(s="xy"))
print(Solution().countHomogenous(s="zzzzz"))
