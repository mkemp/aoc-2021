with open('input') as f:
    values = [line for line in f.read().strip().split('\n')]


deltas = (
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1)
)
rows, cols = len(values), len(values[0])
grid = {}
for x, row in enumerate(values):
    for y, col in enumerate(row):
        grid[(x, y)] = int(col)


def neighbors(x, y):
    if 0 <= x < rows and 0 <= y < cols:
        for (d_x, d_y) in deltas:
            i, j = x + d_x, y + d_y
            if (i, j) in grid:
                yield (i, j)


def step(g):
    flashers = set()
    for r in range(rows):
        for c in range(cols):
            g[(r, c)] += 1
            if g[(r, c)] > 9:
                flashers.add((r, c))
    flashes = 0
    already_flashed = set()
    while flashers:
        already_flashed.update(flashers)
        flashes += len(flashers)
        more_flashers = set()
        for x, y in flashers:
            for k in neighbors(x, y):
                if k not in already_flashed:
                    g[k] += 1
                    if g[k] > 9:
                        more_flashers.add(k)
        flashers = more_flashers
    for k in already_flashed:
        g[k] = 0
    # print_grid(g)
    return flashes


def print_grid(g):
    print('')
    for r in range(rows):
        print(''.join(['*' if g[(r, c)] > 9 else str(g[(r, c)]) for c in range(cols)]))
    print('')


# Part 1
flashes = 0
g = grid.copy()
for _ in range(100):
    flashes += step(g)

print(flashes)
# 1661

# Part 2
count = 0
g = grid.copy()
while set(g.values()) != {0}:
    count += 1
    _ = step(g)

print(count)
# 334
