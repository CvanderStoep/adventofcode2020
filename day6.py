import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split("\n\n")

    return content


def count_answers(answers: list) -> int:
    pattern = "[a-z]"
    answer_set = set()
    for answer in answers:
        letters = re.findall(pattern, answer)
        answer_set.update(letters)

    return len(answer_set)


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    sum_of_unique_answers = 0
    for line in inputs:
        line = line.splitlines()
        sum_of_unique_answers += count_answers(line)

    print(f'{sum_of_unique_answers= }')
    return sum_of_unique_answers


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    return 0


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input6.txt')}")
    print(f"Part II: {compute_part_two('input/input6.txt')}")
