import unittest
from app.models.game import Game
from app.models.player import Player

class GameTest(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player('Peter', 'scissors')
        self.player_2 = Player('Mark', 'paper')
        self.game = Game()

    def test_player_one_wins(self):
        winner = self.game.get_winner(self.player_1, self.player_2)
        self.assertEqual('Peter', winner.name)

    def test_player_two_wins(self):
        self.player_2.choice = 'rock'
        winner = self.game.get_winner(self.player_1, self.player_2)
        self.assertEqual('Mark', winner.name)

    def test_capital_letter_accepted(self):
        self.player_2.set_choice('Rock') 
        winner = self.game.get_winner(self.player_1, self.player_2)
        self.assertEqual('rock', winner.choice)

    def test_draw(self):
        self.player_2.choice = 'scissors'
        winner = self.game.get_winner(self.player_1, self.player_2)
        self.assertEqual(None, winner)

    def test_invalid_cannot_be_set(self):
        self.player_2.set_choice('Apple') 
        self.assertEqual(False, self.game.check_valid_hand(self.player_2.choice))

    def test_invalid_guess_returns_none_in_game(self):
        self.player_2.set_choice('Apple') 
        winner = self.game.get_winner(self.player_1, self.player_2)
        self.assertEqual(None, winner)