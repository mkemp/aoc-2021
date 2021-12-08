from statistics import mean, median

with open('input') as f:
    values = [int(token) for token in f.read().strip().split(',')]


# Part 1
align_on = int(round(median(values)))
print(sum(abs(x - align_on) for x in values))
# 355764


# Part 2
align_on = int(round(mean(values)))
costs = {0: 0}
for x in range(1, max(values) - align_on + 1):
    costs[x] = costs[x - 1] + x
print(sum(costs[abs(x - align_on)] for x in values))
# 99634572
