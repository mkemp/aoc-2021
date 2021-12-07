from collections import defaultdict

class Segment(object):

    def __init__(self, x_1, y_1, x_2, y_2):
        super(Segment, self).__init__()
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

    @classmethod
    def from_line(cls, line):
        one, _, two = line.partition(' -> ')
        return cls(*(tuple(map(int, one.split(','))) + tuple(map(int, two.split(',')))))

    def row_or_col_points(self):
        if self.x_1 == self.x_2:
            return [(self.x_1, y) for y in range(min(self.y_1, self.y_2), max(self.y_1, self.y_2) + 1)]
        if self.y_1 == self.y_2:
            return [(x, self.y_1) for x in range(min(self.x_1, self.x_2), max(self.x_1, self.x_2) + 1)]
        return []

    def points(self):
        if self.x_1 != self.x_2 and self.y_1 != self.y_2:
            d_x = 1 if self.x_1 < self.x_2 else -1
            d_y = 1 if self.y_1 < self.y_2 else -1
            return [(x, y) for (x, y) in zip(range(self.x_1, self.x_2 + d_x, d_x), range(self.y_1, self.y_2 + d_y, d_y))]
        return self.row_or_col_points()

    def __repr__(self):
        return f'<Segment: ({self.x_1},{self.y_1}) -> ({self.x_2},{self.y_2})>'


with open('input') as f:
    values = [line for line in f.read().strip().split('\n')]


segments = [Segment.from_line(line) for line in values]


# Part 1
vents = defaultdict(int)
for segment in segments:
    for point in segment.row_or_col_points():
        vents[point] += 1

print(len(list(filter(lambda x: x > 1, vents.values()))))
# 7468


# Part 2
vents = defaultdict(int)
for segment in segments:
    for point in segment.points():
        vents[point] += 1

print(len(list(filter(lambda x: x > 1, vents.values()))))
# 22364
