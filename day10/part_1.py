lines = [list(x) for x in open('day10/0.in').read().splitlines()]

pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
openers = set(pairs.values())

score = 0
for line in lines:
    stack = [line[0]]
    for c in line[1:]:
        if c in openers:  # Opening marker
            stack.append(c)
        elif stack.pop() != pairs[c]:  # Incorrect close
            score += points[c]
            break

print(f'Part 1: {score}')
