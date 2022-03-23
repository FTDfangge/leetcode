# -*- coding: utf-8 -*-
# @Time    : 2022-03-23 4:45 p.m.
# @Author  : qkzhong
# @FileName: jianzhi65_add.py
# @Software: PyCharm

class Solution:
    def add(self, a: int, b: int) -> int:

        if a>=0 and b>=0:
            add_on = 0
            bin_a = bin(a)[2:]
            bin_b = bin(b)[2:]
            res = ''
            for bit in range(max(bin_a.__len__(), bin_b.__len__())):
                aa = 0
                bb = 0
                if bit in range(bin_a.__len__()) and bit in range(bin_b.__len__()):
                    aa = int(bin_a[::-1][bit])
                    bb = int(bin_b[::-1][bit])
                    res += str(aa ^ bb ^ add_on)
                elif bit in range(bin_a.__len__()) and bit not in range(bin_b.__len__()):
                    aa = int(bin_a[::-1][bit])
                    bb = 0
                    res += str(aa ^ bb ^ add_on)
                elif bit not in range(bin_a.__len__()) and bit in range(bin_b.__len__()):
                    aa = 0
                    bb = int(bin_b[::-1][bit])
                    res += str(aa ^ bb ^ add_on)
                # modify add_on
                if (aa and bb) or ((aa or bb) and add_on):
                    add_on = 1
                else:
                    add_on = 0

            if add_on:
                res += '1'
            res += 'b0'
            return int(res[::-1], 2)
        elif a<=0 and b<=0:
            add_on = 0
            bin_a = bin(a)[3:]
            bin_b = bin(b)[3:]
            res = ''
            for bit in range(max(bin_a.__len__(), bin_b.__len__())):
                aa = 0
                bb = 0
                if bit in range(bin_a.__len__()) and bit in range(bin_b.__len__()):
                    aa = int(bin_a[::-1][bit])
                    bb = int(bin_b[::-1][bit])
                    res += str(aa ^ bb ^ add_on)
                elif bit in range(bin_a.__len__()) and bit not in range(bin_b.__len__()):
                    aa = int(bin_a[::-1][bit])
                    bb = 0
                    res += str(aa ^ bb ^ add_on)
                elif bit not in range(bin_a.__len__()) and bit in range(bin_b.__len__()):
                    aa = 0
                    bb = int(bin_b[::-1][bit])
                    res += str(aa ^ bb ^ add_on)
                # modify add_on
                if (aa and bb) or ((aa or bb) and add_on):
                    add_on = 1
                else:
                    add_on = 0

            if add_on:
                res += '1'
            res += 'b0-'
            return int(res[::-1], 2)
        elif a>=0 and b<=0 and abs(a) > abs(b):
            add_on = 0
            bin_a = bin(a)[2:]
            bin_b = bin(b)[3:]
            res = ''
            for bit in range(max(bin_a.__len__(), bin_b.__len__())):
                aa = 0
                bb = 0
                if bit in range(bin_a.__len__()) and bit in range(bin_b.__len__()):
                    aa = int(bin_a[::-1][bit])
                    bb = int(bin_b[::-1][bit])
                    res += str(aa ^ bb ^ add_on)
                elif bit in range(bin_a.__len__()) and bit not in range(bin_b.__len__()):
                    aa = int(bin_a[::-1][bit])
                    bb = 0
                    res += str(aa ^ bb ^ add_on)
                elif bit not in range(bin_a.__len__()) and bit in range(bin_b.__len__()):
                    aa = 0
                    bb = int(bin_b[::-1][bit])
                    res += str(aa ^ bb ^ add_on)
                # modify add_on
                if (aa < bb) or (aa == bb and add_on):
                    add_on = 1
                else:
                    add_on = 0
            res += 'b0'
            if add_on:
                res += '-'
            return int(res[::-1], 2)
        elif a>=0 and b<=0 and abs(a) < abs(b):
            return -self.add(-a, -b)
        else:
            return self.add(b, a)


print(Solution().add(0, -3))
