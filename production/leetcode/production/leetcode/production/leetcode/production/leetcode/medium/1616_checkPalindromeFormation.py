def check_palindromes(s: str) -> bool:
    return s == s[::-1]


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = a.__len__()
        left = 0
        right = n - 1
        a_pre = ''
        a_back = ''
        b_pre = ''
        b_back = ''
        while left < right:
            a_pre += a[left]
            b_pre += b[left]
            a_back += a[right]
            b_back += b[right]
            if a_pre != b_back and b_pre != a_back:
                break
            left += 1
            right -= 1
        else:
            return True
        if check_palindromes(a[left:right + 1]) or check_palindromes(b[left:right + 1]):
            return True
        return False


# print(Solution().checkPalindromeFormation('x', 'y'))
# print(Solution().checkPalindromeFormation('abdef', 'fecab'))
# print(Solution().checkPalindromeFormation(a="ulacfd", b="jizalu"))
print(Solution().checkPalindromeFormation("pvhmupgqeltozftlmfjjde",
                                          "yjgpzbezspnnpszebzmhvp"))
