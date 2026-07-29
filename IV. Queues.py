###############################
# Node Class, just used to help 
# initialize node in 
# Queue class
###############################

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


###################################
# Start of Queue class
###################################

class Queue:

    ###############################
    #Initialize/Construct the List
    ###############################
    def __init__(self,value):