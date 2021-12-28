from time import sleep
from human import Human
from ai import AI
class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.win_conditions = (('0', '2'), ('2', '1'), ('1', '0'), ('0', '3'), ('3', '4'), ('4', '2'),
                               ('2', '3'), ('3', '1'),('1', '4'), ('4', '0'))

    def run_game(self):
        self.welcome()
        self.choose_game_mode()
        self.play_round()
        self.best_of_three()
        self.play_again()

    def welcome(self):
        print()
        print()
        print()
        print()
        print()
        print()
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        print()
        print("each match will be best of three games")
        print("Use the nubmer keys to enter your selection")
        print()
        print()
        sleep(.5)
        print("Scissors cut Paper")
        sleep(.5)
        print("Paper covers Rock")
        sleep(.5)
        print("Rock crushes Lizard")
        sleep(.5)
        print("Lizard poisons Spock")
        sleep(.5)
        print("Spock smashes Scissors")
        sleep(.5)
        print("Scissors decapitates Lizard")
        sleep(.5)
        print("Lizard eats Paper")
        sleep(.5)
        print("Paper disproves Spock")
        sleep(.5)
        print("Spock vaporizes Rock")
        sleep(.5)
        print("Rock crushes Scissors")
        print()

    def choose_game_mode(self):
            print("How many players? 1, 2 or 3 for a surprise")
            response = input()
            if response == "2":
                self.player_one = Human()
                self.player_two = Human()
            elif response == "1":
                self.player_one = Human()
                self.player_two = AI("AI")
            elif response == "3":
                self.player_one = AI("AI ONE")
                self.player_two = AI("AI TWO")
            else:
                print("please enter 1 or 2")
                self.choose_game_mode()

    def play_round(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            sleep(2)
            print()
            print("Its a tie, play again!")
            print()
            self.best_of_three()
        elif (self.player_one.chosen_gesture, self.player_two.chosen_gesture) in self.win_conditions:
            sleep(2)
            print()
            print("Player one is the winner!")
            print()
            self.player_one.score += 1
            self.best_of_three()
        else:
            sleep(2)
            print()
            print("Player two is the winner!")
            print()
            self.player_two.score += 1
            self.best_of_three()

    def best_of_three(self):
        if self.player_one.score == 2:
            print("Player 1 wins best of 3")
            print()
            self.play_again()
        elif self.player_two.score == 2:
            print("Player 2 wins best of 3!")
            print()
            self.play_again()
        else:
            sleep(1.5)
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("Next round, first player to win twice is the winner!")
            print()
            self.play_round()

    def play_again(self):
        while True:
            replay_answer = input("Do you want to play again?(y/n)")
            if replay_answer == "y":
                self.clear_score()
                break
            elif replay_answer == "n":
                print("Thank you for playing!")
                break
            else:
                print("That is not a valid response. Please try again.")

    def clear_score(self):
        self.player_one.score = 0
        self.player_two.score = 0
        self.run_game()




