# montecarlosimulator

# Metadata
Name: Katherine Sejas

Project Name: Monte Carlo Simulator

# Synopsis 

A package that lets you run Monte Carlo experiments. The user defines their "die", which can represent a variety of random variables, which the package utilizes for the random sampling to obtain statistics such as the the number of face counts per roll or the number of times a game results in all faces being identical or overall the number of times each unique combination of faces occurs in a given game (the size of the game is chosen by the user.).

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

# Die

Description

    The Die Class creates a die with N sides or faces and assigns a weight to each face. The Die Class
    has three methods: change_weight_of_a_single_side, roll_die, and view_faces_weights.
    
    Note that what we are calling a die can represent a variety of random variables associated with 
    stochastic processes, such as using a deck of cards or flipping a coin or speaking a language. 
    The user can create these models by increasing the number of sides and defining the values of their 
    faces. Our probability models for such variables are, however, very simple, since our weights apply 
    to single events. The events are assumed to be independent.   
    
    The weight assigned to each face defaults to 1.0 when the die object is created. However, by using 
    the change_weight_of_a_single_side method the default weight assigned to any given face on the die 
    can be changed to a new weight. The die can be rolled one or more times to select a face, by using 
    the method roll_die. The user can see the die's current set of faces and weights by using the 
    view_faces_weights method.  
    
The public methods that Die has are: __init__, change_weight_of_a_single_side, roll_die, and view_faces_weights. 

# __init__ 

Docstring: 
        The __init__ takes one argument, an array that contains the face values of a die called 
        faces_array. The faces_array may have a data type of strings or numbers. 
        The face values contained in faces_array must be unique, therefore a test in this __init__
        is included to verify that there are no duplicate face values. If there is a duplicate then 
        a message will be printed that warns the user that the faces in faces_array are not unique.
        The __init__ initializes w as equal to 1.0 for each face, 
        which represents the defualt weight of each face in faces_array. 

Parameters: 

faces_array

Return Values: 

None

# change_weight_of_a_single_side 

Docstring: 

	The change_weight_of_a_single_side method takes two arguments: face_value and new_weight.
        The face_value represents the face of the die that should have its weight changed to the new 
        weight value specified by new_weight. 
        The method first checks whether the provided face_value is a face on the die object.
        When the face_value is confirmed as an included value then the new_weight value is checked 
        to see if it is a float. If the new_weight value is not a float but an integer or a number stored 
        as a string which can be converted to a float then the value is converted to a float.
        Otherwise, if the new_weight is not a number then an error message is displayed. If both checks pass
        then the new weight value is assigned to the specified face.

Parameters:

face_value
new_weight

Return Values: 

None

# roll_die 

Docstring:

        The roll_die method takes one argument called number_of_rolls, which represents the number
        of times the die is to be rolled. The default value assigned to the number_of_rolls is 1.
        The rolling of the die is essentially a random sample from the die faces according to the weights.
        The results of the die roll are stored in roll_list, which is returned to the user. 

Parameters:

number_of_rolls=1

Return Values: 

roll_list (list)

# view_faces_weights

Docstring:

The view_faces_weights method returns/shows the user the die's current set of faces and weights.

Parameters:

None

Return Values: 

faces_with_weights (dataframe)

# Game

Description

    The Game Class consists of rolling one or more dice of the same kind one or more times. Each die in a 
    given game has the same number of sides and set of faces, but each die object may have its own weights.
    The Game Class has two methods: play and result_of_recent_play. 

    The Game Class is initialized with a list of one or more dice. The user will specify how many times
    to roll the dice(s) as the parameter for the play method. The results of the recent play can be 
    displayed to the user by using the result_of_recent_play method. 
    
The public methods that Game has are: __init__, play, result_of_recent_play

# __init__

Docstring:

        The __init__ takes one argument: the die_object_list is a list of already instantiated 
        similar Die objects. 

Parameters:

die_object_list

Return Values: 

None

# play

Docstring:

        The play method takes one argument called number_of_rolls, which is an integer that represents the 
        number of times the dice is to be rolled. The results of the play/rolls are saved in a wide form 
        dataframe. 
        The index of the wide form dataframe is called roll_num_index and represents the given roll number. 
        The columns in the dataframe each represent one die. Each cell for a given roll number and die stores
        the face resulting from each roll of die. 

Parameters:

number_of_rolls:int

Return Values: 

None

# result_of_recent_play

Docstring:

        The result_of_recent_play method takes one argument called shape_type, which is a string that
        specifies the dataframe form. The shape_type has two valid values: wide or narrow. If the user 
        provides a different value for shape_type then an exception is raised. 
        
        The play method produces a wide form dataframe therefore this parameter defaults to wide form. 
        The narrow form dataframe has a two-column index with the roll number and the die number, and 
        a single column for the face rolled. 

Parameters:

shape_type:str

Return Values: 

result_of_play

	If the user selects wide as the shape type. 
	
result_of_play_t

	If the user selects narrow as the shape type. 

An error "User passed an invalid option for the shape type of the dataframe. A shape type of wide or narrow was not passed." if the user does not provide a valid shape type. 

# Analyzer

Description

    The Analyzer Class takes the results of a single game and computes the following statistics by using one of its 
    three methods:
        -  The face_counts_per_roll method calculates the number of times a given face is rolled in each event. 
        
        -  The jackpot method calculates the number of times a roll resulted in all faces having the same value 
           such as six twos for a six-sided dice.

        -  The combo method calculates the number of times each distinct combination of faces is rolled.

    The Analyzer Class is initialized with a game object. 

The public methods that Analyzer has are: __init__, face_counts_per_roll, jackpot, combo

# __init__ 

Docstring:

        The __init__ takes one argument: the game_object. 
        The __init__ then takes the game_object and infers the data type of the die faces.

Parameters:

game_object

Return Values: 

None

# face_counts_per_roll 

Docstring:

        The face_counts_per_roll method calculates the number of times a given face is rolled in each event and stores the results
        in a wide form dataframe that has an index of the roll number and face values as columns. 

Parameters:

None

Return Values: 

faces_with_counts (dataframe)

# jackpot

Docstring:

        The jackpot method calculates and returns the number of times a roll resulted in all faces having the same value 
        such as six twos for a six-sided dice.
        The jackpot method also stores the results in the faces_with_counts_sel dataframe which has a column called jackpot
        that identifies the observation/roll number that resulted in all faces having the same value. 

Parameters:

None

Return Values: 

Returns the number of times a roll resulted in all faces having the same value. 

# combo

Docstring:

        The combo method calculates the number of times each distinct combination of faces is rolled.
        The results are saved in a dataframe called faces_with_counts_combos, which has the combinations identified by the
        sorted multi-columned index. 
	
Parameters:

None

Return Values: 

faces_with_counts_combos
