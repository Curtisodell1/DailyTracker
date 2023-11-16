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

#recursively a linked list is solved in much the same way

def print_list_recursively(head):
    #base case is below
    if head is None:
        return
    #here we can have our action we want to perform. In this case printing the value.
    print(head.val)
    #lastly we need a way to call the function again
    print_list_recursively(head.next)

#Tortoise and Hare style problems 
#Used to determine if a list is circular

def cycle_check(head):
    if not head:
        return False
    tortoise = head
    hare = head
    
    while tortoise is not None and hare is not None:

        hare = hare.next.next 
        tortoise = tortoise.next

        if hare == tortoise:
            return True
        
    return False