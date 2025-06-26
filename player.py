class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def choose_card(self, top_card):
        for card in self.hand:
            if card.is_pest() and card.can_be_played_on(top_card):
                self.hand.remove(card)
                return card
        playable = [c for c in self.hand if c.can_be_played_on(top_card)]
        if playable:
            best = max(playable, key=lambda c: c.value)
            self.hand.remove(best)
            return best
        return None

    def has_uno(self):
        return len(self.hand) == 1

    def has_won(self):
        return len(self.hand) == 0
