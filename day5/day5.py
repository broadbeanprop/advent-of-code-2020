def take_first_half(min, max):
    diff = (max + 1) - min
    new_max = max - (diff / 2)
    return (min, new_max)

def take_second_half(min, max):
    diff = (max + 1) - min
    new_min = min + (diff / 2)
    return (new_min, max)

with open('day5/input.txt', 'r') as file:
    input = file.read().splitlines()
    highest_seat_id = 0
    seats = {}

    for ticket in input:
        rows = (0, 127)
        columns = (0, 7)

        for action in ticket:
            if action == "F":
                rows = take_first_half(rows[0], rows[1])

            if action == "B":
                rows = take_second_half(rows[0], rows[1])

            if action == "L":
                columns = take_first_half(columns[0], columns[1])

            if action == "R":
                columns = take_second_half(columns[0], columns[1])

        seat_id = int((rows[0] * 8) + columns[0])

        seats[seat_id] = "X"

        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    print("The highest seat id is: " + str(highest_seat_id))
    
    for i in range(min(seats), max(seats)):
        if seats.get(i) == None:
            print("Your seat id is: " + str(i))