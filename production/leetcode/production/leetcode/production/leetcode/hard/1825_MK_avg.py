from typing import List


def bin_search_and_add(l: List[int], target: int) -> List[int]:
    if l.__len__() == 0:
        return [target]
    elif l.__len__() == 1:
        if target > l[0]:
            return [l[0], target]
        else:
            return [target, l[0]]
    else:
        mid = l.__len__() // 2 - 1
        if l[mid] < target < l[mid + 1]:
            return l[:mid + 1] + [target] + l[mid + 1:]
        elif l[mid] >= target:
            return bin_search_and_add(l[:mid + 1], target) + l[mid + 1:]
        elif l[mid + 1] <= target:
            return l[:mid + 1] + bin_search_and_add(l[mid + 1:], target)


class MKAverage:

    def __init__(self, m: int, k: int):
        self.list = []
        self.k_min = []
        self.k_max = []
        self.mid = []
        self.total_num = 0
        self.avg = -1
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        if self.total_num < self.m:
            self.list.append(num)
            self.total_num += 1
            if self.total_num == self.m:
                self.list.sort()
                self.k_min = self.list[:self.k]
                self.k_max = self.list[-self.k:]
                self.mid = self.list[self.k: -self.k]
                self.avg = sum(self.mid) / (self.m - 2 * self.k)
        else:
            if num < self.k_min[-1]:
                self.k_min = bin_search_and_add(self.k_min, num)
                self.avg = (self.avg * self.mid.__len__() + self.k_min[-1]) / (self.mid.__len__() + 1)
                self.mid = [self.k_min[-1]] + self.mid
                self.k_min = self.k_min[:-1]
            elif num > self.k_max[0]:
                self.k_max = bin_search_and_add(self.k_max, num)
                self.avg = (self.avg * self.mid.__len__() + self.k_max[0]) / (self.mid.__len__() + 1)
                self.mid = self.mid + [self.k_max[0]]
                self.k_max = self.k_max[1:]
            else:
                self.avg = (self.avg * self.mid.__len__() + num) / (self.mid.__len__() + 1)
                self.mid = bin_search_and_add(self.mid, num)

    def calculateMKAverage(self) -> int:
        return self.avg


# Your MKAverage object will be instantiated and called as such:
obj = MKAverage(3, 1)
obj.addElement(3)
obj.addElement(1)
print(obj.calculateMKAverage())
obj.addElement(10)
print(obj.calculateMKAverage())
obj.addElement(5)
obj.addElement(5)
obj.addElement(5)
print(obj.calculateMKAverage())
