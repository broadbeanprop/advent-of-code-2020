with open('day6/input.txt', 'r') as file:
    groups = file.read().split('\n\n')
    amount_of_distinct_answers = 0
    distinct_answers = set()

    for group in groups:
        person_answers = group.split('\n')
        
        for answers in person_answers:
            for answer in answers:
                distinct_answers.add(answer)
        
        amount_of_distinct_answers += len(distinct_answers)
        distinct_answers = set()
    
    print("The answer is: " + str(amount_of_distinct_answers))
