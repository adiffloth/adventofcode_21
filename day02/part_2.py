lines = [(x.split()[0], int(x.split()[1])) for x in open('day02/0.in').read().splitlines()]

def forward(x, h_pos, depth, aim):
    h_pos += x
    depth += aim * x
    return h_pos, depth, aim

def up(x, h_pos, depth, aim):
    aim -= x
    return h_pos, depth, aim

def down(x, h_pos, depth, aim):
    aim += x
    return h_pos, depth, aim

dirs = {'forward': forward,
        'up': up,
        'down': down
        }

h_pos = depth = aim = 0

for line in lines:
    h_pos, depth, aim = dirs[line[0]](line[1], h_pos, depth, aim)

print(h_pos, depth)
print(h_pos * depth)
