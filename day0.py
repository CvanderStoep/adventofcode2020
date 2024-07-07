def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    print(inputs)
    return 0


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    return 0


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input2.txt')}")
    print(f"Part II: {compute_part_two('input/input2.txt')}")
