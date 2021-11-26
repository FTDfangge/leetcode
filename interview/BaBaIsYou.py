# -*- coding: utf-8 -*-
# @Time    : 2021-11-2011:17 a.m.
# @Author  : raynor
# @FileName: BaBaIsYou.py
# @Software: PyCharm

def traverseSolution():
    wordList = [["flag", 1],  # 0
                ["win", 1],  # 1
                ["pillar", 1],  # 2
                ["push", 1],  # 3
                ["wall", 1],  # 4
                ["stop", 1],  # 5
                ["baba", 1],  # 6
                ["you", 1],  # 7
                ["star", 1],  # 8
                ["defeat", 1],  # 9
                ["is", 5]]  # 10

    subjects = []
    appendMany(wordList, subjects, [0, 2, 4, 6, 8])

    objects = []
    appendMany(wordList, objects, [1, 3, 5, 7, 9, 0, 2, 4, 6, 8])

    while hasWord(wordList):
        print("\nPicture:")
        sentences = 0
        while sentences in range(wordList[10][1]):
            for i in [0, 2, 4, 6, 8]:
                for j in [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]:
                    if wordList[i][1] > 0 and wordList[j][1] > 0:
                        wordList[i][1] -= 1
                        wordList[j][1] -= 1
                        print(wordList[i][0] + " is " + wordList[j][0], end=".  |  ")
                        sentences += 1


def appendMany(wordList, toAdd, indexs):
    for i in indexs:
        toAdd.append(wordList[i])


def hasWord(wordList):
    for i in range(wordList.__len__() - 1):
        if wordList[i][1] >= 1:
            return True
    return False


if __name__ == '__main__':
    traverseSolution()
