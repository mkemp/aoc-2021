import heapq


class GridWithWeights(object):

    def __init__(self, grid):
        super(GridWithWeights, self).__init__()
        self.grid = grid
        self.cols = max(x for x, _ in grid.keys()) + 1
        self.rows = max(y for _, y in grid.keys()) + 1

    def cost(self, from_node, to_node):
        return self.grid.get(to_node, 1)

    def neighbors(self, node):
        x, y = node
        if 0 <= x < self.rows and 0 <= y < self.cols:
            if 0 < x:
                yield (x - 1, y)
            if x < self.rows - 1:
                yield (x + 1, y)
            if 0 < y:
                yield (x, y - 1)
            if y < self.cols - 1:
                yield (x, y + 1)


class PriorityQueue(object):

    def __init__(self):
        super(PriorityQueue, self).__init__()
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(one, two):
    (x1, y1) = one
    (x2, y2) = two
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    # path.append(start) # optional, we don't count first node anyway
    # path.reverse() # optional, are just looking for the total cost
    return path


with open('input') as f:
    values = [line for line in f.read().strip().split('\n')]

grid = {}
for y, row in enumerate(values):
    for x, val in enumerate(row):
        grid[(x, y)] = int(val)


# Part 1
graph = GridWithWeights(grid)
start, goal = (0, 0), (graph.cols - 1, graph.rows - 1)
came_from, cost_so_far = a_star_search(graph, start, goal)
print(sum(grid[node] for node in reconstruct_path(came_from, start, goal)))
# 589


# Part 2
def shift_and_increment(grid, d_x, d_y):
    g, i = {}, d_x + d_y
    for (x, y), v in grid.items():
        v = v + i
        g[(x + d_x * 100, y + d_y * 100)] = v - 9 if v > 9 else v
    return g


new_grid = {}
for d_y in range(5):
    for d_x in range(5):
        if d_x != 0 or d_y != 0:
            new_grid.update(shift_and_increment(grid, d_x, d_y))
        else:
            new_grid.update(grid)


graph = GridWithWeights(new_grid)
start, goal = (0, 0), (graph.cols - 1, graph.rows - 1)
came_from, cost_so_far = a_star_search(graph, start, goal)
print(sum(new_grid[node] for node in reconstruct_path(came_from, start, goal)))
# 2885
