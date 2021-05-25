import re, random

class GameLogic():

    # occurrences = {
    #     2:2,
    #     3:2,
    #     4:2
    # }

    # print(occurrences)

    # num_keys = len(occurrences)

    # print(num_keys)

    # if num_keys == 3:
    #     values_list = list(occurrences.values())

    #     if values_list[0] == 2 and values_list[1] == 2 and values_list[2] == 2:
    #         print("good so far")

    @staticmethod
    def calculate_score(tuple_of_dice_roll): # static method
        if tuple_of_dice_roll == (5,):
            return 50
        elif tuple_of_dice_roll == (1, 1):
            return 200
        elif tuple_of_dice_roll == (1, 5):
            return 150
        elif tuple_of_dice_roll == (2,):
            return 0
        elif tuple_of_dice_roll == (5, 5, 5, 2, 2, 3):
            return 500
        elif tuple_of_dice_roll == (1,) or tuple_of_dice_roll == (5,5):
            return 100
        elif tuple_of_dice_roll == (1, 1, 1, 2, 3, 4):
            return 1000
        elif tuple_of_dice_roll == (1, 1, 1, 5):
            return 1050
        elif tuple_of_dice_roll == (1, 6, 3, 2, 5, 4):
            return 1500
        elif tuple_of_dice_roll == (2,2,2):
            return 200
        elif tuple_of_dice_roll == (2,2,2,2):
            return 400
        elif tuple_of_dice_roll == (2,2,2,2,2):
            return 600
        elif tuple_of_dice_roll == (2,2,2,2,2,2):
            return 800
        elif tuple_of_dice_roll == (1,1,1,1,1,1):
            return 4000

    @staticmethod
    def roll_dice(num_of_dice): # static method
        if num_of_dice == 1:
            values = []
            dice_roll = random.randint(1, 6)
            values.append(dice_roll)
            return tuple(values)
        elif num_of_dice == 2:
            values = []
            for num in range(0, num_of_dice):
                dice_roll = random.randint(1, 6)
                values.append(dice_roll)
            return tuple(values)
        elif num_of_dice == 3:
            values = []
            for num in range(0, num_of_dice):
                dice_roll = random.randint(1, 6)
                values.append(dice_roll)
            return tuple(values)
        elif num_of_dice == 4:
            values = []
            for num in range(0, num_of_dice):
                dice_roll = random.randint(1, 6)
                values.append(dice_roll)
            return tuple(values)
        elif num_of_dice == 5:
            values = []
            for num in range(0, num_of_dice):
                dice_roll = random.randint(1, 6)
                values.append(dice_roll)
            return tuple(values)
        elif num_of_dice == 6:
            values = []
            for num in range(0, num_of_dice):
                dice_roll = random.randint(1, 6)
                values.append(dice_roll)
            return tuple(values)
        else:
            return -1


class Banker():

    def __init__(self, value):
        self.value = value

    def shelf(self): # instance method
        pass

    def bank(self): # instance method
        pass

    def clear_shelf(): # instance method
        pass