import itertools


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def transform_cubes_to_set(grid: list) -> set:
    cube_set = set()
    for i, line in enumerate(grid):
        for j, letter in enumerate(line):
            if letter == '#':
                cube_set.add((i, j, 0))
    return cube_set


def find_min_max(cubes: set) -> (int, int, int, int, int, int):
    x_min, x_max = min(cubes, key=lambda item: item[0])[0], max(cubes, key=lambda item: item[0])[0]
    y_min, y_max = min(cubes, key=lambda item: item[1])[1], max(cubes, key=lambda item: item[1])[1]
    z_min, z_max = min(cubes, key=lambda item: item[2])[2], max(cubes, key=lambda item: item[2])[2]
    return x_min, x_max, y_min, y_max, z_min, z_max


def apply_rules_to_cube(cubes: set) -> set:
    new_cubes = set()
    x_min, x_max, y_min, y_max, z_min, z_max = find_min_max(cubes)
    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1, y_max + 2):
            for z in range(z_min - 1, z_max + 2):
                if (x, y, z) in cubes:
                    number_of_neighbours = 0
                    for dx, dy, dz in neighbours():
                        if (x + dx, y + dy, z + dz) in cubes:
                            number_of_neighbours += 1
                    if 2 <= number_of_neighbours <= 3:
                        new_cubes.add((x, y, z))
                else:
                    number_of_neighbours = 0
                    for dx, dy, dz in neighbours():
                        if (x + dx, y + dy, z + dz) in cubes:
                            number_of_neighbours += 1
                    if number_of_neighbours == 3:
                        new_cubes.add((x, y, z))

    return new_cubes


def neighbours() -> list:
    digits = [-1, 0, 1]
    combinations = list(itertools.product(digits, repeat=3))
    combinations.remove((0, 0, 0))
    return combinations


def compute_part_one(file_name: str) -> int:
    cubes = read_input_file(file_name)
    cubes = transform_cubes_to_set(cubes)
    for _ in range(6):
        cubes = apply_rules_to_cube(cubes)
    return len(cubes)


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)

    return 0


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input17.txt')}")
    print(f"Part II: {compute_part_two('test/input/input17.txt')}")
