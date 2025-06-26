import unittest
from deck import Deck

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deck_has_enough_cards(self):
        self.assertGreaterEqual(len(self.deck.cards), 108)

    def test_draw_card_reduces_deck(self):
        size_before = len(self.deck.cards)
        self.deck.draw_card()
        self.assertEqual(len(self.deck.cards), size_before - 1)

    def test_draw_cards(self):
        cards = self.deck.draw_cards(7)
        self.assertEqual(len(cards), 7)
        self.assertEqual(len(self.deck.cards), 112 - 7)

if __name__ == "__main__":
    unittest.main()
