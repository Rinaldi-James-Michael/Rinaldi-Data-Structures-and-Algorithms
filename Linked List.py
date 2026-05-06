###############################
# Node Class, just used to help 
# initialize node in LinkedList 
# class
###############################

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None



###############################
# Start of Linked list class
###############################

class LinkedList:

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
    #Append/add value onto the list's 
    # last position
    ###############################
    def append(self,value):
        new_node = Node(value)
        #if list is empty, head and tail are the node itself
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        #if list has data, set the tail and it's next pointer to this node (appended data)
        else:
            self.tail.next = new_node
            self.tail = new_node 
        self.length+=1

    ################################
    #Pop/Remove last value from List
    ################################
    def pop(self):
        #if list is empty
        if self.length == 0:
            return None
        
        #Temporarily assign head value to temp and pre
        # Temp is the last value to be popped, 
        # and pre is the value right before it
        temp = self.head
        pre = self.head

        #Traverse through list to reach the last value
        # as long as there is a value after temp
        while(temp.next):
            pre = temp
            temp = temp.next

        #Point to the second last value and remove
        #the pointer that points to the next value
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        #if the popped item was the last in the list
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    ##################################################
    #Prepend/Add value to the first position in a List
    ##################################################
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            #Set the current head value to be the next value of the new head
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    ##################################################
    #Pop from first position in a List
    ##################################################
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    ##################################################
    #Get - Return node at specified index
    ################################################## 
    def get(self,index):
        if index<0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    ##################################################
    #Set - Edit value in a LinkedList
    ################################################## 
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    ##################################################
    #Insert value into particular index 
    # (prepend and append included)
    ################################################## 
    def insert(self, index, value):
        #if index value given is out of range of the list itself
        if index<0 or index >= self.length:
            #returns False because it is the
            # opposite of returning True
            return False
        
        #if value to be inserted at start, just prepend
        if index==0:
            return self.prepend(value)
        
        #if value to be inserted at the end, just append
        if index == self.length:
            return self.append(value)
        
        #Insert value in the middle of a list
        new_node = Node(value)
        
        #set temp as the value right before the
        #position you want to insert value in
        temp = self.get(index-1)

        #Point new value's 'next' pointer to the value
        # that the preceding value pointed to
        new_node.next = temp.next

        #Point the preceding value's next pointer
        # to the new node 
        temp.next = new_node
        
        #increment length of list value
        self.length += 1
        return True

    ##################################################
    #Remove value from particular index
    # including (Pop and Pop first)
    ##################################################    
    def remove(self, index):
        if index < 0 or index >= self.length:
            #returns None because it is the 
            # oppposite of returning a Node
            return None
        
        #if index is first item, pop first
        if index == 0:
            return self.pop_first()
        
        #if index is last value, pop
        if index == self.length-1:
            return self.pop()
        
        #value preceding what needs to be removed
        prev = self.get(index-1)

        #Temp is the value you want to remove
        temp = prev.next

        #Previous value should now point to the
        # node after the removed node
        prev.next = temp.next
        temp.next = None

        #Updated length of the list
        self.length-= 1
        return temp

    ##################################################
    #Reverse a linked list
    ################################################## 
    def reverse(self):

        #swap head and tail nodes
        temp = self.head
        self.head = self.tail
        self.tail = temp

        #Set 'before' and 'after' value
        # Before is None, Temp is the first node / head
        # After is the second node
        after = temp.next
        before = None

        #Order -> before : temp : after

        #Loop through all nodes to reverse.
        #Basically traversing each node from the head
        # and pointing temp node the other way.
        for _ in range(self.length):
            #move the 'after' pointer to the next node
            #(won't matter in the first loop)
            after = temp.next

            #next pointer should now point the other way
            temp.next = before

            #Move temp pointer from before position to after position
            #Before value should now be the current/temp node (for the next loop)
            before = temp
            #Current/temp node is now the following/after node (for the next loop)
            temp = after       

    ##################################################
    #Find the middle node
    ################################################## 
    def find_middle_node(self):
        #Move slow node, one node at a time
        slow = self.head

        #Move fast node, two nodes at a time
        fast = self.head
        
        #Iterate till the fast node
        # reaches the end/none
        while fast!=None:
            
            #Next node would be empty
            # if total length is odd
            if fast.next == None:
                return slow
            fast = fast.next
            
            #Next node would be empty
            # if total length is even
            if fast.next == None:
                return slow.next
            fast = fast.next
            
            #Iterate one node
            slow = slow.next

    ##################################################
    #Verify if the linked list is looped
    ################################################## 
    def has_loop(self):
        #Move slow node, one node at a time
        slow = self.head

        #Move fast node, two nodes at a time
        fast = self.head
        
        if self.length==1:
            return False
        
        while fast!=None:
            if fast==None:
                return False
                
            if fast.next != None:
                fast = fast.next.next
            else:
                fast = None
            slow = slow.next
            
            if fast == slow:
                return True
        
        return False
            


###############################
# End of Linked list class
###############################



# ###############################################
# ###############################################
# ###############################################

###############################
#Reverse a Linked list testing
###############################
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.print_list()

my_linked_list.reverse()
print("\n")
my_linked_list.print_list()


# ###############################
# #Remove in the middle of list testing
# ###############################
# my_linked_list = LinkedList(11)

# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# my_linked_list.print_list()

# my_linked_list.remove(2)

# print("\nLinked List is now:")
# my_linked_list.print_list()


# ###############################
# #Insert in the middle of list testing
# ###############################
# my_linked_list = LinkedList(0)
# my_linked_list.append(2)
# my_linked_list.print_list()

# print("\n")

# my_linked_list.insert(1,1)
# my_linked_list.print_list()


# ###############################
# #Set testing
# ###############################
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# my_linked_list.print_list()

# # print("\n")
# # print(my_linked_list.get(1).value)

# my_linked_list.set_value(1,4)

# print("\nLinked List is now:")
# my_linked_list.print_list()


# ###############################
# #Get testing
# ###############################
# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)

# # print(f"Value at position 2: {my_linked_list.get(2)}")
# print(my_linked_list.get(2))


# ###############################
# #Pop first testing
# ###############################
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)

# print("List is:\n")
# my_linked_list.print_list()

# my_linked_list.pop_first()
# print("\nList after pop first:\n")
# my_linked_list.print_list()


# ###############################
# #Prepend testing
# ###############################
# my_linked_list = LinkedList(4)
# my_linked_list.append(5)

# print("List is now:")
# my_linked_list.print_list()
# print("\n")

# my_linked_list.prepend(1)

# print("List is now:")
# my_linked_list.print_list()
# print("\n")



# ###############################
# #Print, Pop testing
# ###############################

# print("List is now:")
# my_linked_list.print_list()
# print("\n")
  
# #(2) Items - Returns 2 Node
# my_linked_list.pop()
# print("Popped and List is now:")
# my_linked_list.print_list()
# print("\n")

# #(1) Item - Returns 1 Node
# my_linked_list.pop()
# print("Popped and List is now:")
# my_linked_list.print_list()
# print("\n")

# #(0) Items - Returns "None"
# my_linked_list.pop()
# print("Popped and List is now:")
# my_linked_list.print_list()
# print("\n")