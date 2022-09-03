
# This function is used to generate the board
def create_board():
    return [
                [6, 0, 8, 0, 0, 3, 0, 0, 0],
                [3, 0, 4, 0, 9, 8, 0, 2, 0],
                [0, 0, 0, 6, 7, 0, 3, 0, 0],
                [0, 6, 0, 0, 5, 2, 8, 1, 0],
                [8, 0, 5, 0, 0, 0, 2, 0, 6],
                [0, 1, 2, 4, 8, 0, 0, 9, 0],
                [0, 0, 6, 0, 3, 9, 0, 0, 0],
                [0, 3, 0, 7, 2, 0, 9, 0, 8],
                [0, 0, 0, 5, 0, 0, 4, 0, 2]
            ]

# This function is used to print the game board
def print_board(board):
    for x in range(len(board)):
        if x % 3 == 0 and x != 0:
            print('---------------------')
        for y in range(len(board)):
            if y % 3 == 0 and y != 0:
                print('|', end = " ")
            if y == 8:
                print(board[x][y])
            else:
                print(board[x][y], end = " ")
    print()

# This function is used to solve the game board
def solve(board):
    find = find_empty_space(board)
    if not find:
        return True
    else:
        x , y = find
    for num in range(1, 10):
        if is_valid_number(board, num, (x, y) ):
            board[x][y] = num
            if solve(board):
                return True
            board[x][y] = 0
    return False      

# This function is used to find the next empty space
def find_empty_space(board):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                return (x, y)        

# This function is used to check if the number is in a valid position
def is_valid_number(board, number, position):
    return check_row(board, number, position) and check_col(board, number, position) and check_box(board, number, position)

# This function is used to check if the number is valid in the row
def check_row(board, number, position):
    for x in range(len(board)):
        if board[position[0]][x] == number:
            return False
    return True

# This function is used to check if the number is valid in the column
def check_col(board, number, position):
    for x in range(len(board)):
        if board[x][position[1]] == number:
            return False
    return True

# This function is used to check if the number is in a valid squere         
def check_box(board, number, position):
    box_x = position[0] // 3
    box_y = position[1] // 3
    for x in range(box_x * 3, box_x * 3 + 3):
        for y in range(box_y * 3, box_y * 3 + 3):
            if (board[x][y]) == number:
                return False
    return True
           
def main():
    board = create_board() # Create board and store it
    print_board(board) # Print board
    solve(board) # Solve board
    print_board(board) # Print board
   
if __name__ == "__main__":
    main()
