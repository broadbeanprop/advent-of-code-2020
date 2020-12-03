def find_answer(input):
    input_range = range(len(input))

    for i in input_range:
        for j in input_range:
            for k in input_range:
                if i != j != k and int(input[i]) + int(input[j]) + int(input[k]) == 2020:
                    return int(input[i]) * int(input[j]) * int(input[k])
