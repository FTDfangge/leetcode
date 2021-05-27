# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 10:59 a.m.
# @Author  : qkzhong
# @FileName: 242_anagram.py
# @Software: PyCharm
import collections


# AC but slow
def isAnagram(s: str, t: str) -> bool:
    hash_table = collections.Counter()
    for char in s:
        hash_table[ord(char)] += 1

    for char in t:
        hash_table[ord(char)] -= 1

    for ASCII in hash_table:
        if hash_table[ASCII] != 0:
            return False
    return True


# AC but also slow
def isAnagram_new(s: str, t: str) -> bool:
    if s.__len__() != t.__len__():
        return False
    else:
        hash_table = collections.Counter()
        for char in s:
            hash_table[ord(char)] += 1

        for char in t:
            if hash_table[ord(char)] == 0:
                return False
            else:
                hash_table[ord(char)] -= 1
        return True


if __name__ == '__main__':
    print(isAnagram("anagram", "nagaram"))
