import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    password_inputs = []
    for line in content:
        policy, password = line.split(": ")
        password_inputs.append([policy, password])

    return password_inputs


def check_valid_password(policy, password) -> bool:
    pwd_range = re.findall(r'(\d+)', policy)
    min_range, max_range = int(pwd_range[0]), int(pwd_range[1])
    pwd_letter = re.findall(r'[a-z]', policy)[0]
    number_of_occurrences = password.count(pwd_letter)

    if min_range <= number_of_occurrences <= max_range:
        return True

    return False


def check_valid_password_new(policy, password) -> bool:
    pwd_range = re.findall(r'(\d+)', policy)
    first_position, second_position = int(pwd_range[0]), int(pwd_range[1])
    pwd_letter = re.findall(r'[a-z]', policy)[0]

    first_check = password[first_position - 1] == pwd_letter
    second_check = password[second_position - 1] == pwd_letter

    # only one of the checks must be valid -> XOR operation
    valid = first_check != second_check

    return valid


def compute_part_one(file_name: str) -> int:
    password_inputs = read_input_file(file_name)
    number_of_valid_passwords = 0
    for line in password_inputs:
        policy, password = line[0], line[1]
        valid_password = check_valid_password(policy, password)
        if valid_password:
            number_of_valid_passwords += 1
    print(f"{number_of_valid_passwords= }")

    return number_of_valid_passwords


def compute_part_two(file_name: str) -> int:
    password_inputs = read_input_file(file_name)
    number_of_valid_passwords = 0
    for line in password_inputs:
        policy, password = line[0], line[1]
        valid_password = check_valid_password_new(policy, password)
        if valid_password:
            number_of_valid_passwords += 1
    print(f"{number_of_valid_passwords= }")

    return number_of_valid_passwords


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input2.txt')}")
    print(f"Part II: {compute_part_two('test/input/input2.txt')}")
