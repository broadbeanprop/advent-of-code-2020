with open('day10/input.txt', 'r') as file:
    numbers = [int(i) for i in file.read().splitlines()]
    numbers.sort()

    numbers.insert(0, 0)
    numbers.append(max(numbers) + 3)

    DP = {}

    def dp(i):
        if i == len(numbers) - 1:
            return 1

        if i in DP:
            return DP[i]
        
        answer = 0
        
        for j in range(i + 1, len(numbers)):
            if numbers[j] - numbers[i] <= 3:
                answer += dp(j)
        
        DP[i] = answer
        return answer

    print("The answer is: " + str(dp(0)))