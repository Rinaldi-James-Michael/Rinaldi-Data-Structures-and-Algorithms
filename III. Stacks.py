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
    #Initialize/Construct the Stack
    ###############################
    def __init__(self,value):

        #Create new node object
        newNode = Node(value)

        #Create 'top' pointer
        self.top = newNode

        #no need to track the 'bottom'
        #self.bottom = newNode

        #Update stack height
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


    ###############################
    #Push - Add a new node on top
    # of the stack
    ###############################
    def push(self,value):
        newNode = Node(value)

        #When stack is empty
        if self.height == 0:
            self.top = newNode

        #When stack has values,
        # point new node's 'next' pointer
        # to the existing 'top', and update
        # 'top' to be the new node
        else:
            newNode.next = self.top
            self.top = newNode

        #Update stack height
        self.height += 1


    ###############################
    #Pop - Remove and return the  
    #node from the top of the stack
    ###############################
    def pop(self):

        #When stack is empty
        if self.height==0:
            return None

        #--------------------------------------#
        #Else, remove top node and it's
        # 'next' pointer
        
        #Temporarily store 'top' node
        # This will be returned.
        temp = self.top

        #Update 'top' node as node under old 'top'
        self.top = self.top.next

        #Remove the old 'top's' next pointer
        temp.next = None
        #--------------------------------------#

        #Update height
        self.height -= 1

        return temp


###################################
# End of Stacks class
###################################





################################################
################################################
################################################





##################################
#I. Create stack with a node & print
##################################
print("I. Creating stack with one node and print\n")

#Create stack with one node and print
myStack = Stack(1)
myStack.printStack()

print("\n#---------------#\n")


#####################################
#II. Push node into the stack
#####################################
print("II. Add new value/node to the stack\n")

#Add value to the top and print
myStack.push(2)
myStack.printStack()

print("\n#---------------#\n")


#####################################
#III. Pop node from the stack
#####################################
print("III. Popping top node from the stack\n")

#Fill in some values
myStack.push(3)
myStack.push(4)
myStack.push(5)

print("Stack before pop:")
myStack.printStack()

#Pop the value '5', which is at the top
poppedNode = myStack.pop().value
print(f"\nStack after popping: {poppedNode}")
myStack.printStack()

print("\n#---------------#\n")