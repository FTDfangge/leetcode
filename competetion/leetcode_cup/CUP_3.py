from collections import defaultdict
from typing import List, Optional


class ForceField:
    def __init__(self, start_x: float, end_x: float, start_y: float, end_y: float):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

    def __str__(self):
        return 'x: %2f -> %2f, y: %f -> %2f' % (self.start_x, self.end_x, self.start_y, self.end_y)


class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        if not forceField:
            return 0

        def get_intersect(field1: ForceField, field2: ForceField) -> Optional[ForceField]:
            x_start = max(field1.start_x, field2.start_x)
            x_end = min(field1.end_x, field2.end_x)
            y_start = max(field1.start_y, field2.start_y)
            y_end = min(field1.end_y, field2.end_y)
            if x_end >= x_start and y_end >= y_start:
                return ForceField(x_start, x_end, y_start, y_end)

        force_level = defaultdict(list)
        max_force = 1
        x0, y0, side0 = forceField[0]
        force_level[1] = [ForceField(x0 - side0 / 2, x0 + side0 / 2, y0 - side0 / 2, y0 + side0 / 2)]
        for x, y, side in forceField[1:]:
            this_field = ForceField(x - side / 2, x + side / 2, y - side / 2, y + side / 2)
            temp = [[], [this_field]]
            force = 1
            while force in range(1, max_force + 1):
                for field in force_level[force]:
                    inter = get_intersect(field, this_field)
                    if inter:
                        print(force + 1, inter)
                        try:
                            temp[force + 1].append(inter)
                        except IndexError:
                            temp.append([inter])
                            max_force = force + 1
                force += 1
            for f in range(1, temp.__len__()):
                force_level[f].extend(temp[f])
        return max_force


print(Solution().fieldOfGreatestBlessing(forceField=[[0, 0, 1], [1, 0, 1]]))
print(Solution().fieldOfGreatestBlessing(forceField=[[4, 4, 6], [7, 5, 3], [1, 6, 2], [5, 6, 3]]))
print(Solution().fieldOfGreatestBlessing([[7, 7, 9], [7, 5, 3], [1, 8, 5], [5, 6, 3], [9, 10, 2], [8, 4, 10]]))
