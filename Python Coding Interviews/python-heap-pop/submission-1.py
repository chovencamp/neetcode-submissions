import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    #create the list we will return 
    output = []
    #Use a while loop here because if we do a for loop it changes the size of the heap and a for loop needs to have a range. 
    while heap:
        #append each value popped out of the heap into the list.
        output.append(heapq.heappop(heap))
    return output 




# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
