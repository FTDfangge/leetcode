from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str):
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

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

    def starts_with(self, pre: str) -> bool:
        return self.search_prefix(pre) is not None

    def check_all_prefix(self, word: str) -> bool:
        node = self
        for w in word:
            idx = ord(w) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
            if not node.is_end:
                return False
        return True

    def __str__(self):
        ans = []
        for idx, i in enumerate(self.children):
            if i:
                ans.append(chr(idx + ord('a')))
        return str(ans)


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        # init trie
        for w in words:
            trie.insert(w)
        words.sort()
        words = sorted(words, key=lambda x: x.__len__(), reverse=True)
        for w in words:
            if trie.check_all_prefix(w):
                return w
        return ''


print(Solution().longestWord(words=["k", "ki", "kir", "kira", "kiran"]))
print(Solution().longestWord(words=["a", "banana", "app", "appl", "ap", "apply", "apple"]))
print(Solution().longestWord(words=["abc", "bc", "ab", "qwe"]))
