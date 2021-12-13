import numpy as np

lines = [x.splitlines() for x in open('day13/0.in').read().split('\n\n')]
points = {(int(p.split(',')[1]), int(p.split(',')[0])) for p in lines[0]}
folds = [(f.split('=')[0][-1], int(f.split('=')[1])) for f in lines[1]]

x_max = 0
y_max = 0
for point in points:
    y_max = max(y_max, point[0])
    x_max = max(x_max, point[1])

grid = np.zeros((y_max + 1, x_max + 1), dtype=bool)

for point in points:
    grid[point] = 1

for i, fold in enumerate(folds):
    if fold[0] == 'y':
        upper = grid[:fold[1]]
        lower = grid[fold[1] + 1:]
        grid = upper + np.flipud(lower)
    else:
        left = grid[:, :fold[1]]
        right = grid[:, fold[1] + 1:]
        grid = left + np.fliplr(right)
    if i == 0:
        print(f'Part 1: {sum(sum(grid))}')

print('Part 2:')
for r in grid:
    for c in r:
        if c:
            print(u'\u2588', end='')
        else:
            print(' ', end='')
    print()
