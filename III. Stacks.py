###############################
# Node Class, just used to help 
# initialize node in 
# Stack class
###############################

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


###################################
# Start of Stack class
###################################

class Stack:

    ###############################
    #Initialize/Construct the List
    ###############################
    def __init__(self,value):

        #Create new node object
        newNode = Node(value)

        #Create 'top' pointer
        self.top = newNode

        #no need to track the 'bottom'
        #self.bottom = newNode

        #Update height
        self.height = 1

    ###############################
    #Print the stack
    ###############################

