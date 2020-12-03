def find_answer(input):
    input_range = range(len(input))

    for i in input_range:
        for j in input_range:
            if i != j and int(input[i]) + int(input[j]) == 2020:
                return int(input[i]) * int(input[j])
