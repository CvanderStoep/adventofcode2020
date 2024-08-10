import re
import string
from functools import reduce

PATTERN = "[a-z]"


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        return f.read().split("\n\n")


def compute_answers(group_answers: list[str], answer_operator, initial_answer_set) -> int:
    group_answers_sets = list(map(lambda person_answers: set(re.findall(PATTERN, person_answers)), group_answers))
    answer_set = reduce(answer_operator, group_answers_sets, initial_answer_set)
    return len(answer_set)


def compute_part(file_name, answer_operator, initial_answer_set) -> int:
    inputs = read_input_file(file_name)
    group_count = map(lambda group_answers: compute_answers(group_answers.splitlines(), answer_operator, initial_answer_set), inputs)
    return sum(group_count)


if __name__ == '__main__':
    print(f"Part I: {compute_part('test/input/input6.txt', lambda xs, ys: xs.union(ys), set())}")
    print(f"Part II: {compute_part('test/input/input6.txt', lambda xs, ys: xs.intersection(ys), set(string.ascii_lowercase))}")
