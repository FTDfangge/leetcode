from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def cal_total(player: List[int]) -> int:
            total = 0
            double_count = 0
            for i in player:
                if double_count:
                    total += i * 2
                    double_count -= 1
                else:
                    total += i

                if i == 10:
                    double_count = 2
            return total

        total1 = cal_total(player1)
        total2 = cal_total(player2)
        if total1 > total2:
            return 1
        elif total1 < total2:
            return 2
        else:
            return 0


print(Solution().isWinner(player1=[4, 10, 7, 9], player2=[6, 5, 2, 3]))
print(Solution().isWinner(player1=[3, 5, 7, 6], player2=[8, 10, 10, 2]))
print(Solution().isWinner(player1=[2, 3], player2=[4, 1]))
