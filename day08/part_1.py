lines = [x.split(' | ') for x in open('day08/0.in').read().splitlines()]
segments = [line[1].split() for line in lines]

ans = 0
for segment in segments:
    ans += sum(1 for s in segment if len(s) in [2, 3, 4, 7])

print(f'Part 1: {ans}')
