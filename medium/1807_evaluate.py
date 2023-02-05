from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        key_dict = dict()
        for i in knowledge:
            if i[0] not in key_dict:
                key_dict[i[0]] = i[1]

        key_list = []
        key = ['', []]
        is_key = False
        for idx, e in enumerate(s):
            if e == '(':
                is_key = True
                key[1].append(idx)
            elif e == ')':
                is_key = False
                key[1].append(idx)
                key_list.append(key)
                key = ['', []]
            elif is_key:
                key[0] += e
        ans = ''
        pre = 0
        for i in key_list:
            if i[0] not in key_dict:
                ans += s[pre:i[1][0]] + '?'
            else:
                ans += s[pre:i[1][0]] + key_dict[i[0]]

            pre = i[1][1] + 1
        ans += s[pre:]
        return ans


print(Solution().evaluate(s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]]))
print(Solution().evaluate(s="hi(name)", knowledge=[["a", "b"]]))
print(Solution().evaluate(s="(a)(a)(a)aaa", knowledge=[["a", "yes"]]))
