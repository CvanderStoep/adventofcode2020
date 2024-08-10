def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def grid_size(grid) -> (int, int):
    rows = len(grid)
    cols = len(grid[0])

    return rows, cols


def compute_part_one(file_name: str) -> int:
    grid = read_input_file(file_name)
    rows, cols = grid_size(grid)

    slope = (3, 1)
    step_i, step_j = slope
    number_of_trees = 0
    for j in range(0, rows, step_j):
        i = int(step_i / step_j * j)
        if grid[j][i % cols] == "#":
            number_of_trees += 1

    return number_of_trees


def compute_part_two(file_name: str) -> int:
    grid = read_input_file(file_name)
    rows, cols = grid_size(grid)

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    multiply_number_of_trees = 1
    for slope in slopes:
        step_i, step_j = slope
        number_of_trees = 0
        for j in range(0, rows, step_j):
            i = int(step_i / step_j * j)
            if grid[j][i % cols] == "#":
                number_of_trees += 1
        multiply_number_of_trees *= number_of_trees
        print(number_of_trees)

    return multiply_number_of_trees


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input3.txt')}")
    print(f"Part II: {compute_part_two('test/input/input3.txt')}")
