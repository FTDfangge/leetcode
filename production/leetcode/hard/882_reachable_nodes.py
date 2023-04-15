# -*- coding: utf-8 -*-
# @Time    : 2022-11-26 9:41 a.m.
# @Author  : qkzhong
# @FileName: 882_reachable_nodes.py
# @Software: PyCharm
import copy
from typing import List

from graphs.adjacency2graph import adjacency2graph


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        adjacency_matrix = [[-1] * n for _ in range(n)]
        # construct adjacency matrix
        for e in edges:
            adjacency_matrix[e[0]][e[1]] = e[2]
            adjacency_matrix[e[1]][e[0]] = e[2]
        moving_matrix = copy.deepcopy(adjacency_matrix)
        q = []
        count = 0
        # node_visited, avoid mutiple visit same node
        node_visited = [0] * n
        node_visited[0] = 1

        # add node 0, and init the queue
        for index, i in enumerate(moving_matrix[0]):
            if i >= 0:
                if i < maxMoves:
                    if maxMoves - i - 1 > 0:
                        q.append([index, maxMoves - i - 1])
                    node_visited[index] += 1
                    moving_matrix[0][index] = -1
                    moving_matrix[index][0] = -1
                else:
                    moving_matrix[0][index] = i - maxMoves
        while q:
            current_node, remain_moves = q.pop(0)
            for index, i in enumerate(moving_matrix[current_node]):
                if i >= 0:
                    if i < remain_moves:
                        # add the most remain_moves into queue
                        for nde in q:
                            if nde[0] == index:
                                nde[1] = max(nde[1], remain_moves - i - 1)
                                break
                        else:
                            if remain_moves - i - 1 > 0:
                                q.append([index, remain_moves - i - 1])
                        node_visited[index] += 1
                        moving_matrix[current_node][index] = -1
                        moving_matrix[index][current_node] = -1
                    else:
                        moving_matrix[current_node][index] = i - remain_moves
        print(adjacency_matrix)
        adjacency2graph(adjacency_matrix)
        print(moving_matrix)
        adjacency2graph(moving_matrix)
        # count
        for node in node_visited:
            if node:
                count += 1
        for i in range(n):
            for j in range(i + 1, n):
                if adjacency_matrix[i][j] >= 0:
                    if moving_matrix[i][j] <= 0:  # this edge exist and has been all visited
                        count += adjacency_matrix[i][j]
                    else:
                        # add two directions
                        count += min(
                            adjacency_matrix[i][j] - moving_matrix[i][j] + adjacency_matrix[i][j] - moving_matrix[j][i],
                            adjacency_matrix[i][j])
        return count


# print(Solution().reachableNodes(edges=[[0, 1, 10], [0, 2, 1], [1, 2, 2]], maxMoves=6, n=3))  # 13

# print(Solution().reachableNodes(edges=[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], maxMoves=10, n=4))  # 23
# print(Solution().reachableNodes(edges=[[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], maxMoves=17, n=5))  # 1
print(Solution().reachableNodes(
    [[4, 6, 11], [5, 6, 2], [2, 6, 11], [0, 3, 19], [1, 7, 21], [5, 7, 1], [1, 5, 4], [0, 7, 12], [6, 7, 3], [3, 6, 22],
     [0, 5, 24], [1, 2, 8], [3, 7, 11], [1, 3, 14], [4, 5, 7], [4, 7, 14], [0, 4, 5], [2, 4, 7], [3, 4, 11], [3, 5, 15],
     [2, 5, 13], [2, 3, 6], [1, 4, 6], [0, 2, 3], [1, 6, 20]],
    18,
    8))  # 233
