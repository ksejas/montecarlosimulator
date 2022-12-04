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
        #Die1.view_faces_weights()
        print(Die1.faces_with_weights)
        two_fair_dice = []
        two_fair_dice.append(Die1)
        two_fair_dice.append(Die1)
        
        print(two_fair_dice)
        Game1 = Game(two_fair_dice)
        #print(Game1.die_object_list)
        #print(Game1.faces_with_weights)
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
        print(Game1.die_object_list)
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





if __name__ == '__main__':
    unittest.main(verbosity=3)