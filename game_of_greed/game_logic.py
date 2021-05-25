import re, random, collections

class GameLogic():

    @staticmethod
    def roll_dice(num_of_dice): # static method
        values = []
        for i in range(num_of_dice):
            values.append(random.randint(1,6))
        return tuple(values)

        # if num_of_dice == 1:
        #     values = []
        #     dice_roll = random.randint(1, 6)
        #     values.append(dice_roll)
        #     return tuple(values)
        # elif num_of_dice == 2:
        #     values = []
        #     for num in range(0, num_of_dice):
        #         dice_roll = random.randint(1, 6)
        #         values.append(dice_roll)
        #     return tuple(values)
        # elif num_of_dice == 3:
        #     values = []
        #     for num in range(0, num_of_dice):
        #         dice_roll = random.randint(1, 6)
        #         values.append(dice_roll)
        #     return tuple(values)
        # elif num_of_dice == 4:
        #     values = []
        #     for num in range(0, num_of_dice):
        #         dice_roll = random.randint(1, 6)
        #         values.append(dice_roll)
        #     return tuple(values)
        # elif num_of_dice == 5:
        #     values = []
        #     for num in range(0, num_of_dice):
        #         dice_roll = random.randint(1, 6)
        #         values.append(dice_roll)
        #     return tuple(values)
        # elif num_of_dice == 6:
        #     values = []
        #     for num in range(0, num_of_dice):
        #         dice_roll = random.randint(1, 6)
        #         values.append(dice_roll)
        #     return tuple(values)
        # else:
        #     return -1

    @staticmethod
    def calculate_score(tuple_of_dice_roll): # static method
        score = 0
        dice_roll = tuple_of_dice_roll
        # A Counter is a container that keeps track of how many times equivalent values are added.
        # most_common(): Return a list of the n most common elements and their counts from the most common to the least. If n is omitted or None, returns all elements in the counter.
        counter = collections.Counter(tuple_of_dice_roll).most_common()

         #Empty
        if len(dice_roll) == 0:
            score += 0
            return score

        # straights: 6 of the same number
        if len(counter) == 6:
            score += 1500
            return score

        # pairs, only (1,1) and (5,5) are scoring
        if len(counter) == 2:
            if dice_roll == (1,1):
                score += 200
                return score
            
            if dice_roll == (5,5):
                score += 100
                return score
            
            else:
                score += 0
                return score

        # singles, only 1 and 5 are scoring
        if len(counter) == 1:
            if dice_roll == (1,):
                score += 100
                return score
            
            if dice_roll == (5,):
                score += 50
                return score
            
            else:
                score += 0
                return score


        # if tuple_of_dice_roll == (5,):
        #     return 50
        # elif tuple_of_dice_roll == (1, 1):
        #     return 200
        # elif tuple_of_dice_roll == (1, 5):
        #     return 150
        # elif tuple_of_dice_roll == (2,):
        #     return 0
        # elif tuple_of_dice_roll == (5, 5, 5, 2, 2, 3):
        #     return 500
        # elif tuple_of_dice_roll == (1,) or tuple_of_dice_roll == (5,5):
        #     return 100
        # elif tuple_of_dice_roll == (1, 1, 1, 2, 3, 4):
        #     return 1000
        # elif tuple_of_dice_roll == (1, 1, 1, 5):
        #     return 1050
        # elif tuple_of_dice_roll == (1, 6, 3, 2, 5, 4):
        #     return 1500
        # elif tuple_of_dice_roll == (2,2,2):
        #     return 200
        # elif tuple_of_dice_roll == (2,2,2,2):
        #     return 400
        # elif tuple_of_dice_roll == (2,2,2,2,2):
        #     return 600
        # elif tuple_of_dice_roll == (2,2,2,2,2,2):
        #     return 800
        # elif tuple_of_dice_roll == (1,1,1,1,1,1):
        #     return 4000
        


class Banker():

    def __init__(self, value):
        self.value = value

    def shelf(self): # instance method
        pass

    def bank(self): # instance method
        pass

    def clear_shelf(): # instance method
        pass