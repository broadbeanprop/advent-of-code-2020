from Direction import Direction
from ShipPart1 import ShipPart1
from ShipPart2 import ShipPart2
from Action import Action


with open('day12/input.txt', 'r') as file:
    instructions = file.read().splitlines()
    ship1 = ShipPart1()
    ship2 = ShipPart2()

    for instruction in instructions:
        action = Action(instruction[0])
        number = int(instruction[1:])

        ship1.action(action, number)
        ship2.action(action, number)

    print(abs(ship1.current_coordinates[Direction.North]) + abs(ship1.current_coordinates[Direction.East]))
    print(abs(ship2.current_coordinates[Direction.North]) + abs(ship2.current_coordinates[Direction.East]))