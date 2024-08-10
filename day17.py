import itertools


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def transform_cubes_to_set(grid: list, part: int) -> set:
    cube_set = set()
    for i, line in enumerate(grid):
        for j, letter in enumerate(line):
            if letter == '#':
                if part == 1:
                    cube_set.add((i, j, 0))
                else:
                    cube_set.add((i, j, 0, 0))

    return cube_set


def find_min_max(cubes: set, part: int):
    x_min, x_max = min(cubes, key=lambda item: item[0])[0], max(cubes, key=lambda item: item[0])[0]
    y_min, y_max = min(cubes, key=lambda item: item[1])[1], max(cubes, key=lambda item: item[1])[1]
    z_min, z_max = min(cubes, key=lambda item: item[2])[2], max(cubes, key=lambda item: item[2])[2]
    if part == 2:
        w_min, w_max = min(cubes, key=lambda item: item[3])[3], max(cubes, key=lambda item: item[3])[3]
        return x_min, x_max, y_min, y_max, z_min, z_max, w_min, w_max

    return x_min, x_max, y_min, y_max, z_min, z_max


def apply_rules_to_cube_3d(cubes: set) -> set:
    part = 1
    new_cubes = set()
    x_min, x_max, y_min, y_max, z_min, z_max = find_min_max(cubes, part)
    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1, y_max + 2):
            for z in range(z_min - 1, z_max + 2):
                if (x, y, z) in cubes:
                    number_of_neighbours = 0
                    for dx, dy, dz in neighbours(part):
                        if (x + dx, y + dy, z + dz) in cubes:
                            number_of_neighbours += 1
                    if 2 <= number_of_neighbours <= 3:
                        new_cubes.add((x, y, z))
                else:
                    number_of_neighbours = 0
                    for dx, dy, dz in neighbours(part):
                        if (x + dx, y + dy, z + dz) in cubes:
                            number_of_neighbours += 1
                    if number_of_neighbours == 3:
                        new_cubes.add((x, y, z))

    return new_cubes


def apply_rules_to_cube_4d(cubes: set) -> set:
    part = 2
    new_cubes = set()
    x_min, x_max, y_min, y_max, z_min, z_max, w_min, w_max = find_min_max(cubes, part)
    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1, y_max + 2):
            for z in range(z_min - 1, z_max + 2):
                for w in range(w_min -1, w_max + 2):
                    if (x, y, z, w) in cubes:
                        number_of_neighbours = 0
                        for dx, dy, dz, dw in neighbours(part):
                            if (x + dx, y + dy, z + dz, w + dw) in cubes:
                                number_of_neighbours += 1
                        if 2 <= number_of_neighbours <= 3:
                            new_cubes.add((x, y, z, w))
                    else:
                        number_of_neighbours = 0
                        for dx, dy, dz, dw in neighbours(part):
                            if (x + dx, y + dy, z + dz, w + dw) in cubes:
                                number_of_neighbours += 1
                        if number_of_neighbours == 3:
                            new_cubes.add((x, y, z, w))

    return new_cubes


def neighbours(part: int) -> list:
    if part == 1:
        digits = [-1, 0, 1]
        combinations = list(itertools.product(digits, repeat=3))
        combinations.remove((0, 0, 0))
    else:
        digits = [-1, 0, 1]
        combinations = list(itertools.product(digits, repeat=4))
        combinations.remove((0, 0, 0, 0))

    return combinations


def compute_part_one(file_name: str) -> int:
    part = 1
    cubes = read_input_file(file_name)
    cubes = transform_cubes_to_set(cubes, part)
    for _ in range(6):
        cubes = apply_rules_to_cube_3d(cubes)
    return len(cubes)


def compute_part_two(file_name: str) -> int:
    part = 2
    cubes = read_input_file(file_name)
    cubes = transform_cubes_to_set(cubes, part)
    for _ in range(6):
        cubes = apply_rules_to_cube_4d(cubes)
    return len(cubes)


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input17.txt')}")
    print(f"Part II: {compute_part_two('test/input/input17.txt')}")
