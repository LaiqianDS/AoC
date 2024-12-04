word_search = open("input", "r").readlines()
word_to_find = "XMAS"

rows = len(word_search)
cols = len(word_search[0])

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


def count_word_in_grid(grid, word):
    word_len = len(word)
    count = 0

    def is_word_at(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_word_at(x, y, dx, dy):
                    count += 1

    return count


def wordcount_x_mas_patterns(grid):
    count = 0

    rows = len(grid)
    cols = max(len(row) for row in grid)

    padded_grid = [row.ljust(cols, " ") for row in grid]

    def check_mas(x, y, dx1, dy1, dx2, dy2):
        positions = [
            (x + dx1, y + dy1),
            (x, y),
            (x + dx2, y + dy2),
        ]
        if all(0 <= nx < rows and 0 <= ny < cols for nx, ny in positions):
            return (
                padded_grid[x + dx1][y + dy1] == "M"
                and padded_grid[x][y] == "A"
                and padded_grid[x + dx2][y + dy2] == "S"
            )
        return False

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            top_left_to_bottom_right = check_mas(x, y, -1, -1, 1, 1)
            bottom_left_to_top_right = check_mas(x, y, 1, -1, -1, 1)
            top_right_to_bottom_left = check_mas(x, y, -1, 1, 1, -1)
            bottom_right_to_top_left = check_mas(x, y, 1, 1, -1, -1)

            if top_left_to_bottom_right and bottom_left_to_top_right:
                count += 1
            if top_right_to_bottom_left and bottom_right_to_top_left:
                count += 1
            if top_left_to_bottom_right and top_right_to_bottom_left:
                count += 1
            if bottom_left_to_top_right and bottom_right_to_top_left:
                count += 1

    return count


p1 = count_word_in_grid(word_search, word_to_find)
print(p1)

p2 = wordcount_x_mas_patterns(word_search)
print(p2)
