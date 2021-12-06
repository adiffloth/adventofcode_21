from collections import defaultdict

def make_line(x1, y1, x2, y2):
    if x1 == x2:
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    elif y1 == y2:
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    else:
        return []

lines = []
for line in open('day05/0.in').read().splitlines():
    lines.append([(int(x.split(',')[0]), int(x.split(',')[1])) for x in line.split(' -> ')])

points = defaultdict(int)

for line in lines:
    for point in make_line(*line[0], *line[1]):
        points[point] += 1

print(f'Part 1: {sum([1 for cnt in points.values() if cnt >= 2])}')
