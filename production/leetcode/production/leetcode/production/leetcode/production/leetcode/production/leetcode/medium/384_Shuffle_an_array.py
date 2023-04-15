# -*- coding: utf-8 -*-
# @Time    : 2021-11-087:26 p.m.
# @Author  : raynor
# @FileName: 384_Shuffle_an_array.py
# @Software: PyCharm

#AC

import copy
import random
from typing import List


# shuffle the array on itself. left is the unshuffled, right is the shuffled.
# Each time choose a random index from the unshuffled and swap it with the last of unshuffled.
# The last unshuffled index -1
class Solution:
    __slots__ = {'original'}

    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        shuffled = copy.deepcopy(self.original)
        last_unshuffled = shuffled.__len__() - 1
        while last_unshuffled >= 0:
            temp = shuffled[last_unshuffled]
            random_index = random.randint(0, last_unshuffled)
            shuffled[last_unshuffled] = shuffled[random_index]
            shuffled[random_index] = temp
            last_unshuffled -= 1
        return shuffled


if __name__ == '__main__':
    obj = Solution([1, 2, 3])
    print(obj.shuffle())
    print(obj.reset())
    print((obj.shuffle()))
