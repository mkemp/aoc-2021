from itertools import combinations, permutations, product


add_offset = lambda one, two: (one[0] + two[0], one[1] + two[1], one[2] + two[2])
sub_offset = lambda one, two: (one[0] - two[0], one[1] - two[1], one[2] - two[2])


class Scanner(object):

    def __init__(self, idx, beacons):
        super(Scanner, self).__init__()
        self.idx = idx
        self.beacons = beacons
        self.offset = None
        self.failed_to_align = set()

    def __hash__(self):
        return self.idx

    def __repr__(self):
        return f'<Scanner: {self.idx} @ {self.offset}>'

    def try_to_align(self, known_beacons):
        untried = set()
        for axis in permutations(range(3)):
            for sign in product((-1, 1), (-1, 1), (-1, 1)):
                candidates = {(b[axis[0]] * sign[0], b[axis[1]] * sign[1], b[axis[2]] * sign[2]) for b in self.beacons}
                untried = known_beacons - self.failed_to_align
                for cb in candidates:
                    for ub in untried:
                        offset = sub_offset(ub, cb)
                        attempt = set(map(lambda beacon: add_offset(beacon, offset), candidates))
                        if len(known_beacons & attempt) >= 12:
                            known_beacons.update(attempt)
                            self.offset = offset
                            return True
        self.failed_to_align.update(untried)
        return False


with open('input') as f:
    raw_scanners = f.read().strip().split('\n\n')
    scanners = {}
    for i, lines in enumerate(raw_scanners):
        scanners[i] = Scanner(i, [tuple(map(int, line.split(','))) for line in lines.split('\n')[1:]])
    scanners[0].offset = (0, 0, 0)


# Part 1
beacons = set(scanners[0].beacons)
to_align = {scanners[i] for i in range(1, len(scanners))}
while to_align:
    # print(f'Remaining to align:')
    # print(', '.join(map(str, to_align)))
    for scanner in to_align:
        if scanner.try_to_align(beacons):
            to_align.remove(scanner)
            break

print(len(beacons))
# 378


# Part 2
def manhattan_dist(one, two):
    return sum(map(abs, sub_offset(one, two)))


print(max(manhattan_dist(one.offset, two.offset) for one, two in combinations(scanners.values(), 2)))
# 13148
