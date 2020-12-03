import part1

def find_answer():
    total_trees  = part1.find_answer(1, 1)
    total_trees *= part1.find_answer(3, 1)
    total_trees *= part1.find_answer(5, 1)
    total_trees *= part1.find_answer(7, 1)
    total_trees *= part1.find_answer(1, 2)
    return total_trees
