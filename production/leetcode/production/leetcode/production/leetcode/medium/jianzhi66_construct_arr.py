# -*- coding: utf-8 -*-
# @Time    : 2022-03-25 4:13 p.m.
# @Author  : qkzhong
# @FileName: jianzhi66_construct_arr.py
# @Software: PyCharm
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        output1 = [1] * a.__len__()
        for i in range(1, a.__len__()):
            output1[i] = output1[i-1] * a[i-1]
        output2 = [1] * a.__len__()
        for j in range(a.__len__()-2, -1, -1):
            output2[j] = output2[j+1] * a[j+1]
        res = [1] * a.__len__()
        for k in range(a.__len__()):
            res[k] = output1[k] * output2[k]
        return res


print(Solution().constructArr([1, 2, 3, 4, 5]))
