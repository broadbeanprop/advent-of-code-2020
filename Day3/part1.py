current_coordinates = [0, 0]
entries = open('input.txt', 'r').read().splitlines()

def find_answer(slope_right, slope_down):
    global current_coordinates
    current_coordinates = [0, 0]
    amount_of_trees = 0

    while current_coordinates[0] < len(entries):
        if get_at_coordinates() == "#":
            amount_of_trees +=1

        slope(slope_right, slope_down)

    return amount_of_trees

def slope(slope_right, slope_down):
    current_coordinates[0] += slope_down
    width = len(str(entries[0]))

    possible_steps = (current_coordinates[1] + slope_right) - (width - 1)

    if possible_steps < 1:
        current_coordinates[1] += slope_right
    else:
        current_coordinates[1] = possible_steps - 1

def get_at_coordinates():
    return entries[current_coordinates[0]][current_coordinates[1]]
