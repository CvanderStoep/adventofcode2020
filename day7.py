import re
import queue


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        return f.read().splitlines()


def process_rule(rule: str, bags_dict: dict) -> dict:
    color, contain = rule.split("contain ")
    color1, color2, _ = color.split()
    color = color1 + color2
    bag_list = []
    bags_dict.update({color: bag_list})
    content = contain.split(", ")
    for bags in content:
        if "no " not in bags:
            _, color1, color2, _ = bags.split()
            color = color1 + color2
            bag_list.append(color)

    return bags_dict


def convert_children_to_parents(bag_dict: dict) -> dict:
    parent_dict = dict()
    for key in bag_dict:
        values = bag_dict[key]
        for value in values:
            bag_list = parent_dict.get(value, [])
            bag_list.append(key)
            parent_dict.update({value: bag_list})
    return parent_dict


def find_all_parents(starting_color: str, parents_dict: dict) -> set:
    parent_set = set()
    parent_queue = queue.Queue()
    parent_queue.put(starting_color)
    while not parent_queue.empty():
        parent = parent_queue.get()
        for parents in parents_dict.get(parent, []):
            parent_queue.put(parents)
            parent_set.update([parents])

    return parent_set


def compute_part_one(file_name: str) -> int:
    rules = read_input_file(file_name)
    bags_dict = dict()
    for rule in rules:
        bags_dict = process_rule(rule, bags_dict)
    parents_dict = convert_children_to_parents(bags_dict)
    parent_set = find_all_parents(starting_color="shinygold", parents_dict=parents_dict)
    print(parent_set)
    return len(parent_set)


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    return 0


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input7.txt')}")
    print(f"Part II: {compute_part_two('input/input7.txt')}")
