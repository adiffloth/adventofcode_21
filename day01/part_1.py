lines = [int(x) for x in open('day01/0.in').read().splitlines()]

print(f'Part 1: {sum([lines[x + 1] > lines[x] for x in range(len(lines) - 1)])}')

depths = [sum(lines[i:i + 3]) for i in range(len(lines) - 2)]

print(f'Part 2: {sum((depths[x + 1] > depths[x] for x in range(len(depths) - 1)))}')


# This is more clever. There is no need to calculate the rolling windows.
# The last two numbers of each window cancel the first two numbers of the next window.
# All you have to compare is i and i + 3.
# A
# B B  -> cancels
# C C  -> cancels
#   D  -> just compare A and D
print(f'Part 1: {sum((b > a) for (a, b) in zip(lines, lines[1:]))}')
print(f'Part 2: {sum((b > a) for (a, b) in zip(lines, lines[3:]))}')
