from Passport import Passport

def find_answer(input):
    valid_passports = 0
    passports = parse_passports(input)
    
    for passport in passports:
        if passport.is_valid():
            valid_passports += 1
    
    return valid_passports
        
    
def parse_passports(input):
    passports = []
    passport_line = ""

    for line in input:

        if line == "":
            passports.append(Passport(passport_line))
            passport_line = ""
        else:
            passport_line += " " + line

    passports.append(Passport(passport_line))

    return passports
