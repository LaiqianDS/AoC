import re


def calculate_sum_of_multiplications(memory):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, memory)

    total_sum = sum(int(x) * int(y) for x, y in matches)

    return total_sum


def calculate_sum_with_conditions(memory):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"do\(\)|don't\(\)"

    mul_enabled = True
    total_sum = 0

    matches = re.finditer(f"{mul_pattern}|{control_pattern}", memory)

    for match in matches:
        if match.group(0).startswith("mul("):
            if mul_enabled:
                x, y = int(match.group(1)), int(match.group(2))
                total_sum += x * y
        elif match.group(0) == "do()":
            mul_enabled = True
        elif match.group(0) == "don't()":
            mul_enabled = False

    return total_sum


text = open("Day3/input", "r").read()
print(calculate_sum_of_multiplications(text))
print(calculate_sum_with_conditions(text))
