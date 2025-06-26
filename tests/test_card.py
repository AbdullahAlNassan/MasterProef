import unittest
from card import Card

class TestCard(unittest.TestCase):

    def test_repr(self):
        card = Card("Rood", "5")
        self.assertEqual(repr(card), "Rood 5")

    def test_can_be_played_on_same_color(self):
        c1 = Card("Rood", "5")
        c2 = Card("Rood", "9")
        self.assertTrue(c1.can_be_played_on(c2))

    def test_can_be_played_on_same_value(self):
        c1 = Card("Groen", "5")
        c2 = Card("Rood", "5")
        self.assertTrue(c1.can_be_played_on(c2))

    def test_is_pest_true(self):
        pest = Card("Blauw", "+2")
        self.assertTrue(pest.is_pest())

    def test_is_pest_false(self):
        normaal = Card("Geel", "4")
        self.assertFalse(normaal.is_pest())

if __name__ == "__main__":
    unittest.main()
