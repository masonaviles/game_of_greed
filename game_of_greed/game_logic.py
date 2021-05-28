import re, random
from collections import Counter

scoresheet = {
  '1': {'1': 100, '2': 200, '3': 1000, '4': 2000, '5': 3000, '6': 4000},
  '2': {'1': 0, '2': 0, '3': 200, '4': 400, '5': 600, '6': 800},
  '3': {'1': 0, '2': 0, '3': 300, '4': 600, '5': 900, '6': 1200},
  '4': {'1': 0, '2': 0, '3': 400, '4': 800,'5': 1200, '6': 1600},
  '5': {'1': 50, '2': 100, '3': 500, '4': 1000,'5': 1500, '6': 2000},
  '6': {'1': 0, '2': 0, '3': 600, '4': 1200,'5': 1800, '6': 2400},
  'special': {'straight': 1500, 'three pair': 1500}
}

class GameLogic():

    @staticmethod
    def roll_dice(num_of_dice):
        values = []
        for i in range(num_of_dice):
            values.append(random.randint(1,6))
        return tuple(values)

    @staticmethod
    def calculate_score(dice): # (2,2)
        counter = 0
        occurrences = {} # { '2' : 2 }
        for num in dice: # (2,2)
            times_rolled = dice.count(num) 
            occurrences[num] = times_rolled
        
        if sorted(dice) == [1,2,3,4,5,6]:
            counter += scoresheet['special']['straight']
            return counter

        keys = list(occurrences.keys())
        if len(keys) == 3:
            if (occurrences[keys[0]] == 2) and (occurrences[keys[1]] == 2) and (occurrences[keys[2]] == 2):
                counter += scoresheet['special']['three pair']
                return counter

        for num in occurrences:
            counter += scoresheet[str(num)][str(occurrences[num])]

        return counter

    @staticmethod
    # def validate_keepers(roll, keepers):
    #     roll_counter = Counter(roll)
    #     keepers_counter = Counter(keepers)
    #     return roll_counter - keepers_counter
    
    @staticmethod
    def validate_keepers(roll, keepers):
        for num in keepers:
            if str(num).isnumeric():
                if keepers.count(num) > roll.count(int(num)):
                    return False
        return True


class Banker():

    def __init__(self):
        self.banked = 0
        self.shelved = 0
        
    def shelf(self, round_score): 
        self.shelved += round_score
        return self.shelved
        
    def clear_shelf(self): 
        self.shelved = 0
        return self.shelved

    def bank(self): 
        temp_total = self.shelved
        self.banked += temp_total
        self.shelved = 0
        return temp_total


