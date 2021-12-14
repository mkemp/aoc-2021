from collections import Counter

with open('input') as f:
    template, values = f.read().strip().split('\n\n')
    rules = dict(line.split(' -> ') for line in values.split('\n'))


def do_reaction(iterations):
    polymer = Counter()
    for i in range(len(template) - 1):
        polymer[template[i:i + 2]] += 1
    for _ in range(iterations):
        next_polymer = Counter()
        for k, v in polymer.items():
            next_polymer[k[0] + rules[k]] += v
            next_polymer[rules[k] + k[1]] += v
        polymer = next_polymer
    count = Counter()
    for k, v in polymer.items():
        count[k[0]] += v
    count[template[-1]] += 1
    return max(count.values()) - min(count.values())


# Part 1
print(do_reaction(10))
# 3284


# Part 2
print(do_reaction(40))
# 4302675529689
