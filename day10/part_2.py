import statistics
# lines = [list(x) for x in open('day10/0.in').read().splitlines()]
lines = [list(x) for x in open('day10/0.in').read().splitlines()]

pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
points = {'(': 1, '[': 2, '{': 3, '<': 4}
openers = set(pairs.values())

scores = []
for line in lines:
    score = 0
    corrupt = False
    stack = [line[0]]
    for c in line[1:]:
        if c in openers:  # Opening marker
            stack.append(c)
        elif stack.pop() != pairs[c]:  # Incorrect close
            corrupt = True
            break
    if not corrupt:
        while stack:
            c = stack.pop()
            score = score * 5 + points[c]
        scores.append(score)

print(f'Part 2: {statistics.median(scores)}')
