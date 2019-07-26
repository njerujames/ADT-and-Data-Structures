'''A dictionary class adt'''
class Mapping():
    
    def __init__(self,my_dict):
        '''This method initializes the mapping class.

        Creates an instance of the class.
        '''
        self.my_dict = {}

    def create_dict(self,key,value):
        '''This method creates a dictionary that takes four keys together with respective values.

        Parameters:
            key -- Enables user input of the key.
            value -- Enables user input of the value

        Returns: a key- value dictionary.

        Runtime function: O(1)
         '''
        for i in range(4):
            self.key = input('Please enter a key:')
            self.value = int(input('Please enter value:'))
            self.my_dict[self.key] = self.value
        return self.my_dict 

    def get_item(self):
        '''This uses the key to search for a value in the dictionary.

        Returns: A value according to its key.

        Runtime function: O(1)
        '''
        self.name = input('Please enter a name:')
        if self.name in self.my_dict:

            return self.my_dict[self.name]
        else:
            print('Item is not in the dictionary')

    def clear_dict(self):
        '''This removes all items in the dictionary.

        Runtime function: O(1)
        '''
        self.my_dict.clear()
    def update(self):
        '''This method adds element(s) to the dictionary if the key is not in the dictionary.

        If the key is in the dictionary, it updates the key with the new value.

        Returns: An updated dictionary.

        Runtime function: O(1)
        '''
        self.key = input('Please enter a key:')
        self.value = int(input('Please enter value:'))
        self.my_dict[self.key] = self.value
        return self.my_dict

    def dict_len(self):
        '''This method returns the length of the dictionary.
                
        Runtime function: O(1)
        '''
        return len(self.my_dict)

    def dict_keys(self):
        '''This returns the names(keys) in the dictionary.

        Runtime function: O(1)
        '''
        return self.my_dict.keys()

    def dict_values(self):
        '''This returns dictionary ages(values).

        Runtime function: O(1)
        '''
        return self.my_dict.values()

    def pop_item(self):
        '''This method removes a value at a specific index and returns it.

        Returns: A dictionary without the item that was removed.

        Runtime function: O(1)
        '''
        
        self.key = input('Please enter a key:')
        self.my_dict.pop(self.key)
        return self.my_dict

    def remove_item(self):
        '''This permanently removes an item from the dictionary.

        Returns: A dictionary without the item.

        Runtime function: O(1)
        '''
        self.key = input('Please enter a key in the dictionary:')
        if self.key in self.my_dict:
            del self.my_dict[self.name]
        else:
            print('The name is not in the dictionary')
        return self.my_dict
