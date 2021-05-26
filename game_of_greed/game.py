from game_of_greed.game_logic import GameLogic

class Game():
    def __init__(self, round):
        self.round = 1


    def play(self, roller=None): ##ADDED None as default
        """Entry point for playing of declining game
        
        Args:
            roller (function, optional):
            Allows passing in a custom dice roller function.
            Defaults to None
            """
        # self.roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_input = input("> ")

        if user_input == "n":
            print("OK. Maybe another time")

        elif user_input == "y":
            round = 1
            points = 0 #self.banker.balance

            num_of_dice = 6 
            dice_roll = GameLogic.roll_dice(num_of_dice) # USE self.roller???
            dice_roll_string = " ".join([str(i) for i in dice_roll])
            # dice_string = dice_roll_string.join([str(i) for i in dice_roll])

            #Starting round 1
            print(f"Starting round {round}") 
            print(f"Rolling {num_of_dice} dice...") # USE ROLLER????
            print(f"*** {dice_roll_string} ***")
            print("Enter dice to keep, or (q)uit:")
            user_quit_answer = input("> ")
            print(f"Thanks for playing. You earned {points} points") 
            # print(f"Thanks for playing. You earned {self.banker.balance} points")

            print("(r)oll again, (b)ank your points or (q)uit:")
            user_points_answer = input("> ")

        if user_points_answer is int: # or if user_points_answer.isnumeric():
            #use calculate score in GameLogic(). this function ist expecting dice
            dice_values = tuple(int(char) for char in user_points_answer)
            score = GameLogic.calculate_score(dice_values)
            self.banker.shelf(score)
            # num_of_dice -= len(user_points_answer)

            print("You have 50 unbanked points and 5 dice remaining") 
            # print(f"You have {self.banker.shelved} unbanked points and {num_of_dice} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:") 
            user_points_answer = input("> ")
            

        if user_points_answer == "r":
            pass

        if user_points_answer == "b":
            # self.banker.bank()
            # print(f"You banked {self.banker.balance} points in round {round}")
            print("You banked 50 points in round 1") # dynamic shelved pionts count (banker function?)
            # print(f"Total score is {self.banker.balance} points") 
            print("Total score is 50 points") # dynamic point counter (banker function?)
            print("Starting round 2") ## Round counter here

        if user_quit_answer == "q" or user_points_answer == "q":
            print(f"Thanks for playing. You earned 50 points")
            
        else:
            print("Enter valid character")
            user_points_answer = input("> ") # I am pretty sure we need this.
