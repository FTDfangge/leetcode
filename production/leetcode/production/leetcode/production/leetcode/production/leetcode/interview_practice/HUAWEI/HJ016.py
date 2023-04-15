# -*- coding: utf-8 -*-
# @Time    : 2022-09-04 10:10 p.m.
# @Author  : qkzhong
# @FileName: HJ016.py
# @Software: PyCharm

# 描述
# 王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
# 主件
# 附件
# 电脑
# 打印机，扫描仪
# 书柜
# 图书
# 书桌
# 台灯，文具
# 工作椅
# 无
# 如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。
# 每个主件可以有
# 0
# 个、 1
# 个或
# 2
# 个附件。附件不再有从属于自己的附件。
# 王强查到了每件物品的价格（都是
# 10
# 元的整数倍），而他只有
# N
# 元的预算。除此之外，他给每件物品规定了一个重要度，用整数
# 1
# ~ 5
# 表示。他希望在花费不超过
# N
# 元的前提下，使自己的满意度达到最大。
# 满意度是指所购买的每件物品的价格与重要度的乘积的总和，假设设第ii件物品的价格为v[i]
# v[i]，重要度为w[i]
# w[i]，共选中了kk件物品，编号依次为j_1, j_2, ..., j_kj
# 1
# ​
# , j
# 2
# ​
# , ..., j
# k
# ​
# ，则满意度为：v[j_1] * w[j_1] + v[j_2] * w[j_2] + … +v[j_k] * w[j_k]
# v[j
# 1
# ​
# ]∗w[j
# 1
# ​
# ]+v[j
# 2
# ​
# ]∗w[j
# 2
# ​
# ]+…+v[j
# k
# ​
# ]∗w[j
# k
# ​
# ]。（其中 * 为乘号）
# 请你帮助王强计算可获得的最大的满意度。
#
#
# 输入描述：
# 输入的第
# 1
# 行，为两个正整数N，m，用一个空格隔开：
#
# （其中
# N （ N < 32000 ）表示总钱数， m （m < 60 ）为可购买的物品的个数。）
#
#
# 从第
# 2
# 行到第
# m + 1
# 行，第
# j
# 行给出了编号为
# j - 1
# 的物品的基本数据，每行有
# 3
# 个非负整数
# v
# p
# q
#
#
# （其中
# v
# 表示该物品的价格（ v < 10000 ）， p
# 表示该物品的重要度（ 1
# ~ 5 ）， q
# 表示该物品是主件还是附件。如果
# q = 0 ，表示该物品为主件，如果
# q > 0 ，表示该物品为附件， q
# 是所属主件的编号）
#
#
#
#
# 输出描述：
# 输出一个正整数，为张强可以获得的最大的满意度。

total, item_num = list(map(int, input().split(" ")))
total = total // 10
satisfaction = [[0, 0, 0] for _ in range(item_num)]
values = [[0, 0, 0] for _ in range(item_num)]
primary_keys = []

for i in range(item_num):
    value, priority, primary = list(map(int, input().split(" ")))
    value = value // 10
    if primary == 0:  # 主件
        satisfaction[i][0] = value * priority
        values[i][0] = value
        primary_keys.append(i)
    else:  # 附件
        if not satisfaction[primary - 1][1]:  # 附件1
            satisfaction[primary - 1][1] = value * priority
            values[primary - 1][1] = value
        else:  # 附件2
            satisfaction[primary - 1][2] = value * priority
            values[primary - 1][2] = value
s = []
v = []
for i in primary_keys:
    s.append(satisfaction[i])
    v.append(values[i])
satisfaction = s
values = v

dp = [[0] * (total + 1) for _ in range(primary_keys.__len__() + 1)]
for i in range(primary_keys.__len__()):
    for remain in range(total + 1):
        # 不放
        dp[i + 1][remain] = dp[i][remain]
        if remain >= values[i][0]:  # 可放主件
            dp[i + 1][remain] = max(dp[i][remain],
                                    dp[i][remain - values[i][0]] + satisfaction[i][0])
        if remain >= values[i][0] + values[i][1]:  # 可放主件+附件1
            dp[i + 1][remain] = max(dp[i][remain],
                                    dp[i][remain - values[i][0]] + satisfaction[i][0],
                                    dp[i][remain - values[i][0] - values[i][1]] + satisfaction[i][0] + satisfaction[i][
                                        1])
        if remain >= values[i][0] + values[i][2]:  # 可放主件+附件2
            dp[i + 1][remain] = max(dp[i][remain],
                                    dp[i][remain - values[i][0]] + satisfaction[i][0],
                                    dp[i][remain - values[i][0] - values[i][2]] + satisfaction[i][0] + satisfaction[i][
                                        2])
        if remain >= values[i][0] + values[i][1] + values[i][2]:  # 可放主件+附件1+附件2
            dp[i + 1][remain] = max(dp[i][remain],
                                    dp[i][remain - values[i][0]] + satisfaction[i][0],
                                    dp[i][remain - values[i][0] - values[i][1]] + satisfaction[i][0] + satisfaction[i][
                                        1],
                                    dp[i][remain - values[i][0] - values[i][2]] + satisfaction[i][0] + satisfaction[i][
                                        2],
                                    dp[i][remain - values[i][0] - values[i][1] - values[i][2]] + satisfaction[i][0] +
                                    satisfaction[i][1] + satisfaction[i][2])
print(dp[primary_keys.__len__()][total] * 10)

# 通过但是超时
def failed_solution():
    total, number_of_things = input().split(" ")
    total = int(total)
    number_of_things = int(number_of_things)
    inputs = [] #输入的所有物件

    for i in range(number_of_things):
        val, priority, primary = input().split(" ")
        val = int(val)
        priority = int(priority)
        primary = int(primary)
        inputs.append([val, priority, primary])

    def dp(i, remain) -> int: #将第 i 件算上后，以剩余金钱可以放进去的最大满足度
        if i == -1:
            return 0
        if remain < 0:
            return 0
        addons = [[0,0,0], [0,0,0]]
        if inputs[i][2] == 0: #主件
            index = 0
            for j in range(number_of_things):
                if inputs[j][2] - 1 == i:
                    addons[index] = inputs[j]
                    index += 1
            if remain >= inputs[i][0]: #可放主件
                if remain >= inputs[i][0] + addons[0][0] + addons[1][0]: #可放附件1+2
                    return max(dp(i-1, remain), #不放
                           dp(i-1, remain - inputs[i][0]) + inputs[i][0] * inputs[i][1], #放主件
                           dp(i-1, remain - inputs[i][0] - addons[0][0]) + inputs[i][0] * inputs[i][1] + addons[0][0] * addons[0][1], #放主件+附件1
                           dp(i-1, remain - inputs[i][0] - addons[1][0]) + inputs[i][0] * inputs[i][1] + addons[1][0] * addons[1][1], #放主件+附件2
                           dp(i-1, remain - inputs[i][0] - addons[0][0] - addons[1][0]) + inputs[i][0] * inputs[i][1] + addons[0][0] * addons[0][1] + addons[1][0] * addons[1][1]
                          )
                elif remain >= inputs[i][0] + addons[0][0]: #可放附件1
                    return max(dp(i-1, remain), #不放
                           dp(i-1, remain - inputs[i][0]) + inputs[i][0] * inputs[i][1], #放主件
                           dp(i-1, remain - inputs[i][0] - addons[0][0]) + inputs[i][0] * inputs[i][1] + addons[0][0] * addons[0][1] #放主件+附件1
                          )
                elif remain >= inputs[i][0] + addons[1][0]: #可放附件2
                    return max(dp(i-1, remain), #不放
                           dp(i-1, remain - inputs[i][0]) + inputs[i][0] * inputs[i][1], #放主件
                           dp(i-1, remain - inputs[i][0] - addons[1][0]) + inputs[i][0] * inputs[i][1] + addons[1][0] * addons[1][1] #放主件+附件2
                          )
                else: # 只可放主件
                    return max(dp(i-1, remain), #不放
                           dp(i-1, remain - inputs[i][0]) + inputs[i][0] * inputs[i][1] #放主件
                           )
            else:
                return dp(i-1,remain)
        else:
            return dp(i-1, remain)

    print(dp(number_of_things-1, total))
