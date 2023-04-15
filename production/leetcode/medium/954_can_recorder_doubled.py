# -*- coding: utf-8 -*-
# @Time    : 2022-04-01 2:54 p.m.
# @Author  : qkzhong
# @FileName: 954_can_recorder_doubled.py
# @Software: PyCharm


from collections import Counter
from typing import List


class Solution:
    def count_and_del_zero(self, l:List[int]) -> int:
        count = 0
        i=0
        while i in range(l.__len__()):
            if l[i] == 0:
                l.remove(0)
                count += 1
                continue
            else:
                i += 1
        return count

    def abs_sort(self, l: List[int]):
        for i in range(l.__len__()):
            for j in range(1, l.__len__() - i):
                if abs(l[j - 1]) > abs(l[j]):
                    l[j - 1] = l[j - 1] + l[j]
                    l[j] = l[j - 1] - l[j]
                    l[j - 1] = l[j - 1] - l[j]

    def canReorderDoubled(self, arr: List[int]) -> bool:
        if self.count_and_del_zero(arr) % 2:
            return False
        arr = sorted(arr, key=abs)
        pre = arr[:arr.__len__() // 2]
        back = arr[arr.__len__() // 2:]
        i=0
        while i in range(pre.__len__()):
            if back[i] == 2 * pre[i]:
                pre.remove(pre[i])
                back.remove(back[i])
                continue
            else:
                return False
        return True


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        if cnt[0] % 2:
            return False
        for x in sorted(cnt, key=abs):
            if cnt[2 * x] < cnt[x]:
                return False
            cnt[2 * x] -= cnt[x]
        return True

print(Solution().canReorderDoubled([4,-2,2,-4]))
