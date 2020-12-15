import collections

input = [14,1,17,0,3,20]

numbers_spoken = collections.defaultdict(int)
current_round = 1

def get_current_number():
    if current_round <= len(input):
        numbers_spoken[current_round] = input[current_round - 1]
    else:
        previous_number = numbers_spoken[current_round - 1]
        indexes = []

        for value in numbers_spoken:
            if numbers_spoken[value] == previous_number:
                indexes.append(value)

        if len(indexes) <= 1:
            numbers_spoken[current_round] = 0
        else:
            numbers_spoken[current_round] = indexes[-1] - indexes[-2]


target_number = 2020
while current_round <= target_number:
    get_current_number()
    current_round += 1

print(numbers_spoken[target_number])