def find_answer():
    entries = open('input.txt', 'r').readlines()
    entries_range = range(len(entries))

    for i in entries_range:
        for j in entries_range:
            if i != j and int(entries[i]) + int(entries[j]) == 2020:
                return int(entries[i]) * int(entries[j])
