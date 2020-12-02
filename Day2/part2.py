def find_answer():
    with open('input.txt', 'r') as file:
        amount_of_correct_passwords = 0

        for item in file:
            parts = item.split(' ')
            indexes = parts[0].split('-')
            index1 = int(indexes[0])-1
            index2 = int(indexes[1])-1
            character = parts[1][0]
            password = parts[2]

            character_at_indexes = 0

            if password[index1] == character:
                character_at_indexes += 1

            if password[index2] == character:
                character_at_indexes += 1

            if character_at_indexes == 1:
                amount_of_correct_passwords += 1

        return amount_of_correct_passwords
