# montecarlosimulator

# Metadata
Name: Katherine Sejas
Project Name: Monte Carlo Simulator

# Synopsis 

Three simple demonstrations of this code/package and how the classes are used can be found at https://github.com/ksejas/montecarlosimulator/blob/main/montecarlosimulator/montecarlo_demo.ipynb. 

# Installing 

To install from root of montecarlosimulator : pip install .
To install from Github: pip install git+ssh://git@github.com/ksejas/montecarlosimulator.git@main

# Importing

To import the class Die, Game, and Analyzer, you need to run the following "from montecarlo import *"

# Creating Dice Objects 

The following code listed below creates two dices each with six faces. The first dice is called fair_die and it keeps the default weight of 1 for each face. The second dice called unfair_die_type1 changes the weight of a single face from the default weight of 1 to 5 for face 6.

import numpy as np
from montecarlo import *
faces_array = np.array([1,2,3,4,5,6], dtype = int)

fair_die = Die(faces_array)
fair_die.view_faces_weights()

	w	  faces
0	1.0	1
1	1.0	2
2	1.0	3
3	1.0	4
4	1.0	5
5	1.0	6

unfair_die_type1 = Die(faces_array)
unfair_die_type1.change_weight_of_a_single_side(6, 5)
unfair_die_type1.view_faces_weights()

  w	  faces
0	1.0	1
1	1.0	2
2	1.0	3
3	1.0	4
4	1.0	5
5	5.0	6


# Playing games 

The following code listed below creates an additional dice called unfair_die_type2 with six faces and changes the weight of a single face from the default weight of 1 to 5 for face 1. Afterwards the code creates a die object list where there are 5 dices: two fair_die, one unfair_die_type_1, and two unfair_die_type2. Afterwards it calls Game and as its parameter uses the die object list called two_unfair_type1_one_unfair_type2_two_fair_dice. Afterwards, a game of 10,000 rolls is played. 

unfair_die_type2 = Die(faces_array)
unfair_die_type2.change_weight_of_a_single_side(1, 5)
unfair_die_type2.view_faces_weights()

	w	  faces
0	5.0	1
1	1.0	2
2	1.0	3
3	1.0	4
4	1.0	5
5	1.0	6

two_unfair_type1_one_unfair_type2_two_fair_dice = []

two_unfair_type1_one_unfair_type2_two_fair_dice.append(fair_die)
two_unfair_type1_one_unfair_type2_two_fair_dice.append(fair_die)
two_unfair_type1_one_unfair_type2_two_fair_dice.append(unfair_die_type1)
two_unfair_type1_one_unfair_type2_two_fair_dice.append(unfair_die_type1)
two_unfair_type1_one_unfair_type2_two_fair_dice.append(unfair_die_type2)

game_with_five_dice = Game(two_unfair_type1_one_unfair_type2_two_fair_dice)
game_with_five_dice.play(10000)
game_with_five_dice.result_of_recent_play('wide')

	              dice_0	dice_1	dice_2	dice_3	dice_4
roll_num_index					
0	              6.0	    1.0   	2.0	    5.0   	5.0
1		            5.0	    3.0	    6.0	    5.0   	1.0
2		            3.0   	5.0	    6.0	    3.0   	6.0
3		            4.0   	3.0	    6.0   	2.0	    1.0
4		            6.0   	4.0	    6.0   	2.0   	6.0
...	...	...	...	...	...
9995		        2.0   	5.0   	1.0   	6.0   	5.0
9996			      2.0   	3.0   	6.0	    6.0	    1.0
9997			      6.0   	3.0   	2.0	    6.0	    1.0
9998			      4.0   	1.0   	6.0	    6.0	    6.0
9999			      2.0   	3.0   	6.0	    2.0   	6.0

# Analyzing Games 

The following code listed below takes the results of playing the 10,000 rolls and calculates the face counts per roll and the relative frequency of jackpots (instances where all faces in a given roll are identical). 

unfair_game_dice = Analyzer(game_with_five_dice.result_of_play)
unfair_game_dice.face_counts_per_roll()

unfair_game_dice.jackpot()
relative_freq_jackpot_unfair_dice = 100*(unfair_game_dice.number_of_jackpots/1000)
relative_freq_no_jackpot_unfair_dice = 100-relative_freq_jackpot_unfair_dice

print(relative_freq_jackpot_unfair_dice)

0.6

# API Description 

