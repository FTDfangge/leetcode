# -*- coding: utf-8 -*-
# @Time    : 2022-11-27 11:58 a.m.
# @Author  : qkzhong
# @FileName: 123.py
# @Software: PyCharm
class TarjanSCC:
    def __init__(self, graph):
        self.graph = graph
        self.index = 0
        self.stack = []
        self.lowlink = {}
        self.visited = set()
        self.scc_list = []

    def tarjan(self, node):
        self.lowlink[node] = self.index
        self.index += 1
        self.visited.add(node)
        self.stack.append(node)

        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.tarjan(neighbor)
                self.lowlink[node] = min(self.lowlink[node], self.lowlink[neighbor])
            elif neighbor in self.stack:
                self.lowlink[node] = min(self.lowlink[node], self.lowlink[neighbor])

        if self.lowlink[node] == self.index:
            scc = []
            while True:
                neighbor = self.stack.pop()
                scc.append(neighbor)
                if neighbor == node:
                    break
            self.scc_list.append(scc)

    def find_scc(self):
        for node in self.graph:
            if node not in self.visited:
                self.tarjan(node)
        return self.scc_list

# Example usage:
graph = {
    1: [2],
    2: [3],
    3: [1, 4],
    4: [5],
    5: [6],
    6: [4, 7],
    7: []
}

tarjan_scc = TarjanSCC(graph)
result = tarjan_scc.find_scc()
print("Strongly Connected Components:", result)
