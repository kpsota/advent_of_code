

def load_stacks(file):

    with open(file) as inf:

        stacks = []
        reversed_lines = [l.replace('\n', '') for l in list(reversed(inf.readlines()))]
        stacks_numbers = reversed_lines.pop(0)
        stacks_numbers_list = list(filter(None, stacks_numbers.split(' ')))
        for sn in stacks_numbers_list:
            stacks.append([stacks_numbers.index(sn)])

        for row in reversed_lines:
            for stack in stacks:
                if stack[0] <= len(row) and row[stack[0]].strip():
                    stack.append(row[stack[0]])

        return stacks


def move_crates(stacks, file, method):

    with open(file) as inf:
        for row in inf:
            move = list(filter(None, [m.replace('move', '').replace('from', '').replace('to', '').replace('\n', '') for m in row.split(' ')]))
            stack_from = stacks[int(move[1]) - 1]
            stack_to = stacks[int(move[2]) - 1]

            if method == 'one by one':
                crates_to_move = list(reversed(stack_from[-int(move[0]):]))
            elif method == 'at once':
                crates_to_move = stack_from[-int(move[0]):]

            for i in range(0, len(crates_to_move)):
                stack_from.pop(-1)

            for c in crates_to_move:
                stack_to.append(c)

# first part
stacks = load_stacks('data/input_stacks.txt')
move_crates(stacks, 'data/input_moves.txt', 'one by one')
print(''.join([s[len(s) - 1] for s in stacks]))

# second part
stacks = load_stacks('data/input_stacks.txt')
move_crates(stacks, 'data/input_moves.txt', 'at once')
print(''.join([s[len(s) - 1] for s in stacks]))