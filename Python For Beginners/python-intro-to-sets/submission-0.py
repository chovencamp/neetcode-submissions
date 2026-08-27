from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    #create the set 
    my_set = set()
    #loop on the list of nums
    for num in nums:
        #take each num and add it to the set we made on line 5 
        my_set.add(num)
    #return the final set 
    return my_set

# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
