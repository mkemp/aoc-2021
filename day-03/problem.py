from operator import ge, lt

with open('input') as f:
    values = [line for line in f.read().strip().split('\n')]

rows, cols = len(values), len(values[0])
threshold = rows / 2
gamma, epsilon = '', ''

# Part 1
for c in range(cols):
    ones = sum(int(row[c]) for row in values)
    if ones >= threshold:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

# print(f'gamma = {gamma} | epsilon = {epsilon}')
print(int(gamma, 2) * int(epsilon, 2))
# 2954600


# Part 2
def find_common(values, op, col=0):
    if len(values) == 1:
        return values[0]
    threshold = len(values) / 2
    ones = sum(int(row[col]) for row in values)
    if op(ones, threshold):
        return find_common([row for row in values if row[col] == '1'], op, col + 1)
    else:
        return find_common([row for row in values if row[col] == '0'], op, col + 1)


oxy = find_common(values, ge)
co2 = find_common(values, lt)
# print(f'oxy = {oxy} | co2 = {co2}')
print(int(oxy, 2) * int(co2, 2))
# 1662846
