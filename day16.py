import re
from z3 import *


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split("\n\n")

    return content


def process_ranges(input_range: list) -> list:
    output_range = []
    for line in input_range:
        b, e = line.split('-')
        b, e = int(b), int(e)
        output_range.append((b, e))
    return output_range


def process_tickets(input_tickets: list) -> list:
    output_tickets = []
    for line in input_tickets:
        tickets = line.split(",")
        tickets = [int(t) for t in tickets]
        output_tickets += tickets
    return output_tickets


def process_tickets_two(input_tickets: list) -> list:
    output_tickets = []
    for line in input_tickets:
        tickets = line.split(",")
        tickets = [int(t) for t in tickets]
        output_tickets.append(tickets)
    return output_tickets


def is_ticket_in_range(range: tuple, ticket: int) -> bool:
    b, e = range
    if b <= ticket <= e:
        return True

    return False


def check_valid_tickets(valid_ranges: list, nearby_tickets: list) -> list:
    invalid_tickets = []
    for ticket in nearby_tickets:
        valid = False
        for b, e in valid_ranges:
            if b <= ticket <= e:
                valid = True
                break
        if not valid:
            invalid_tickets.append(ticket)

    return invalid_tickets


def check_positions_two(valid_ranges: list, nearby_tickets: list) -> list:
    no_tickets = len(nearby_tickets)
    no_ranges = int(len(valid_ranges) / 2)
    nearby_tickets = list(zip(*nearby_tickets))
    matrix = [[True] * no_ranges for _ in range(no_ranges)]
    for i in range(no_ranges):
        for j, position in enumerate(nearby_tickets):
            in_range_pos = []
            for t in position:
                in_range = [is_ticket_in_range(valid_ranges[2 * i], t), is_ticket_in_range(valid_ranges[2 * i + 1], t)]
                in_range_pos.append(any(in_range))
            matrix[i][j] = all(in_range_pos)

    return matrix


def check_valid_tickets_two(valid_ranges: list, nearby_tickets: list) -> list:
    valid_tickets = []
    for ticket in nearby_tickets:
        valid = True
        for t in ticket:
            valid_t = False
            for b, e in valid_ranges:
                if b <= t <= e:
                    valid_t = True
                    break
            if not valid_t:
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    return valid_tickets


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    valid_range = re.findall(r'(\d+\-\d+)', inputs[0])
    valid_range = process_ranges(valid_range)
    nearby_tickets = inputs[2].splitlines()[1:]
    nearby_tickets = process_tickets_two(nearby_tickets)
    valid_tickets = check_valid_tickets_two(valid_range, nearby_tickets)
    matrix = check_positions_two(valid_range, valid_tickets)

    solver = Solver()
    no_of_variables = len(matrix)
    X = [Int('x%s' % i) for i in range(no_of_variables)]
    solver.add([Distinct([X[i] for i in range(no_of_variables)])])

    for i in range(no_of_variables):
        solver.add(Or([X[i] == j for j in range(no_of_variables) if matrix[i][j]]))

    # print(solver)
    solver.check()
    model = solver.model()

    your_tickets = inputs[1].splitlines()[1:]
    your_tickets = your_tickets[0].split(",")
    your_tickets = [int(yt) for yt in your_tickets]

    total_product = 1
    for d in model:
        value2 = model[d].as_long()
        variable = d.name()
        value = int(re.findall(r'\d+', variable)[0])
        if 0 <= int(value) < 6:
            total_product *= your_tickets[value2]

    return total_product


def solver_demo():
    solver = Solver()
    X = [Int('x%s' % i) for i in range(5)]
    solver.add([Distinct([X[i] for i in range(5)])])
    solver.add(Sum([X[i] for i in range(5)]) == 15)
    solver.add([X[i] > 0 for i in range(5)])
    solver.add(Or([X[4] == 1, X[3] == 1]))
    print(solver)
    solver.check()
    model = solver.model()
    print(model)


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    valid_range = re.findall(r'(\d+\-\d+)', inputs[0])
    valid_range = process_ranges(valid_range)
    nearby_tickets = inputs[2].splitlines()[1:]
    nearby_tickets = process_tickets(nearby_tickets)
    invalid_tickets = check_valid_tickets(valid_range, nearby_tickets)
    return sum(invalid_tickets)


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input16.txt')}")
    print(f"Part II: {compute_part_two('test/input/input16.txt')}")
    solver_demo()
