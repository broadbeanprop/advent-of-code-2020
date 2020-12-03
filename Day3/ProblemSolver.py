class ProblemSolver:

    def __init__(self, input):
        self.data = input
        self.current_coordinates = [0, 0]

    def find_answer(self, slope_right, slope_down):
        global current_coordinates
        current_coordinates = [0, 0]
        amount_of_trees = 0

        while current_coordinates[0] < len(self.data):
            if self.get_at_coordinates() == "#":
                amount_of_trees +=1

            self.slope(slope_right, slope_down)

        return amount_of_trees

    def slope(self, slope_right, slope_down):
        current_coordinates[0] += slope_down
        width = len(str(self.data[0]))

        possible_steps = (current_coordinates[1] + slope_right) - (width - 1)

        if possible_steps < 1:
            current_coordinates[1] += slope_right
        else:
            current_coordinates[1] = possible_steps - 1

    def get_at_coordinates(self):
        return self.data[current_coordinates[0]][current_coordinates[1]]
