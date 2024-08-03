import math
import re
from dataclasses import dataclass


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


@dataclass
class Ship:
    x: int
    y: int
    heading: str


# x --->
# y
# |
# \/

@dataclass
class Waypoint:
    rx: int
    ry: int


def process_rule_part_one(rule: str, ship: Ship) -> Ship:
    directions = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
    headings_degrees = {0: "N", 90: "E", 180: "S", 270: "W"}
    headings_compass = {"N": 0, "E": 90, "S": 180, "W": 270}
    direction = re.findall(r'[A-Z]', rule)[0]
    moves = int(re.findall(r'\d+', rule)[0])

    match direction:
        case "F":
            ship.x += moves * directions[ship.heading][0]
            ship.y += moves * directions[ship.heading][1]
        case "L":
            current_heading = headings_compass[ship.heading]
            new_heading = current_heading - moves
            new_heading = new_heading % 360
            ship.heading = headings_degrees[new_heading]
        case "R":
            current_heading = headings_compass[ship.heading]
            new_heading = current_heading + moves
            new_heading = new_heading % 360
            ship.heading = headings_degrees[new_heading]
        case _:
            ship.x += moves * directions[direction][0]
            ship.y += moves * directions[direction][1]

    return ship


def process_rule_part_two(rule: str, ship: Ship, waypoint: Waypoint) -> (Ship, Waypoint):
    directions = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
    direction = re.findall(r'[A-Z]', rule)[0]
    moves = int(re.findall(r'\d+', rule)[0])  # linear moves or rotation in degrees

    # TODO modify below rules.
    match direction:
        case "F":
            ship.x += moves * waypoint.rx
            ship.y += moves * waypoint.ry
        case "L":
            moves = math.radians(moves)
            x, y = waypoint.rx, -waypoint.ry  # formula corrected for y pointing downwards
            X = x * math.cos(moves) - y * math.sin(moves)
            Y = x * math.sin(moves) + y * math.cos(moves)
            waypoint.rx, waypoint.ry = round(X), -round(Y)
        case "R":
            moves = -math.radians(moves)
            x, y = waypoint.rx, -waypoint.ry
            X = x * math.cos(moves) - y * math.sin(moves)
            Y = x * math.sin(moves) + y * math.cos(moves)
            waypoint.rx, waypoint.ry = round(X), -round(Y)
        case _:  # N E S W
            waypoint.rx += moves * directions[direction][0]
            waypoint.ry += moves * directions[direction][1]

    return ship, waypoint


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    ship = Ship(0, 0, "E")
    for rule in inputs:
        ship = process_rule_part_one(rule, ship)

    return ship.x + ship.y


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    ship = Ship(0, 0, "E")
    waypoint = Waypoint(10, -1)  # starting point 10 E, 1 N
    for rule in inputs:
        ship, waypoint = process_rule_part_two(rule, ship, waypoint)

    return ship.x + ship.y


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input12.txt')}")
    print(f"Part II: {compute_part_two('input/input12.txt')}")
