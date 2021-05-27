from game_of_greed.game_logic import GameLogic, Banker

class Game():
    def __init__(self, round=1, num_of_rounds=20):
        self.round = round
        self.num_of_rounds = num_of_rounds
        self.banker = Banker()


    def play(self, roller=None): ##ADDED None as default
        """Entry point for playing of declining game
        
        Args:
            roller (function, optional):
            Allows passing in a custom dice roller function.
            Defaults to None
            """

        self.dice_roll = roller or GameLogic.roll_dice() 
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_input = input("> ")

        if user_input == "n":
            print("OK. Maybe another time")

        elif user_input == "y":
            self.start_game()

    def start_round(self, round):
        pass





    def start_game(self):
        self.round = 1
        while self.round <= self.num_of_rounds:
            self.start_round(self.round)
            self.round += 1
            # add total score to loop


        
        num_of_dice = 6
        roll = self.dice_roll(num_of_dice)
        dice_roll_string = " ".join([str(i) for i in roll])
        print(f"Starting round {round}") 
        print(f"Rolling {num_of_dice} dice...") 
        print(f"*** {dice_roll_string} ***")
        print("Enter dice to keep, or (q)uit:")
        user_points_answer = input("> ")
        print("You have 350 unbanked points and 2 dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_rbq_answer = input("> ")

    #while loop here
        if user_points_answer.isnumeric():
            #use calculate score in GameLogic(). this function ist expecting dice
            dice_values = tuple(int(char) for char in user_points_answer)
            score = GameLogic.calculate_score(dice_values)
            self.banker.shelf(score)
            num_of_dice -= len(user_points_answer)
            
            print("(r)oll again, (b)ank your points or (q)uit:") 
            user_points_answer = input("> ")
            

        if user_points_answer == "b":
            # self.banker.bank()
            # print(f"You banked {self.banker.balance} points in round {round}")
            print("You banked 350 points in round 1") 
            # print(f"Total score is {self.banker.balance} points") 
            print("Total score is 350 points") # dynamic point counter (banker function?)

            print("Starting round 2") ## Round counter here
            print(f"Rolling {num_of_dice} dice...")
            print("*** 6 4 5 2 3 1 ***")
            print("Enter dice to keep, or (q)uit:")
            input("> ")
            print(f"You have {self.banker.shelved} unbanked points and {num_of_dice} dice remaining")
            
        if user_points_answer == "r":
            print(f"You have {self.banker.shelved} unbanked points and {num_of_dice} dice remaining")
            print(f"Starting round {round}") 
            print(f"Rolling {num_of_dice} dice...") 
            print(f"*** {dice_roll_string} ***")
            print("Enter dice to keep, or (q)uit:")
            user_quit_answer = input("> ")
            print(f"Thanks for playing. You earned {self.banker.banked} points")

    # quit function
        # if user_rbq_answer == "q" or user_points_answer == "q":
            # print(f"Thanks for playing. You earned {self.banker.banked} points")


            
            
        else:
            # print("Enter valid character")
            user_points_answer = input("> ") 


    # def quit_game_function():
    #     if user_rbq_answer == "q" or user_points_answer == "q":
    #     print(f"Thanks for playing. You earned {self.banker.banked} points")
    #     break
    #     start_game()
    # # Thought process is I need to restart the game right here after the user exits?

        