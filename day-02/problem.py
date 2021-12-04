def parse(line):
    cmd, _, val = line.partition(' ')
    axis, multiplier = {
        'forward': ('x', 1),
        'up': ('y', -1),
        'down': ('y', 1)
    }[cmd]
    return axis, int(val) * multiplier


with open('input') as f:
    values = [parse(line) for line in f.read().strip().split('\n')]


# Part 1
x, y = 0, 0
for axis, value in values:
    if axis == 'x':
        x += value
    else:
        y += value

print(x * y)
# 2027977


# Part 2
x, y, aim = 0, 0, 0
for axis, value in values:
    if axis == 'x':
        x += value
        y += aim * value
    else:
        aim += value

print(x * y)
# 1903644897
