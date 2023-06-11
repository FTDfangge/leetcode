import heapq
from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.d = dict()
        self.freqs = dict()

    def add(self, number: int) -> None:
        try:
            self.d[number] += 1
            self.freqs[self.d[number] - 1] -= 1
            if self.freqs[self.d[number] - 1] == 0:
                self.freqs.pop(self.d[number] - 1)
            try:
                self.freqs[self.d[number]] += 1
            except KeyError:
                self.freqs[self.d[number]] = 1
        except KeyError:
            self.d[number] = 1
            try:
                self.freqs[self.d[number]] += 1
            except KeyError:
                self.freqs[self.d[number]] = 1

    def deleteOne(self, number: int) -> None:
        try:
            self.freqs[self.d[number]] -= 1
            if self.freqs[self.d[number]] == 0:
                self.freqs.pop(self.d[number])
            self.d[number] -= 1
            if self.d[number] == 0:
                self.d.pop(number)
            else:
                try:
                    self.freqs[self.d[number]] += 1
                except KeyError:
                    self.freqs[self.d[number]] = 1
        except KeyError:
            pass

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freqs


ops = ["FrequencyTracker", "add", "deleteOne", "hasFrequency"]
vals = [[], [1], [1], [1]]
obj = FrequencyTracker()
ans = [None]
for i in range(ops.__len__()):
    if ops[i] == 'add':
        ans.append(obj.add(*vals[i]))
    elif ops[i] == 'deleteOne':
        ans.append(obj.deleteOne(*vals[i]))
    elif ops[i] == 'hasFrequency':
        ans.append(obj.hasFrequency(*vals[i]))
