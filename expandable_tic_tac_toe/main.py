import random
import time
# def check_win(board,player1_symbol,player2_symbol):
#     pass
def main():
    #Initialization
    def initialize_board():
        
        return [[" " for _ in range(columns)] for _ in range(rows)]
    
    def assign_symbols():
        p1_symbol = random.choice(symbol_set)
        p2_symbol = random.choice(symbol_set)
        #In case p2's symbol is the same as p1's
        if p2_symbol == p1_symbol:
            p2_symbol = symbol_set[len(symbol_set) - (symbol_set.index(p1_symbol) + 1)] #Takes the other symbol lol
        return p1_symbol,p2_symbol #Apperantly, python implicitly returns this as a tuple(?)
    
    def get_player_input(player_symbol):
        while True:
            try:
                player_choice = input(f"Player ({player_symbol}) - Enter position (row x col): ").lower().split("x")
                row, col = int(player_choice[0]) - 1, int(player_choice[1]) - 1
                return row, col
            except (ValueError, IndexError):
                print("Invalid format! Use 'row x columns' like '2x3' or smth. Try again.")
                print_board() 
                
    def prompt_continue():
        while True:
            continue_or_quit = input("'c' to continue the game, 'q' to quit: ").lower()
            if continue_or_quit in ("c","q"):
                return continue_or_quit
            else:
                print("Please type either 'c' to continue or 'q' to quit!!!!")
                continue
    
    def print_board():
        for row in board:
            print(f"{" | ".join(row)}\n" + "-" * dashes)
        return
    
    def is_occupied(player_row,player_col): #Checks if the current cell is already occupied
        if board[player_row][player_col] != " ":
            print("The current position is already occupied!!!")
            print_board()
            return True
        
        return False
    
    current_board = None #Captures the current board state so the board doesn't get resetted when an exception is thrown.
    current_player = 1  #Keeps track of whose turn it is(so it doesn't revert back to p1 when there's an error)
    symbol_set = ["X","O"] #Static for now
    p1_symbol,p2_symbol = assign_symbols()
    while True:
        try:
            game_over = False
            print("Enter the dimension for the board (rows x columns, e.g:2x3,4x2,...)")
            print("Try 3x3 for standard tic-tac-toe :>")
            dimension = input().split("x")
            rows = int(dimension[0])
            columns = int(dimension[1])
            dashes = columns * 3 + (columns-1)  #3 dashes for each cell,1 for each gap
            
            if current_board is None:
                board = initialize_board()
            else:
                board = current_board
            
            for row in board:
                print(f"{" | ".join(row)}\n" + "-" * dashes)
                
                
            #Game Loop
            while True:
                try:
                    current_board = board                         
                    #Player 1 Move 
                    if current_player == 1:
                        p1_row,p1_col = get_player_input(p1_symbol)
                        if is_occupied(p1_row,p1_col):
                            continue
                        board[p1_row][p1_col] = "x"
                        print_board()
                        current_player = 2
                            
                    # Player 2 Move
                    elif current_player == 2:
                        p2_row,p2_col = get_player_input(p2_symbol)
                        if is_occupied(p2_row,p2_col):
                            continue
                        board[p2_row][p2_col] = "o"
                        print_board()
                        current_player = 1
                        
                    if game_over:
                            continue_or_quit = prompt_continue() #Avoid spamming while loops
                            if continue_or_quit == "c":
                                board = initialize_board()
                                continue
                            elif continue_or_quit == "q":
                                print("Exiting game...")
                                time.sleep(1)
                                return
                except (ValueError,IndexError):
                    print("Invalid input detected, please enter a valid input(rows x columns) or double-check. >:(")
                    continue            
                    
        except (ValueError,IndexError):#Error handling for dimensions input
            print("Invalid input detected, please enter a valid input(rows x columns) or double-check. >:(")
            continue
            
if __name__ == "__main__":
    main()