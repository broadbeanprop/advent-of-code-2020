from Direction import Direction
from Action import Action

class Ship:

    def __init__(self, start_direction = Direction.East):
        self.current_coordinates = { Direction.North : 0, Direction.East : 0 }
        self.current_direction = start_direction

    def action(self, action, number):
        if action == Action.MoveNorth:
            self.current_coordinates[Direction.North] += number

        elif action == Action.MoveEast:
            self.current_coordinates[Direction.East] += number

        elif action == Action.MoveSouth:
            self.current_coordinates[Direction.North] -= number

        elif action == Action.MoveWest:
            self.current_coordinates[Direction.East] -= number

        elif action == Action.MoveForward:
            self.__move_forward(number)

        elif action == Action.TurnLeft:
            if number == 90:
                self.__turn_left()
            elif number == 270:
                self.__turn_right()
            elif number == 180:
                self.__turn_around() 

        elif action == Action.TurnRight:
            if number == 90:
                self.__turn_right()
            if number == 270:
                self.__turn_left()
            elif number == 180:
                self.__turn_around()

    def __move_forward(self, number):
        if self.current_direction == Direction.North or self.current_direction == Direction.East:
            self.current_coordinates[self.current_direction] += number

        elif self.current_direction == Direction.South:
            self.current_coordinates[Direction.North] -= number

        elif self.current_direction == Direction.West:
            self.current_coordinates[Direction.East] -= number

    def __turn_left(self):
        if self.current_direction == Direction.North:
            self.current_direction = Direction.West
        else:
            self.current_direction = Direction(self.current_direction.value - 1)

    def __turn_right(self):
        if self.current_direction == Direction.West:
            self.current_direction = Direction.North
        else:
            self.current_direction = Direction(self.current_direction.value + 1)

    def __turn_around(self):
        if self.current_direction == Direction.North:
            self.current_direction = Direction.South

        elif self.current_direction == Direction.East:
            self.current_direction = Direction.West

        elif self.current_direction == Direction.South:
            self.current_direction = Direction.North

        elif self.current_direction == Direction.West:
            self.current_direction = Direction.East