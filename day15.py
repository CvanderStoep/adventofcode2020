def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    content = content[0].split(",")
    content = [int(c) for c in content]

    return content


def find_pattern(data: list[int]) -> tuple[list[int], list[int]]:
    for p in range(len(data)):
        sd = data[p:]
        for r in range(2, len(sd) // 2 + 1):
            # print(f'{r= }, {sd= }')
            if sd[0:r] == sd[r:2 * r]:
                # print(f'2{sd= }')
                if all([(sd[0:r] == sd[y:y + r]) for y in range(r, len(sd) - r, r)]):
                    return data[:p], data[p:p + r]
    return [], []


def find_occurrences(inputs: list, last_number: int) -> int:
    occurrences = [i for i, x in enumerate(inputs) if x == last_number]
    return occurrences[-1] - occurrences[-2]


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    number_of_rounds = 10
    for i in range(number_of_rounds):
        last_number = inputs[-1]
        if last_number not in inputs[:-1]:
            inputs.append(0)
        else:
            turns_apart = find_occurrences(inputs, last_number)
            inputs.append(turns_apart)

    preamble, repetition = find_pattern(inputs)
    print(f'{preamble= }')
    print(f'{repetition= }')
    print(inputs)

    return inputs[number_of_rounds - 1]


def compute_part_two(file_name: str) -> int:
    # might check 2022-day17 for cycle patterns
    inputs = read_input_file(file_name)
    return 0


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input15.txt')}")
    print(f"Part II: {compute_part_two('test/input/input15.txt')}")
