'''A class that implements a list adt using a Multi dimentional array.'''
class MultiDArray:

    def __init__(self):
        '''A constructor for the MultiDArray class.
       
           Parameters:
            myarray -- The empty array that is to be manipulated.'''
        self.my_array = []

    def create_array(self,n):
        '''This method creates an initial matrix made up of 0s.

           Parameters:
            n -- A default arguement that takes creates a square matrix.

           Runtime function: O(n2)
        '''
        self.my_array = [[[0 for x in range(n)] for y in range(n)] for z in range(n)]
        return self.my_array

    def array_len(self):
        '''Checks the number of items in the array.

           Returns: The number of items.

           Runtime function: O(1)'''
        return len(self.my_array)

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

    def access_array(self,array):
        '''Accesses an inner array.

        Parameters:
            array -- This is the index of the inner array.

        Returns: The indexed inner array.

        Runtime function: O(1)
        '''
        return self.my_array[array]

    def access_element(self,array,row,col):
        '''Accessing a value in the 3d array.

            Parameters:
                array -- This is the index of the inner array.
                row -- This indicates the row position of the element.
                col -- This indicates the column position of the element.

            Returns: returns a single value in that has been accecessed.

            Runtime function: O(1)'''
        return self.my_array[array][row][col]

    def delete_element(self,array,row,col):
        '''Deleting an element in the multi dimention array.

            Parameters:
                array -- This is the index of the inner array.
                row -- This indicates the row position of the element.
                col -- This indicates the column position of the element.

            Returns: returns the array that no longer has the element that was deleted.

            Runtime function: O(n)
            '''
        del self.my_array[array][row][col]
        return self.my_array
        




    





