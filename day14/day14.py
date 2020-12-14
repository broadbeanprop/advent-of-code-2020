import collections

def apply_mask(number, mask):
    number_as_binary = list('{0:036b}'.format(number))

    for i in range(len(mask)):
        if mask[i] == "X":
            continue

        number_as_binary[i] = mask[i]

    return int("".join(number_as_binary), 2)

with open('day14/input.txt', 'r') as file:
    instructions = file.read().splitlines()
    mem = collections.defaultdict(int)
    mask = ""

    for instruction in instructions:
        instruction_parts = instruction.split(" = ")

        if instruction_parts[0] == "mask":
            mask = instruction_parts[1]

        else:
            instruction_parts[1] = apply_mask(int(instruction_parts[1]), mask)
            command = " = ".join(str(x) for x in instruction_parts)
            exec(command)

    total = 0
    for item in mem:
        total += mem[item]

    print(total)