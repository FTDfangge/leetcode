class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return set(list(s)).__len__()
