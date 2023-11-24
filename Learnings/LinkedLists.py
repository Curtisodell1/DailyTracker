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

#Combining Linked Lists using a zipper method -
#this could be a helpful way of merging two lists but is also a basis for other functionality

def zipper_lists(head_1, head_2):
    #a tail will basically act as our pointer. 
    #like in a game of snake the tail will be growing to acount for each new value we add in
    tail = head_1
    #We'll always be starting with the head_1 in this example so we want to make sure we pre-empt the increment
    current_1 = head_1.next
    current_2 = head_2
    #count is the logic we are using to alternate. We could also use this for every nth value 
    count = 0
    while current_1 is not None and current_2 is not None:
    #combining two spotify playlists so they merge together smoothly could be an example of changing the dividing number
        if count % 2 == 0:
        tail.next = current_2
        current_2 = current_2.next
    # our logic here is simply if the count is divisible by the number (in this case 2) but we can also insert other logic at this point
        else:
        tail.next = current_1
        current_1 = current_1.next
        tail = tail.next
        count += 1
    #lastly we'll almost always have a remainder that we need to take care of. here is that.
    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2
        
    return head_1 