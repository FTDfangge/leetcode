# -*- coding: utf-8 -*-
# @Time    : 2022-03-16 8:41 p.m.
# @Author  : qkzhong
# @FileName: jianzhi46_translate_num.py
# @Software: PyCharm

# AC

class Solution:
    def translateNum(self, num: int) -> int:
        num_str = str(num)

        def num_of_translate(untranslate_ptr: int) -> int:
            if untranslate_ptr == 0:
                return 1

            if 25 >= int(num_str[untranslate_ptr - 1] + num_str[untranslate_ptr]) >= 10:
                if untranslate_ptr == 1:
                    return 2
                else:
                    return num_of_translate(untranslate_ptr - 1) + num_of_translate(untranslate_ptr - 2)
            else:
                return num_of_translate(untranslate_ptr - 1)

        return num_of_translate(num_str.__len__() - 1)


if __name__ == '__main__':
    print(Solution().translateNum(12258))
