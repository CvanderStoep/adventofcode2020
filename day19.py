import queue
import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split('\n\n')

    return content


def make_rule_dict(lines: str) -> dict:
    """
    input 1: 2 3 | 3 2
    2: "a"

    output {1: [[2,3], [3,2]], 2: 'a'}
    """
    lines = lines.splitlines()
    rules = dict()
    for rule in lines:
        line = rule.split(": ")
        key = int(line[0])
        value = line[1].replace('"', '')
        if value != "a" and value != "b":
            values = []
            value = value.split("|")
            for v in value:
                numbers = re.findall(r'\d+', v)
                numbers = [int(n) for n in numbers]
                values.append(numbers)
            rules.update({key: values})
        else:
            rules.update({key: value})

    print(f'{rules= }')
    return rules


def yield_message(lines):
    solution_queue = queue.Queue()
    rules = make_rule_dict(lines[0])
    start_sequence = rules[0][0]
    valid_message = ""
    solution_queue.put((start_sequence, valid_message))
    # start_sequence = rules[0][1]
    # valid_message = ""
    # solution_queue.put((start_sequence, valid_message))

    # start the queue with: ([4,1,5], "")
    # remove element from queue and check for letters a/b
    #

    valid_message_set = set()
    while not solution_queue.empty():
        solution, message = solution_queue.get()
        number = solution[0]
        solution = solution[1:]
        value = rules[number]
        if isinstance(value, str):
            message += value
            if len(solution) > 0:
                solution_queue.put((solution, message))
            else:
                valid_message_set.add(message)
        else:
            for l in value:
                new_solution = l + solution
                solution_queue.put((new_solution, message))

    return valid_message_set


def compute_part_one(file_name: str) -> int:
    lines = read_input_file(file_name)

    valid_message_set = yield_message(lines)

    messages = lines[1].split()
    no_of_valid_messages = 0
    for message in messages:
        if message in valid_message_set:
            no_of_valid_messages += 1

    return no_of_valid_messages


def compute_part_two(file_name: str) -> int:
    lines = read_input_file(file_name)
    return 0


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input19.txt')}")
    print(f"Part II: {compute_part_two('test/input/input19.txt')}")
