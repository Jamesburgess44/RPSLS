from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None


    def run_game(self):
        self.welcome()
        self.choose_game_mode()
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()


    def welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        print()
        print("each match will be best of three games")
        print("Use the nubmer keys to enter your selection")
        print()

    def choose_game_mode(self):
            print("How many players? 1 or 2")
            response = input()
            if response == 2:
                self.player_two = Human()
            else:
                self.player_two = AI()


        # Game Rounds
        # Player one chooses gesture
        # Player two chooses gesture
        # Determine winner of round, winner's score increases
        # Loop to continue gameplay until best of three occurs

        # End Game
        # Display winner of game
        # Prompt to play again? - Not MVP
            pass


