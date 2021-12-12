from functools import reduce

with open('input') as f:
    values = [line for line in f.read().strip().split('\n')]

rows, cols = len(values), len(values[0])
grid = {}
for x, row in enumerate(values):
    for y, col in enumerate(row):
        grid[(x, y)] = int(col)


def neighbors(x, y):
    if 0 <= x < rows and 0 <= y < cols:
        if 0 < x:
            yield (x - 1, y)
        if x < rows - 1:
            yield (x + 1, y)
        if 0 < y:
            yield (x, y - 1)
        if y < cols - 1:
            yield (x, y + 1)


# Part 1
risk_level = 0
for r in range(rows):
    for c in range(cols):
        height = grid[(r, c)]
        if all(height < grid[(i, j)] for (i, j) in neighbors(r, c)):
            risk_level += height + 1

print(risk_level)
# 600


# Part 2
def fill_size(basin, x, y):
    size = 1
    basin.remove((x, y))
    to_expand = {k for k in neighbors(x, y) if k in basin}
    while to_expand:
        size += len(to_expand)
        basin -= to_expand
        next_to_expand = set()
        for x, y in to_expand:
            next_to_expand.update(k for k in neighbors(x, y) if k in basin)
        to_expand = next_to_expand
    return size


basin = {k for k, v in grid.items() if v != 9}
features = []
for r in range(rows):
    for c in range(cols):
        if (r, c) in basin:
            features.append(fill_size(basin, r, c))

print(reduce(lambda a, b: a * b, sorted(features, reverse=True)[:3]))
# 987840
