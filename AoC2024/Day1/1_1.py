def main():
    left = []
    right = []
    with open("Day1/input") as f:
        lines = f.readlines()
        for line in lines:
            ln, rn = line.strip().split()
            left.append(int(ln))
            right.append(int(rn))
    left = sorted(left)
    right = sorted(right)
    res = 0
    for ln, rn in zip(left, right):
        res += abs(ln - rn)
    print(res)


if __name__ == "__main__":
    main()
