from collections import Counter, defaultdict

with open('input') as f:
    values = [int(token) for token in f.read().strip().split(',')]


def spawn_for_day(current):
    next = defaultdict(int)
    if 0 in current:
        next[6] += current[0]
        next[8] += current[0]
    for r in range(1, 9):
        if r in current:
            next[r - 1] += current[r]
    return next


# Part 1
lf = Counter(values)

population = lf
for _ in range(80):
    population = spawn_for_day(population)

print(sum(population.values()))

# Part 2
population = lf
for _ in range(256):
    population = spawn_for_day(population)

print(sum(population.values()))
