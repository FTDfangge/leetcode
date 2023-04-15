# -*- coding: utf-8 -*-
# @Time    : 2022-03-29 3:49 p.m.
# @Author  : qkzhong
# @FileName: jianzhi20_is_number.py
# @Software: PyCharm


class Solution:
    def isNumber(self, s: str) -> bool:
        # check if is a integer or decimal
        def is_decimal(ss: str):
            if ss.__len__() == 0:
                return False
            # start with '+' or '-'
            if ss[0] == '+' or ss[0] == '-':
                ss = ss[1:]
            if ss.__len__() == 0:
                return False
            could_no_following = False
            # at least one digit, followed by '.'
            if ord(ss[0]) in range(48, 58):  # first is a digit
                could_no_following = True
            num_of_point = 0
            for i in range(ss.__len__()):
                if ord(ss[i]) not in range(48, 58) and ss[i] != '.':  # ith is a digit
                    return False
                if ss[i] == '.':
                    num_of_point += 1
                    if num_of_point >= 2:
                        return False
                    if not could_no_following:  # should be a following
                        if i != ss.__len__() - 1 and ord(ss[i + 1]) in range(48, 58):  # there is a following number
                            print()
                        else:
                            return False
            return True

        # check is integer
        def is_integer(ss: str):
            if ss.__len__() == 0:
                return False
            # start with '+' or '-'
            if ss[0] == '+' or ss[0] == '-':
                ss = ss[1:]
            if ss.__len__() == 0:
                return False
            for i in range(ss.__len__()):
                if ord(ss[i]) not in range(48, 58):  # ith is a digit
                    return False
            return True

        pre = 0
        back = s.__len__() - 1
        # check the pre blanks
        for pre in range(s.__len__()):
            if s[pre] != ' ':
                break
        # delete the back blanks
        for back in range(s.__len__() - 1, -1, -1):
            if s[back] != ' ':
                break

        # find the 'e' position
        is_e = False
        e_position = back
        if 'e' in s or 'E' in s:
            is_e = True
            e_position = back
            while s[e_position] != 'E' and s[e_position] != 'e':
                e_position -= 1
        if is_e:
            if is_integer(s[pre:e_position]) or is_decimal(s[pre:e_position]):
                if is_integer(s[e_position+1:back + 1]):
                    return True
            return False
        else:
            return is_integer(s[pre:back+1]) or is_decimal(s[pre:back+1])


print(Solution().isNumber('+eo'))
