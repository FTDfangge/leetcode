# -*- coding: utf-8 -*-
# @Time    : 2022-04-21 10:08 a.m.
# @Author  : qkzhong
# @FileName: 824_to_goat_latin.py
# @Software: PyCharm
from tqdm import tqdm

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        res = ''
        for i in tqdm(range(len(words))):
            if words[i][0] in vowel:
                words[i] += 'ma'
            else:
                f = words[i][0]
                words[i] = words[i][1:]
                words[i] += f + 'ma'
            words[i] += (i+1) * 'a'
            res += words[i] + ' '
        res = res [:-1]
        return res


print(Solution().toGoatLatin("I speak Goat Latin"))
