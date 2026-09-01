def add_two_numbers() -> int:
    #convert to a list with the split() funciton 
    user_input = input().split(",")

    #since it was converted to a list find the first number stored via its index 
    numberOne = user_input[0]
    #find the second number via its index 
    numberTwo = user_input[1]

    #type cast so that it will not be a string concat and it can be added 
    return int(numberOne) + int(numberTwo)




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
