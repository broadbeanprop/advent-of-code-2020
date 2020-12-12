import enum

class Action(enum.Enum):
    MoveNorth = "N"
    MoveEast = "E"
    MoveSouth = "S"
    MoveWest = "W"
    MoveForward = "F"
    TurnLeft = "L"
    TurnRight = "R"