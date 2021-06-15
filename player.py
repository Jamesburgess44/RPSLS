class Player:
    def __init__(self):
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "Spock"]

    def choose_gesture(self):
        print("Override this method")
        pass