def find_answer(input):
    amount_of_correct_passwords = 0

    for item in input:
        parts = item.split(' ')
        indexes = parts[0].split('-')
        min_amount = int(indexes[0])
        max_amount = int(indexes[1])
        character = parts[1][0]
        password = parts[2]

        selected_characters_in_password = password.count(character)

        if selected_characters_in_password >= min_amount and selected_characters_in_password <= max_amount:
            amount_of_correct_passwords += 1

    return amount_of_correct_passwords
