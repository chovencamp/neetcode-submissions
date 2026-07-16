from typing import List # this is used to add type hints for List type

'''This works because lists are immutable so when we append to the 
original list it can be changed unlike strings
'''
def append_to_list(my_list: List[int], elements: List[int]) -> List:
    for num in elements: #loop over elements 
        my_list.append(num) #append each element to the original list 
    return my_list #return updated list 


# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
