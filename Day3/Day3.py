import part1
import part2

with open('day3/input.txt', 'r') as file:
    input = file.read().splitlines()

print("The answer to part 1 is " + str(part1.find_answer(input)))
print("The answer to part 2 is " + str(part2.find_answer(input)))
