lines = [(x.split()[0], int(x.split()[1])) for x in open('day02/0.in').read().splitlines()]

def forward(x, h_pos, depth):
    h_pos += x
    return h_pos, depth

def up(x, h_pos, depth):
    depth -= x
    return h_pos, depth

def down(x, h_pos, depth):
    depth += x
    return h_pos, depth

dirs = {'forward': forward,
        'up': up,
        'down': down
        }

h_pos = depth = 0

for line in lines:
    h_pos, depth = dirs[line[0]](line[1], h_pos, depth)

print(h_pos, depth)
print(h_pos * depth)
