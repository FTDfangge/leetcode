# -*- coding: utf-8 -*-
# @Time    : 2022-04-02 3:25 p.m.
# @Author  : qkzhong
# @FileName: jianzhi59_I_max_sliding_window.py
# @Software: PyCharm
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        q = deque()
        res = []
        for i in range(k-1):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        for i in range(k-1, nums.__len__()):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i-k >= q[0]:
                q.popleft()
            res.append(nums[q[0]])

        return res


print(Solution().maxSlidingWindow(nums =
[1,3,-1,-3,5,3,6,7], k = 3))