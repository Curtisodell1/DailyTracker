#creating a binary tree comes down to building nodes and assigning in the empty (None) value spaces
#This can be done manually by assigning a value after creating a Node or programmatically for most real world scenarios

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#instantiation can look something like the following
a = Node("a") 
b = Node("b")

a.left = b

#this would look like 
#   a
#  / 
# b  

#Traversing a Binary Tree (Breadth First vs Depth First)

def breadth_first(root):
    #self explanatory, if no root value exists stop. 
    if root == None:
        return []
    #build a basket to store info (values in this case)
    values = []
    queue = [ root ]
    #while queue variable has a truthy value do these things
    while queue:
        #assign a new variable 'current' to the value at the start of the list
        current = queue.pop(0)
        #put this value into our basket
        values.append(current.val)

        #check for values on the left and right, if they exist add them to our queue of values to be explored
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        
    return values

#the main difference in an iterative approach of both depth first and breadth first is the position of where you'll be using the .pop() method to pull the value from.
#in Depth first we use a stack which focuses on exploring the last value added to it
#in contrast, a queue will look at and explore each route in a first in first out order

#with this example the main difference lives in '.pop()' by default this will take the last value added to the list. 
def depth_first(root):
    if not root:
        return []
    
    stack = [root]
    values = []
    
    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values