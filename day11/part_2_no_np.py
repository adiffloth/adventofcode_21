# lines = [[list(x) for x in open('day11/0.in').read().splitlines()]]
lines = [list(map(int, x)) for x in open('day11/0.in').read().splitlines()]
print(lines)

def neighbors_8(y, x):
    deltas = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    neighbs = []
    for d in deltas:
        if 0 <= y + d[0] < len(lines) and 0 <= x + d[1] < len(lines[0]):
            neighbs.append((y + d[0], x + d[1]))
    return neighbs

def visit_pt(y, x):
    if lines[y][x] <= 9 or (y, x) in flashed:  # I'm not going to flash
        return

    flashed.add((y, x))  # I've flashed, so increment neighbors and cascade
    stack = [(y, x)]
    while stack:
        curr_y, curr_x = stack.pop()
        neighbs = neighbors_8(curr_y, curr_x)
        for neighb_y, neighb_x in neighbs:
            lines[neighb_y][neighb_x] += 1
            if lines[neighb_y][neighb_x] > 9 and (neighb_y, neighb_x) not in flashed:
                flashed.add((neighb_y, neighb_x))
                stack.append((neighb_y, neighb_x))

step = 0
flashed = set()
while len(flashed) < 100:
    step += 1
    flashed = set()
    lines = [[i + 1 for i in line] for line in lines]

    for j in range(len(lines)):
        for i in range(len(lines[0])):
            visit_pt(j, i)

    lines = [[i if i <= 9 else 0 for i in line] for line in lines]

print(f'Part 2: {step}')
