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
    #Add value onto the list
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
        
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next

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
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

###############################
# End of Linked list class
###############################

###############################
#Prepend testing
###############################
my_linked_list = LinkedList(4)
my_linked_list.append(5)

print("List is now:")
my_linked_list.print_list()
print("\n")

my_linked_list.prepend(1)

print("List is now:")
my_linked_list.print_list()
print("\n")



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