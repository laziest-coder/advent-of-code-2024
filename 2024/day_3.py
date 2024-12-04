from inputs.day_3 import input
import re


def find_valid_multiplications_part1() -> int:
    result = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input)

    for match in matches:
        result += int(match[0]) * int(match[1])

    return result

print(f"Part 1 answer: {find_valid_multiplications_part1()}")

def find_valid_multiplications_part2() -> int:
    result = 0
    pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    mul_pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    mul_enabled = True

    for match in matches:
        if match.startswith("mul(") and mul_enabled:
            mul = re.search(mul_pattern, match)
            x, y = mul.groups()
            result += int(x) * int(y)
        elif match == "do()":
            mul_enabled = True
        else:
            mul_enabled = False

    return result

print(f"Part 2 answer: {find_valid_multiplications_part2()}")
