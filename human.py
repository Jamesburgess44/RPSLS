from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        gesture_index = 0
        for gesture in self.gestures:
            print(f"Choose {gesture_index} for {gesture}.")
            gesture_index += 1
        human_input = input("Choose your gesture.")
        self.chosen_gesture = int(human_input)
