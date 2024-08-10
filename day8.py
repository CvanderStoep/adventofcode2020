from dataclasses import dataclass
from enum import Enum


def read_input_file(file_name: str) -> list[str]:
    with open(file_name) as f:
        return f.read().splitlines()


class Operator(Enum):
    NOP = "nop"
    ACC = "acc"
    JMP = "jmp"


@dataclass
class Instruction:
    operator: Operator
    operand: int
    visited: bool


def parse_instruction(instruction: str) -> Instruction:
    operator, argument = instruction.split()
    return Instruction(Operator(operator), int(argument), False)


def parse_input(inputs: list[str]) -> list[Instruction]:
    return list(map(parse_instruction, inputs))


def process_instruction(instructions: list, position: int, accumulator: int) -> (int, bool):
    while not instructions[position].visited:
        instruction = instructions[position]
        instruction.visited = True
        operator = instruction.operator
        argument = instruction.operand

        match operator:
            case Operator.NOP:
                position += 1
            case Operator.ACC:
                position += 1
                accumulator += argument
            case Operator.JMP:
                position += argument
        if position >= len(instructions):
            return accumulator, True

    return accumulator, False


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    instructions = parse_input(inputs)
    position, accumulator = 0, 0
    accumulator, _ = process_instruction(instructions, position, accumulator)
    return accumulator


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    instructions = parse_input(inputs)
    error_fixed = False
    accumulator = 0
    for i in range(len(instructions)):
        position, accumulator = 0, 0
        for instruction in instructions:
            instruction.visited = False
        match instructions[i].operator:
            case Operator.JMP:
                instructions[i].operator = Operator.NOP
                accumulator, error_fixed = process_instruction(instructions, position, accumulator)
                instructions[i].operator = Operator.JMP
            case Operator.NOP:
                instructions[i].operator = Operator.JMP
                accumulator, error_fixed = process_instruction(instructions, position, accumulator)
                instructions[i].operator = Operator.NOP
            case _:
                pass
        if error_fixed:
            return accumulator
    return accumulator


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input8.txt')}")
    print(f"Part II: {compute_part_two('test/input/input8.txt')}")
