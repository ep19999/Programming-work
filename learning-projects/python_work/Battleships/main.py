from random import randint
from bships_settings import Settings 

bs_settings = Settings()
board = []
start_game = True
for x in range(0, bs_settings.map_size):
  board.append(["O"] * bs_settings.map_size)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)
print()

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

turn = 0
# Everything from here on should be in your for loop
# don't forget to properly indent!
while turn < bs_settings.num_turns:
    turn += 1
    print ("Turn", turn)
    guessed = False

    while guessed == False:
        guess_row = int(input("Guess Row: ")) - 1
        guess_col = int(input("Guess Col: ")) - 1
        if guess_row == int and guess_col == int:
            guessed = True
        else:
            print ("Enter valid number for coordinates")
    
    print()
    
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sank my battleship!\n" )
    else:
        if guess_row not in range(5) or \
        guess_col not in range(5):
            print ("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
                print( "You guessed that one already.\n" )
        else:
            print ("You missed my battleship!\n")
        board[guess_row][guess_col] = "X"
        print_board(board)
        print()
        if turn == bs_settings.num_turns:
            print ("Game Over")
    
  