import itertools

PREAMBLE = 25


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    content = [int(c) for c in content]

    return content


def check_sum(numbers: list, target_sum: int) -> bool:
    for a, b in itertools.combinations(numbers, 2):
        if a + b == target_sum:
            return True

    return False


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    for i in range(len(inputs) - PREAMBLE):
        sub_input_set = inputs[i: i + PREAMBLE]
        target_sum = inputs[i + PREAMBLE]
        valid_sum = check_sum(sub_input_set, target_sum)
        if not valid_sum:
            return target_sum
    return 0


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    target_sum = compute_part_one('test/input/input9.txt')

    for position in range(len(inputs)):
        for length in range(2, len(inputs)):
            sub_sum = sum(inputs[position:position+length])
            if sub_sum == target_sum:
                encryption_weakness = min(inputs[position:position+length]) + max(inputs[position:position+length])
                return encryption_weakness
    return 0


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input9.txt')}")
    print(f"Part II: {compute_part_two('test/input/input9.txt')}")
