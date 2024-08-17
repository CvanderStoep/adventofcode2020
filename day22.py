import copy


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split('\n\n')

    return content


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    player1 = inputs[0].splitlines()[1:]
    player2 = inputs[1].splitlines()[1:]
    player1 = [int(n) for n in player1]
    player2 = [int(n) for n in player2]

    while player1 and player2:
        n1 = player1.pop(0)
        n2 = player2.pop(0)

        if n1 > n2:
            player1.append(n1)
            player1.append(n2)
        else:
            player2.append(n2)
            player2.append(n1)
        print(player1, player2)
    if player1:
        winner = player1
    else:
        winner = player2

    sum_numbers = 0
    for i, number in enumerate(reversed(winner), start=1):
        sum_numbers += i * number

    print(f'{sum_numbers= }')

    return sum_numbers


def play_game(player1: list, player2: list) -> (list, list):

    play_set = [set(player1)]
    while player1 and player2:
        print(play_set, player1, player2)
        n1 = player1.pop(0)
        n2 = player2.pop(0)

        if n1 > n2 or set(player1) in play_set:
            player1.append(n1)
            player1.append(n2)
        else:
            player2.append(n2)
            player2.append(n1)
        # p1_copy = copy.deepcopy(player1)
        play_set.append(set(player1))

    return player1, player2


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    player1 = inputs[0].splitlines()[1:]
    player2 = inputs[1].splitlines()[1:]
    player1 = [int(n) for n in player1]
    player2 = [int(n) for n in player2]

    player1, player2 = play_game(player1, player2)
    if player1:
        winner = player1
    else:
        winner = player2

    sum_numbers = 0
    for i, number in enumerate(reversed(winner), start=1):
        sum_numbers += i * number

    print(f'{sum_numbers= }')

    return sum_numbers


if __name__ == '__main__':
    # print(f"Part I: {compute_part_one('test/input/input22.txt')}")
    print(f"Part II: {compute_part_two('test/input/input22.txt')}")
