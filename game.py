from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.win_conditions = ((0, 2), (2, 1), (1, 0), (0, 3), (3, 4), (4, 2), (2, 3), (3, 1), (1, 4), (4, 0))



    def run_game(self):
        self.welcome()
        self.choose_game_mode()
        self.choose_winner()


    def welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        print()
        print("each match will be best of three games")
        print("Use the nubmer keys to enter your selection")
        print()

    def choose_game_mode(self):
            print("How many players? 1 or 2")
            response = input()
            if response == "2":
                self.player_two = Human()
            else:
                self.player_two = AI()
    def choose_winner(self):
        if (self.player_one.choose_gesture()) == (self.player_two.choose_gesture()):
            print("Its a tie, play again!")
        elif ((self.player_one.chosen_gesture),(self.player_two.chosen_gesture)) in self.win_conditions():
            print("Player one is the winner!")
        else:
            print("Player two is the winner!")
        # Determine winner of round, winner's score increases
        # Loop to continue gameplay until best of three occurs

        # End Game
        # Display winner of game
        # Prompt to play again? - Not MVP



