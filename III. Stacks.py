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
    def printStack(self):

        #Create temporary variable
        # that starts from the top
        temp = self.top

        #Loop through stack till empty
        while temp is not None:
            print(temp.value)
            temp = temp.next


###################################
# End of Doubly Linked list class
###################################





################################################
################################################
################################################





##################################
#I. Create list, add nodes and print
##################################

#Create stack with one node
myStack = Stack(4)

myStack.printStack()