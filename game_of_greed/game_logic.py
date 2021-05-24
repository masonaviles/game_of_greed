import re, random

class GameLogic():

    dice_roll = random.randint(1, 6)

    @staticmethod
    def calculate_score(self): # static method
        pass

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