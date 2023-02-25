from typing import List


class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children else []


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        visited = [0] * roads.__len__()
        root = Node(0)
        q = [root]
        while q:
            node = q.pop(0)
            for idx, r in enumerate(roads):
                if not visited[idx]:
                    if node.val == r[0]:
                        visited[idx] = 1
                        new_node = Node(r[1])
                        node.children.append(new_node)
                        q.append(new_node)
                    if node.val == r[1]:
                        visited[idx] = 1
                        new_node = Node(r[0])
                        node.children.append(new_node)
                        q.append(new_node)

        def min_cost_with_passenger(target_city: Node) -> tuple:
            passes = 0
            fuel = 0
            for c in target_city.children:
                temp_fuel, temp_pass = min_cost_with_passenger(c)
                passes += temp_pass
                fuel += temp_fuel
                fuel += (temp_pass // seats) + 1 if (temp_pass % seats != 0) else temp_pass // seats
            print('to city {0}, fuel is {1}!, city {0} have {2} people'.format(target_city, fuel, passes + 1))
            return fuel, passes + 1

        return min_cost_with_passenger(root)[0]


print(Solution().minimumFuelCost(roads=[[0, 1], [0, 2], [0, 3]], seats=5))
print(Solution().minimumFuelCost(roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats=2))
