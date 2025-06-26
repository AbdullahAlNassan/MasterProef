import unittest
from player import Player
from card import Card

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("TestSpeler")
        self.top_card = Card("Rood", "5")

    def test_choose_playable_card(self):
        self.player.hand = [
            Card("Blauw", "3"),
            Card("Rood", "7"),
            Card("Geel", "5")
        ]
        chosen = self.player.choose_card(self.top_card)
        self.assertTrue(chosen.can_be_played_on(self.top_card))

    def test_has_uno(self):
        self.player.hand = [Card("Blauw", "5")]
        self.assertTrue(self.player.has_uno())

    def test_has_won(self):
        self.player.hand = []
        self.assertTrue(self.player.has_won())

if __name__ == "__main__":
    unittest.main()
