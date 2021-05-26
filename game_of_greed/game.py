
class Game():
    # def __init__(self, round):
    #     self.round = 1


    def play(self, roller):
        round = 1
        num_of_dice = 6
        dice_roll = "4 4 5 2 3 1"
        points = 0
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_input = input("> ")
        if user_input == "n":
            print("OK. Maybe another time")
        elif user_input == "y":
            print(f"Starting round {round}") 
            print(f"Rolling {num_of_dice} dice...")
            print(f"*** {dice_roll} ***")
            print("Enter dice to keep, or (q)uit:")
            user_quit_answer = input("> ")
            if user_quit_answer == "q":
                print(f"Thanks for playing. You earned {points} points")

