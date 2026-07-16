from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    #create a counter 
    counter = 0
    #loop the list and check x in numbs if so updated a counter and return it 
    for i in nums:
        if i == x: #check if interger passed is equal to the element being checked 
            counter += 1 #update counter
    return counter #return the counter 



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
