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
        
        #Start from head
        temp = self.head

        #And loop through all values
        #printing each value
        while temp is not None:
            print(temp.value)
            temp = temp.next

    ###############################
    #Append/Add value to the end of 
    # the list
    ###############################
    def append(self,value):

        #Create new node based on provided value
        newNode = Node(value)

        #For empty lists
        #Check if head is None
        # Can also use self.length == 0
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
    
    ###############################
    #Pop/Remove value from
    #  the end of the list
    ###############################
    def pop(self):

        #For empty lists, check size 
        # and return None
        if self.length == 0:
            return None
        
        #----------------------------------------#        
        #Swap tail value to one position before it. 
        #And break all connection from the old tail

        #Create new value 'temp' to store tail value
        temp = self.tail

        #If size of List was 'one'/1, 
        # set head and tail to None
        if self.length == 1:
            self.head = None
            self.tail = None

        #Else size of list is more than 'one'/1
        else:
            #Update tail as the node before initial/nth node - 'tail'
            # i.e. (n-1)th node
            self.tail = self.tail.prev

            #Break 'next' pointer of the new tail
            self.tail.next = None

            #And 'prev' pointer of the old tail
            temp.prev = None
        #----------------------------------------#

        #Finalize function by reducing list size by 1
        self.length -= 1

        #Return node that was popped
        return temp.value
    

    ###############################
    #Prepend/Add new value to the 
    # start of the list
    ###############################
    def prepend(self,value):
        
        #Create new node with  
        # provided value
        newNode = Node(value)

        #If list is empty
        #Set head and tail as new node
        if self.length == 0:

            self.head = newNode
            self.tail = newNode
        
        #Else swap head value and
        # update prev and next connections
        else:

            #Point new node's next 
            # pointer to 'old head'
            newNode.next = self.head

            #Point current head's prev pointer
            # to the new node
            self.head.prev = newNode

            #Update head as the new node
            self.head = newNode

        #Update length of list
        self.length += 1

        #Return true on completion
        return True

    
###################################
# End of Doubly Linked list class
###################################





################################################
################################################
################################################





##################################
#I. Create list, add nodes and print
##################################
print("Creating list, adding value and printing\n")

#Test DLL creation with one element
myDoublyLinkedList = DoublyLinkedList(1)

#Test append value
myDoublyLinkedList.append(2)

#Print the List
myDoublyLinkedList.print_list()

print("\n#---------------#\n")



##################################
#II. Test pop
##################################
# print("\nPopping nodes\n")

# # (2) Items - Returns '2' Node
# print(myDoublyLinkedList.pop())

# # (1) Items - Returns '1' Node
# print(myDoublyLinkedList.pop())

# # (0) Items - Returns '1' Node
# print(myDoublyLinkedList.pop())

# #Print the list
# myDoublyLinkedList.print_list()
# print(f"\nSize of list is now: {myDoublyLinkedList.length}")

# print("\n#---------------#\n")


##################################
#III. Test prepend
##################################
print("\nPrepending List with value '0'\n")

#Prepend value in the list
myDoublyLinkedList.prepend(0)

#Print result
myDoublyLinkedList.print_list()

print("\n#---------------#\n")