# -*- coding: utf-8 -*-
# @Time    : 2022-03-19 6:07 p.m.
# @Author  : qkzhong
# @FileName: jianzhi45_min_number.py
# @Software: PyCharm
from typing import List


class Solution:
    def compare(self, num1, num2) -> bool: # num1 > num2 :True
        list1 = []
        list2 = []
        if num1 == 0:
            list1.append(0)
        if num2 == 0:
            list2.append(0)

        while num1>0:
            list1.append(num1 % 10)
            num1 = num1 // 10
        while num2>0:
            list2.append(num2 % 10)
            num2 = num2 // 10

        first = n1 = list1.pop()
        second = n2 = list2.pop()
        if n1 > n2:
            return True
        elif n1 < n2:
            return False
        while list1 and list2:
            n1 = list1.pop()
            n2 = list2.pop()
            if n1 > n2:
                return True
            elif n1 < n2 :
                return False
        while list1:
            n1 = list1.pop()
            if n1 > second:
                return True
            elif n1 < second:
                return False
            else:
                return n1 > n2
        while list2:
            n2 = list2.pop()
            if first > n2:
                return True
            elif first < n2:
                return False
            else:
                return n1 > n2

    def compare2(self, num1, num2) -> bool: # num1 > num2 :True
        return int(str(num1) + str(num2)) > int(str(num2) + str(num1))

    def minNumber(self, nums: List[int]) -> str:
        for i in range(nums.__len__() - 1):
            for j in range(1, nums.__len__() - i):
                if self.compare(nums[j-1], nums[j]):
                    temp = nums[j-1]
                    nums[j-1] = nums[j]
                    nums[j] = temp
        print(nums)
        s = ''
        for e in nums:
            s += str(e)
        return s


if __name__ == '__main__':
    # print(Solution().compare(12, 121))
    # print(Solution().compare(121, 12))
    print(Solution().minNumber([1,2,3,4,5,6,7,8,9,0]))