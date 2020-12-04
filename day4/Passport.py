import re

class Passport:
    
    def __init__(self, input):
        dictionary = self.__to_dictionary(input.split(" "))
        
        self.birth_year      = dictionary.get("byr")
        self.issue_year      = dictionary.get("iyr")
        self.expiration_year = dictionary.get("eyr")
        self.height          = dictionary.get("hgt")
        self.hair_color      = dictionary.get("hcl")
        self.eye_color       = dictionary.get("ecl")
        self.passport_id     = dictionary.get("pid")
        self.country_id      = dictionary.get("cid")

    def is_missing_required_fields(self):
        if (self.birth_year      != None and
            self.issue_year      != None and
            self.expiration_year != None and
            self.height          != None and
            self.hair_color      != None and
            self.eye_color       != None and
            self.passport_id     != None):
            return False
        else:
            return True

    def is_valid(self):
        return (not self.is_missing_required_fields() and
                self.__birth_year_is_valid() and
                self.__issue_year_is_valid() and
                self.__expiration_year_is_valid() and
                self.__height_is_valid() and
                self.__hair_color_is_valid() and
                self.__eye_color_is_valid() and
                self.__passport_id_is_valid())

    def __birth_year_is_valid(self):
        if (int(self.birth_year) < 1920 or
            int(self.birth_year) > 2002):
           return False
        else:
            return True

    def __issue_year_is_valid(self):
        if (int(self.issue_year) < 2010 or
            int(self.issue_year) > 2020):
           return False
        else:
            return True

    def __expiration_year_is_valid(self):
        if (int(self.expiration_year) < 2020 or
            int(self.expiration_year) > 2030):
           return False
        else:
            return True
    
    def __height_is_valid(self):
        height_as_string = str(self.height)
        
        if height_as_string.endswith("cm"):
            height_in_cm = int(height_as_string[0:-2])
            
            if (height_in_cm < 150 or
                height_in_cm > 193):
                return False
            else:
                return True

        elif height_as_string.endswith("in"):
            height_in_in = int(height_as_string[0:-2])
            
            if (height_in_in < 59 or
                height_in_in > 76):
                return False
            else:
                return True

        else:
            return False

    def __hair_color_is_valid(self):
        return re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.hair_color)

    def __eye_color_is_valid(self):
        possibilities = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.eye_color in possibilities

    def __passport_id_is_valid(self):
        return (len(self.passport_id) == 9 and
                self.__is_number(self.passport_id))
        
    def __is_number(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def __to_dictionary(self, input):
        dictionary = {}

        for item in input:
            if item == '':
                continue

            prop = item.split(":")
            dictionary[prop[0]] = prop[1]
        
        return dictionary
