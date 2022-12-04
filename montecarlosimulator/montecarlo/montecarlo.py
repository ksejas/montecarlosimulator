
import pandas as pd
import numpy as np

class Die:
    '''
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
    '''

    def __init__(self, faces_array):
        ''' 
        The __init__ takes one argument, an array that contains the face values of a die called 
        faces_array. The faces_array may have a data type of strings or numbers. 
        The face values contained in faces_array must be unique, therefore a test in this __init__
        is included to verify that there are no duplicate face values. If there is a duplicate then 
        a message will be printed that warns the user that the faces in faces_array are not unique.
        The __init__ initializes w as equal to 1.0 for each face, 
        which represents the defualt weight of each face in faces_array. 
        '''
        unique_faces = []
        for face in faces_array:
            if face not in unique_faces:
                unique_faces.append(face)
        self.w=[1.0]
        self.faces_array=unique_faces
        w_length = [1.0]*len(self.faces_array)
        self.faces_with_weights = pd.DataFrame({
            'w' : w_length,
            'faces' : faces_array
        }).astype(dtype = {'w' : float})
        count=self.faces_with_weights.faces.unique().size
        rows_num=len(self.faces_with_weights)
        test_unique=count==rows_num
        if True==test_unique:
            pass
        else: 
            print("The faces included in the faces_array are not unique. There is at least one face value that has at least one duplicate. Therefore, faces_array has now been made as unique. The duplicate faces have been dropped from faces_array.")

    def change_weight_of_a_single_side(self, face_value, new_weight):
        '''The change_weight_of_a_single_side method takes two arguments: face_value and new_weight.
        The face_value represents the face of the die that should have its weight changed to the new 
        weight value specified by new_weight. 
        The method first checks whether the provided face_value is a face on the die object.
        When the face_value is confirmed as an included value then the new_weight value is checked 
        to see if it is a float. If the new_weight value is not a float but an integer or a number stored 
        as a string which can be converted to a float then the value is converted to a float.
        Otherwise, if the new_weight is not a number then an error message is displayed. If both checks pass
        then the new weight value is assigned to the specified face.'''
        if any(self.faces_with_weights.faces == face_value)==True:
            if isinstance(new_weight, float)==True:
                row_num=self.faces_with_weights[self.faces_with_weights['faces']==face_value].index[0] 
                self.faces_with_weights.iloc[row_num, 0]=new_weight
            elif isinstance(new_weight, int)==True:
                new_weight_float=float(new_weight)
                row_num=self.faces_with_weights[self.faces_with_weights['faces']==face_value].index[0]
                self.faces_with_weights.iloc[row_num, 0]=new_weight_float   
            elif isinstance(new_weight, str==True):
                try:
                    new_weight_float=float(new_weight) 
                    row_num=self.faces_with_weights[self.faces_with_weights['faces']==face_value].index[0]
                    self.faces_with_weights.iloc[row_num, 0]=new_weight_float   
                except:
                    print("The new_weight value is not a number stored as a string.")      
            else: 
                print("Error: The new weight is not a number.")
        else:
            print("The new face value is a face value that is not included as a face on the die object, no change made.")
        
    def roll_die(self, number_of_rolls=1):
        '''
        The roll_die method takes one argument called number_of_rolls, which represents the number
        of times the die is to be rolled. The default value assigned to the number_of_rolls is 1.
        The rolling of the die is essentially a random sample from the die faces according to the weights.
        The results of the die roll are stored in roll_list, which is returned to the user. 
        '''
        self.rolled_faces_with_weights = self.faces_with_weights.sample(n=number_of_rolls, replace = True, weights="w").reset_index(drop=True)
        self.roll_list=self.rolled_faces_with_weights['faces'].values.tolist()
        return self.roll_list

    def view_faces_weights(self):
        '''
        The view_faces_weights method returns/shows the user the die's current set of faces and weights. '''
        return self.faces_with_weights

class Game:
    '''
    The Game Class consists of rolling one or more dice of the same kind one or more times. Each die in a 
    given game has the same number of sides and set of faces, but each die object may have its own weights.
    The Game Class has two methods: play and result_of_recent_play. 

    The Game Class is initialized with a list of one or more dice. The user will specify how many times
    to roll the dice(s) as the parameter for the play method. The results of the recent play can be 
    displayed to the user by using the result_of_recent_play method. 
    
    '''

    def __init__(self, die_object_list):
        '''
        The __init__ takes one argument: the die_object_list is a list of already instantiated 
        similar Die objects. 
        '''
        self.die_object_list=die_object_list


    def play(self, number_of_rolls:int):
        '''
        The play method takes one argument called number_of_rolls, which is an integer that represents the 
        number of times the dice is to be rolled. The results of the play/rolls are saved in a wide form 
        dataframe. 
        The index of the wide form dataframe is called roll_num_index and represents the given roll number. 
        The columns in the dataframe each represent one die. Each cell for a given roll number and die stores
        the face resulting from each roll of die. 
         '''
        self.number_of_rolls=number_of_rolls
        self.result_of_play = pd.DataFrame()
        self.result_of_play.index.rename('roll_num_index', inplace=True)
        for die_num, die in enumerate(self.die_object_list):
            for roll_num in range(number_of_rolls):
                self.result_of_play.loc[roll_num, die_num] = Die.roll_die(1)[0]

    def result_of_recent_play(self, shape_type:str):
        '''
        The result_of_recent_play method takes one argument called shape_type, which is a string that
        specifies the dataframe form. The shape_type has two valid values: wide or narrow. If the user 
        provides a different value for shape_type then an exception is raised. 
        
        The play method produces a wide form dataframe therefore this parameter defaults to wide form. 
        The narrow form dataframe has a two-column index with the roll number and the die number, and 
        a single column for the face rolled. 

        '''
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

class Analyzer:
    '''
    The Analyzer Class takes the results of a single game and computes the following statistics by using one of its 
    three methods:
        -  The face_counts_per_roll method calculates the number of times a given face is rolled in each event. 
        
        -  The jackpot method calculates the number of times a roll resulted in all faces having the same value 
           such as six twos for a six-sided dice.

        -  The combo method calculates the number of times each distinct combination of faces is rolled.

    The Analyzer Class is initialized with a game object. 
         
    '''

    def __init__(self, game_object):
        '''
        The __init__ takes one argument: the game_object. 
        The __init__ then takes the game_object and infers the data type of the die faces.
        '''
        self.game_object = game_object
        self.game_object_type = self.game_object.dtypes
 

    def face_counts_per_roll(self):
        '''
        The face_counts_per_roll method calculates the number of times a given face is rolled in each event and stores the results
        in a wide form dataframe that has an index of the roll number and face values as columns. 

        '''
        game = self.game_object
        self.faces_with_counts = game.apply(lambda faces_series: faces_series.value_counts(), axis = 1).fillna(0).rename_axis(columns = 'roll_num')
        return self.faces_with_counts

    def jackpot(self):
        '''
        The jackpot method calculates and returns the number of times a roll resulted in all faces having the same value 
        such as six twos for a six-sided dice.
        The jackpot method also stores the results in the faces_with_counts_sel dataframe which has a column called jackpot
        that identifies the observation/roll number that resulted in all faces having the same value. 
        '''
        self.faces_with_counts_sel=self.faces_with_counts.copy()
        self.column_num = len(self.faces_with_counts_sel.columns)
        self.first_row = self.faces_with_counts_sel.iloc[0:1,]
        self.number_of_dice = self.first_row.values.sum()
        self.column_names = self.faces_with_counts_sel.columns
        self.faces_with_counts_sel.loc[:, 'jackpot'] = 0
        for column in self.column_names:
            for row in range(len(self.faces_with_counts_sel)):
                if abs(self.faces_with_counts_sel.loc[row].at[column] - self.number_of_dice)<=0.01: 
                    self.faces_with_counts_sel.loc[row,"jackpot"] = 1
        self.number_of_jackpots = sum(self.faces_with_counts_sel['jackpot'])
        return self.number_of_jackpots

    def combo(self):
        '''
        The combo method calculates the number of times each distinct combination of faces is rolled.
        The results are saved in a dataframe called faces_with_counts_combos, which has the combinations identified by the
        sorted multi-columned index. 
        '''
        self.faces_with_counts_sel2=self.faces_with_counts.copy()
        self.faces_with_counts_sel2['Count'] = 1
        self.column_names_sel = list(self.faces_with_counts_sel2.columns[:-1])
        self.faces_with_counts_combos = self.faces_with_counts_sel2.groupby(self.column_names_sel)['Count'].sum().to_frame()
        self.faces_with_counts_combos.sort_values(by=self.column_names_sel)
        return self.faces_with_counts_combos



