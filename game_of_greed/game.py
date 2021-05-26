
class Game():
    # def __init__(self, play):
    #     self.play = play

    def play(self, roller):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        user_input = input("> ")
        if user_input == "n":
            print("OK. Maybe another time")
            
