'''
    create a 2array 
    create a method that takes arguments rows and columns and creates a 2d array
    create a method that  returns the number of rows
    create a method that returns the number of columns
    create a method that clears the array, parsing in the value you want to clear the array with
    create a method that  accepts the row and column and returns the element in that position
    create a method called set element that accpets the row and column and the value to be set '''

'''A class that implements a list adt using a Two dimentional array data stucture'''

class TwoDimArray:

    def __init__(self,row_number,column_number):
        '''A constructor for the Two Dimentional Array class.

        Parameters:
            row_number -- The number of rows the array with have.
            column_number -- The number of columns of the array.
        '''
        self.row_number = row_number
        self.column_number = column_number
        self.two_d_array = [[0 for col in range(self.column_number)] for row in range(self.row_number)]


    def num_rows(self):
        '''Method returns the number of rows.
        
        Returns : Number of rows in the two D array.

        Runtime function: O(n2)
         '''
        for row in range(self.row_number):
            for col in range(self.column_number):
                self.two_d_array[row][col]= row*col
                return len(self.two_d_array)
    def num_cols(self):
        '''Method returns the number of columns.
        
        Returns : Number of columns in the two D array.

        Runtime function: O(1)'''
        return len(self.two_d_array[1])
        
    def clear_array(self,value):
        '''Method Updates the values of the items in the array.
        
        Returns : An updated multi dimentional array.

        Runtime function: O(n2)'''
        self.value = value
        self.two_d_array = [[self.value for col in range(self.column_number)] for row in range(self.row_number)]
        return self.two_d_array

    def access_element(self,array,row,col):
        '''Accessing a value in the 3d array.

            Parameters:
                array -- This is the index of the inner array.
                row -- This indicates the row position of the element.
                col -- This indicates the column position of the element.

            Returns: returns a single value in that has been accecessed.

            Runtime function: O(1)'''
        return self.my_array[array][row][col]

    def update_elements(self,array,row,col,new_element):
        
        '''This method changes the value of an element in a specified index.

           Parameters:
                array -- This is the index of the inner array.
                row -- This indicates the row position of the element.
                col -- This indicates the column position of the element.
                new_element -- This is the value of new the element.

            Returns: returns the updated array ie my_array with the new value.

            Runtime function: O(1)
            '''
        try:
            self.my_array[array][row][col] = new_element
        except IndexError:
            print('Man your list index is hell out of range!!')
        return self.my_array

        