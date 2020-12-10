with open('day10/input.txt', 'r') as file:
    numbers = [int(i) for i in file.read().splitlines()]
    numbers.sort()
    jumps = { 1:0, 3:0 }

    numbers.insert(0, 0)
    numbers.append(max(numbers) + 3)

    for i in range(len(numbers)):
        if i == 0:
            continue
        
        diff = numbers[i] - numbers[i-1]
        jumps[diff] += 1

    print("The answer is: " + str(jumps[1] * jumps[3]))