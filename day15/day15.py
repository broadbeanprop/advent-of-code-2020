import collections

input = [14,1,17,0,3,20]

numbers_spoken = collections.defaultdict(list)
current_round = 1
previous_number = 0

def get_current_number():
    global previous_number

    if current_round <= len(input):
        previous_number = input[current_round - 1]
        numbers_spoken[previous_number].append(current_round)
    else:
        if len(numbers_spoken[previous_number]) <= 1:
            previous_number = 0
        else:
            previous_number = numbers_spoken[previous_number][-1] - numbers_spoken[previous_number][-2]
        
        numbers_spoken[previous_number].append(current_round)

target_number = 30000000
while current_round <= target_number:
    get_current_number()
    current_round += 1

print(previous_number)