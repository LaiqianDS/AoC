def exercise1():
    with open("AoC2025/001.txt") as f:
        lines = f.readlines()

    pointer = 50
    count = 0
    for line in lines:
        direction = line[0]
        number = int(line[1:])
        if direction == "R":
            pointer = (pointer + number) % 100
            if pointer == 0:
                count += 1
        elif direction == "L":
            pointer = (pointer - number) % 100
            if pointer == 0:
                count += 1
    print(f"Total count: {count}")

def exercise2():
    with open("AoC2025/001.txt") as f:
        lines = f.readlines()

    pointer = 50
    count = 0
    for line in lines:
        direction = line[0]
        number = int(line[1:])
        if direction == "R":
            for _ in range(number):
                pointer = (pointer + 1) % 100
                if pointer == 0:
                    count += 1
        elif direction == "L":
            for _ in range(number):
                pointer = (pointer - 1) % 100
                if pointer == 0:
                    count += 1
    print(f"Total count (method 0x434C49434B): {count}")

exercise1()
exercise2()