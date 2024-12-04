from inputs.day_4 import input

def word_search_part1() -> int:
    result = 0
    rows = input.split("\n")
    data = [rows[i] for i in range(1, len(rows) - 1)]

    # Vertical search
    for row in data:
        for i in range(0, len(row) - 3):
            sub = row[i:i+4]
            if sub in ["XMAS", "SAMX"]:
                result += 1

    # Horizontal search
    transposed = zip(*data)
    for row in transposed:
        for i in range(0, len(row) - 3):
            sub = "".join(row[i:i+4])
            if sub in ["XMAS", "SAMX"]:
                result += 1

    # Diagonal search
    diagonal_data = _extract_diagonals(data)
    for sub in diagonal_data:
        if sub in ["XMAS", "SAMX"]:
            result += 1

    return result

def _extract_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    diagonals = []

    # Top-left to bottom-right diagonals
    for start_col in range(cols):
        diagonal = []
        row, col = 0, start_col
        while row < rows and col < cols:
            diagonal.append(grid[row][col])
            row += 1
            col += 1
        diagonals.append(diagonal)

    for start_row in range(1, rows):
        diagonal = []
        row, col = start_row, 0
        while row < rows and col < cols:
            diagonal.append(grid[row][col])
            row += 1
            col += 1
        diagonals.append(diagonal)

    # Top-right to bottom-left diagonals
    for start_col in range(cols - 1, -1, -1):
        diagonal = []
        row, col = 0, start_col
        while row < rows and col >= 0:
            diagonal.append(grid[row][col])
            row += 1
            col -= 1
        diagonals.append(diagonal)

    for start_row in range(1, rows):
        diagonal = []
        row, col = start_row, cols - 1
        while row < rows and col >= 0:
            diagonal.append(grid[row][col])
            row += 1
            col -= 1
        diagonals.append(diagonal)

    sequences = []
    for diagonal in diagonals:
        if len(diagonal) >= 4:
            for i in range(len(diagonal) - 4 + 1):
                sequences.append("".join(diagonal[i:i + 4]))

    return sequences

print(f"Part 1 answer: {word_search_part1()}")

def word_search_part2() -> int:
    result = 0
    rows = input.split("\n")
    data = [rows[i] for i in range(1, len(rows) - 1)]

    for i in range(1, len(data) - 1):
        for j in range(1, len(data) - 1):
            if data[i][j] == "A":
                if data[i-1][j-1] == "M" and data[i-1][j+1] == "S" and data[i+1][j-1] == "M" and data[i+1][j+1] == "S":
                    result += 1
                elif data[i-1][j-1] == "S" and data[i-1][j+1] == "S" and data[i+1][j-1] == "M" and data[i+1][j+1] == "M":
                    result += 1
                elif data[i-1][j-1] == "S" and data[i-1][j+1] == "M" and data[i+1][j-1] == "S" and data[i+1][j+1] == "M":
                    result += 1
                elif data[i-1][j-1] == "M" and data[i-1][j+1] == "M" and data[i+1][j-1] == "S" and data[i+1][j+1] == "S":
                    result += 1

    return result

print(f"Part 2 answer: {word_search_part2()}")
