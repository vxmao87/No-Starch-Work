from random import randint

class Die:
    """
    A class representing dice.
    """
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(f"{randint(1, self.sides + 1)} for a dice with {self.sides} sides")