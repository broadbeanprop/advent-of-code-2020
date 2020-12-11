CHANGED = True
OCCUPIED = "#"
EMPTY = "L"
FLOOR = "."

def is_occupied(grid, x, y):
    if (y < 0 or
        x < 0 or 
        y >= len(grid) or
        x >= len(grid[y])):
        return False
    
    return grid[y][x] == OCCUPIED

def find_amount_of_adjacent_occupied_seats(grid, x, y):
    amount = 0

    if is_occupied(grid, x+1, y):
        amount += 1
    if is_occupied(grid, x-1, y):
        amount += 1
    if is_occupied(grid, x, y+1):
        amount += 1
    if is_occupied(grid, x, y-1):
        amount += 1
    if is_occupied(grid, x+1, y+1):
        amount += 1
    if is_occupied(grid, x-1, y-1):
        amount += 1
    if is_occupied(grid, x+1, y-1):
        amount += 1
    if is_occupied(grid, x-1, y+1):
        amount += 1

    return amount

def get_next_grid(grid):
    global CHANGED

    next_grid = []
    CHANGED = False
    for y in range(len(grid)):
        next_grid.append("")

        for x in range(len(grid[y])):
            position = grid[y][x]
            amount_of_adjacent_occupied_seats = find_amount_of_adjacent_occupied_seats(grid, x, y)
            
            if position == EMPTY and amount_of_adjacent_occupied_seats == 0:
                next_grid[y] += OCCUPIED
                CHANGED = True
            elif position == OCCUPIED and amount_of_adjacent_occupied_seats >= 4:
                next_grid[y] += EMPTY
                CHANGED = True
            else:
                next_grid[y] += position

    return next_grid

def print_grid(grid):
    for row in grid:
        print(row)

def get_amount_of_occupied_seats_in_grid(grid):
    amount = 0

    for row in grid:
        for position in row:
            if position == OCCUPIED:
                amount += 1
    
    return amount


with open('day11/input.txt', 'r') as file:
    grid = file.read().splitlines()

round = 1

while CHANGED == True:
    print("Round " + str(round))
    round += 1
    grid = get_next_grid(grid)

    print_grid(grid)
    print(str(get_amount_of_occupied_seats_in_grid(grid)) + " seats are occupied.")
    print("-------------------------")
