# -*- coding: utf-8 -*-
# @Time    : 2022-03-19 9:25 p.m.
# @Author  : qkzhong
# @FileName: jianzhi40_get_least_numbers.py
# @Software: PyCharm
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr:
            return []

        if k == 0:
            return []

        minset = []
        for e in arr:
            if minset.__len__() < k:
                # min set is not full
                minset.append(e)
            else:
                # min set is full
                if e < max(minset):
                    # update minset
                    minset.remove(max(minset))
                    minset.append(e)
        output = []
        for i in minset:
            output.append(i)
        return output

    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        out = []
        for i in range(k):
            out.append(arr[i])
        return out



if __name__ == '__main__':
    print(Solution().getLeastNumbers2([3,2,1,5,-1], 2))

