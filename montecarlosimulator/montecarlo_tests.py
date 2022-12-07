import unittest
from montecarlo import *

import pandas as pd
import numpy as np


faces_array = np.array([1,2,3,4,5,6], dtype = int)
class DieTestSuite(unittest.TestCase):
    
    def test_change_weight_of_a_single_side(self): 
        Die1=Die(faces_array)
        Die1.change_weight_of_a_single_side(2.0, 4.0)
        test_face_value=2.0
        test_new_weight=4.0
        row_num=Die1.faces_with_weights[Die1.faces_with_weights['faces']==test_face_value].index[0]
        testvalue=Die1.faces_with_weights.iloc[row_num, 0]==test_new_weight
        message = "Test value is not true. The weight has not been updated to be the new specified weight."
        self.assertTrue(testvalue, message)

    def test_roll_die(self):
        Die1=Die(faces_array)
        Die1.roll_die(1)
        testvalue=len(Die1.roll_list)==1
        message="Test value is not true. The size of the random sample (roll_list) is not equal to the number of specified rolls."
        self.assertTrue(testvalue, message)

    def test_view_faces_weights(self): 
        Die1=Die(faces_array)
        testvalue=Die1.faces_with_weights.empty
        message="Test value is not false. The faces_with_weights dataframe that specifies the die faces with its corresponding weights is empty."
        self.assertFalse(testvalue, message)


class GameTestSuite(unittest.TestCase):

    def test_play(self):
        Die1 = Die(faces_array)
        two_fair_dice = []
        two_fair_dice.append(Die1)
        two_fair_dice.append(Die1)
        Game1 = Game(two_fair_dice)
        Game1.play(5)
        Game1.result_of_recent_play('wide')
        testvalue = len(Game1.result_of_play)==5
        message = "The number of observations/rolls in result_of_play does not match the user specified number of rolls."
        self.assertTrue(testvalue, message)

    def test_result_of_recent_play(self):
        fair_dice = Die(faces_array)
        two_fair_dice = []
        for i in range(0,2):
            two_fair_dice.append(fair_dice)
        Game1=Game(two_fair_dice)
        Game1.play(4)
        Game1.result_of_recent_play(shape_type="wide")
        Game2=Game(two_fair_dice)
        Game2.play(4)
        Game2.result_of_recent_play(shape_type="narrow")
        testvalue1 = len(Game2.result_of_play_t.columns) < len(Game1.result_of_play.columns)
        testvalue2 = len(Game2.result_of_play_t) > len(Game1.result_of_play)
        if testvalue1 == True: 
            if testvalue2 == True:
                testvalue3 = True
        else:
            testvalue3 = False
        message = "The test value is not true. The size of the dataframe dimensions when comparing the narrow with wide form do not follow the correct pattern."
        self.assertTrue(testvalue3, message)

class AnalyzerTestSuite(unittest.TestCase):

    def test_face_counts_per_roll(self):

        fair_dice = Die(faces_array)
        two_fair_dice = []
        for i in range(0,2):
            two_fair_dice.append(fair_dice)
        Game3=Game(two_fair_dice)
        Game3.play(10)
        fair_game = Analyzer(Game3.result_of_play)
        fair_game.face_counts_per_roll()
        number_of_dice = fair_game.faces_with_counts.sum(axis=1)
        unique_number_of_dice = []
        for num in number_of_dice:
            if num not in unique_number_of_dice:
                unique_number_of_dice.append(num)
        testvalue1 = len(unique_number_of_dice) == 1
        if testvalue1 == True: 
            testvalue2 = (2- sum(unique_number_of_dice)<0.01)
        else: 
            print("The number of dice per row is not equal across all the rows in the whole dataframe. The face counts per roll calculation is incorrect.")
        message = "The test value is not true. The face counts per roll calculation is incorrect."
        self.assertTrue(testvalue2, message)

    def test_jackpot(self):
        fair_dice = Die(faces_array)
        two_fair_dice = []
        for i in range(0,2):
            two_fair_dice.append(fair_dice)
        Game3=Game(two_fair_dice)
        Game3.play(100)
        fair_game = Analyzer(Game3.result_of_play)
        fair_game.face_counts_per_roll()
        fair_game.jackpot()
        jackpots_only_df = fair_game.faces_with_counts_sel.loc[fair_game.faces_with_counts_sel['jackpot']!=0].iloc[:,0:6]   
        column_names = list(jackpots_only_df.columns)
        obs_ob_num = list(jackpots_only_df.index.values)
        unique_values = []
        for row in obs_ob_num:
            for column in column_names:
                cell_value=jackpots_only_df.loc[row, column]
                if abs(cell_value-2)<0.01 or abs(cell_value-0)<0.01:
                    testvalue1 = True
                else:
                    testvalue1 = False
        message = "The test value is not true. The number of rolls per dice and observation is not equal to either the total number of rolls or zero." 
        self.assertTrue(testvalue1, message)

    def test_combo(self):
        fair_dice = Die(faces_array)
        two_fair_dice = []
        for i in range(0,2):
            two_fair_dice.append(fair_dice)
        Game3=Game(two_fair_dice)
        Game3.play(100)
        fair_game = Analyzer(Game3.result_of_play)
        fair_game.face_counts_per_roll()
        fair_game.combo()
        one_combo = fair_game.faces_with_counts_combos.iloc[0:1,] 
        faces_with_counts_sel3=fair_game.faces_with_counts_sel2.iloc[:,:-1]
        column_names = list(faces_with_counts_sel3.columns)
        merge_results = one_combo.merge(faces_with_counts_sel3, how='inner', on= column_names)
        testvalue1 = len(merge_results) == one_combo.iloc[0]['Count']
        message = "The test value is not true. The calculated count of the specified combination does not equal the number of times the specified combination occurs in the dataframe."
        self.assertTrue(testvalue1, message)        

if __name__ == '__main__':
    unittest.main(verbosity=3)