class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total = 0

        def travel():
            nonlocal total
            nonlocal mainTank
            nonlocal additionalTank
            if additionalTank == 0:
                total += mainTank * 10
                return
            if mainTank > 0:
                if mainTank >= 5:
                    mainTank -= 5
                    total += 50
                    if additionalTank > 0:
                        mainTank += 1
                        additionalTank -= 1
                else:
                    total += mainTank * 10
                    mainTank = 0

            else:
                return
            travel()

        travel()
        return total


print(Solution().distanceTraveled(9, 2))
