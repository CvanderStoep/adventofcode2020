import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
        numbers = re.findall(r'\d', content[0])
        numbers = [int(n) for n in numbers]

    return numbers


def rotation(numbers: list, n: int) -> list:
    numbers = numbers[n:] + numbers[:n]
    return numbers


def compute_part_one(file_name: str) -> str:
    numbers = read_input_file(file_name)

    for i in range(1, 101):
        current_cup_location = 0
        current_cup_number = numbers[current_cup_location]
        pick_up = numbers[current_cup_location + 1: current_cup_location + 4]
        numbers = [current_cup_number] + numbers[current_cup_location + 4:]
        destination = current_cup_number - 1
        if destination < 1:
            destination = 9
        while destination in pick_up:
            destination -= 1
            if destination < 1:
                destination = 9
        destination_cup_location = numbers.index(destination)
        numbers = numbers[current_cup_location:destination_cup_location + 1] + pick_up + numbers[
                                                                                         destination_cup_location + 1:]
        current_cup_location = numbers.index(current_cup_number)
        next_cup_number = numbers[current_cup_location + 1]
        next_cup_location = numbers.index(next_cup_number)
        numbers = rotation(numbers, next_cup_location)

    numbers = rotation(numbers, numbers.index(1))
    number_string = ""
    for i in numbers[1:]:
        number_string += str(i)

    print(f'{number_string= }')

    return number_string


def compute_part_two(file_name: str) -> str:
    numbers = read_input_file(file_name)
    extra = [i for i in range(10, 1_000_001)]
    numbers = numbers + extra
    print(numbers[-10:])

    for i in range(1, 101):
        current_cup_location = 0
        current_cup_number = numbers[current_cup_location]
        pick_up = numbers[current_cup_location + 1: current_cup_location + 4]
        numbers = [current_cup_number] + numbers[current_cup_location + 4:]
        destination = current_cup_number - 1
        if destination < 1:
            destination = 1_000_000
        while destination in pick_up:
            destination -= 1
            if destination < 1:
                destination = 1_000_000
        destination_cup_location = numbers.index(destination)
        numbers = numbers[current_cup_location:destination_cup_location + 1] + pick_up + numbers[
                                                                                         destination_cup_location + 1:]
        current_cup_location = numbers.index(current_cup_number)
        next_cup_number = numbers[current_cup_location + 1]
        next_cup_location = numbers.index(next_cup_number)
        numbers = rotation(numbers, next_cup_location)

    numbers = rotation(numbers, numbers.index(1))
    number_string = ""
    for i in numbers[1:]:
        number_string += str(i)

    print(f'{number_string= }')

    return number_string


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input23.txt')}")
    # print(f"Part II: {compute_part_two('test/input/input23.txt')}")
