with open('day6/input.txt', 'r') as file:
    groups = file.read().split('\n\n')
    total = 0

    for group in groups:
        answers_per_person = group.split('\n')
        yes_by_question = {}

        for answers in answers_per_person:
            for answer in answers:
                if yes_by_question.get(answer) == None:
                    yes_by_question[answer] = 1
                else:
                    yes_by_question[answer] += 1

        for test in yes_by_question:
            if yes_by_question.get(test) == len(answers_per_person):
                total += 1

    print("The answer is: " + str(total))