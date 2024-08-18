import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def get_next_coordinate(direction: str, x: int, y: int) -> (int, int):
    match direction:
        case 'e':
            x += 2
        case 'w':
            x -= 2
        case 'ne':
            x += 1
            y += 1
        case 'nw':
            x -= 1
            y += 1
        case 'se':
            x += 1
            y -= 1
        case 'sw':
            x -= 1
            y -= 1
    return x, y


def get_list_of_directions(inputs: str) -> list:
    directions = []
    while inputs:
        if inputs[:2] in ['ne', 'nw', 'se', 'sw']:
            directions.append(inputs[:2])
            inputs = inputs[2:]
        else:
            directions.append(inputs[:1])
            inputs = inputs[1:]

    return directions


def get_min_max(tiles) -> (int, int, int, int):
    x_min, x_max, y_min, y_max = 0, 0, 0, 0
    if tiles:
        x_min = min(tiles.keys(), key=lambda item: item[0])[0] - 2
        x_max = max(tiles.keys(), key=lambda item: item[0])[0] + 2
        y_min = min(tiles.keys(), key=lambda item: item[1])[1] - 2  # to make sure we cover the edges
        y_max = max(tiles.keys(), key=lambda item: item[1])[1] + 2

    return x_min, x_max, y_min, y_max


def flip_flop(tiles: dict) -> dict:
    neighbours = [(2, 0), (-2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    # x_min, x_max, y_min, y_max = get_min_max(tiles)
    new_tiles = dict()
    search_area = set()  # search area consists of current black tiles + neighbours
    for key in tiles.keys():
        search_area.add(key)
        for dx, dy in neighbours:
            x, y = key
            search_area.add((x + dx, y + dy))
    # range (x,y):  y is even, x = -2, 0, 2, 4, etc
    #               y is odd,  x = -1, 1, 3, 5, etc
    # for y in range(y_min, y_max):
    #     if y % 2 == 0:
    #         x_min_mod, x_max_mod = x_min // 2 * 2, x_max // 2 * 2 + 2
    #     else:
    #         x_min_mod, x_max_mod = x_min // 2 * 2 - 1, x_max // 2 * 2 + 1
    #     for x in range(x_min_mod, x_max_mod, 2):
    for x, y in search_area:
        color = tiles.get((x, y), 0)
        no_black_neighbours_tiles = 0
        for dx, dy in neighbours:
            if tiles.get((x + dx, y + dy), 0) == 1:
                no_black_neighbours_tiles += 1

        if color == 1:
            if no_black_neighbours_tiles == 0 or no_black_neighbours_tiles > 2:
                new_tiles.update({(x, y): 0})
            else:
                new_tiles.update({(x, y): 1})

        else:
            if no_black_neighbours_tiles == 2:
                new_tiles.update({(x, y): 1})
            else:
                new_tiles.update({(x, y): 0})

    # remove the white tiles, you don't need them
    tiles = dict()
    for key in new_tiles.keys():
        if new_tiles.get(key) == 1:
            tiles.update({key: 1})

    return tiles


def change_tiles(inputs: list) -> dict:
    tiles = dict()
    # tiles.update({(0, 0): 0})  # starting locations, color == 0 == white; 1 == black
    for l in inputs:
        directions = get_list_of_directions(l)
        x, y = 0, 0
        for direction in directions:
            x, y = get_next_coordinate(direction, x, y)
        color = tiles.get((x, y), 0)
        tiles.update({(x, y): 1 - color})

    return tiles


def compute_part_one(file_name: str) -> int:
    directions = read_input_file(file_name)
    tiles = change_tiles(directions)
    return sum(tiles.values())


def compute_part_two(file_name: str) -> int:
    directions = read_input_file(file_name)
    tiles = change_tiles(directions)
    for _ in range(100):
        tiles = flip_flop(tiles)

    return sum(tiles.values())


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input24.txt')}")
    print(f"Part II: {compute_part_two('test/input/input24.txt')}")
