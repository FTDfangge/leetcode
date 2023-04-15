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

    def searchPrefix(self, prefix: str) -> 'Trie':
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.children[idx]:
                node = node.children[idx]
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        result = self.searchPrefix(word)
        return result and result.is_end

    def startsWith(self, pre: str) -> bool:
        return self.search_prefix(pre) is not None


