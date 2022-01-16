from collections import defaultdict, namedtuple
import math
from heapq import heappop, heappush
from networkx.classes.digraph import DiGraph
import numpy as np
import networkx as nx


def L1_dist(one, two):
    return abs(one[0] - two[0]) + abs(one[1] - two[1])

def L2_dist(one, two):
    return math.sqrt((one[0] - two[0]) ** 2 + (one[1] - two[1]) ** 2)

def neighbors(y, x, y_dim, x_dim):
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighbs = []
    for d in deltas:
        if 0 <= y + d[0] < y_dim and 0 <= x + d[1] < x_dim:
            neighbs.append((y + d[0], x + d[1]))
    return neighbs

def print_path(grid, path):
    path_matrix = np.array(grid, dtype=str)
    for point in path:
        path_matrix[point] = u'\u2588'
    for j in range(len(path_matrix)):
        for i in range(len(path_matrix[0])):
            print(path_matrix[j, i], end='')
        print()

def shortest_path(grid, start, goal, algo='dijkstra'):
    best_cum_costs = defaultdict(lambda: Point(np.inf, None))  # {node: (cumulative cost, prev)}
    best_cum_costs[start] = Point(grid[start], None)
    q = [PQ_item(grid[start], start)]
    y_dim, x_dim = grid.shape
    while q:
        curr = heappop(q).coords
        if curr == goal:
            total_risk = best_cum_costs[curr].cost
            path = []
            path.append(curr)
            while curr != start:
                curr = best_cum_costs[curr].prev
                path.append(curr)
            return path[::-1], total_risk

        for neighb in neighbors(*curr, y_dim, x_dim):
            neighb_cost = best_cum_costs[curr].cost + grid[neighb]
            if neighb_cost < best_cum_costs[neighb].cost:
                best_cum_costs[neighb] = Point(neighb_cost, curr)
                heuristic = L1_dist(neighb, goal) if algo == 'astar' else 0
                est_total_cost = neighb_cost + heuristic
                heappush(q, PQ_item(est_total_cost, neighb))

    return 'No route found.'


Point = namedtuple('Point', ['cost', 'prev'])
PQ_item = namedtuple('PQ_item', ['priority', 'coords'])
cg_pt1 = np.genfromtxt('day15/0.in', delimiter=1, dtype=int)

cg_pt2 = np.zeros((len(cg_pt1) * 5, len(cg_pt1[0]) * 5), int)
for y in range(len(cg_pt2)):
    for x in range(len(cg_pt2[0])):
        # Cycle through smaller grid: cg[y % y_dim from smaller grid].
        # Add 1 for each subsequent panel in the 5x5 repetition, in the x and y dimensions.
        # Minus one cause the input doesn't start at zero.
        # Finally mod 9 + 1 because the output cycles 1 through 9.
        cg_pt2[y, x] = (cg_pt1[y % cg_pt1.shape[0], x % cg_pt1.shape[1]] + y // cg_pt1.shape[0] + x // cg_pt1.shape[1] - 1) % 9 + 1

dijks_path = shortest_path(cg_pt1, (0, 0), (cg_pt1.shape[0] - 1, cg_pt1.shape[1] - 1))
print(f'Part 1 dijks: {dijks_path[1] - cg_pt1[(0, 0)]}')  # Don't count the first one

astar_path = shortest_path(cg_pt1, (0, 0), (len(cg_pt1) - 1, len(cg_pt1[0]) - 1), algo='astar')
print(f'Part 1 astar: {astar_path[1] - cg_pt1[(0, 0)]}')

dijks_path_pt2 = shortest_path(cg_pt2, (0, 0), (cg_pt2.shape[0] - 1, cg_pt2.shape[1] - 1))
print(f'Part 2 dijks: {dijks_path_pt2[1] - cg_pt2[(0, 0)]}')  # Don't count the first one

astar_path_pt2 = shortest_path(cg_pt2, (0, 0), (len(cg_pt2) - 1, len(cg_pt2[0]) - 1), algo='astar')
print(f'Part 2 astar: {astar_path_pt2[1] - cg_pt2[(0, 0)]}')


G_pt1 = nx.grid_2d_graph(len(cg_pt1), len(cg_pt1[0]), create_using=DiGraph)
for u, v in G_pt1.edges:
    G_pt1[u][v]['weight'] = cg_pt1[v[1]][v[0]]

G_pt2 = nx.grid_2d_graph(len(cg_pt2), len(cg_pt2[0]), create_using=DiGraph)
for u, v in G_pt2.edges:
    G_pt2[u][v]['weight'] = cg_pt2[v[1]][v[0]]

print(f'Part 1 Networkx: {nx.shortest_path_length(G_pt1, (0, 0), (len(cg_pt1) - 1, len(cg_pt1[0]) - 1), weight="weight")}')
print(f'Part 2 Networkx: {nx.shortest_path_length(G_pt2, (0, 0), (len(cg_pt2) - 1, len(cg_pt2[0]) - 1), weight="weight")}')
