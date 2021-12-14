from collections import defaultdict, deque

with open('input') as f:
    values = [line.split('-') for line in f.read().strip().split('\n')]


links = defaultdict(list)
for one, two in values:
    if one != 'end' and two != 'start':
        links[one].append(two)
    if two != 'end' and one != 'start':
        links[two].append(one)


# Part 1
def solve_p1():
    start = ('start', {'start'}, None)
    path = 0
    dq = deque([start])
    while dq:
        pos, small, twice = dq.popleft()
        if pos == 'end':
            path += 1
            continue
        for link in links[pos]:
            if link not in small:
                link_small = set(small)
                if link.lower() == link:
                    link_small.add(link)
                dq.append((link, link_small, twice))
    return path


print(solve_p1())
# 5104


# Part 2
def solve_p2():
    start = ('start', {'start'}, None)
    path = 0
    dq = deque([start])
    while dq:
        pos, small, twice = dq.popleft()
        if pos == 'end':
            path += 1
            continue
        for link in links[pos]:
            if link not in small:
                link_small = set(small)
                if link.lower() == link:
                    link_small.add(link)
                dq.append((link, link_small, twice))
            elif link in small and twice is None and link not in ('start', 'end'):
                dq.append((link, small, link))
    return path


print(solve_p2())
# 149220
