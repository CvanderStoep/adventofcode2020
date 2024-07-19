def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def calculate_range(letter: str, begin: int, end: int) -> (int, int):
    match letter:
        case "F" | "L":
            end = int(begin + (end - begin + 1) / 2 - 1)
        case "B" | "R":
            begin = int(begin + (end - begin + 1) / 2)
            pass
        case _:
            print('invalid letter')
    return begin, end


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    max_seat_id = 0
    for seat in inputs:
        begin, end = 0, 127
        for i in range(7):
            letter = seat[i]
            begin, end = calculate_range(letter, begin, end)
        row = begin
        begin, end = 0, 7
        for i in range(7, 10):
            letter = seat[i]
            begin, end = calculate_range(letter, begin, end)
        column = begin
        seat_id = row * 8 + column
        max_seat_id = max(max_seat_id, seat_id)
        # print(f'{seat= }, {row= }, {column= }, {seat_id= }')
    # print(f'{max_seat_id= }')
    return max_seat_id


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    seats = []
    your_seat = 1
    for seat in inputs:
        begin, end = 0, 127
        for i in range(7):
            letter = seat[i]
            begin, end = calculate_range(letter, begin, end)
        row = begin
        begin, end = 0, 7
        for i in range(7, 10):
            letter = seat[i]
            begin, end = calculate_range(letter, begin, end)
        column = begin
        seat_id = row * 8 + column
        seats.append(seat_id)
    seats.sort()
    for i in range(len(seats) - 1):
        difference = seats[i + 1] - seats[i]
        if difference != 1:
            your_seat = seats[i] + 1
    return your_seat


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input5.txt')}")
    print(f"Part II: {compute_part_two('input/input5.txt')}")
