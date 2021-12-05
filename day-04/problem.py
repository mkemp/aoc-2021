class Board(object):

    def __init__(self, raw, num_to_row_col):
        self.raw = raw
        self.dim = len(raw)
        # num => (i, j)
        self.num_to_row_col = num_to_row_col
        # marked (i, j) coordinates
        self.marked = set()
        # number of marks by i row
        self.marked_rows = dict((i, 0) for i in range(self.dim))
        # number of marks by j column
        self.marked_cols = dict((j, 0) for j in range(self.dim))

    @classmethod
    def from_lines(cls, lines):
        num_to_row_col = {}
        for i, row in enumerate(lines):
            for j, col in enumerate(row.strip().split()):
                num_to_row_col[int(col)] = (i, j)
        return cls(tuple(lines), num_to_row_col)

    def reset(self):
        self.marked = set()
        self.marked_rows = dict((i, 0) for i in range(self.dim))
        self.marked_cols = dict((j, 0) for j in range(self.dim))

    def mark(self, num):
        i, j = self.num_to_row_col.get(num, (None, None))
        if i is not None and j is not None and (i, j) not in self.marked:
            self.marked.add((i, j))
            self.marked_rows[i] += 1
            self.marked_cols[j] += 1
        # are we a winner yet?
        return self.dim in self.marked_rows.values() or self.dim in self.marked_cols.values()

    def unmarked_sum(self):
        return sum(num for num, (i, j) in self.num_to_row_col.items() if (i, j) not in self.marked)

    def __repr__(self):
        return '\n'.join(self.raw)


with open('input') as f:
    values = [line for line in f.read().strip().split('\n')]

numbers = [int(x) for x in values[0].split(',')]
boards = [
    Board.from_lines(values[i:i + 5])
    for i in range(2, len(values), 6)
]


# Part 1
result, board = None, None
for num in numbers:
    for board in boards:
        result = board.mark(num)
        if result:
            break
    if result:
        print(num * board.unmarked_sum())
        break
# 50008


# Utility
for board in boards:
    board.reset()


# Part 2
winners, losers, remaining = [], [], boards
for num in numbers:
    for board in remaining:
        result = board.mark(num)
        if result:
            winners.append(board)
        else:
            losers.append(board)
    remaining, losers = losers, []
    if not remaining:
        board = winners[-1]
        print(num * board.unmarked_sum())
        break
# 17408
