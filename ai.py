from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__()
        self.score = 0


    def choose_gesture(self):
        self.chosen_gesture = str(random.randint(0,4))
        print(f"Ai has picked {self.chosen_gesture}")

