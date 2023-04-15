from typing import List


class Solution:
    def __init__(self):
        self.buy = []
        self.sell = []

    def get_numbers(self) -> int:
        res = 0
        for i in self.buy:
            res += i[1]
        for i in self.sell:
            res += i[1]
        return res

    def bin_search(self, add_list: List[List[int]], price):
        if not add_list:
            return 0

        mid = add_list.__len__() // 2
        if add_list[mid][0] == price:
            return mid
        elif add_list[mid][0] > price:  # search left
            return self.bin_search(add_list[mid:], price)
        else:
            return mid + self.bin_search(add_list[:mid], price) + 1

    def add(self, price, amount, add_list: str):
        if add_list == 'buy':
            index = self.bin_search(self.buy, price)
            l = [price, amount]
            self.buy = self.buy[:index] + [l] + self.buy[index:]
        else:
            index = self.bin_search(self.sell, price)
            l = [price, amount]
            self.sell = self.sell[:index] + [l] + self.sell[index:]

    def do_buy(self, price, amount):
        if not self.sell:
            self.add(price, amount, 'buy')
        else:
            while self.sell and amount:
                if self.sell[0][0] <= price:
                    self.sell[0][1] -= 1
                    if self.sell[0][1] == 0:
                        self.sell.pop(0)
                    amount -= 1
                else:
                    break
            self.add(price, amount, 'buy')

    def do_sell(self, price, amount):
        if not self.buy:
            self.add(price, amount, 'sell')
        else:
            while self.buy and amount:
                if self.buy[0][0] >= price:
                    self.buy[0][1] -= 1
                    if self.buy[0][1] == 0:
                        self.buy.pop(0)
                    amount -= 1
                else:
                    break
            self.add(price, amount, 'sell')

    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        for i in orders:
            if i[2] == 0:  # buy
                self.do_buy(i[0], i[1])
            elif i[2] == 1:  # sell
                self.do_sell(i[0], i[1])

        return self.get_numbers()


print(Solution().getNumberOfBacklogOrders(orders=[[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]))
print(Solution().getNumberOfBacklogOrders(orders=[[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]))
