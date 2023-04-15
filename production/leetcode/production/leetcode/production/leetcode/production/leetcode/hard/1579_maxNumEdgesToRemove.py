from typing import List


class Dsu:
    def __init__(self, size: int):
        self.pa = [i for i in range(size)]
        self.size = [1] * size
        self.useless_union = 0

    def find(self, x) -> int:
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x, y) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            self.useless_union += 1
            return True
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.pa[y] = x
        self.size[x] += self.size[y]
        return False

    def check_all_connected(self) -> bool:
        root = self.find(0)
        for i in range(1, self.pa.__len__()):
            if self.find(i) != root:
                return False
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        both_edges = []
        removed = set()
        removed_twice = 0

        def max_num_edges_to_remove(connections: List[List[int]]) -> int:
            dsu = Dsu(n)
            for c1, c2 in connections:
                if dsu.union(c1, c2):  # useless union
                    if [c1, c2] in both_edges:
                        temp = removed
                        removed.add((c1, c2))
                        if temp == removed.__len__():
                            nonlocal removed_twice
                            removed_twice += 1
            if dsu.check_all_connected():
                return dsu.useless_union
            else:
                return -1

        alice = []
        bob = []
        for e in edges:
            if e[0] == 1:
                alice.append([e[1] - 1, e[2] - 1])
            elif e[0] == 2:
                bob.append([e[1] - 1, e[2] - 1])
            else:
                both_edges.append([e[1] - 1, e[2] - 1])
        alice_ans = max_num_edges_to_remove(both_edges + alice)
        if alice_ans == -1:
            return -1
        bob_ans = max_num_edges_to_remove(both_edges + bob)
        if bob_ans == -1:
            return -1
        return alice_ans + bob_ans - removed_twice