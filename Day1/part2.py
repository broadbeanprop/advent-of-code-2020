def find_answer():
    entries = open('input.txt', 'r').readlines()
    entries_range = range(len(entries))

    for i in entries_range:
        for j in entries_range:
            for k in entries_range:
                if i != j != k and int(entries[i]) + int(entries[j]) + int(entries[k]) == 2020:
                    return int(entries[i]) * int(entries[j]) * int(entries[k])
