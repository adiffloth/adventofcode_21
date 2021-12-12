from collections import defaultdict

def paths(curr_node, visited, doubled):
    if curr_node == 'end':
        return 1
    if curr_node.islower() and curr_node in visited:
        if not doubled:
            doubled = True
        else:
            return 0

    visited = visited | {curr_node}
    length = 0
    for next_node in reachables[curr_node]:
        length += paths(next_node, visited, doubled)
    return length

lines = [x.split('-') for x in open('day12/0.in').read().splitlines()]

reachables = defaultdict(set)
for a, b in lines:
    if b != 'start':
        reachables[a].add(b)
    if a != 'start':
        reachables[b].add(a)

print(f'Part 1: {paths("start", set(), True)}')
print(f'Part 2: {paths("start", set(), False)}')