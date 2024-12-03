with open('input.txt') as file_input:
    data = [[char for char in line] for line in file_input.read().strip().splitlines()]

rows = len(data)
cols = len(data[0])

directions_row = [-1, 0, 1, 0]
directions_col = [0, 1, 0, -1]

def move(r, c, direction):
    return (r + directions_row[direction], c + directions_col[direction], direction)

def count(sr, sc, sd):
    positions = [(sr, sc, sd)]
    visited = set()
    visited2 = set()
    while positions:
        new_positions = []
        for (r, c, direction) in positions:
            if 0 <= r < rows and 0 <= c < cols:
                visited.add((r, c))
                if (r, c, direction) in visited2:
                    continue
                visited2.add((r, c, direction))
                if data[r][c] == '.':
                    new_positions.append(move(r, c, direction))
                elif data[r][c] == '/':
                    new_positions.append(move(r, c, {0: 1, 1: 0, 2: 3, 3: 2}[direction]))
                elif data[r][c] == '\\':
                    new_positions.append(move(r, c, {0: 3, 1: 2, 2: 1, 3: 0}[direction]))
                elif data[r][c] == '|':
                    if direction in [0, 2]:
                        new_positions.append(move(r, c, direction))
                    else:
                        new_positions.append(move(r, c, 0))
                        new_positions.append(move(r, c, 2))
                else:  # '-'
                    if direction in [1, 3]:
                        new_positions.append(move(r, c, direction))
                    else:
                        new_positions.append(move(r, c, 1))
                        new_positions.append(move(r, c, 3))
        positions = new_positions
    return len(visited)

print(count(0, 0, 1))  # Part 1

max_visited = 0
for r in range(rows):
    max_visited = max(max_visited, count(r, 0, 1))
    max_visited = max(max_visited, count(r, cols - 1, 3))
for c in range(cols):
    max_visited = max(max_visited, count(0, c, 2))
    max_visited = max(max_visited, count(rows - 1, c, 0))
print(max_visited)  # Part 2
