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
        #return temp.value
        return temp
    

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
    
    
    ###############################
    #Pop First - Remove first item
    # from the list and return what
    # was popped
    ###############################
    def popFirst(self):

        #For empty list return 'False'
        if self.length <= 0:
            return None
        
        #--------------#
        
        #Temporarily store current head node
        temp = self.head

        #For list of size 1
        #Set head and tail as none
        if self.length == 1:
            self.head = None
            self.tail = None

        #For lists greater than length one/'1'
        # Make the 2nd Node as the head
        # And disconnect 'next' and 'prev' pointers
        else:

            #Set head as the 2nd node
            self.head = temp.next

            #Disconnect prev pointer from new head
            self.head.prev = None

            #Disconnect next pointer from old head
            temp.next = None

        #Update length of the list
        self.length -= 1
        
        #Return popped node
        #return temp.value
        return temp


    ###############################
    #Get - Fetch item from the list
    # based on 'index' input
    # And return the node
    ###############################
    def get(self,index):

        #If index provided is out of bounds
        if index<0 or index>=self.length:
            return None
        
        #Temporarily store the current head
        # value in 'temp'
        temp = self.head

        #Loop through all nodes
        # if index is before first half
        if index < (self.length)/2:
            print("Get method used - First half of list.")
            
            for _ in range(index):
                temp = temp.next

        #Else parse through all nodes in
        # the latter half starting from tail
        else:
            print("Get method used - Second half of list.")
            temp = self.tail

            #start from last node, which is usually n-1
            # and subtract value by '1' to reach index
            for _ in range(self.length-1, index, -1):
                temp = temp.prev

        #Return node after all steps complete
        return temp
    
    ################################
    #Set - Edit/change value at 
    # specified index, and return 
    # True or False
    ################################
    def set(self,index,value):

        #Get and store current node 
        # at that index
        temp = self.get(index)

        #If temp points to a node, 
        # replace value
        if temp:
            temp.value = value
            return True
        
        #Temp doesn't point to a node?
        return False

    ################################
    #Insert - add value into specific
    # position while keeping all 
    # existing values - Return T or F
    ################################
    def insert(self,value,index):

        #If provided index is out of bounds
        if index<0 or index>self.length:
            return False

        #Use existing prepend function for
        # index - 0
        if index == 0:
            return self.prepend(value)

        #Use existing append function for
        # last node, which is same as length
        if index == self.length:
            return self.append(value)

        #For nodes except first and last. 
        #---------------------------------------#
        #---------------------------------------#
        #Create new node, and store existing nodes 
        # in 'before' and 'after'

        #Create a new node with provided value
        newNode = Node(value)

        #Get value of node, right
        # before index position.
        # This will be on the left 
        # of the new node.
        before = self.get(index-1)

        #Get 'current node'.
        # This will move to
        # the right of the new node
        after = before.next
        #---------------------------------------#
        #Update the 'prev' and 'next' pointers
        # of the three nodes

        #New Node
        newNode.prev = before
        newNode.next = after

        #Before node
        before.next = newNode

        #After node - Old node at that index
        after.prev = newNode

        #---------------------------------------#
        #---------------------------------------#

        #Update list length
        self.length += 1

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
print("\nPrepending List with value '0'.\n")

#Prepend value in the list
myDoublyLinkedList.prepend(0)

#Print result
myDoublyLinkedList.print_list()

print("\n#---------------#\n")


##################################
#IV. Pop first
##################################
print("Popping first value in the List.\n")

#Pop first value in the list
myDoublyLinkedList.popFirst()

#Print result
myDoublyLinkedList.print_list()

print("\n#---------------#\n")


##################################
#V. Get Node
##################################

print("Get value from list based on index.\n")

#Adding some values
myDoublyLinkedList.prepend(0)
myDoublyLinkedList.append(3)
myDoublyLinkedList.append(4)
myDoublyLinkedList.append(5)

print(f"New list is now \n")
myDoublyLinkedList.print_list()
print("\n")

#Get values at first and second half
print(myDoublyLinkedList.get(2).value)
print(myDoublyLinkedList.get(4).value)

print("\n#---------------#\n")


##################################
#VI. Set Node
##################################
print("Set/edit value at provided 'index'.\n")

#Set value at fifth position as '6'
myDoublyLinkedList.set(5,6)

myDoublyLinkedList.print_list()

print("\n#---------------#\n")


##################################
#VII. Insert Node
##################################
print("Insert value at provided 'index'.\n")

#Insert value at fifth position as '5'
myDoublyLinkedList.insert(5,5)

myDoublyLinkedList.print_list()

print("\n#---------------#\n")