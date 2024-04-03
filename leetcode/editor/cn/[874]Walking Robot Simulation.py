# A robot on an infinite XY-plane starts at point (0, 0) facing north. The 
# robot can receive a sequence of these three possible types of commands: 
# 
#  
#  -2: Turn left 90 degrees. 
#  -1: Turn right 90 degrees. 
#  1 <= k <= 9: Move forward k units, one unit at a time. 
#  
# 
#  Some of the grid squares are obstacles. The iᵗʰ obstacle is at grid point 
# obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead 
# stay in its current location and move on to the next command. 
# 
#  Return the maximum Euclidean distance that the robot ever gets from the 
# origin squared (i.e. if the distance is 5, return 25). 
# 
#  Note: 
# 
#  
#  North means +Y direction. 
#  East means +X direction. 
#  South means -Y direction. 
#  West means -X direction. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 3 units to (3, 4).
# The furthest point the robot ever gets from the origin is (3, 4), which 
# squared is 3² + 4² = 25 units away.
#  
# 
#  Example 2: 
# 
#  
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1,
#  4).
# 4. Turn left.
# 5. Move north 4 units to (1, 8).
# The furthest point the robot ever gets from the origin is (1, 8), which 
# squared is 1² + 8² = 65 units away.
#  
# 
#  Example 3: 
# 
#  
# Input: commands = [6,-1,-1,6], obstacles = []
# Output: 36
# Explanation: The robot starts at (0, 0):
# 1. Move north 6 units to (0, 6).
# 2. Turn right.
# 3. Turn right.
# 4. Move south 6 units to (0, 0).
# The furthest point the robot ever gets from the origin is (0, 6), which 
# squared is 6² = 36 units away.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= commands.length <= 10⁴ 
#  commands[i] is either -2, -1, or an integer in the range [1, 9]. 
#  0 <= obstacles.length <= 10⁴ 
#  -3 * 10⁴ <= xi, yi <= 3 * 10⁴ 
#  The answer is guaranteed to be less than 2³¹. 
#  
# 
#  Related Topics 数组 模拟 👍 219 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        farthest = 0
        x, y = 0, 0
        direction = 0  # 0 N, 1 E, 2 S, 3 W
        for c in commands:
            if c == -2:
                direction -= 1
                direction = direction % 4
                continue
            if c == -1:
                direction += 1
                direction = direction % 4
                continue
            # move
            if direction == 0:
                # North
                xx, yy = x, y + c
                for i in range(y + 1, yy + 1):
                    if (x, i) in obstacles:
                        # stop
                        xx, yy = x, i - 1
                        break
            elif direction == 1:
                # East
                xx, yy = x + c, y
                for i in range(x + 1, xx + 1):
                    if (i, y) in obstacles:
                        # stop
                        xx, yy = i - 1, y
                        break
            elif direction == 2:
                # South
                xx, yy = x, y - c
                for i in range(y - 1, yy - 1, -1):
                    if (x, i) in obstacles:
                        # stop
                        xx, yy = x, i + 1
                        break
            else:
                # West
                xx, yy = x - c, y
                for i in range(x - 1, xx - 1, -1):
                    if (i, y) in obstacles:
                        # stop
                        xx, yy = i, y + 1
                        break
            x, y = xx, yy
            farthest = max(farthest, x ** 2 + y ** 2)
        return farthest


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().robotSim(
    [2, -1, -1, -1, -2, 1, 7, -2, 9, 2, 3, -1, 4, 9, 7, 7, 2, 4, 2, -2, 1, 5, 8, -2, -2, 4, 2, 9, 7, 5, 5, -2, 2, 2, 1,
     -1, -1, 1, 6, 6, -1, 7, -1, 7, 1, 8, 2, -1, 8, 7, -1, 2, -2, 2, 2, 4, 9, -1, 4, -1, -2, 8, -1, 3, 6, -2, 7, -2, 6,
     7, 9, 6, -2, -1, 3, 6, 2, 8, 6, 6, -2, -2, 4, 2, 4, 1, 2, 2, 2, 8, 6, 4, 6, 7, -1, 1, -2, -1, -1, 7],
    [[75, 61], [-27, -13], [-85, 77], [-40, -30], [-71, -34], [41, -39], [73, -54], [-19, 16], [76, 50], [-12, -9],
     [-25, -100], [45, -86], [-43, -88], [50, -23], [-46, -89], [-66, 91], [-57, -46], [-82, 51], [78, 98], [65, -61],
     [83, -14], [24, -17], [28, 77], [-63, -3], [77, -39], [18, -63], [10, -91], [-11, -15], [-75, -80], [68, 92],
     [21, -70], [91, -53], [-68, -64], [9, -68], [1, 40], [-73, 20], [56, 15], [-90, -43], [-100, 99], [-19, 7],
     [14, 76], [-80, -2], [24, -34], [47, 7], [25, 73], [-99, -39], [-55, -9], [85, 31], [14, 0], [-68, 94], [-25, 25],
     [44, -77], [-94, 59], [92, -47], [40, 5], [-68, -58], [87, 39], [-43, 93], [-83, -77], [-95, 81], [82, 37],
     [66, 21], [-5, 73], [-75, 32], [30, 70], [22, -68], [-27, 31], [-91, 80], [82, -58], [-95, -24], [15, 22],
     [-10, 38], [85, 96], [68, 26], [81, -18], [23, -47], [-80, -78], [30, 18], [-56, 4], [1, 33], [-21, 2], [-69, 85],
     [41, 92], [-72, 79], [-48, -34], [-34, 63], [48, -78], [17, 73], [16, 28], [-13, -14], [16, 24], [11, -27],
     [44, 52], [-78, 67], [93, 65], [-32, -33], [6, -2], [67, -100], [95, 77], [-6, 28], [10, 81], [-45, 48], [80, -34],
     [-49, 46], [-38, 17], [7, -81], [-29, 52], [46, -82], [5, -71], [79, -87], [39, -82], [-78, -82], [-85, 19],
     [74, -55], [22, 45], [-40, -24], [44, 97], [41, -21], [-17, -92], [17, 49], [-1, -33], [39, -36], [37, -38],
     [41, -29], [72, -88], [-100, 57], [-95, 74], [-27, -16], [57, -34], [74, -85], [62, 92], [44, 0], [83, 57],
     [90, 96], [-65, 70], [-58, 99], [-70, -86], [75, -74], [-63, 11], [-64, 20], [-35, -40], [-86, -71], [-77, -62],
     [4, -95], [97, 76], [36, -62], [-1, 90], [99, 91], [55, 89], [80, 77], [40, 54], [79, -11], [44, -36], [-35, 21],
     [-13, -86], [-55, 84], [27, 94], [74, 91], [-77, -45], [-90, 44], [-80, -35], [-38, 80], [34, -28], [45, -77],
     [1, 28], [-88, -50], [-100, 87], [19, 93], [-26, -39], [-83, -100], [-6, 43], [89, 42], [-35, -95], [-67, -96],
     [14, 22], [-25, 8], [-31, -9], [-94, 48], [82, -3], [39, 95], [44, 47], [-62, -71], [73, -30], [92, -11], [2, 85],
     [-91, 97], [99, -18], [-57, -17], [57, 73], [-41, 9], [44, 9], [17, -96], [-95, -16], [40, -3], [-48, -41],
     [95, 18], [-34, -94], [15, -90], [42, 11], [-65, -57]]))
