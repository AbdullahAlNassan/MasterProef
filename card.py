class Card:
    #Constructor (de __init__-functie): dit is de functie die een kaart maakt met een kleur en een waarde.
    def __init__(self, color, value):
        self.color = color
        self.value = value

    #Deze methode zorgt ervoor dat een kaart netjes wordt weergegeven als tekst
    def __repr__(self):
        return f"{self.color} {self.value}"
    
    # Bepaalt of deze kaart op een andere kaart gespeeld kan worden.
    def can_be_played_on(self, other_card):
        return self.color == other_card.color or self.value == other_card.value
    
    #Controleert of de kaart een pestkaart is – dit zijn kaarten met speciale effecten.
    def is_pest(self):
        return self.value in ["+2", "+4", "Skip", "Reverse", "Wild"]