from re import compile

INPUT_RE = compile('^(on|off) x=(-?\d+)\\.\\.(-?\d+),y=(-?\d+)\\.\\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$')


class Cube(object):

    def __init__(self, on, x_min, x_max, y_min, y_max, z_min, z_max):
        super(Cube, self).__init__()
        self.x_min, self.x_max = x_min, x_max
        self.y_min, self.y_max = y_min, y_max
        self.z_min, self.z_max = z_min, z_max
        self.on = on

    @property
    def size(self):
        return (self.x_max - self.x_min) * (self.y_max - self.y_min) * (self.z_max - self.z_min)

    def overlap(self, other):
        return (self.x_min <= other.x_max and other.x_min <= self.x_max) and \
               (self.y_min <= other.y_max and other.y_min <= self.y_max) and \
               (self.z_min <= other.z_max and other.z_min <= self.z_max)


with open('input') as f:
    values = [INPUT_RE.match(line).groups() for line in f.read().strip().split('\n')]
    commands = [(v[0], tuple(map(int, v[1:]))) for v in values]


cubes = []
for cmd, (x_min, x_max, y_min, y_max, z_min, z_max) in commands:
    x_max += 1
    y_max += 1
    z_max += 1
    cube = Cube(cmd == 'on', x_min, x_max, y_min, y_max, z_min, z_max)
    new_cubes = []
    for c in cubes:
        if cube.overlap(c):
            if c.x_min < cube.x_min:
                new_c = Cube(c.on, c.x_min, cube.x_min, c.y_min, c.y_max, c.z_min, c.z_max)
                c.x_min = cube.x_min
                new_cubes.append(new_c)
            if c.x_max > cube.x_max:
                new_c = Cube(c.on, cube.x_max, c.x_max, c.y_min, c.y_max, c.z_min, c.z_max)
                c.x_max = cube.x_max
                new_cubes.append(new_c)
            if c.y_min < cube.y_min:
                new_c = Cube(c.on, c.x_min, c.x_max, c.y_min, cube.y_min, c.z_min, c.z_max)
                c.y_min = cube.y_min
                new_cubes.append(new_c)
            if c.y_max > cube.y_max:
                new_c = Cube(c.on, c.x_min, c.x_max, cube.y_max, c.y_max, c.z_min, c.z_max)
                c.y_max = cube.y_max
                new_cubes.append(new_c)
            if c.z_min < cube.z_min:
                new_c = Cube(c.on, c.x_min, c.x_max, c.y_min, c.y_max, c.z_min, cube.z_min)
                c.z_min = cube.z_min
                new_cubes.append(new_c)
            if c.z_max > cube.z_max:
                new_c = Cube(c.on, c.x_min, c.x_max, c.y_min, c.y_max, cube.z_max, c.z_max)
                c.z_max = cube.z_max
                new_cubes.append(new_c)
        else:
            new_cubes.append(c)
    new_cubes.append(cube)
    cubes = new_cubes


# Part 1
initialization = Cube(False, -50, 51, -50, 51, -50, 51)
print(sum(c.size for c in cubes if c.on and initialization.overlap(c)))
# 600458


# Part 2
print(sum(c.size for c in cubes if c.on))
# 1334275219162622
