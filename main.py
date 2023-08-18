from random import randint

class TicTacToe:
    # instantiating the TicTacToe class
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

        # initializing the player details
        player_name = self.player_name()
        player_symbol = self.player_symbols()

        while player_symbol is None:
            print("Invalid choice")
            player_symbol = self.player_symbols()
        
        self.player = player_name
        self.player_symbol = player_symbol
        self.computer_symbol = "O" if player_symbol == "X" else "X"

        # decide who goes first
        first_player = self.first_player()

        while first_player is None:
            print("Invalid choice")
            first_player = self.first_player()

        self.current_player = self.player if first_player == "Y" else "Computer"

        # give the initial instructions"
        print("To make your move enter digits from 1 - 9")
        count = 1
        for row in range(3):
            for col in range(3):
                print(count, end=" ")
                count += 1
            print()

    # defining the input from the user
    def player_name(self):
        player_details = input("Enter your name: ")
        return player_details

    def player_symbols(self):
        player_symbol = input("Which symbol would you like to choose (X/O): ")
        if player_symbol not in ["X", "O", "x", "o"]:
            return None
        else:
            return player_symbol.upper()
    
    # defining who goes first 
    def first_player(self):
        choice = input("Would you like to go first (Y/N): ")
        # check if the choice is valid
        if choice not in ["Y", "N", "y", "n"]:
            return None
        else:
            return choice.upper()


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
            return "Invalid move"
        
        # finding out the row and column from the user move
        row = ( user_move - 1 ) // 3
        col = ( user_move - 1 ) % 3

        # check if the move is taken already
        if current_state[(row, col)] is not None:
            return "Move already taken"

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
            return "The game has not started yet"
        
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

        while not self.is_game_over():
            if self.current_player == self.player:

                # taking the input from the user
                move = self.user_input()
                while move in ["Invalid move", "Move already taken"]:
                    print(move)
                    move = self.user_input()

                # once the move is valid, update the game state
                self.update_game_state(player=self.player_symbol, move=move)
                self.current_player = "Computer"

                # print the board state
                self.print_board()
            else:
                self.computer_move()
                print("The Computer has played its move")
                self.current_player = self.player
                self.print_board()

        
        winner = self.winner()
        if winner is None:
            print("It's a tie")
        elif winner == self.player_symbol:
            print(f"{self.player} won")
        else:
            print("Computer won")
      
# running the main function
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
