with open('day8/input.txt', 'r') as file:
    instructions = file.read().splitlines()
    accumulator = 0
    current_instruction = 0
    instruction_count = {}
    loops = False

    def execute(instruction_to_change):
        global accumulator
        global current_instruction
        global instruction_count
        global loops

        if instruction_count.get(current_instruction) == None:
            instruction_count[current_instruction] = 1
        else:
            loops = True
            return False

        if current_instruction >= len(instructions):
            return True

        instruction_parts = instructions[current_instruction].split(" ")
        instruction = instruction_parts[0]
        argument = eval(instruction_parts[1])
        
        if instruction_to_change == current_instruction:
            if instruction == "nop":
                instruction = "jmp"
            
            elif instruction == "jmp":
                instruction = "nop"

        if instruction == "acc":
            accumulator += argument
            current_instruction += 1
        elif instruction == "jmp":
            current_instruction += argument
        elif instruction == "nop":
            current_instruction += 1
    
    def find_instruction_to_change():
        global accumulator
        global current_instruction
        global instruction_count
        global loops

        for instruction_to_change in range(len(instructions)):
            while not loops:
                if execute(instruction_to_change):
                    return
            
            accumulator = 0
            current_instruction = 0
            instruction_count = {}
            loops = False

    find_instruction_to_change()
    print("The accumulator with the working instructions is: " + str(accumulator))