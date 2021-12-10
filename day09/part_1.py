import math
lines = [[int(x) for x in line] for line in open('day09/0.in').read().splitlines()]

risk_lvl = 0
for y, row in enumerate(lines):
    for x, height in enumerate(row):
        if x > 0 and row[x - 1] <= height:
            continue
        if x < len(row) - 1 and row[x + 1] <= height:
            continue
        if y > 0 and lines[y - 1][x] <= height:
            continue
        if y < len(lines) - 1 and lines[y + 1][x] <= height:
            continue
        risk_lvl += 1 + height

print(f'Part 1: {risk_lvl}')

def neighbors(y, x):
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbs = []
    for d in deltas:
        if 0 <= y + d[0] < len(lines) and 0 <= x + d[1] < len(lines[0]):
            neighbs.append((y + d[0], x + d[1]))
    return neighbs

def visit_point(y, x):
    if lines[y][x] == 9 or (y, x) in visited:
        return 0

    basin_size = 0
    stack = [(y, x)]
    visited.add((y, x))
    while stack:  # Flood fill with stack
        curr_y, curr_x = stack.pop()
        basin_size += 1
        neighbs = neighbors(curr_y, curr_x)
        for neighb_y, neighb_x in neighbs:
            if lines[neighb_y][neighb_x] != 9 and (neighb_y, neighb_x) not in visited:
                stack.append((neighb_y, neighb_x))
                visited.add((neighb_y, neighb_x))
    return basin_size

visited = set()
basin_sizes = [visit_point(y, x) for y in range(len(lines)) for x in range(len(lines[0]))]

print(f'Part 2: {math.prod(sorted(basin_sizes)[-3:])}')
