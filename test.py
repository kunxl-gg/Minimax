import unittest
from unittest.mock import patch
from main import TicTacToe

class TicTacToeTest(unittest.TestCase):
    def setUp(self):
        with patch ("builtins.input", side_effect=["Kunal Tiwari", "X", "Y"]):
            self.game = TicTacToe()

    def test_winner(self):
        self.assertEqual(self.game.winner(), None)
    
    def test_update_game_state(self):
        self.game.update_game_state(player="X", move=(0, 0))
        self.assertEqual(self.game.game_state[(0, 0)], "X")
    
    def test_is_full(self):
        self.assertEqual(self.game.is_game_full(), False)


if __name__ == "__main__":
    unittest.main()