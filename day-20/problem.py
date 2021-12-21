with open('input') as f:
    raw_algorithm, raw_grid = f.read().strip().split('\n\n')
    algorithm = {i for i, c in enumerate(raw_algorithm) if c == '#'}
    grid = set()
    for y, row in enumerate(raw_grid.split('\n')):
        for x, col in enumerate(row):
            if col == '#':
                grid.add((x, y))



deltas = (
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (0, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
)


def neighbors(x, y):
    for (d_x, d_y) in deltas:
        yield x + d_x, y + d_y


def enhance(grid, track_on=True):
    next_grid = set()
    min_x, max_x = min(x for x, _ in grid) - 5, max(x for x, _ in grid) + 6
    min_y, max_y = min(y for _, y in grid) - 5, max(y for _, y in grid) + 6
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            b = 0
            for n in neighbors(x, y):
                b = (b << 1) | int((n in grid) == track_on)
            if track_on != (b in algorithm):
                next_grid.add((x, y))
    return next_grid


def print_image(grid):
    print('')
    min_x, max_x = min(x for x, _ in grid) - 5, max(x for x, _ in grid) + 6
    min_y, max_y = min(y for _, y in grid) - 5, max(y for _, y in grid) + 6
    for y in range(min_y, max_y):
        print(''.join('#' if (x, y) in grid else '.' for x in range(min_x, max_x)))


# Part 1
image = grid.copy()
for i in range(2):
    image = enhance(image, i % 2 == 0)
    # print_image(image)

print(len(image))
# 5687

# Part 2
image = grid.copy()
for i in range(50):
    image = enhance(image, i % 2 == 0)
    # print_image(image)

print(len(image))
# 18723
