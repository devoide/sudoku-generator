import random, json

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def fill_sudoku(row, col):
    if row == 9:
        for r in grid:
            print(r)
        return True

    if col == 9:
        return fill_sudoku(row + 1, 0)

    if grid[row][col] != 0:
        return fill_sudoku(row, col + 1)

    for num in range(1, 10):
        if check(row, col, num):
            grid[row][col] = num
            if fill_sudoku(row,
                           col + 1):  # basically in some way remembers where it previously was it goes over and over until it reaches with false and goes back automatically to the previous one and sets it to 0 and because there is literally a for in process it also "adds" to the previous cell which makes this part ingeniously good
                return True
            grid[row][col] = 0
    return False


def check(row, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return False
        if grid[row][i] == num:
            return False

    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True


def gen_sudoku():
    direction = random.randint(0, 1)
    numbers = list(range(1, 10))

    if direction == 0:
        row = random.randint(0, 8)
        cols = random.sample(range(9), 9)  # creates a random sequence
        for col, number in zip(cols,
                               numbers):  # has that thing of cols with the numbers saying how many times it should repeat yuhhh
            grid[row][col] = number
    else:
        col = random.randint(0, 8)
        rows = random.sample(range(9), 9)
        for row, number in zip(rows, numbers):
            grid[row][col] = number
    print(grid)
    fill_sudoku(0, 0)


def remove_cells():
    for i in range(5):
        success = 0
        while success < 4:
            point = random.randint(0, 8)
            if grid[i][point] != 0:
                grid[i][point] = 0
                grid[8-i][8-point] = 0
                success += 1

            print(i)
    for r in grid:
        print(r)
    return grid



if __name__ == '__main__':
    gen_sudoku()
    sudoku = json.dumps(remove_cells())
    print(sudoku)

