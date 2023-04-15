class ExamRoom:

    def __init__(self, n: int):
        self.positions = []  # sorted
        self.pos_num = n

    def seat(self) -> int:
        if not self.positions:
            self.positions.append(0)
            return 0
        max_len = [-1, 0]
        # check seat 0
        if self.positions[0] != 0:
            if self.positions[0] - 0 > max_len[1]:
                max_len = [0, self.positions[0] - 0]

        # check seat in the middle
        for i in range(1, self.positions.__len__()):
            mid = (self.positions[i] + self.positions[i - 1]) // 2
            if mid - self.positions[i - 1] > max_len[1]:
                max_len = [mid, mid - self.positions[i - 1]]
        # check last seat
        if self.positions[-1] != self.pos_num - 1:
            if self.pos_num - 1 - self.positions[-1] > max_len[1]:
                max_len = [self.pos_num - 1, self.pos_num - 1 - self.positions[-1]]

        # add seat into position
        if max_len[0] == self.pos_num - 1:
            self.positions.append(max_len[0])
            return max_len[0]

        for i in range(self.positions.__len__()):
            if self.positions[i] > max_len[0]:
                self.positions = self.positions[:i] + [max_len[0]] + self.positions[i:]
                break
        return max_len[0]

    def leave(self, p: int) -> None:
        for i in range(self.positions.__len__()):
            if self.positions[i] == p:
                self.positions = self.positions[:i] + self.positions[i + 1:]
                break


# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(4)
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.seat())
obj.leave(1)
obj.leave(3)
print(obj.seat())
