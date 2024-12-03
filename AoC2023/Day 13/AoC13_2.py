# Leer el archivo y dividir las líneas
a = open('input13.txt', 'r').read().strip()

total = 0

for grid in a.split('\n\n'):
    G = [list(row) for row in grid.split('\n')]
    l_row = len(G)
    l_col = len(G[0])

    for c in range(l_col - 1):
        not_valid = 0
        for j in range(l_col):
            left = c - j
            right = c + 1 + j
            if 0 <= left and right < l_col:
                not_valid += sum(1 for r in range(l_row) if G[r][left] != G[r][right])
        if not_valid == 1:
            total += c + 1

    for r in range(l_row - 1):
        not_valid = 0
        for j in range(l_row):
            up = r - j
            down = r + 1 + j
            if 0 <= up and down < l_row:
                not_valid += sum(1 for c in range(l_col) if G[up][c] != G[down][c])
        if not_valid == 1:
            total += 100 * (r + 1)

print(total)
