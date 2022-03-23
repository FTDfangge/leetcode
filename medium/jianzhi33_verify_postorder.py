# -*- coding: utf-8 -*-
# @Time    : 2022-03-23 2:32 p.m.
# @Author  : qkzhong
# @FileName: jianzhi33_verify_postorder.py
# @Software: PyCharm
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        if postorder.__len__() == 1:
            return True
        root_val = postorder[postorder.__len__() - 1]
        i = postorder.__len__() - 2
        while i >= 0:
            if postorder[i] < root_val:
                break
            i -= 1

        # check the left list
        for j in range(i + 1):
            if postorder[j] > root_val:
                return False

        return self.verifyPostorder(postorder[:i + 1]) and self.verifyPostorder(
            postorder[i + 1:postorder.__len__() - 1])


print(Solution().verifyPostorder([1,3,2,6,5]))
