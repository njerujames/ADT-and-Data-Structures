'''A class that implements a list adt using an array.'''
class Array:
    '''A constructor for the Array class.
       
       Parameters:
        myarray -- The empty array that is to be manipulated.'''
    def __init__(self,myarray):
        self.myarray = []

    def append_array(self,item):
        '''Adds an item at the end of the array.
           
           Parameters:
                item -- The data item that it will add.
           
           Returns: The array with the added item.

           Runtime function: O(1)
        '''
        return (self.myarray.append(self.item))

    def array_size(self):
        '''Checks the number of items in the array.

           Returns: The number of items.

           Runtime function: O(1)
        '''
        return len(self.myarray)
    
    def insert_item(self,index,item):
        '''Inserts a new item at a specified index position.

           Parameters:
                index -- indicates the index position for inserting.
                item -- The item to be inserted
            
            Runtime Function : O(n)
        '''
        try:
            self.myarray.insert(index,item)
        except Exception:
            print('Index is out of Range, please try again')
        else:
            return self.myarray

    def delete_item(self,index):
        '''Removes the item at the given position in the array.
           
           Parameters:
                index -- The position of the item that will be removed.

            Returns: The array without the item that was removed.

            Runtime function: O(1)
        '''
        self.myarray.pop(index)
        return self.myarray
    



