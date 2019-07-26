'''A class that implements a list adt using a Stack data structure.'''

class Stack:
    def __init__(self,mystack):
        '''Initializing attributes of Stack class.

        Para6meters:
            mystack -- The list that will be implemented by the stack data structure.

        Runtime function: Constant time/O(1).
        '''
        self.mystack = []
        
    def stack_len(self):
        '''This method prints out the number of items in the stack.

        Runtime: Constant time/O(1).
        '''
        print('This stack contains {} items'.format(len(self.mystack)))

    def stack_status(self):
        '''Checks if the stack is empty is not.

        Runtime: Constant time/O(1).
        '''
        if not self.mystack:
            print('Your stack is empty')
        else:
            print('Your stack is not empty')

    def add_items(self,item):
        '''Adds items in the stack.

        Parameters:
            item - This arguement inputs an item to be added to the list.

        Runtime: Constant time/ O(1)
        '''
        self.mystack.append(item)
        return self.mystack
        
    def remove_item(self):
        '''Removing the top most item and printing out the stack thereafter.

        Runtime: Constant time/O(1).
        '''
        try:
            self.mystack.pop()
        except Exception:
            print('Your Stack is empty so there is nothing to remove')
        else:
            print(self.mystack)

    def peek(self):
        '''Prints out the item at the top of the stack.

        Runtime: linear time/O(n).
        '''
        try:
            top_item = (self.mystack[-1])
        except Exception:
            print('Your Stack is empty so there is nothing to peek')
        else:
            print('The item at the top of the stack is {}'.format(top_item))
    

