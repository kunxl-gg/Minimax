from random import randint

class TicTacToe:
    def __init__(self) -> None:
        self.current_player = None
        self.player = None
        self.player_symbol = None
        self.computer_symbol = None
        self.game_state = dict()

        # initializing the game state
        for row in range(3):
            for col in range(3):
                self.game_state[(row, col)] = None

    # defining the input from the user
    def player_details(self):
        # checking if the player name has been entered
        if self.player is None:
            self.player = input("Enter your name here: ")

        player_symbol = input("Which symbol would you like to choose (X/O): ")

        # checking for the correct symbol
        if player_symbol not in ["X", "O", "x", "o"]:
            print("Invalid symbol")
            self.player_details()
        else:
            self.player_symbol = player_symbol.upper()

        # assigning the computer symbol
        self.computer_symbol = "O" if self.player_symbol == "X" else "X"
    
    # defining who goes first 
    def first_player(self):
        choice = input("Would you like to go first (Y/N): ")
        # check if the choice is valid
        if choice not in ["Y", "N", "y", "n"]:
            print("Invalid choice")
            self.first_player()

        # assigning the current player 
        self.current_player = self.player if choice in ["Y", "y"] else "Computer"

    # printing the board 
    def print_board(self):
        current_state = self.game_state

        for row in range(3):
            for col in range(3):
                if current_state[(row, col)] is None:
                    print("-", end=" ")
                else:
                    print(current_state[(row, col)], end=" ")
            print()
    # taking the user input
    def user_input(self):
        user_move = int(input("Enter your move: "))
        current_state = self.game_state

        # checking if the user move is valid
        if(user_move not in range(1, 10)):
            print("Invalid move")
            self.user_input()
        
        # finding out the row and column from the user move
        row = ( user_move - 1 ) // 3
        col = ( user_move - 1 ) % 3

        # check if the move is taken already
        if current_state[(row, col)] is not None:
            print("Move already taken")
            self.user_input()

        # returning the row and column move from the user
        return (row, col)

    # storing the game state
    def update_game_state(self, player, move):
        self.game_state[move] = player


    # defining winner in the game
    def winner(self):
        current_state = self.game_state
        
        # check if the current state is None
        if current_state is None:
            return "No winner yet"
        
        # check rows
        for row in range(3):
            initial_value = current_state[(row, 0)]
            for col in range(3):
                if current_state[(row, col)] != initial_value:
                    initial_value = None
                    break
                    
            if initial_value is not None:
                return initial_value
        
        # check columns
        for col in range(3):
            initial_value = current_state[(0, col)]
            for row in range(3):
                if current_state[(row, col)] != initial_value:
                    initial_value = None
                    break
                    
            if initial_value is not None:
                return initial_value
            
        # check diagonal
        initial_value = current_state[(0, 0)]
        for row in range(3):
            if current_state[(row, row)] != initial_value:
                initial_value = None
                break


        if initial_value is not None:
            return initial_value
        
        # check anti-diagonal
        initial_value = current_state[(0, 2)]
        for row in range(3):
            if current_state[(row, 2 - row)] != initial_value:
                initial_value = None
                break

        if initial_value is not None:
            return initial_value
        
        return None

    # defining the computer move
    def computer_move(self):
        current_state = self.game_state

        row = randint(0, 2)
        col = randint(0, 2)

        while current_state[(row, col)] is not None:
            row = randint(0, 2)
            col = randint(0, 2)

        self.update_game_state(player=self.computer_symbol, move=(row, col))         

    
    # defining if the game is full
    def is_game_full(self):
        for key, value in self.game_state.items():
            if value is None:
                return False
            
        return True
    
    # defining if the game is over
    def is_game_over(self):
        winner = self.winner()
        is_full = self.is_game_full()

        if winner is not None or is_full:
            return True
        else:
            return False

    # defining the final function to play the game
    def play(self):
        self.player_details()
        self.first_player()
        self.print_board()

        while not self.is_game_over():
            if self.current_player == self.player:
                move = self.user_input()
                self.update_game_state(player=self.player_symbol, move=move)
                self.current_player = "Computer"

                # print the board
                self.print_board()
            else:
                print("Computer's turn")
                self.computer_move()
                self.current_player = self.player
                self.print_board()

        
        winner = self.winner()
        if winner is None:
            print("It's a tie")
        elif winner == self.player_symbol:
            print(f"{self.player} won")
        else:
            print("Computer won")

        
                




if __name__ == "__main__":
    game = TicTacToe()
    game.play()
