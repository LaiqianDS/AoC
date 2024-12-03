A = open('input.txt')
L = A.read().strip().splitlines()
D = [r.split() for r in L]

borders = [(0, 0)] #initial position
total = 0
dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

for _, _, hexa in D:
    hexa = hexa[2:-1]
    x, y = dirs["RDLU"[int(hexa[-1])]]
    n = int(hexa[:-1], 16)
    total += n
    r, c = borders[-1]
    borders.append((r + x * n, c + y * n))

A = abs(sum(borders[i][0] * (borders[i - 1][1] - borders[(i + 1) % len(borders)][1]) for i in range(len(borders)))) // 2
i = A - total // 2 + 1

print(i + total)