# -*- coding: utf-8 -*-
# @Time    : 2022-03-29 4:59 p.m.
# @Author  : qkzhong
# @FileName: 2024_max_consecutive_answers.py
# @Software: PyCharm

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        start = 0
        end = 0
        max_answers = 0
        num_of_t = 0
        num_of_f = 0
        if answerKey[0] == 'T':
            num_of_t += 1
        else:
            num_of_f += 1
        while start <= end < answerKey.__len__():
            if min(num_of_t, num_of_f) <= k:  # means this part could be consecutive
                max_answers = max(max_answers, end - start + 1)
                end += 1
                if end in range(answerKey.__len__()) and answerKey[end] == 'T':
                    num_of_t += 1
                elif end in range(answerKey.__len__()) and answerKey[end] == 'F':
                    num_of_f += 1
            else:  # means this part could not be consecutive
                if start in range(answerKey.__len__()) and answerKey[start] == 'T':
                    num_of_t -= 1
                elif start in range(answerKey.__len__()) and answerKey[start] == 'F':
                    num_of_f -= 1
                start += 1
        return max_answers


print(Solution().maxConsecutiveAnswers(answerKey="TFFT", k=1))
