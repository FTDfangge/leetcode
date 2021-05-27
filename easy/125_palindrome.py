# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 11:28 a.m.
# @Author  : qkzhong
# @FileName: 125_palindrome.py
# @Software: PyCharm

def is_num_or_letter(s):
    if (ord(s) in range(97, 123)) or (ord(s) in range(65, 91)) or (ord(s) in range(48, 58)):
        return True
    else:
        return False


# AC but slow, because there is some function is defined and I did not use
def isPalindrome(s: str) -> bool:
    head = 0
    back = s.__len__() - 1
    while head < back:
        while not is_num_or_letter(s[head]):
            head += 1
            if head >= s.__len__() - 1 or back <= 0:
                return True
        while not is_num_or_letter(s[back]):
            back -= 1
            if head >= s.__len__() - 1 or back <= 0:
                return True

        if s[head] != s[back]:
            if ord(s[head]) in range(97, 123) and s[back] == chr(ord(s[head]) - 32):
                pass
            elif ord(s[back]) in range(97, 123) and s[head] == chr(ord(s[back]) - 32):
                pass
            else:
                return False
        head += 1
        back -= 1
    return True


def isPalindrome_new(s: str) -> bool:
    n = s.__len__()
    left = 0
    right = n-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right:
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1
    return True


if __name__ == '__main__':
    print(isPalindrome_new(",;"))
