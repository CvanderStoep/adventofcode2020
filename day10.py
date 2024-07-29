def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    content = [int(c) for c in content]

    return content


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    inputs.sort()
    number_of_one_diff = 1  # start with charging outlet (0)
    number_of_three_diff = 1  # ends with built-in adapter (3)
    for i in range(len(inputs) - 1):
        if inputs[i + 1] - inputs[i] == 1:
            number_of_one_diff += 1
        if inputs[i + 1] - inputs[i] == 3:
            number_of_three_diff += 1
    return number_of_one_diff * number_of_three_diff


count_cache = {0: 1, 1: 1}


def count_arrangements_cache(inputs, n: int) -> int:
    # building a cache for fast retrieval
    if n < 0:
        return 0
    if n in count_cache:
        return count_cache[n]
    if n not in inputs:
        return 0
    else:
        count = (count_arrangements_cache(inputs, n - 1) +
                 count_arrangements_cache(inputs, n - 2) +
                 count_arrangements_cache(inputs, n - 3))
        count_cache[n] = count
        return count


def count_arrangements(inputs: list, n: int) -> int:
    # this works, but only for small numbers
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n not in inputs:
        return 0
    return count_arrangements(inputs, n - 1) + count_arrangements(inputs, n - 2) + count_arrangements(inputs, n - 3)


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    max_adapter = max(inputs)
    # num = count_arrangements(inputs, max_adapter)
    num = count_arrangements_cache(inputs, max_adapter)

    return num


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input10.txt')}")
    print(f"Part II: {compute_part_two('input/input10.txt')}")
