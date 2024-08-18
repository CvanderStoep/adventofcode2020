def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    card_public_key = int(inputs[0])
    door_public_key = int(inputs[1])
    division_value = 20201227
    card_subject_number = 7
    door_subject_number = 7

    card_value = 1
    door_value = 1
    card_loop_size = 0
    while card_value != card_public_key:
        card_loop_size += 1
        card_value = card_value * card_subject_number
        card_value = card_value % division_value
    print(f'{card_loop_size= }, {card_value= }')

    door_loop_size = 0
    while door_value != door_public_key:
        door_loop_size += 1
        door_value = door_value * door_subject_number
        door_value = door_value % division_value
    print(f'{door_loop_size= }, {door_value= }')

    card_value = 1
    for i in range(door_loop_size):
        card_value *= card_public_key
        card_value = card_value % division_value
    print(f'{i= }, {card_value= }')

    return card_value


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    return 0


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input25.txt')}")
    print(f"Part II: {compute_part_two('test/input/input25.txt')}")
