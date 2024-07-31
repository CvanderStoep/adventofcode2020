import copy

directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    content = [list(c) for c in content]
    return content


def grid_size(grid) -> (int, int):
    rows = len(grid)
    cols = len(grid[0])

    return rows, cols


def check_empty(grid, x, y) -> bool:
    rows, cols = grid_size(grid)
    for dx, dy in directions:
        x1 = x + dx
        y1 = y + dy
        if x1 < 0 or x1 >= cols or y1 < 0 or y1 >= rows:
            continue
        if grid[y1][x1] == "#":
            return False
    return True


def check_empty_long(grid, x, y) -> bool:
    rows, cols = grid_size(grid)
    for dx, dy in directions:
        for i in range(1, cols):
            x1 = x + i * dx
            y1 = y + i * dy
            if x1 < 0 or x1 >= cols or y1 < 0 or y1 >= rows:
                break
            elif grid[y1][x1] == "#":
                return False
            elif grid[y1][x1] == "L":
                break
    return True


def check_occupied(grid, x, y) -> bool:
    rows, cols = grid_size(grid)
    number_occupied_seats = 0
    for dx, dy in directions:
        x1 = x + dx
        y1 = y + dy
        if x1 < 0 or x1 >= cols or y1 < 0 or y1 >= rows:
            continue
        if grid[y1][x1] == "#":
            number_occupied_seats += 1
    if number_occupied_seats >= 4:
        return True
    return False


def check_occupied_long(grid, x, y) -> bool:
    rows, cols = grid_size(grid)
    number_occupied_seats = 0
    for dx, dy in directions:
        for i in range(1, cols):
            x1 = x + i * dx
            y1 = y + i * dy
            if x1 < 0 or x1 >= cols or y1 < 0 or y1 >= rows:
                break
            elif grid[y1][x1] == "#":
                number_occupied_seats += 1
                break
            elif grid[y1][x1] == "L":
                break
    if number_occupied_seats >= 5:
        return True
    return False


def check_for_equality(grid1, grid2) -> bool:
    return grid1 == grid2


def count_occupied_seats(grid) -> int:
    count = 0
    for line in grid:
        count += line.count("#")
    return count


def compute_part_one(file_name: str) -> int:
    grid = read_input_file(file_name)
    rows, cols = grid_size(grid)

    rounds = 0
    while True:
        rounds += 1
        new_grid = copy.deepcopy(grid)
        for y in range(0, rows):
            for x in range(0, cols):
                match grid[y][x]:
                    case "L":
                        if check_empty(grid, x, y):
                            new_grid[y][x] = "#"
                    case "#":
                        if check_occupied(grid, x, y):
                            new_grid[y][x] = "L"
                    case ".":
                        pass
        if grid == new_grid:
            print(f'{rounds= }')
            occupied_seats = count_occupied_seats(grid)
            print(f'{occupied_seats= }')
            break
        grid = copy.deepcopy(new_grid)

    return occupied_seats


def compute_part_two(file_name: str) -> int:
    grid = read_input_file(file_name)
    rows, cols = grid_size(grid)

    rounds = 0
    while True:
        rounds += 1
        new_grid = copy.deepcopy(grid)
        for y in range(0, rows):
            for x in range(0, cols):
                match grid[y][x]:
                    case "L":
                        if check_empty_long(grid, x, y):
                            new_grid[y][x] = "#"
                    case "#":
                        if check_occupied_long(grid, x, y):
                            new_grid[y][x] = "L"
                    case ".":
                        pass
        if grid == new_grid:
            print(f'{rounds= }')
            occupied_seats = count_occupied_seats(grid)
            print(f'{occupied_seats= }')
            break
        grid = copy.deepcopy(new_grid)
    return occupied_seats


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input11.txt')}")
    print(f"Part II: {compute_part_two('input/input11.txt')}")
