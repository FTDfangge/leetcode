# -*- coding: utf-8 -*-
# @Time    : 2022-09-10 10:26 p.m.
# @Author  : qkzhong
# @FileName: HJ028.py
# @Software: PyCharm
import math


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

import math
def check(num): #判断是否是素数
    for i in range(2,int(math.sqrt(num)) + 2): #除去1和本身的数没有其他的因子称为素数，但其实检验到int(math.sqrt(num)) + 1即可（数学证明略），不然会超时
        if(num % i == 0):
            return False
    return True

def find(odd, visited, choose, evens): #配对的过程
    for j,even in enumerate(evens):
        if check(odd+even) and not visited[j]: #如果即能配对，这两个数之前没有配过对（即使两个不能配对visit值为0，但是也不能过是否是素数这一关，所以visit就可以看为两个能配对的素数是否能配对）
            visited[j] = True #代表这两个数能配对
            if choose[j]==0 or find(choose[j],visited,choose,evens): #如果当前偶数没有和任何一个奇数现在已经配对，那么认为找到一组可以连接的，如果当前的奇数已经配对，那么就让那个与之配对的偶数断开连接，让他再次寻找能够配对的奇数
                choose[j] = odd #当前奇数已经和当前的偶数配对
                return True
    return False #如果当前不能配对则返回False

while True:
    try:
        num = int(input())
        a = input()
        a = a.split()
        b = []
        count = 0
        for i in range(len(a)):
            a[i] = int(a[i])
        evens = []
        odds = []
        for i in a: #将输入的数分为奇数和偶数
            if(i % 2 != 0):
                odds.append(i)
            else:
                evens.append(i)
        choose = [0]*len(evens) #choose用来存放当前和这个奇数配对的那个偶数
        for odd in odds:
            visited = [False]*len(evens) #visit用来存放当前奇数和偶数是否已经配过对
            if find(odd,visited,choose,evens):
                count += 1
        print(count)
    except:
        break
