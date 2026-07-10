###############################
# Node Class, just used to help 
# initialize node in 
# Doubly LinkedList class
###############################

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

        #Differentiating part between 
        # singly and doubly linked list
        self.prev = None


###################################
# Start of Doubly Linked list class
###################################

class DoublyLinkedList:

    ###############################
    #Initialize/Construct the List
    ###############################
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    ###############################
    #Print the List
    ###############################
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    ###############################
    #Add value to the end of the list
    ###############################
    def append(self,value):
        newNode = Node(value)

        #For empty lists
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        #For lists with existing nodes
        else:
            #Point value after 'current tail' 
            # to 'new node'
            self.tail.next = newNode
            #Point value behind(prev) the 'new node' 
            # to 'current tail'
            newNode.prev = self.tail
            #Update the 'tail' variable value 
            # as the 'new node'
            self.tail = newNode

        #Update length of list
        self.length += 1

        #Confirm success of function
        return True
        
    
    
###################################
# End of Doubly Linked list class
###################################

################################################
################################################
################################################

#Test DLL creation with one element
myDoublyLinkedList = DoublyLinkedList(1)

#Test append value
myDoublyLinkedList.append(2)

#Print the List
myDoublyLinkedList.print_list()