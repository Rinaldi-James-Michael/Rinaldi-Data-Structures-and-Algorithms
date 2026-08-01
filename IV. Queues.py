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
        newNode = Node(value)

        #Setup 'first' and 'last'
        self.first = newNode
        self.last = newNode

        #Set measurement variable
        self.length = 1

    ###############################
    #Print the queue
    ###############################
    def printQueue(self):

        #Start with first node
        temp = self.first

        #Loop through all nodes
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #################################
    #Enqueue - Add items to the end of
    # the queue
    #################################
    def enqueue(self,value):

        newNode = Node(value)

        #For empty queue, just set
        # 'first' and 'last'
        if self.first is None:
            self.first = newNode
            self.last = newNode

        #For existing queues,
        # add value as the new 'last'
        else:
            self.last.next = newNode
            self.last = newNode

        #Update length of queue
        self.length += 1


    #################################
    #Dequeue - Remove item from the 
    # start of the queue, and return 
    # the removed node
    #################################
    def dequeue(self):

        #Case I: If the queue is empty, 
        # return None
        if self.length == 0:
            return None

        # Store first value in 'temp'
        temp = self.first

        # Case II: if size of queue is 1
        if self.length == 1:
            self.first = None
            self.last = None

        # Case III: Size of queue more than 1
        # Update 'first' to the second node
        #  and unlink the old 'next'
        else:
            self.first = self.first.next
            temp.next = None

        #Finalize by updating length 
        # and return node
        self.length -= 1
        return temp



###################################
# End of Queues class
###################################





################################################
################################################
################################################





##################################
#I. Create queue with a node & print
##################################
print("I. Creating stack with one node and print\n")

#Create stack with one node and print
myQueue = Queue(1)
myQueue.printQueue()

print("\n#---------------#\n")



##################################
#II. Enqueue - add value to queue
##################################
print("II. Enqueue - Add value in queue\n")

#Add value '2' to the queue and print
myQueue.enqueue(2)
myQueue.printQueue()

print("\n#---------------#\n")



##################################
#III. Dequeue - remove value from 
# the start of the queue
##################################
print("III. Dequeue - Remove value '1' from queue\n")

#Adding value for testing
myQueue.enqueue(3)
myQueue.printQueue()

#Remove 'first' index value from the queue and print
print("\nRemove 'first' value:")
removedNode1 = myQueue.dequeue()
myQueue.printQueue()

#Remove 'first' index value from the queue and print
print("\nRemove 'first' value:")
removedNode2 = myQueue.dequeue()
myQueue.printQueue()

#Remove 'first' index value from the queue and print
print("\nRemove 'first' value:")
removedNode3 = myQueue.dequeue()
myQueue.printQueue()

print("\n#---------------#\n")
