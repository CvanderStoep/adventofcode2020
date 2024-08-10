import re
import sys
from z3 import *


# pip install z3-solver

def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def find_next_departure_time(earliest: int, bus_id: int) -> int:
    next_time = int(earliest / bus_id + 1) * bus_id

    return next_time


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    earliest = int(inputs[0])
    bus_ids = re.findall(r'\d+', inputs[1])
    bus_ids = [int(i) for i in bus_ids]
    next_time = sys.maxsize
    first_bus = 0

    for bus_id in bus_ids:
        nt = find_next_departure_time(earliest, bus_id)
        if nt < next_time:
            next_time = nt
            first_bus = bus_id

    waiting_time = next_time - earliest
    print(f'{next_time= }, {first_bus= }, {waiting_time= }')

    return first_bus * waiting_time


def compute_part_two(file_name: str) -> int:
    # this works, but way too slow ...
    solver = Solver()
    t = Int('t')
    a = Int('a')
    b = Int('b')
    c = Int('c')

    # solver.add(t % 23 == 0)
    # solver.add((t + 13) % 41 == 0)
    # solver.add((t + 23) % 733 == 0)
    # solver.add((t + 36) % 13 == 0)
    # solver.add((t + 37) % 17 == 0)
    # solver.add((t + 42)%19 == 0)
    # solver.add((t + 52)%29 == 0)
    # solver.add((t + 54)%449 == 0)
    # solver.add((t + 91)%37 == 0)
    # solver.add(t > 0)

    # solver.add(t == 1789 * a)
    # solver.add(t + 1 == 37 * b)
    # solver.add(t + 2 == 47 * c)
    # solver.add(t + 3 == 1889 * d)
    # solver.add(t > 0)
    solver.check()

    m = solver.model()
    print(m)

    "traversing model..."
    for d in m.decls():
        print("%s = %s" % (d.name(), m[d]))
    return 0


def compute_using_wolfram(file_name: str) -> str:
    inputs = read_input_file(file_name)
    ids = inputs[1].split(',')
    print('https://www.wolframalpha.com/input/?i=0+%3D+' + '+%3D+'.join(
        ['((n+%2B+{})+mod+{})'.format(i, n) for i, n in enumerate(ids) if n != 'x']))

    return 'copy-paste above in your browser!'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input13.txt')}")
    print(f"Part I: {compute_part_two('test/input/input13.txt')}")
    print(f"Part II: {compute_using_wolfram('test/input/input13.txt')}")
