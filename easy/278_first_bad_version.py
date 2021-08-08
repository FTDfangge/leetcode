# -*- coding: utf-8 -*-
# @Time    : 2021-06-04 11:22 a.m.
# @Author  : qkzhong
# @FileName: 278_first_bad_version.py
# @Software: PyCharm

# AC

versions = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 1, 1, 1,
            1, 1, 1, 1, 1]


def isBadVersion(version):
    if versions[version - 1] == 1:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def bin_search(left, right):
            if left == right:
                return left
            if isBadVersion((left + right) // 2):
                right = (left + right) // 2
            else:
                left = (left + right) // 2 + 1
            return bin_search(left, right)

        return bin_search(1, n)


if __name__ == '__main__':
    print(Solution().firstBadVersion(20))
