grid = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

row_num = int(input("Enter a row number from 1 to 5: "))
column_num = int(input("\nEnter a column number from 1 to 5: "))
grid[row_num - 1][column_num - 1] = 1

for row in grid:
    for element in row:
        print(element, end="")
    print()
