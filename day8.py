from dataclasses import dataclass


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


@dataclass
class Instruction:
    operator: str
    argument: int
    visited: bool


def convert_input(inputs: list) -> list:
    instructions = []
    for instruction in inputs:
        operation, argument = instruction.split()
        argument = int(argument)
        instr = Instruction(operation, argument, False)
        instructions.append(instr)

    return instructions


def process_instruction(instructions: list, position: int, accumulator: int) -> (int, bool):
    # print(instructions)
    error_fixed = False
    while not instructions[position].visited:
        instruction = instructions[position]
        instruction.visited = True
        operator = instruction.operator
        argument = instruction.argument

        match operator:
            case "nop":
                position += 1
            case "acc":
                position += 1
                accumulator += argument
            case "jmp":
                position += argument
        if position >= len(instructions): # part 2, reached the end of instructions, no loop
            print('error is fixed')
            print(f'{accumulator= }')
            error_fixed = True
            return accumulator, error_fixed

    return accumulator, error_fixed


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    instructions = convert_input(inputs)
    position, accumulator = 0, 0
    accumulator, _ = process_instruction(instructions, position, accumulator)
    return accumulator


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    instructions = convert_input(inputs)
    error_fixed = False
    accumulator = 0
    for i in range(len(instructions)):
        position, accumulator = 0, 0
        for instruction in instructions:
            instruction.visited = False
        match instructions[i].operator:
            case "jmp":
                instructions[i].operator = "nop"
                accumulator, error_fixed = process_instruction(instructions, position, accumulator)
                instructions[i].operator = "jmp"
            case "nop":
                instructions[i].operator = "jmp"
                accumulator, error_fixed = process_instruction(instructions, position, accumulator)
                instructions[i].operator = "nop"
            case _:
                pass
        if error_fixed:
            return accumulator
    return accumulator


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input8.txt')}")
    print(f"Part II: {compute_part_two('test/input/input8.txt')}")
