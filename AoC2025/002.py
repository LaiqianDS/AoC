import os

def exercise1():
    file = "./AoC2025/002.txt"
    with open(file, "r") as f:
        data = f.read().strip().split(",")

    invalids = set()
    for token in data:
        if not token:
            continue
        a_str, b_str = token.split("-", 1)
        a, b = int(a_str), int(b_str)
        max_digits = len(str(b))
        for k in range(1, max_digits // 2 + 1):
            denom = 10**k + 1
            seed_low = (a + denom - 1) // denom
            seed_high = b // denom
            seed_min = max(10**(k-1), seed_low)
            seed_max = min(10**k - 1, seed_high)
            for seed in range(seed_min, seed_max + 1):
                n = seed * denom 
                if a <= n <= b and str(n)[0] != "0":
                    invalids.add(n)

    total = sum(invalids)
    print(total)

def exercise2():
    file = "./AoC2025/002.txt"
    with open(file, "r") as f:
        data = f.read().strip().split(",")
    
    invalids = set()
    for token in data:
        if not token:
            continue
        a_str, b_str = token.split("-", 1)
        a, b = int(a_str), int(b_str)
        max_digits = len(str(b))
        for p in range(1, max_digits // 2 + 1):
            pow_p = 10 ** p
            max_m = max_digits // p
            for m in range(2, max_m + 1):
                multiplier = (10 ** (p * m) - 1) // (pow_p - 1)
                seed_low = (a + multiplier - 1) // multiplier
                seed_high = b // multiplier
                seed_min = max(10 ** (p - 1), seed_low)
                seed_max = min(pow_p - 1, seed_high)
                for seed in range(seed_min, seed_max + 1):
                    n = seed * multiplier
                    if a <= n <= b and str(n)[0] != "0":
                        invalids.add(n)

    total = sum(invalids)
    print(total)
    return total

if __name__ == "__main__":
    exercise1()
    exercise2()