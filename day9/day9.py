with open('day9/input.txt', 'r') as file:
    numbers = [int(i) for i in file.read().splitlines()]
    preamble_length = 25

    def find_invalid_number():
        for i in range(preamble_length, len(numbers)):
            indexes_to_consider = range(i - preamble_length, i)
            is_valid = False

            for x in indexes_to_consider:
                for y in indexes_to_consider:
                    if x != y and numbers[x] != numbers[y]:
                        if numbers[x] + numbers[y] == numbers[i]:
                            is_valid = True

            if not is_valid:
                return numbers[i]

    def find_contigious_range_with_sum(invalid_number):
        a = 0
        b = 1
        total = 0

        while a != b and total != invalid_number:
            total = sum(numbers[a:b + 1])

            if total > invalid_number:
                a += 1
            else:
                b += 1
            
        contigious_range = []
        for i in range(a, b):
            contigious_range.append(numbers[i])
        
        contigious_range.sort()

        lowest = contigious_range[0]
        highest = contigious_range[len(contigious_range)-1]
        return lowest + highest



    invalid_number = find_invalid_number()
    print("The answer to part 1 is: " + str(invalid_number))
    
    encryption_weakness = find_contigious_range_with_sum(invalid_number)
    print("The answer to part 2 is: " + str(encryption_weakness))