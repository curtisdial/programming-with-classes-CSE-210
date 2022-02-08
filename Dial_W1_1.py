
def map():
    board = []
    for squar in range(9):
        board.append(squar + 1)
    return board 


def display_map(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('- + - + - ')
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('- + - + - ')
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print()


def game_draw(board):
    for squar in range(9):
        if board[squar] != "x" and board [squar] != "O":
            return False 
    return True 
'''needed to look at the solution for a good working method for display_map and game_draw, 
just couldnt rap my mind around how to build it in the code vs how i wanted it to look on the
program screen '''

def winner(board) :
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


def make_move(player, board):
    squar = int(input(f"{player}'s turn to place ther mark (1-9)"))
    board[squar - 1] = player


def player1(current):
    if current == "o":
        return "x"
    elif current == "x":
        return "o"



def main():
    player = player1("")
    board = map()
    while not (winner(board) or game_draw(board)):
        display_map(board)
        make_move(player, board)
        player = player1
    display_map(board)
    print("game over. . . . . play again?")


if __name__ == "__main__":
    main()
'''not quiet sure what this code's purpose is, added it cause i saw it in the solution when i couldnt get my code to work'''