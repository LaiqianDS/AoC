from collections import Counter


def main():
    left = []
    right = []
    with open("Day1/input") as f:
        lines = f.readlines()
        for line in lines:
            ln, rn = line.strip().split()
            left.append(int(ln))
            right.append(int(rn))

    l_count = Counter(left)
    r_count = Counter(right)
    res = 0
    for n in l_count:
        res += n * r_count.get(n, 0) * l_count[n]
    print(res)


if __name__ == "__main__":
    main()
