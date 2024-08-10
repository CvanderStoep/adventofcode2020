import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    memory_set = dict()
    for line in inputs:
        if "mask" in line:
            mask = line.split(' = ')[1]
            continue
        memory = int(re.findall(r'\d+', line.split(' = ')[0])[0])
        value = int(line.split(' = ')[1])

        for match in re.finditer(r'\d', mask):
            position_from_end = len(mask) - match.start() - 1
            bit = mask[match.start()]
            match bit:
                case "0":
                    value = clear_bit(value, position_from_end)
                case "1":
                    value = set_bit(value, position_from_end)
        memory_set.update({memory: value})
    return sum(memory_set.values())


def apply_mask_to_memory(mask: str, memory: str) -> list:
    decimal_memory = dec2bin(memory)
    leading_zeros = "0" * (len(mask) - len(decimal_memory))
    decimal_memory = list(leading_zeros + decimal_memory)
    for match in re.finditer(r'X', mask):
        decimal_memory[match.start()] = "X"
    decimal_memory = "".join(decimal_memory)
    memory_list = [decimal_memory]
    memory_output = []
    while memory_list:
        mem = memory_list.pop()
        if "X" not in mem:
            dec_mem = int(mem, 2)
            memory_output.append(dec_mem)
            continue
        index = mem.find('X')
        mem = mem[:index] + "0" + mem[index + 1:]
        memory_list.append(mem)
        mem = mem[:index] + "1" + mem[index + 1:]
        memory_list.append(mem)
    return memory_output


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    memory_set = dict()
    for line in inputs:
        if "mask" in line:
            mask = line.split(' = ')[1]
            continue
        memory = int(re.findall(r'\d+', line.split(' = ')[0])[0])
        value = int(line.split(' = ')[1])

        for match in re.finditer(r'\d', mask):
            position_from_end = len(mask) - match.start() - 1
            bit = mask[match.start()]
            match bit:
                case "0":
                    pass
                case "1":
                    memory = set_bit(memory, position_from_end)
        alist = apply_mask_to_memory(mask, memory)
        for mem in alist:
            memory_set.update({mem: value})
    return sum(memory_set.values())


def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


def dec2bin(number: int):
    ans = ""
    if number == 0:
        return 0
    while number:
        ans += str(number & 1)
        number = number >> 1

    ans = ans[::-1]

    return ans


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('test/input/input14.txt')}")
    print(f"Part II: {compute_part_two('test/input/input14.txt')}")
