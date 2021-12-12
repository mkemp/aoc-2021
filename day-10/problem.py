with open('input') as f:
    values = [line for line in f.read().strip().split('\n')]


class Parser(object):
    openers = '([{<'
    closers = ')]}>'
    def __init__(self, line):
        self.line = line
        self.corruption = None
        self.solution = ''
    def __repr__(self):
        return f'<Parser: "{self.line}">'
    def is_corrupted(self):
        if self.corruption:
            return True
        try:
            self.parse()
            return False
        except ValueError as e:
            self.corruption = e.args
            return True
        except IndexError as e:
            return False
    def parse(self, idx=0):
        while idx < len(self.line):
            {
                '(': self.parens,
                '[': self.square,
                '{': self.curly,
                '<': self.carrot
            }[self.line[idx]](idx + 1)
    def parens(self, idx):
        try:
            # print(f'[parens] eval {self.line[idx]} @ {idx}')
            while self.line[idx] in self.openers:
                idx = {
                    '(': self.parens,
                    '[': self.square,
                    '{': self.curly,
                    '<': self.carrot
                }[self.line[idx]](idx + 1)
            if len(self.line) <= idx:
                raise IndexError('Incomplete')
            if self.line[idx] != ')':
                raise ValueError('Corrupted', ')', self.line[idx], idx)
            return idx + 1
        except IndexError as e:
            self.solution += ')'
            raise e
    def square(self, idx):
        try:
            # print(f'[square] eval {self.line[idx]} @ {idx}')
            while self.line[idx] in self.openers:
                idx = {
                    '(': self.parens,
                    '[': self.square,
                    '{': self.curly,
                    '<': self.carrot
                }[self.line[idx]](idx + 1)
            if len(self.line) <= idx:
                raise IndexError('Incomplete')
            if self.line[idx] != ']':
                raise ValueError('Corrupted', ']', self.line[idx], idx)
            return idx + 1
        except IndexError as e:
            self.solution += ']'
            raise e
    def curly(self, idx):
        try:
            # print(f'[curly] eval {self.line[idx]} @ {idx}')
            while self.line[idx] in self.openers:
                idx = {
                    '(': self.parens,
                    '[': self.square,
                    '{': self.curly,
                    '<': self.carrot
                }[self.line[idx]](idx + 1)
            if len(self.line) <= idx:
                raise IndexError('Incomplete')
            if self.line[idx] != '}':
                raise ValueError('Corrupted', '}', self.line[idx], idx)
            return idx + 1
        except IndexError as e:
            self.solution += '}'
            raise e
    def carrot(self, idx):
        try:
            # print(f'[carrot] eval {self.line[idx]} @ {idx}')
            while self.line[idx] in self.openers:
                idx = {
                    '(': self.parens,
                    '[': self.square,
                    '{': self.curly,
                    '<': self.carrot
                }[self.line[idx]](idx + 1)
            if len(self.line) <= idx:
                raise IndexError('Incomplete')
            if self.line[idx] != '>':
                raise ValueError('Corrupted', '>', self.line[idx], idx)
            return idx + 1
        except IndexError as e:
            self.solution += '>'
            raise e


parsers = [Parser(line) for line in values]

# Part 1
score = 0
for p in parsers:
    if p.is_corrupted():
        score += {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }[p.corruption[2]]

print(score)
# 265527


# Part 2
scores = []
for p in parsers:
    if not p.is_corrupted():
        score = 0
        for c in p.solution:
            score *= 5
            score += {
                ')': 1,
                ']': 2,
                '}': 3,
                '>': 4
            }[c]
        scores.append(score)

print(sorted(scores)[int(len(scores) / 2)])
# 3969823589
