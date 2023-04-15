from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        self.index = -1

    def insert(self, word: str, index: int):
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True
        node.index = index

    def search_prefix(self, prefix: str) -> 'Trie':
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return None
            node = node.children[idx]
        return node

    def search(self, word: str) -> bool:
        result = self.search_prefix(word)
        return result and result.is_end

    def from_prefix_search_word(self, prefix: str) -> List[int]:
        node = self.search_prefix(prefix)
        if node:
            ans = []
            q = [node]
            while q:
                current = q.pop(0)
                if current.is_end:
                    ans.append(current.index)
                for i in range(26):
                    if current.children[i]:
                        q.append(current.children[i])
            return ans
        else:
            return []

    def starts_with(self, pre: str) -> bool:
        return self.search_prefix(pre) is not None

    def __str__(self):
        ans = []
        for i in range(self.children.__len__()):
            if self.children[i]:
                ans.append(chr(i + ord('a')))
        return str(ans)


def check_palindrome(s: str) -> bool:
    return s == s[::-1]


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie1 = Trie()
        for i, w in enumerate(words):
            trie1.insert(w[::-1], i)

        ans = set()
        for i, w in enumerate(words):
            results = trie1.from_prefix_search_word(w)
            for r in results:
                if r != i:
                    if check_palindrome(words[r][::-1][w.__len__():]):
                        ans.add((i, r))

        trie2 = Trie()
        for i, w in enumerate(words):
            trie2.insert(w, i)

        for i, w in enumerate(words):
            results = trie2.from_prefix_search_word(w[::-1])
            for r in results:
                if r != i:
                    if check_palindrome(words[r][w.__len__():]):
                        ans.add((r, i))
        ans_list = []
        for a in ans:
            ans_list.append([a[0], a[1]])
        return ans_list


print(Solution().palindromePairs(words=["abcd", "dcbaee", "lls", "s", "sssll"]))
print(Solution().palindromePairs(words=["abcd", "dcba", "lls", "s", "sssll"]))
print(Solution().palindromePairs(words=["bat", "tab", "cat"]))
print(Solution().palindromePairs(words=["a", ""]))
