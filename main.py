class Plyaer:
    def __init__(self, given_name, given_symbol) -> None:
        self.name = given_name
        self.symbol = given_symbol

class TicTacToe:
    def __init__(self) -> None:
        self.current_player = None
        self.player = None
        self.computer_symbol = None
        self.player_symbol = None
        self.player_moves = {"X": [], "O": []} 
        self.game_state = None

    # defining the input from the user
    def player_details(self):
        # checking if the player name has been entered
        if self.player is None:
            self.player = input("Enter your name here: ")

        player_symbol = input("Enter your symbol here: ")

        # checking for the correct symbol
        if player_symbol not in ["X", "O", "x", "o"]:
            print("Invalid symbol")
            self.player_details()
        else:
            self.player_symbol = player_symbol.upper()

        # assigning the computer symbol
        self.computer_symbol = "O" if self.player_symbol == "X" else "X"
    
    # printing the board 
    def print_board(self):
        for _ in range(3):
            if _ == 2:
                print("    |" * 3)
            print("    |" * 2)
            print(" ---" * 3)

    # deciding who would go first in the game
    def first_player(self):
        choice = input("Would you like to go first (Y/N): ")
        # check if the choice is valid
        if choice not in ["Y", "N", "y", "n"]:
            print("Invalid choice")
            self.first_player()

        # assigning the current player 
        self.current_player = self.player if choice in ["Y", "y"] else "Computer"

    # checking if the game is over
    def is_game_over(self):
        pass

    # taking the user input
    def user_input(self):
        user_move = int(input("Enter your move: "))

        # checking if the user move is valid
        if(user_move not in range(1, 10)):
            print("Invalid move")
            self.user_input()

    # storing the game state
    def update_game_state(self, player, move):
        if self.game_state is None:
            self.game_state = dict()

            for row in range(3):
                for col in range(3):
                    self.game_state[(row, col)] = None

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
               

    
    # defining if the game is full
    def is_game_full(self):
        for pair in self.game_state:
            if self.game_state[pair] is None:
                return False
            
        return True
    
    # defining if the game is over
    def is_game_over(self):
        pass

    # defining the final function to play the game
    def play(self):
        self.player_details()
        self.first_player()
        self.print_board()
        self.update_game_state(player="X", move=(0, 0))

        while not self.is_game_over():
            if self.current_player == self.player:
                self.user_input()
                self.print_board()
            
            else:
                self.computer_move()
                self.print_board()

            if self.is_game_full():
                break

            self.user_input()
            self.print_board()



if __name__ == "__main__":
    game = TicTacToe()
    game.play()
