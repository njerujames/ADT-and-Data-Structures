'''A class that implements a stack adt using a Linked list data structure.'''

class Node:
    '''Initialize the node class.
    
    Creating an instance of an element and the pointer node.

    Parameters:
        data -- This will pass the value of the element

       Runtime : Constant time/O(1)
       '''
    def __init__(self,data):
        self.data = data
        self.next = None

class SLinkedList():
    '''Initializing single linked list class
    Parameters:
    
    Runtime: Constant time/O(1)
    '''
    def __init__(self,data = None):
        self.stack = []
        self.head = Node(data)

    def add_item(self,data):
        '''Inserting a node to the list

        Args:
            data - arguement will add element into the node
           
        Runtime: Constant time/O(1)
        '''
        newnode = self.head.next
        self.stack.append(newnode)

    def stack_len(self):
        '''Checks for number of nodes in the stack.

        Retuns: int type , number of items.

        Runtime function: O(1)'''

        return len(self.stack)

    def delete(self,node):
        '''Deletes a node in the list.
        
        Parameters:
            node -- item to be deleted.

        Runtime function: O(n).'''
        if self.head == node:
            self.head.next.next
            return self.stack

    def peek(self):
        '''Finds the node at the top of the stack.

        Returns: The last in item.

        Runtime function: O(n).
        '''
        while self.head:
            top_item = (self.stack[-1])
            return top_item
        