# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 5:24 p.m.
# @Author  : qkzhong
# @FileName: 38_count_and_say.py
# @Software: PyCharm


# AC 92.77% 85.13%
def countAndSay(n: int) -> str:
    if n == 1:
        return '1'
    pre_str = countAndSay(n - 1)
    new_str = ''
    count = 0
    temp = pre_str[0]
    for i in range(pre_str.__len__()):
        if pre_str[i] == temp:
            count += 1
        else:
            new_str += str(count) + temp
            temp = pre_str[i]
            count = 1
    new_str += str(count) + temp
    return new_str


if __name__ == '__main__':
    print(countAndSay(6))
