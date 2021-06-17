from human import Human
from ai import AI
class Game:
    def __init__(self):
        self.player_one = Human()
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
            elif response == "1":
                self.player_two = AI()
            else:
                print("please enter 1 or 2")
                self.choose_game_mode()
    def play_round(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("Its a tie, play again!")
            print()
            self.best_of_three()
        elif (self.player_one.chosen_gesture, self.player_two.chosen_gesture) in self.win_conditions:
            print("Player one is the winner!")
            print()
            self.player_one.score += 1
            self.best_of_three()
        else:
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
            print("next round, first player to win twice is the winner!")
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




