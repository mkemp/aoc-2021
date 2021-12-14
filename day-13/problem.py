with open('input') as f:
    coordinates, creases = f.read().strip().split('\n\n')
    dots = [tuple(map(int, line.split(','))) for line in coordinates.split('\n')]
    folds = [(line[11:12], int(line[13:])) for line in creases.split('\n')]


def do_fold(dots, x_or_y, at):
    new_dots = set()
    if x_or_y == 'x':
        for x, y in dots:
            if x > at:
                new_dots.add((at - (x - at), y))
            else:
                new_dots.add((x, y))
    else:
        for x, y in dots:
            if y > at:
                new_dots.add((x, at - (y - at)))
            else:
                new_dots.add((x, y))
    return new_dots


def print_dots(dots):
    for y in range(max(y for x, y in dots) + 1):
        text = ''
        for x in range(max(x for x, y in dots) + 1):
            text += '#' if (x, y) in dots else '.'
        print(text)


# Part 1
d = set(dots)
print(len(do_fold(d, *folds[0])))
# 671


# Part 2
d = set(dots)
for fold in folds:
    d = do_fold(d, *fold)

print_dots(d)
# PCPHARKL
