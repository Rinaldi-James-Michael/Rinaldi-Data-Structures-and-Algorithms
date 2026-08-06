###############################
# Node Class, just used to help 
# initialize node in Binary 
# Search Tree class
###############################

class Node:
    def __init__(self,value):
        self.value = value

        #Differentiating parameters
        # for BST
        self.left = None
        self.right = None


###################################
# Start of Binary Search Tree class
###################################

class BinarySearchTree:

    ###############################
    #Initialize/Construct the Tree
    ###############################
    def __init__(self):

        #Creating an emtpy tree
        # Will add value through insert
        self.root = None


    ###############################
    #Insert value in tree
    ###############################
    def insert(self,value):

        #Create the new node
        newNode = Node(value)

        #Case I: If the tree is empty
        # Set node as root and 
        # return 'True'
        if self.root is None:
            self.root = newNode
            return True

        #If tree is not empty, proceed below
        #Store root value in a variable
        temp = self.root

        #Case II:
        # Infinite while loop that stops 
        # when a return statement is reached
        while (True):

            #Value of node should not 
            # already exist. NO DUPLICATES!
            if newNode.value == temp.value:
                return False

            #Assign node to the left of parent
            #If new node value is less than parent value
            if newNode.value < temp.value:

                #If left child of parent is None
                #Assign new node to left child
                if temp.left is None:
                    temp.left = newNode

                    #Exit the while loop
                    # and return status
                    return True

                #Else, if another value already exists on
                # the left slot, update 'temp' as that 
                # left child. And go through loop again.
                temp = temp.left

            #Assign node to the right of parent
            #If new node value is greater than parent value
            else:

                #If right child of parent is None
                #Assign new node to right child
                if temp.right is None:
                    temp.right = newNode

                    #Exit the while loop
                    # and return status
                    return True

                #Else, if another value already exists on
                # the right, update 'temp' as that
                # right child. And go through loop again.
                temp = temp.right


    ###############################
    #Contains - Verify if value 
    # exists in the BST
    ###############################
    def contains(self,value):
        
        #For empty tree - below two
        # lines can be skipped, since
        # while loop condition checks
        # for this

        # if self.root is None:
        #     return False

        #Else, when tree is not empty
        #Store root value in temp
        temp = self.root

        #Loop until 'temp' has 
        # any value / not None
        while temp is not None:

            #Move tracker/temp to
            # the left child 
            if value < temp.value:
                temp = temp.left

            #Move tracker/temp to
            # the right child 
            elif value > temp.value:
                temp = temp.right

            #The matching node will reach
            # this condition since it's
            # not greater or lesser than
            # i.e. equal to our value
            else:
                return True

        #No value existed during the loop
        return False
    



###################################
# End of Queues class
###################################





################################################
################################################
################################################





##################################
#I. Create empty binary search tree 
##################################
print("I. Creating empty binary search tree\n")

#Create the tree and object
myTree = BinarySearchTree()
print(myTree.root)

print("\n#---------------#\n")


##################################
#II. Insert values in binary search tree 
##################################
print("I. Adding binary search tree\n")

#Insert values, with '2' as root
myTree.insert(2)
myTree.insert(1)
myTree.insert(3)

#Print results
print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)

print("\n#---------------#\n")


##################################
#III. Contains - Check for value 
# in binary search tree 
##################################
print("I. Creating empty binary search tree\n")

#Create the tree and object
myTree2 = BinarySearchTree()

#Insert values
myTree2.insert(47)
myTree2.insert(21)
myTree2.insert(76)
myTree2.insert(18)
myTree2.insert(27)
myTree2.insert(52)
myTree2.insert(82)

print(f"Has 27? {myTree2.contains(27)}")
print(f"Has 17? {myTree2.contains(17)}")

print("\n#---------------#\n")