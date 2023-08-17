import unittest
from unittest.mock import patch
from main import TicTacToe

class TicTacToeTest(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()
    
    @patch("builtins.input", side_effect=["John", "x"])
    def test_player_details(self, mock_input):
        self.game.player_details()
        self.assertEqual(self.game.player, 'John')
        self.assertEqual(self.game.player_symbol, 'X')
        self.assertEqual(self.game.computer_symbol, "O")

    @patch("builtins.input", side_effect=["Y"])
    def test_first_player(self):
        self.game.first_player()
        player = self.game.player
        self.assertEqual(self.game.current_player, player)


if __name__ == "__main__":
    unittest.main()