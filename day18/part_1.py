def add(n1, n2):
    return '[' + n1 + ',' + n2 + ']'

def find_reg_num(s, idx, dir='left'):
    increment = -1
    if dir == 'right':
        increment = 1
    while 0 < idx < len(s) - 1:
        idx += increment
        if s[idx].isdigit():
            return int(s[idx]), idx
    return (None, idx)

def explode(s, idx):

    pair = (int(s[idx + 1]), int(s[idx + 3]))
    lt = find_reg_num(s, idx, 'left')
    new_lt = None
    if lt[0]:
        new_lt = (pair[0] + lt[0], lt[1])
    rt = find_reg_num(s, idx + 3, 'right')
    new_rt = None
    if rt[0]:
        new_rt = (pair[1] + rt[0], rt[1])

    new_s = ''
    if new_lt:
        new_s = s[:idx - 2] + str(new_lt[0]) + ','
    else:
        new_s = s[:idx]

    # middle
    new_s += '0' + s[idx + 5:rt[1]]

    if new_rt:
        new_s += str(new_rt[0]) + s[new_rt[1] + 1:]
    else:
        new_s += s[rt[1]:]

    return new_s

def reduce(s):
    depth = 0
    idx = 0
    res = ''
    while idx < len(s):
        if s[idx] == '[':
            depth += 1
        elif s[idx] == ']':
            depth -= 1

        if depth == 5:
            res = explode(s, idx)
            # print(res)
            idx = 0
            depth = 0

        idx += 1
    return res


lines = [x for x in open('day18/1.in').read().splitlines()]

assert reduce('[[[[[9,8],1],2],3],4]') == '[[[[0,9],2],3],4]'
assert reduce('[7,[6,[5,[4,[3,2]]]]]') == '[7,[6,[5,[7,0]]]]'
assert reduce('[[6,[5,[4,[3,2]]]],1]') == '[[6,[5,[7,0]]],3]'
assert reduce('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
assert reduce('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'
assert reduce('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]') == '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'
print(reduce('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'))
assert reduce('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]') == '[[[[0,7],4],[15,[0,13]]],[1,1]]'
assert reduce('[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]') == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
print('Tests passed: explode()')

assert add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]') == '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
print('Tests passed: add()')
