from game_of_greed.game_logic import GameLogic, Banker
# import Counter
import sys

class Game():

    def __init__(self, num_of_rounds=20):
        self.banker = Banker()
        self.num_of_rounds = num_of_rounds
        self.round_num = 0
        self.roller = None
        self.score = 0

    def validate_keepers(roll, keepers):
        roll_counter = Counter(roll)
        keepers_counter = Counter(keepers)
        return roll_counter - keepers_counter

    def game_start_old(self):
        # round = 1 (( we should use self.round_num))
        num_of_dice = 6
        dice_roll = GameLogic.roll_dice(num_of_dice)
        dice_roll_string = " "
        dice_string = " ".join([str(i) for i in dice_roll])
        # points = 0 (( we should use self.score ))
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_input = input("> ")
        if user_input == "n":
            print("OK. Maybe another time")
        if user_input == "y":
            self.start()
        return self.score

    def play(self, roller=None):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_response = input("> ")

        if user_response == 'n':
            print("OK. Maybe another time")

        if user_response == 'y':
            num_of_dice = 6
            self.round_num += 1
            self.roller = roller or GameLogic.roll_dice
            dice_roll = roller(num_of_dice)
            dice_string = " ".join([str(i) for i in dice_roll])
            print(f"Starting round {self.round_num}")
            print(f"Rolling {num_of_dice} dice...")
            print(f"*** {dice_string} ***")
            print("Enter dice to keep, or (q)uit:")
            user_response = input("> ")

            # quit
            if user_response == "q":
                print(f"Thanks for playing. You earned {self.banker.banked} points")

            # this is for keeping dice
            # 5 5 1 2 3 4
            # ex-> > 551
            # -> take the length of user imput and subtract that from number of dice -> remain dice
            if user_response.isnumeric():
                #use calculate score in GameLogic(). this function ist expecting dice
                dice_values = tuple(int(char) for char in user_response)
                score = GameLogic.calculate_score(dice_values)
                self.banker.shelf(score)
                # num_of_dice -= len(user_response)
                print("You have 50 unbanked points and 5 dice remaining")
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

                print(f"You banked {self.banker.bank()} points in round {self.round_num}")
                print(f"Total score is {self.banker.banked} points")
                print(f"Starting round {self.round_num}")
                print(f"Rolling {num_of_dice} dice...")
                print(f"*** {dice_string} ***")
                print("Enter dice to keep, or (q)uit:")
                user_response = input("> ")

                if user_response == "q":
                    print(f"Thanks for playing. You earned {self.banker.banked} points")

                if user_response.isnumeric():
                    self.round_num += 1
                    #use calculate score in GameLogic(). this function ist expecting dice
                    dice_values = tuple(int(char) for char in user_response)
                    score = GameLogic.calculate_score(dice_values)
                    self.banker.shelf(score)
                    # num_of_dice -= len(user_response)
                    print(f"You have {self.banker.bank()} unbanked points and {num_of_dice} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:") 
                    user_response = input("> ")


    # def play_old(self, roller=None):
    #     self.roller = roller or GameLogic.roll_dice

    #     while self.round_num <= self.num_of_rounds:
    
    #         print(f"Starting round {self.round_num}") 
    #         print(f"Rolling {num_of_dice} dice...") 
    #         print(f"*** {dice_string} ***")
    #         print("Enter dice to keep, or (q)uit:")
    #         user_response = input("> ")
    #         print("You have 350 unbanked points and 2 dice remaining")
    #         print("(r)oll again, (b)ank your points or (q)uit:")
    #         user_response = input("> ")

    #         # I'm forgetting what this does
    #         if user_response.isnumeric():
    #             #use calculate score in GameLogic(). this function ist expecting dice
    #             dice_values = tuple(int(char) for char in user_response)
    #             score = GameLogic.calculate_score(dice_values)
    #             self.banker.shelf(score)
    #             num_of_dice -= len(user_response)
                
    #             print("(r)oll again, (b)ank your points or (q)uit:") 
    #             user_response = input("> ")

    #         # I think this one is done
    #         if user_response == "b":
    #             banked = self.banker.bank()
    #             print(f'You banked {banked} points in round {self.round_num}')
    #             print(f'Total score is {self.banker.balance} points')

    #         if user_response == "r":
    #             # Do a dice roll
    #             # if 0 -> zlich
    #             # if user_input q -> quit
    #             # otherwise if, user input will be equal to the number of dice to subtract ((this is where we will need to put the checker for cheat stuff when we get there))
    #             # ex: for char in user_input:
    #             #       if int(char) in dice_roll:
    #             #           dice_count -= 1

    #             roll = self.dice_roll(num_of_dice)
    #             dice_roll_string = " ".join([str(i) for i in roll])
    #             print(f"Rolling {num_of_dice} dice...") 
    #             print(f"*** {dice_roll_string} ***")

    #             # zilch
    #             if score == 0:
    #                 print("Zilch")
    #                 return

    #             # prints when done with the ifs
    #             print('(r)oll again, (b)ank your points or (q)uit:')
    #             user_response = input('> ')
    #             self.banker.bank()
    #             print(f'You banked {self.banker.balance} points in round 1')
    #             print(f'Total score is {self.banker.balance} points')
                


    #         # add to next round when after while
    #         self.round_num += 1