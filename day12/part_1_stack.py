from collections import defaultdict

def count_paths(start, doubled):
    paths = 0
    stack = [([start], doubled)]
    while stack:
        path, doubled = stack.pop()
        last_node = path[-1]

        for next_node in reachables[last_node]:
            if next_node == 'end':
                paths += 1
            elif next_node.isupper() or next_node not in path:
                stack.append((path + [next_node], doubled))
            elif not doubled:
                stack.append((path + [next_node], True))
    return paths

lines = [x.split('-') for x in open('day12/0.in').read().splitlines()]
reachables = defaultdict(set)
for a, b in lines:
    if b != 'start':
        reachables[a].add(b)
    if a != 'start':
        reachables[b].add(a)

print(f'Part 1: {count_paths("start", True)}')
print(f'Part 2: {count_paths("start", False)}')
