from deck import Deck
from player import Player

class Game:
    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.discard_pile = []
        self.current_player_index = 0

    def start(self):
        num_players = int(input("Hoeveel spelers? "))
        self.players = [Player(f"Speler {i+1}") for i in range(num_players)]
        self.deck.shuffle()

        for player in self.players:
            player.hand = self.deck.draw_cards(7)

        self.discard_pile.append(self.deck.draw_card())

        while not self.is_game_over():
            self.play_turn()

        self.show_winner()

    def play_turn(self):
        player = self.players[self.current_player_index]
        top_card = self.discard_pile[-1]

        print(f"\n{player.name} is aan de beurt.")
        print(f"Open kaart: {top_card}")
        print(f"Jouw hand: {player.hand}")

        card = player.choose_card(top_card)
        if card:
            print(f"{player.name} speelt: {card}")
            self.discard_pile.append(card)
        else:
            drawn_card = self.deck.draw_card(self.discard_pile)
            if drawn_card.can_be_played_on(top_card):
                print(f"{player.name} trok en speelde: {drawn_card}")
                self.discard_pile.append(drawn_card)
            else:
                print(f"{player.name} trok {drawn_card} en slaat beurt over.")

        if player.has_uno():
            print(f"{player.name} roept: UNO!")

        if player.has_won():
            print("--------------------------------------------")
            print(f"{player.name} heeft gewonnen!")

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def is_game_over(self):
        return any(player.has_won() for player in self.players)

    def show_winner(self):
        for player in self.players:
            if player.has_won():
                print(f"Winnaar: {player.name}")
