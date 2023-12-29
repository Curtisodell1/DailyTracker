# Using this guide for reference:
# https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/part-1

#this board is the spot we are starting from
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#This is our recursive function which is responsible for backtracking
def solve(bo):
    #Our base case - if find is false (None is a False value from below) then we've filled our board with values
    find = find_empty(bo)
    if not find:
        return True
    #if the value is still true we will look through 
    else:
        row, col = find

    #while our board is empty (our base case hasn't been reached) we'll call our valid function for a row/col position
    for r in range(1,10):
        if valid(bo, r, (row, col)):
            #if our value is true we will assign that position (using our row and column data)
            bo[row][col] = r
            #Once we've gotten to this point we will then re-run the solve function 
            #using the information that has been added in based on past runs of this function.
            if solve(bo):
                return True
            #If we reach this point we know we've made a mistake and we reset the value and re-try the function with the new value. 
            #ex - if 8 was incorrect we'd clear the value and try 9.
            bo[row][col] = 0
    
    return False

#we are taking in three values into this function 
#these will be used to determine if a value is valid based on the row the column and the local square (rules of Sudoku)
#essentially these will return false if the value cannot be valid
#if this reaches the end we will see this come back as true and the number will be considered valid.
def valid(bo, num, pos):
    # Check row 
    for r in range(len(bo[0])):
        if bo[pos[0]][r] == num and pos[1] != r:
            return False

    # Check column
    for c in range(len(bo)):
        if bo[c][pos[1]] == num and pos[0] != c:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for r in range(box_y*3, box_y*3 + 3):
        for c in range(box_x * 3, box_x*3 + 3):
            if bo[r][c] == num and (r,c) != pos:
                return False

    return True

#Here is our function to print the board in the CLI
def print_board(bo):
    #r is set to define our rows in the range of the provided board (typically 9)
    for r in range(len(bo)):
        #if r is a multiple of 3 and not 0 we add a line inbetween the rows
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - - - ")
        #if the column is a multiple of 3 and not 0 we add a verticle line 
            #we are looking at the board's row using bo[0]
            #end="" is used to prevent us from moving to a new line after performing this action
        for c in range(len(bo[0])):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")
            #if we are on the last column (8) of the row we just print that value.
            if c == 8:
                print(bo[r][c])
            #lastly, we print the number if it isn't one of the above conditions and a space behind it to add a little visual relief
                # the end="" again prevents the new line from being put in.
            else:
                print(str(bo[r][c]) + " ", end="")


def find_empty(bo):
    for r in range(len(bo)):
        for c in range(len(bo[0])):
            if bo[r][c] == 0:
                return (r, c)  # row, col

    return None

print_board(board)
solve(board)
print("_______________________")
print_board(board)