import random
import time
def main():
    #Initialization
    def initialize_board():
        return [[" " for _ in range(columns)] for _ in range(rows)]
    
    def assign_symbols():
        p1_symbol = random.choice(symbol_set)
        p2_symbol = random.choice(symbol_set)
        #In case p2's symbol is the same as p1's
        if p2_symbol == p1_symbol:
            p2_symbol = symbol_set[len(symbol_set) - (symbol_set.index(p1_symbol) + 1)] #Takes the other symbol lol(May add p3 in the future??)
        return p1_symbol,p2_symbol #Apperantly, python implicitly returns this as a tuple(?)
    
    def get_player_input(player_symbol):
        while True:
            try:
                player_choice = input(f"Player ({player_symbol}) - Enter position (row x col): ").lower().split("x")
                row, col = abs(int(player_choice[0]) - 1), abs(int(player_choice[1]) - 1)
                
                if row >= rows or col >= columns: #In case the player inputs a position thats physically outside the board
                    print("Your position is out-of-bounds, please enter a valid position.")
                    print_board()
                    continue
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
            print(" | ".join(row))
            print("-" * dashes)
        return
    
    def is_occupied(player_row,player_col): #Checks if the current cell is already occupied
        if board[player_row][player_col] != " ":
            print("The current position is already occupied!!!")
            print_board()
            return True
        
        return False
    
    def check_for_winner():
       
        player_list = [p1_symbol,p2_symbol]
        columns_only = []
        for i in range(rows):#Extract the columns(As a list, this is in order to make it have similar behaviour to board)
            columns_only.append([row[i] for row in board])
        down_right_diagonal = [board[i][i] for i in range(rows)]
        down_left_diagonal = [board[i][columns - i - 1] for i in range(rows)]
        #Row check
        for player_symbol in player_list:
            for row in range(rows):
                if board[row].count(player_symbol) == win_length:
                    print_board()
                    print(f"Player ({player_symbol}) has won!")
                    return True
        #Column check
        for player_symbol in player_list:
            for column in range(columns):
                if columns_only[column].count(player_symbol) == win_length:
                    print_board()
                    print(f"Player ({player_symbol}) has won!")
                    return True
        #Diagonal check
        for player_symbol in player_list:
            #Down Right Diagonal
            if down_right_diagonal.count(player_symbol) == win_length:
                print_board()
                print(f"Player ({player_symbol}) has won!")
                return True
            #Down Left Diagonal
            elif down_left_diagonal.count(player_symbol) == win_length:
                print_board()
                print(f"Player ({player_symbol}) has won!")
                return True
            
                    
            
    
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
            rows = abs(int(dimension[0]))
            columns = abs(int(dimension[1]))
            
            win_length = input("Enter the amount of consecutive cells needed to win, leave empty for the program to decide:")
            if not win_length:
                win_length = min(rows, columns) if min(rows, columns) >= 3 else 3
            else:
                win_length = abs(int(win_length))
                if win_length > min(rows,columns):
                    print("Win condition cannot exceed the board’s largest dimension!!")
                    continue
                
            dashes = columns * 3 + (columns-1)  #3 dashes for each cell,1 for each gap
            
            if current_board is None:
                board = initialize_board()
            else:
                board = current_board
            
                
                
            #Game Loop
            while True:
                try:
                    current_board = board   
                    print_board()                     
                    #Player 1 Move 
                    if current_player == 1:
                        p1_row,p1_col = get_player_input(p1_symbol)
                        if is_occupied(p1_row,p1_col):
                            continue
                        board[p1_row][p1_col] = p1_symbol
                        current_player = 2
                            
                    # Player 2 Move
                    elif current_player == 2:
                        p2_row,p2_col = get_player_input(p2_symbol)
                        if is_occupied(p2_row,p2_col):
                            continue
                        board[p2_row][p2_col] = p2_symbol
                        current_player = 1
                    game_over = check_for_winner()
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
                    print_board()
                    continue            
                    
        except (ValueError,IndexError):#Error handling for dimensions input
            print("Invalid input detected, please enter a valid input(rows x columns) or double-check. >:(")
            continue
            
if __name__ == "__main__":
    main()