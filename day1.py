from itertools import combinations


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    # numbers = []
    # for line in content:
    #     numbers.append(int(line))

    numbers = [int(line) for line in content]

    return numbers


def compute_part_one(file_name: str) -> int:
    numbers = read_input_file(file_name)
    for n1, n2 in combinations(numbers, 2):
        if n1 + n2 == 2020:
            print(n1, n2, n1 * n2)
            return n1 * n2

    return 0


def compute_part_two(file_name: str) -> int:
    numbers = read_input_file(file_name)
    for n1, n2, n3 in combinations(numbers, 3):
        if n1 + n2 + n3 == 2020:
            print(n1, n2, n3, n1 * n2 * n3)
            return n1 * n2 * n3

    return 0


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input1.txt')}")
    print(f"Part II: {compute_part_two('test/input/input1.txt')}")
