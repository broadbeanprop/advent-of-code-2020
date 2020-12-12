from Direction import Direction
from Ship import Ship
from Action import Action


with open('day12/input.txt', 'r') as file:
    instructions = file.read().splitlines()
    ship = Ship()

    for instruction in instructions:
        action = Action(instruction[0])
        number = int(instruction[1:])

        ship.action(action, number)

    print(abs(ship.current_coordinates[Direction.North]) + abs(ship.current_coordinates[Direction.East]))