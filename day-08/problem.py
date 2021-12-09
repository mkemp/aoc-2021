#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

with open('input') as f:
    values = [line.split(' | ') for line in f.read().strip().split('\n')]


# Part 1
count = 0
for _, outputs in values:
    for o in outputs.split():
        count += len(o) in (2, 3, 4, 7)

print(count)
# 301


# Part 2
mapping = {
  'abcefg': '0',
  'cf': '1',
  'acdeg': '2',
  'acdfg': '3',
  'bcdf': '4',
  'abdfg': '5',
  'abdefg': '6',
  'acf': '7',
  'abcdefg': '8',
  'abcdfg': '9',
}


def decode_signals(signals):
    tr = {}
    signals = [set(s) for s in signals]
    zero_six_nine = list(filter(lambda x: len(x) == 6, signals))
    one = next(filter(lambda x: len(x) == 2, signals))
    two_three_five = list(filter(lambda x: len(x) == 5, signals))
    four = next(filter(lambda x: len(x) == 4, signals))
    six = next(filter(lambda x: len(one - x), zero_six_nine))
    seven = next(filter(lambda x: len(x) == 3, signals))
    eight = next(filter(lambda x: len(x) == 7, signals))
    nine = next(filter(lambda x: not len(four - x), zero_six_nine))
    zero = next(filter(lambda x: x is not six and x is not nine, zero_six_nine))
    two_or_three = next(filter(lambda x: len(six - x) == 2, two_three_five))
    tr[next(iter(seven - one))] = 'a'
    tr[next(iter(four - two_or_three - one))] = 'b'
    tr[next(iter(one - six))] = 'c'
    tr[next(iter(eight - zero))] = 'd'
    tr[next(iter(eight - nine))] = 'e'
    tr[next(iter(one - (one - six)))] = 'f'
    tr[next(iter(nine - four - seven))] = 'g'
    return tr


def translate(outputs, tr):
    return int(''.join(mapping[''.join(sorted(tr[c] for c in o))] for o in outputs))


total = 0
for signals, outputs in values:
    total += translate(outputs.split(), decode_signals(signals.split()))

print(total)
# 908067
