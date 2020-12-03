from ProblemSolver import ProblemSolver

def find_answer(input):
    total_trees  = ProblemSolver(input).find_answer(1, 1)
    total_trees *= ProblemSolver(input).find_answer(3, 1)
    total_trees *= ProblemSolver(input).find_answer(5, 1)
    total_trees *= ProblemSolver(input).find_answer(7, 1)
    total_trees *= ProblemSolver(input).find_answer(1, 2)
    return total_trees
