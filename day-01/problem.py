with open('input') as f:
    values = [int(line) for line in f.read().strip().split('\n')]


# Part 1
print(sum(i < j for i, j in zip(values[:-1], values[1:])))
# 1228

# Part 2
new_values = [sum(a) for a in zip(values[:-2], values[1:-1], values[2:])]
print(sum(i < j for i, j in zip(new_values[:-1], new_values[1:])))
# 1257
