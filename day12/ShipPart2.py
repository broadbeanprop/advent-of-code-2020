import copy
from Direction import Direction
from Action import Action

class ShipPart2:

    def __init__(self, start_waypoint = { Direction.North : 1, Direction.East : 10 }):
        self.current_coordinates = { Direction.North : 0, Direction.East : 0 }
        self.current_waypoint = start_waypoint

    def action(self, action, number):
        if action == Action.MoveNorth:
            self.current_waypoint[Direction.North] += number

        elif action == Action.MoveEast:
            self.current_waypoint[Direction.East] += number

        elif action == Action.MoveSouth:
            self.current_waypoint[Direction.North] -= number

        elif action == Action.MoveWest:
            self.current_waypoint[Direction.East] -= number

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
        for i in range(number):
            self.current_coordinates[Direction.North] += self.current_waypoint[Direction.North]
            self.current_coordinates[Direction.East] += self.current_waypoint[Direction.East]

    def __turn_left(self):
        waypoint = copy.copy(self.current_waypoint)
        self.current_waypoint[Direction.East] = -waypoint[Direction.North]
        self.current_waypoint[Direction.North] = waypoint[Direction.East]

    def __turn_right(self):
        waypoint = copy.copy(self.current_waypoint)
        self.current_waypoint[Direction.East] = waypoint[Direction.North]
        self.current_waypoint[Direction.North] = -waypoint[Direction.East]

    def __turn_around(self):
        waypoint = copy.copy(self.current_waypoint)
        self.current_waypoint[Direction.North] = -waypoint[Direction.North]
        self.current_waypoint[Direction.East] = -waypoint[Direction.East]