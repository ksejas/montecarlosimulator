
import pandas as pd
import numpy as np

class Die:
    '''The Die Class '''

    def __init__(self, faces_array):
        ''' The __init__ takes one argument, an array that contains the face values of a die called 
        faces_array. The faces_array may have a data type of strings or numbers. 
        The face values contained in faces_array must be unique, therefore a test in this __init__
        is included to verify that there are no duplicate face values. 
        The __init__ initializes w as equal to 1.0, which represents the weight of each face in faces_array. 
        The faces_array and weight values are used to create a dataframe called faces_with_weights. '''
        self.w=[1.0]
        self.faces_array=faces_array
        w_length = [1.0]*len(self.faces_array)
        #print(w_length)
        # num of sides; define faces; single events - independent events;
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
            print("The faces included in the faces_array are not unique. There is at least one face value that has at least one duplicate.")

    def change_weight_of_a_single_side(self, face_value, new_weight):
        '''The change_weight_of_a_single_side function takes two arguments: face_value and new_weight.
        The face_value represents the face value that has a new weight value. The function first checks
        whether the provided face_value is contained in the faces column of the faces_with_weights dataframe.
        When the face_value is confirmed as an included value in the faces_with_weights dataframe then
        the new_weight value is checked to see if it is a float. If the new_weight value is not a float but
        an integer or a number stored as a string which can be converted to a float then the value is converted.
        Otherwise, if the new_weight is not a number then an error message is displayed.'''
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
            print("The new face value is a face value that is not included in the faces_with_weights dataframe, no change made.")
        
    def roll_die(self, number_of_rolls=1):
        '''The roll_die function '''
        self.rolled_faces_with_weights = self.faces_with_weights.sample(n=number_of_rolls, replace = True, weights="w").reset_index(drop=True)
        #self.roll_list_face=self.rolled_faces_with_weights['faces']
        #roll_list=self.rolled_faces_with_weights.values.tolist()
        self.roll_list=self.rolled_faces_with_weights['faces'].values.tolist()
        #print(roll_list)
        return self.roll_list

    def view_faces_weights(self):
        return self.faces_with_weights

