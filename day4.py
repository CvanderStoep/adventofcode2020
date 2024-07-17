import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split("\n\n")

    return content


def check_passport(passport: list) -> bool:
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # optional field: "cid"
    for required_field in required_fields:
        if required_field not in passport:
            return False

    return True


def check_passport_details(passport: list) -> bool:
    passport = passport.splitlines()
    passport_dict = dict()
    for line in passport:
        items = line.split()
        for field in items:
            f1, f2 = field.split(":")
            passport_dict.update({f1: f2})
    for key in passport_dict.keys():
        value = passport_dict[key]
        match key:
            case "byr":
                value = int(value)
                if not (1920 <= value <= 2002):
                    return False
            case "iyr":
                value = int(value)
                if not (2010 <= value <= 2020):
                    return False
            case "eyr":
                value = int(value)
                if not (2020 <= value <= 2030):
                    return False
            case "hgt":
                pattern = "\d+"
                value = int(re.findall(pattern, value)[0])
                if "cm" in passport_dict[key]:
                    if not (150 <= value <= 193):
                        return False
                else:
                    if not (59 <= value <= 76):
                        return False
            case "hcl":
                if value[0] != "#":
                    return False
                pattern = "[0-9a-f]+"
                hair_color = re.findall(pattern, value)[0]
                if len(hair_color) != 6:
                    return False
            case "ecl":
                if value not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                    return False
            case "pid":
                if len(value) != 9:
                    return False
            case "cid":
                pass  # optional key
            case _:
                print('unknown key value!', key)

    return True


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)

    number_valid_passports = 0
    for passport in inputs:
        if check_passport(passport):
            number_valid_passports += 1
    print(f'{number_valid_passports= }')

    return number_valid_passports


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    number_valid_passports = 0
    for passport in inputs:
        if check_passport(passport) and check_passport_details(passport):
            number_valid_passports += 1
    print(f'{number_valid_passports= }')

    return number_valid_passports

    return 0


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input4.txt')}")
    print(f"Part II: {compute_part_two('input/input4.txt')}")
