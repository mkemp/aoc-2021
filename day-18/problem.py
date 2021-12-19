from itertools import permutations
from math import ceil, floor
from re import compile

left_re = compile('(\d+)[\[\],]*$')
right_re = compile('^[\[\],]*(\d+)')
split_re = compile('(\d\d+)')

with open('input') as f:
    values = [line for line in f.read().strip().split('\n')]


def reduce(line):
    next_line, line = line, None
    while line != next_line:
        line = next_line
        next_line = look_for_explodes(line)
        if next_line == line:
            next_line = look_for_splits(line)
    return next_line


def look_for_explodes(line):
    depth = 0
    for i, c in enumerate(line):
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        if depth > 4:
            open_idx = i
            close_idx = open_idx + line[open_idx:].index(']')
            to_left, _, to_right = line[open_idx + 1:close_idx].partition(',')
            to_left, to_right = int(to_left), int(to_right)
            new_left = line[:open_idx]
            m = left_re.search(line[:open_idx])
            if m:
                replacement = str(int(m.group(1)) + to_left)
                new_left = new_left[:m.start(1)] + replacement + new_left[m.end(1):]
            new_right = line[close_idx + 1:]
            m = right_re.search(line[close_idx + 1:])
            if m:
                replacement = str(int(m.group(1)) + to_right)
                new_right = new_right[:m.start(1)] + replacement + new_right[m.end(1):]
            return new_left + '0' + new_right
    return line


def look_for_splits(line):
    m = split_re.search(line)
    if m:
        value = int(m.group(1))
        replacement = f'[{int(floor(value / 2))},{int(ceil(value / 2))}]'
        return line[:m.start(1)] + replacement + line[m.end(1):]
    return line


def magnitude(line):
    left, right = eval(line)
    return 3 * score(left) + 2 * score(right)


def score(number):
    if isinstance(number, int):
        return number
    return 3 * score(number[0]) + 2 * score(number[1])


# Part 1
number = values[0]
for next_number in values[1:]:
    number = reduce(f'[{number},{next_number}]')

print(magnitude(number))
# 3987


# Part 2
max_magnitude = 0
for a, b in permutations(values, 2):
    max_magnitude = max(max_magnitude, magnitude(reduce(f'[{a},{b}]')))

print(max_magnitude)
# 4500
