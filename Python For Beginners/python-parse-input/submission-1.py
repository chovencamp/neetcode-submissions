from typing import List

def read_integers() -> List[int]:
    user_input = input()
    #removes the commas and from what the input was stored 
    strings = user_input.split(",")
    #create the list that we will use 
    int_list = []

    #loop on the strings 
    for string in strings: 
        #store each char in the string to the list but type cast it as its currently a string when we need to return a list of ints 
        int_list.append(int(string))
    #return the list 
    return int_list

    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
