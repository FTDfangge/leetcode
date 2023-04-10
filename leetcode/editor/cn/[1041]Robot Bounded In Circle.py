# On an infinite plane, a robot initially stands at (0, 0) and faces north. 
# Note that: 
# 
#  
#  The north direction is the positive direction of the y-axis. 
#  The south direction is the negative direction of the y-axis. 
#  The east direction is the positive direction of the x-axis. 
#  The west direction is the negative direction of the x-axis. 
#  
# 
#  The robot can receive one of three instructions: 
# 
#  
#  "G": go straight 1 unit. 
#  "L": turn 90 degrees to the left (i.e., anti-clockwise direction). 
#  "R": turn 90 degrees to the right (i.e., clockwise direction). 
#  
# 
#  The robot performs the instructions given in order, and repeats them forever.
#  
# 
#  Return true if and only if there exists a circle in the plane such that the 
# robot never leaves the circle. 
# 
#  
#  Example 1: 
# 
#  
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
# "G": move one step. Position: (0, 1). Direction: South.
# "G": move one step. Position: (0, 0). Direction: South.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) -
# -> (0, 2) --> (0, 1) --> (0, 0).
# Based on that, we return true.
#  
# 
#  Example 2: 
# 
#  
# Input: instructions = "GG"
# Output: false
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# Repeating the instructions, keeps advancing in the north direction and does 
# not go into cycles.
# Based on that, we return false.
#  
# 
#  Example 3: 
# 
#  
# Input: instructions = "GL"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
# "G": move one step. Position: (-1, 1). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
# "G": move one step. Position: (-1, 0). Direction: South.
# "L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
# "G": move one step. Position: (0, 0). Direction: East.
# "L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) -
# -> (-1, 1) --> (-1, 0) --> (0, 0).
# Based on that, we return true.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= instructions.length <= 100 
#  instructions[i] is 'G', 'L' or, 'R'. 
#  
# 
#  Related Topics 数学 字符串 模拟 👍 145 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # _ori is orientation, 0 -> N, 1 -> E, 2 -> S, 3 -> W
        xx, yy, _ori = 0, 0, 0
        visited = dict()
        visited[(0, 0)] = 1
        for i in instructions:
            if i == 'L':
                _ori -= 1
                _ori = _ori % 4
            elif i == 'R':
                _ori += 1
                _ori = _ori % 4
            elif i == 'G':
                if _ori == 0:
                    yy += 1
                elif _ori == 1:
                    xx += 1
                elif _ori == 2:
                    yy -= 1
                else:
                    xx -= 1
        x, y, ori = 0, 0, 0
        for i in range(4):  # repeat do this, the time of repeating is 4(could be any integer)
            if ori == 0:
                x += xx
                y += yy
            elif ori == 1:
                x += yy
                y -= xx
            elif ori == 2:
                x -= xx
                y -= yy
            elif ori == 3:
                x -= yy
                y += xx
            ori += _ori
            ori %= 4
            if (x, y) in visited:
                return True
            visited[(x, y)] = 1
        return False


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().isRobotBounded("GGLLGG"))
print(Solution().isRobotBounded("GG"))
print(Solution().isRobotBounded("GL"))
