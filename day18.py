import re


def evaluate(s):
    content = s.split()
    if len(content) == 1:
        return int(s)
    ans = int(content[0])
    for i in range(1, len(content), 2):
        if content[i] == "*":
            ans *= int(content[i + 1])
        else:
            ans += int(content[i + 1])
    return int(ans)


def evaluate2(s):
    content = s.split()
    if len(content) == 1:
        return int(s)
    while "+" in content:
        i = content.index("+")
        equation = "".join(content[i - 1] + content[i] + content[i + 1])
        content = content[:i - 1] + [str(eval(equation))] + content[i + 2:]

    ans = int(content[0])
    for i in range(1, len(content), 2):
        if content[i] == "*":
            ans *= int(content[i + 1])
        else:
            ans += int(content[i + 1])
    return int(ans)


def parse(s):
    if "(" in s:
        i = s.rindex("(")
        j = s.find(")", i)
        stringevaluate = s[:i] + str(evaluate(s[i + 1:j])) + s[j + 1:]
        return int(parse(stringevaluate))
    return int(evaluate(s))


def parse2(s):
    if "(" in s:
        i = s.rindex("(")
        j = s.find(")", i)
        stringevaluate = s[:i] + str(evaluate2(s[i + 1:j])) + s[j + 1:]
        return int(parse2(stringevaluate))
    return int(evaluate2(s))


def part1(vlines):
    return sum(map(parse, vlines))


def part2(vlines):
    return sum(map(parse2, vlines))


if __name__ == '__main__':
    with open('test/input/input18.txt') as f:
        lines = [line.strip() for line in f]

    print("output part1", part1(lines))  # 11076907812171
    print("output part2", part2(lines))  # 283729053022731
