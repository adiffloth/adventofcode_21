lines = [x.split(' | ') for x in open('day08/0.in').read().splitlines()]
inputs_ls = []
segments_ls = []
for line in lines:
    inputs_ls.append([set(x) for x in line[0].split()])
    segments_ls.append([set(x) for x in line[1].split()])

sum = 0
for inputs, segments in zip(inputs_ls, segments_ls):
    numbers = [''] * 10
    for input in inputs:  # These can be identified with no previous knowledge
        if len(input) == 2:
            numbers[1] = input
        elif len(input) == 3:
            numbers[7] = input
        elif len(input) == 4:
            numbers[4] = input
        elif len(input) == 7:
            numbers[8] = input

    for input in inputs:  # These use values identified above, need a new for loop.
        if len(input) == 5:
            if len(input - numbers[1]) == 3:
                numbers[3] = input
            elif len(input - numbers[4]) == 3:
                numbers[2] = input
            else:
                numbers[5] = input
        elif len(input) == 6:
            if len(input - numbers[1]) == 5:
                numbers[6] = input
            elif len(input - numbers[4]) == 2:
                numbers[9] = input
            else:
                numbers[0] = input

    sum += int(''.join([str(numbers.index(x)) for x in segments]))

print(f'Part 2: {sum}')
