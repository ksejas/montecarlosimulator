
import pandas as pd
import numpy as np

from Die_Class import Die

class Game:
    '''The Game Class 
    A game consists of rolling one or more dice of the same kind one or more times. '''

    def __init__(self, die_object_list):
        '''The die_object_list is a list of already instantiated similar Die objects. '''
        self.die_object_list=die_object_list


    def play(self, number_of_rolls:int):
        '''The . '''
        self.number_of_rolls=number_of_rolls
        self.result_of_play = pd.DataFrame()
        self.result_of_play.index.rename('roll_num_index', inplace=True)
        Dices=Die(self.die_object_list)
        for r in range(0, len(self.die_object_list)):
            Dice = self.die_object_list[r]
            self.result_of_play[r] = Dices.roll_die(number_of_rolls) 
    def result_of_recent_play(self, shape_type):
        self.shape_type=shape_type
        if self.shape_type=="wide":
            return self.result_of_play
        elif self.shape_type=="narrow":
            result_of_play_reset_index = self.result_of_play.reset_index()
            self.result_of_play_t = pd.wide_to_long(result_of_play_reset_index, "dice_", i="roll_num_index", j="dice_num")
            self.result_of_play_t.set_index('roll_num_index', 'dice_num')
            return self.result_of_play_t
        else:
            raise ValueError("User passed an invalid option for the shape type of the dataframe. A shape type of wide or narrow was not passed.")


