"""
Two Sum problem
Solution from NeetCode
https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf
"""

#Function to return values as an array of integers in list data type
# Parameters: list of integers (nums), integer (target)
def twoSum(nums: list[int], target: int) -> list[int]:

    #Create     empty HashMap/Dictionary | val : index
    prevMap = {}

    #Loop through all values from the List
    for i, n in enumerate(nums):

        #Difference between the target value and current..
        #..value in the list
        diff = target - n

        #Check if the difference is already in the Map we created
        # Map will be empty in the first iteration
        # If it matches, return the positions of both values
        if diff in prevMap:
            return [prevMap[diff], i]
        
        #If nothing, store the value (n) and 
        # it's position (i) in this function's hashmap
        prevMap[n] = i

    return "No match"


#Create the list and test out result
linkedList = [1,2,3,4,5,6,7]
result = twoSum(linkedList,10)
print("Positions of array values: ",result)