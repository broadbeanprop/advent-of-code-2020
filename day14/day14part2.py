import collections
import itertools
import copy

def apply_mask(number, mask):
    number_as_binary = list('{0:036b}'.format(number))

    for i in range(len(mask)):
        if mask[i] == "0":
            continue

        number_as_binary[i] = mask[i]

    return "".join(number_as_binary)

def find_all_occurances_in_string(string, character):
    return [i for i, ltr in enumerate(string) if ltr == character]

with open('day14/input.txt', 'r') as file:
    mem = collections.defaultdict(int)
    instructions = file.read().splitlines()
    mem = collections.defaultdict(int)
    mask = ""

    for instruction in instructions:
        instruction_parts = instruction.split(" = ")

        if instruction_parts[0] == "mask":
            mask = instruction_parts[1]

        else:
            address = instruction_parts[0][4:-1]
            masked_address = apply_mask(int(address), mask)
            occurances = find_all_occurances_in_string(masked_address, "X")
            addresses = []

            for floating_bit in itertools.product(range(2), repeat=masked_address.count("X")):
                new_address = list(copy.copy(masked_address))
                
                for i in range(len(floating_bit)):
                    new_address[occurances[i]] = floating_bit[i]
                
                mem[int("".join(str(x) for x in new_address), 2)] = int(instruction_parts[1])
    
    total = 0
    for item in mem:
        total += mem[item]

    print(total)
