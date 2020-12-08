with open('day8/input.txt', 'r') as file:
    instructions = file.read().splitlines()
    accumulator = 0
    current_instruction = 0
    instruction_count = {}
    keep_running = True

    def execute():
        global accumulator
        global current_instruction
        global instruction_count
        global keep_running

        if instruction_count.get(current_instruction) == None:
            instruction_count[current_instruction] = 1
        else:
            keep_running = False
            return

        instruction_parts = instructions[current_instruction].split(" ")
        instruction = instruction_parts[0]
        argument = eval(instruction_parts[1])
        
        if instruction == "acc":
            accumulator += argument
            current_instruction += 1
        elif instruction == "jmp":
            current_instruction += argument
        elif instruction == "nop":
            current_instruction += 1
        
    while keep_running:
        execute()

    print("The accumulator in part 1 is: " + str(accumulator))
