with open('input.txt', 'r') as input_file:
    notes = input_file.read().split('\n\n')

    rules = notes[0].splitlines()
    my_ticket = notes[1].splitlines()[1]
    nearby_tickets = notes[2].splitlines()[1:]

    invalid_numbers = []

    for ticket in nearby_tickets:
        numbers = map(int, ticket.split(','))
        valid_numbers = []

        for number in numbers:
            is_number_valid = False

            for rule in rules:
                rule_parts = rule.split(': ')
                rule_name = rule_parts[0]
                rule_ranges = rule_parts[1].split(' or ')

                for rule_range in rule_ranges:
                    min_value, max_value = map(int, rule_range.split('-'))

                    if min_value <= number <= max_value:
                        is_number_valid = True

            if not is_number_valid:
                invalid_numbers.append(number)

    print(sum(invalid_numbers))
