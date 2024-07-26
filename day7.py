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


def process_rule2(rule: str, bags_dict: dict) -> dict:
    color, contain = rule.split("contain ")
    color1, color2, _ = color.split()
    color = color1 + color2
    bag_list = []
    bags_dict.update({color: bag_list})
    content = contain.split(", ")
    for bags in content:
        if "no " not in bags:
            n, color1, color2, _ = bags.split()
            color = color1 + color2
            bag_list.append((n, color))

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


def calculate_total_number_of_bags(starting_color: str, bag_dict: dict) -> int:

    bags = bag_dict[starting_color]
    if not bags:
        return 1
    else:
        total = 0
        for bag in bags:
            n, color = bag
            n = int(n)
            total += n * calculate_total_number_of_bags(color, bag_dict)
        return total + 1


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
    rules = read_input_file(file_name)
    bags_dict = dict()
    for rule in rules:
        bags_dict = process_rule2(rule, bags_dict)
    n = calculate_total_number_of_bags(starting_color="shinygold", bag_dict=bags_dict) - 1
    return n


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input7.txt')}")
    print(f"Part II: {compute_part_two('test/input/input7.txt')}")
