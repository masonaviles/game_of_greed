from game_of_greed.game_logic import GameLogic, Banker
import sys

class Game():

    def __init__(self, num_of_rounds=20):
        self.banker = Banker()
        self.num_of_rounds = num_of_rounds
        self.round_num = 0
        self.roller = None
        self.score = 0

    def play(self, roller=None):
        self.roller = roller or GameLogic.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_response = input("> ")

        if user_response == 'n':
            print("OK. Maybe another time")

        if user_response == 'y':
            self.start_game()

    def start_game(self):
        num_of_dice = 6
        # self.round_num = 1
        # self.round_num += 1
        while self.round_num <= self.num_of_rounds:
            # self.round_num += 1
            self.start_round()
            # print(f"Thanks for playing. You earned {self.banker.banked} points")
        self.end_game()

    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.banked} points")
        sys.exit()

    def roll_dice(self, num_dice):
        print(f"Rolling {num_dice} dice...")
        dice_roll = self.roller(num_dice)
        dice_string = " ".join([str(i) for i in dice_roll])
        print(f"*** {dice_string} ***")
        return dice_roll


    def gather_keepers(self, roll, users_keepers):
        while not GameLogic.validate_keepers(roll, users_keepers):
            print("CHEATER, try again")
            print("Enter dice to keep, or (q)uit:")
            user_response = input("> ")
            if user_response.isnumeric():
                self.start_round()
            converted_keepers = self.convert_keepers(user_response)
        return converted_keepers
    
    # user input string (user_keepers) to int so we can score it 
    # list comprehension, for each number in the user_keepers how do you change int(blah)
    def convert_keepers(self, users_keepers):
        users_keepers_list = [int(num) for num in users_keepers if num.isdigit()]
        return users_keepers_list


    # start_round(num_of_dice=(int))
    def start_round(self, num_of_dice=6):
        self.round_num += 1
        print(f"Starting round {self.round_num}")
        
        while True:
            self.roll_dice(num_of_dice) # -> return dice
            # how are we gonna handle keepers
            print("Enter dice to keep, or (q)uit:")
            user_response = input("> ")

            if user_response == "q":
                self.end_game()

            # this is for keeping dice
            # 5 5 1 2 3 4
            # ex-> > 551
            # -> take the length of user imput and subtract that from number of dice -> remain dice
            if user_response.isnumeric():
                #use calculate score in GameLogic(). this function ist expecting dice
                dice_values = tuple(int(char) for char in user_response)

                remaining_dice = 6 - len(dice_values)

                score = GameLogic.calculate_score(dice_values)
                self.banker.shelf(score)
                # num_of_dice -= len(user_response)
                print(f"You have {self.banker.shelved} unbanked points and {remaining_dice} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:") 
                user_response = input("> ")

            # bank
            if user_response == "b":
                # add to next round when after while

                # dice_values = tuple(int(char) for char in user_response)
                # score = GameLogic.calculate_score(dice_values)
                # self.banker.shelf(score)
                # num_of_dice -= len(user_response)

                #self.round_num += 1

                print(f"You banked {self.banker.shelved} points in round {self.round_num}")
                print(f"Total score is {self.banker.bank()} points")
                break


            if user_response == "q":
                self.end_game()

