'''A set adt class.'''
class Set:
    '''A constructor for the set class.

    Parameters:
        myset -- Passes in a set.
        set2 -- Passes in a set
    '''
    def __init__(self,myset,set2):
        self.myset = {}
        self.set2 = {}

    def additem(self,item):
        '''Adds an element into the set.

        Parameters:
            item -- the item that will be added in the set.

        Runtime function: O(1).
        '''
        self.item = item
        self.myset.add(self.item)
        return set(self.myset)

    def len_(self):
        '''Returns the number of items in the set.

        Runtime function: O(1).
        '''
        return len(self.myset)

    def iterate_set(self):
        '''Iterates over the set and prints them one by one.

        Runtime function: O(n).
        '''
        for item in self.myset:
            print(item)

    def popelement(self,index):
        '''Removes an item at a specified position and returns it.

        Parameters:
            index -- The index position of the item to be removed.

        Runtime function: O(n)
        '''
        self.index = int(input('Enter index:'))
        self.myset.pop(self.index)
        return self.myset

    def setunion(self):
        '''Adds up all elements in both sets.
        
        Returns: A new set made up of all elements from both sets.

        Runtime function: O(len(myset)+len(set2))
        '''
        self.set2 = self.myset ** 2
        newset = self.myset + self.set2
        return newset

    def setintersection(self):
        '''Adds up elements that are common in both sets.

        Returns: A new set containing elements common in both sets.
        
        Runtime function: O(len(myset)+len(set2))
        '''
        newset = {}
        for element in self.myset:
            if element in self.set2:
                newset.add(element)
        return newset

    def difference(self):
        '''Computes elements that are in the first set but are not in the second set.

        Returns: A new set containing with elements only present in the first set._
        
        Runtime function: O(len(myset)+len(set2))
        '''
        newset = {}
        for element in self.myset:
            if element not in self.set2:
                newset.add(element)
        return newset



