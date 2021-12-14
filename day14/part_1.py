from collections import Counter, defaultdict
lines = [x for x in open('day14/0.in').read().splitlines()]

template = lines[0]
rules = {r.split(' -> ')[0]: r.split(' -> ')[1] for r in lines[2:]}

pairs = defaultdict(int)
for x in zip(template, template[1:]):
    pairs[''.join(x)] = 1

def calculate_answer(pairs):
    elements = defaultdict(int)
    for pair, count in pairs.items():
        elements[pair[0]] += count
    elements[template[-1]] += 1
    elements = Counter(elements)
    return elements.most_common()[0][1] - elements.most_common()[-1][1]

def insert_pairs(pairs, steps):
    for _ in range(steps):
        new_pairs = defaultdict(int)
        for pair in pairs:
            child_1 = ''.join((pair[0], rules[pair]))
            child_2 = ''.join((rules[pair], pair[1]))
            new_pairs[child_1] += pairs[pair]
            new_pairs[child_2] += pairs[pair]
        pairs = new_pairs
    return pairs

pairs = insert_pairs(pairs, 10)
print(f'Part 1: {calculate_answer(pairs)}')

pairs = insert_pairs(pairs, 30)
print(f'Part 2: {calculate_answer(pairs)}')
