import random
from card import Card

class Deck:
    def __init__(self):
        colors = ["Rood", "Groen", "Blauw", "Geel"]

        # Maakt een lijst van kaartwaardes:
        values = list(map(str, range(0, 10))) + ["+2", "Skip", "Reverse"]
        # Maakt de normale gekleurde kaarten:
        self.cards = [Card(c, v) for c in colors for v in values] * 2
        # Maakt de speciale kaarten:
        self.cards += [Card("Zwart", v) for v in ["+4", "Wild"] * 4]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self, discard_pile=None):
        if not self.cards:
            if discard_pile and len(discard_pile) > 1:
                top_card = discard_pile[-1]
                # Pak alle kaarten behalve de bovenste van de aflegstapel
                self.cards = discard_pile[:-1]
                discard_pile[:] = [top_card]
                self.shuffle()
            else:
                raise IndexError("Geen kaarten meer beschikbaar in de stapel of aflegstapel.")
        return self.cards.pop()

    def draw_cards(self, n):
        return [self.draw_card() for _ in range(n)]
