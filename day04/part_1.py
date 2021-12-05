import numpy as np

def check_rows(h):
    for row in h:
        if np.all(row):
            return True
    return False

def score(b, h):
    return sum(sum(np.multiply(b, np.logical_not(h))))

lines = open('day04/0.in').read().split('\n\n')
moves = [int(x) for x in lines.pop(0).split(',')]
boards_s = [[x.split() for x in line.split('\n')] for line in lines]
boards_ls = [np.array(b, dtype=int) for b in boards_s]
hits_ls = [np.zeros_like(boards_ls[0], dtype=int) for _ in range(len(boards_ls))]

turn = 0
winner = None
while not winner:
    new_hits_ls = []
    for board_id, (board, hits) in enumerate(zip(boards_ls, hits_ls)):
        new_hits = hits + (board == moves[turn])
        new_hits_ls.append(new_hits)
        if check_rows(new_hits) or check_rows(new_hits.T):
            winner = board_id
            break
    hits_ls = new_hits_ls
    turn += 1

print(f'Final score: {score(boards_ls[winner], hits_ls[winner]) * moves[turn - 1]}')
