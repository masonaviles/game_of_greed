from game_of_greed.game_logic import GameLogic

class Game():
    # def __init__(self, round):
    #     self.round = 1


    def play(self, roller):
        round = 1
        num_of_dice = 6
        dice_roll = GameLogic.roll_dice(num_of_dice)
        dice_roll_string = " "
        dice_string = dice_roll_string.join([str(i) for i in dice_roll])
        points = 0
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_input = input("> ")
        if user_input == "n":
            print("OK. Maybe another time")
        elif user_input == "y":
            print(f"Starting round {round}") 
            print(f"Rolling {num_of_dice} dice...")
            print(f"*** {dice_string} ***")
            print("Enter dice to keep, or (q)uit:")
            user_quit_answer = input("> ")
            print("You have 50 unbanked points and 5 dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            user_points_answer = input("> ")


            if user_points_answer == "r":
                pass
            elif user_points_answer == "b":
                print("You banked 50 points in round 1") # dynamic shelved pionts count (banker function?)
                print("Total score is 50 points") # dynamic point counter (banker function?)
                print("Starting round 2") ## Round counter here

            elif user_quit_answer == "q" or user_points_answer == "q":
                print(f"Thanks for playing. You earned 50 points")
            

