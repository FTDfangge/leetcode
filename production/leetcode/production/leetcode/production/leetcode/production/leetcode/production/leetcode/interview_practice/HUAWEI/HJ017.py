# -*- coding: utf-8 -*-
# @Time    : 2022-09-05 9:45 a.m.
# @Author  : qkzhong
# @FileName: HJ017.py
# @Software: PyCharm

commands = input().split(";")
myset = {"W","A","S","D"}
x = 0
y = 0

def is_valid_command(command : str) -> bool:
    if command.__len__() <= 1:
        return False
    else:
        if command[0] not in myset:
            return False
        else:
            for i in command[1:]:
                if i > "9" or i < "0":
                    return False
            return True

for i in commands:
    if is_valid_command(i):
        if i[0] == "W":
            y += int(i[1:])
        elif i[0] == "A":
            x -= int(i[1:])
        elif i[0] == "S":
            y -= int(i[1:])
        elif i[0] == "D":
            x += int(i[1:])
print(str(x)+","+str(y))