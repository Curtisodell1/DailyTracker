#Creating a linked list simple example from Structy

class Node:
    def __init__(self, val):
        #below defines the value as we instantiate new data
        self.val = val
        #as a base the next value should not exist, we can later add the 'next' value 
        self.next = None

#imagining we have built out data for a linked list
#basic traversal can be done iteratively or recursively 

def print_list(head):
    current = head
    while current:
        #do what you want to do with the value here
        print (current.val)
        #below you iterate to the next value in the list
        current = current.next