from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 27
        self.is_end = False
        self.time = 0
        self.sentence_index = -1

    def insert(self, word: str, sentence_idx: int) -> 'Trie':
        node = self
        for ch in word:
            index = ord(ch) - ord('a') if ch != ' ' else 26
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end = True
        node.time += 1
        node.sentence_index = sentence_idx
        return node

    def insert_with_time(self, word: str, times: int, sentence_idx: int) -> 'Trie':
        node = self
        for ch in word:
            index = ord(ch) - ord('a') if ch != ' ' else 26
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end = True
        node.time += times
        node.sentence_index = sentence_idx
        return node

    def search_prefix(self, prefix: str) -> 'Trie':
        node = self
        for ch in prefix:
            index = ord(ch) - ord('a') if ch != ' ' else 26
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def from_prefix_search_word(self, prefix: str) -> List[List[int]]:
        node = self.search_prefix(prefix)
        if node:
            ans = []
            q = [node]
            while q:
                current = q.pop(0)
                if current.is_end:
                    ans.append([current.sentence_index, current.time])
                for i in range(27):
                    if current.children[i]:
                        q.append(current.children[i])
            return ans
        else:
            return []

    def __str__(self):
        ans = []
        for i in range(27):
            if self.children[i]:
                ans.append(chr(i + ord('a')))
        return str(ans)


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        n = sentences.__len__()
        for i in range(n):
            self.trie.insert_with_time(sentences[i], times[i], i)
        self.sentences = sentences
        self.have_input = ''

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.have_input += c
            words_with_time = self.trie.from_prefix_search_word(self.have_input)
            words_with_time = sorted(words_with_time, key=lambda x: self.sentences[x[0]])
            words_with_time = sorted(words_with_time, key=lambda x: x[1], reverse=True)
            ans = []
            for w in words_with_time:
                ans.append(self.sentences[w[0]])
                if ans.__len__() == 3:
                    return ans
            return ans
        else:
            if self.have_input not in self.sentences:
                self.trie.insert(self.have_input, self.sentences.__len__())
                self.sentences.append(self.have_input)
            else:
                node = self.trie.search_prefix(self.have_input)
                node.time += 1
            self.have_input = ''
            return []


# Your AutocompleteSystem object will be instantiated and called as such:
obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
print(obj.input('i'))
print(obj.input(' '))
print(obj.input('a'))
print(obj.input('#'))
print(obj.input('i'))
print(obj.input(' '))
print(obj.input('a'))
print(obj.input('#'))
print(obj.input('i'))
print(obj.input(' '))
print(obj.input('a'))
print(obj.input('#'))
