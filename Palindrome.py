def is_palindrome(input:int):
    lengthofInput = 0
    test = input
    input_array = []

    if input<0:
        print("Not a palindrome due to negative sign")
        return False

    while test>0:
        input_array.append(test%10)
        test = int(test/10)
        lengthofInput+=1

    print(input_array)
        
    i=0
    j=lengthofInput-1

    while i<j:
        if input_array[i]!=input_array[j]:
            print("Not a palindrome")
            return False
        i+=1
        j-=1

    print("Is a palindrome")
    return True



print(is_palindrome(-10001))

